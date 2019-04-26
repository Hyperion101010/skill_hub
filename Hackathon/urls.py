from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import include

urlpatterns = [
    path('', TemplateView.as_view(template_name='user_form/home_page.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('form/', include('user_form.urls')),
    path('predict/predict',include('user_form.urls')),
    path('balance/', TemplateView.as_view(
        template_name='user_form/balance_sheet_management.html'), name='balance'),
     path('auditing/',TemplateView.as_view(template_name='user_form/auditing.html'), name='auditing')
]



"""from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('login.urls')),
    url(r'^form/', include('user_form.urls')),
]"""
