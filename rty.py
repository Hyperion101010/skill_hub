# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import

import urllib

from marionette_driver.by import By

from marionette_harness import MarionetteTestCase


# parent,transform,px
def get_second_transform(direct, ofst):
    return """
   transform: translate{direct}({ofst}px);
  -webkit-transform: translate{direct}({ofst}px);
  -o-transform: translate{direct}({ofst}px);
  -ms-transform: translate{direct}({ofst}px);
  -moz-transform: translate{direct}({ofst}px);
    """.format(for_whom, direct, ofst)


def get_transform(for_whom, direct, ofst):
    if for_whom == "zero-transform":
        return """<style>#zero-transform {\n{0}{1}\n}</style>""".format(get_second_transform('Y', 0),
                                                                        get_second_transform('X', 0))
    else:
        return """<style>#{0}{\n{1}+g\n}</style>""".format(for_whom, get_second_transform(direct, ofst))


def inline(doc):
    return "data:text/html;charset=utf-8,{0}".format(urllib.quote(doc))


def element_direction_doc(direction):
    return inline("""
        <style>
          .element{{
            position: absolute;
            {}: -50px;
            background_color: red;
            width: 100px;
            height: 100px;
          }}
        </style>
        <div class='element'></div>""".format(direction))


class TestVisibility(MarionetteTestCase):

    def testShouldAllowTheUserToTellIfAnElementIsDisplayedOrNot(self):
        test_html = self.marionette.absolute_url("visibility.html")
        self.marionette.navigate(test_html)

        self.assertTrue(self.marionette.find_element(By.ID, "displayed").is_displayed())
        self.assertFalse(self.marionette.find_element(By.ID, "none").is_displayed())
        self.assertFalse(self.marionette.find_element(By.ID,
                                                      "suppressedParagraph").is_displayed())
        self.assertFalse(self.marionette.find_element(By.ID, "hidden").is_displayed())

    def testVisibilityShouldTakeIntoAccountParentVisibility(self):
        test_html = self.marionette.absolute_url("visibility.html")
        self.marionette.navigate(test_html)

        childDiv = self.marionette.find_element(By.ID, "hiddenchild")
        hiddenLink = self.marionette.find_element(By.ID, "hiddenlink")

        self.assertFalse(childDiv.is_displayed())
        self.assertFalse(hiddenLink.is_displayed())

    def testShouldCountElementsAsVisibleIfStylePropertyHasBeenSet(self):
        test_html = self.marionette.absolute_url("visibility.html")
        self.marionette.navigate(test_html)
        shown = self.marionette.find_element(By.ID, "visibleSubElement")
        self.assertTrue(shown.is_displayed())

    def testShouldModifyTheVisibilityOfAnElementDynamically(self):
        test_html = self.marionette.absolute_url("visibility.html")
        self.marionette.navigate(test_html)
        element = self.marionette.find_element(By.ID, "hideMe")
        self.assertTrue(element.is_displayed())
        element.click()
        self.assertFalse(element.is_displayed())

    def testHiddenInputElementsAreNeverVisible(self):
        test_html = self.marionette.absolute_url("visibility.html")
        self.marionette.navigate(test_html)
        shown = self.marionette.find_element(By.NAME, "hidden")
        self.assertFalse(shown.is_displayed())

    # here is csstransform replacement
    def testShouldSayElementsWithNegativeTransformAreNotDisplayed(self):
        self.marionette.navigate(inline(get_transform('parent', 'X', -10000) + """
<div id='parentX'>
  I have a hidden child
  <div id='childX'>
    I am a hidden child
  </div>
</div>"""))
        elementX = self.marionette.find_element(By.ID, 'parentX')
        self.assertFalse(elementX.is_displayed())
        self.marionette.navigate(inline(get_transform('parent', 'Y', -10000) + """
<div id='parentY'>
  I have a hidden child
  <div id='childY'>
    I am a hidden child
  </div>
</div>"""))
        elementY = self.marionette.find_element(By.ID, 'parentY')
        self.assertFalse(elementY.is_displayed())

    def testShouldSayElementsWithParentWithNegativeTransformAreNotDisplayed(self):
        self.marionette.navigate(inline(get_transform('transform', 'X', -10000) + """
          <div id='parentX'>
  I have a hidden child
  <div id='childX'>
    I am a hidden child
  </div>
</div>"""))
        elementX = self.marionette.find_element(By.ID, 'childX')
        self.assertFalse(elementX.is_displayed())
        self.marionette.navigate(inline(get_transform('transform', 'Y', -10000) + """
<div id='parentY'>
  I have a hidden child
  <div id='childY'>
    I am a hidden child
  </div>
</div>"""))
        elementY = self.marionette.find_element(By.ID, 'childY')
        self.assertFalse(elementY.is_displayed())

    def testShouldSayElementWithZeroTransformIsVisible(self):
        self.marionette.navigate(inline(get_transform('zero-transform', 'no_direct', 0) + """
<div id='zero-tranform'>
hyperion was here
</div>"""))
        zero_tranform = self.marionette.find_element(By.ID, 'zero-transform')
        self.assertTrue(zero_tranform.is_displayed())

    # here is csstransform2 replacement
    def testShouldSayElementIsVisibleWhenItHasNegativeTransformButElementisntInANegativeSpace(self):
        self.marionette.navigate(inline("""
          <style>
#negative-percentage-transformY{
  transform: translateY(-75px);
  -webkit-transform: translateY(-75%);
  -o-transform: translateY(-75%);
  -ms-transform: translateY(-75%);
  -moz-transform: translateY(-75%);
}</style>
<div id='negative-percentage-transformY'>I am not a hidden element </div>
         """))
        negative_percent__tranform = self.marionette.find_element(By.ID, 'negative-percentage-transformY')
        self.assertTrue(negative_percent__tranform.is_displayed())

    def testShouldSayElementIsInvisibleWhenOverflowXIsHiddenAndOutOfViewport(self):
        test_html = self.marionette.absolute_url("bug814037.html")
        self.marionette.navigate(test_html)
        overflow_x = self.marionette.find_element(By.ID, "assertMe2")
        self.assertFalse(overflow_x.is_displayed())

    def testShouldShowElementNotVisibleWithHiddenAttribute(self):
        self.marionette.navigate(inline("""
            <p hidden>foo</p>
        """))
        singleHidden = self.marionette.find_element(By.TAG_NAME, "p")
        self.assertFalse(singleHidden.is_displayed())

    def testShouldShowElementNotVisibleWhenParentElementHasHiddenAttribute(self):
        self.marionette.navigate(inline("""
            <div hidden>
                <p>foo</p>
            </div>
        """))
        child = self.marionette.find_element(By.TAG_NAME, "p")
        self.assertFalse(child.is_displayed())

    def testShouldClickOnELementPartiallyOffLeft(self):
        test_html = self.marionette.navigate(element_direction_doc("left"))
        self.marionette.find_element(By.CSS_SELECTOR, '.element').click()

    def testShouldClickOnELementPartiallyOffRight(self):
        test_html = self.marionette.navigate(element_direction_doc("right"))
        self.marionette.find_element(By.CSS_SELECTOR, '.element').click()

    def testShouldClickOnELementPartiallyOffTop(self):
        test_html = self.marionette.navigate(element_direction_doc("top"))
        self.marionette.find_element(By.CSS_SELECTOR, '.element').click()

    def testShouldClickOnELementPartiallyOffBottom(self):
        test_html = self.marionette.navigate(element_direction_doc("bottom"))
        self.marionette.find_element(By.CSS_SELECTOR, '.element').click()
