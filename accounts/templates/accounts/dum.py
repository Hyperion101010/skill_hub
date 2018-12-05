import os
from bs4 import BeautifulSoup
import requests
import re

base_url = 'https://www.naukri.com/'  # the url of the website
total_list_fetched = []

"""for each data we are passing it as individual bsobj from the findall list and hence each data is a bsobj"""


def get_org_name(data):
    dummy = data.find_all('span', {'class': 'orgRating'})
    org_name = dummy[0].text
    return org_name


def get_exp(data):
    dummy = data.find_all('span', {'class': 'exp'})
    exp = dummy[0].text
    return exp


def get_loc(data):
    dummy = data.find_all('span', {'class', 'loc'})
    loc = dummy[0].text
    return loc


# here there might be a problem of return skills of list


def get_skills(data):
    dummy = data.find_all('span', {'class', 'skill'})
    skill = dummy[0].text
    return skill


# here there might be a problem of return skills of list


def get_job_desc(data):
    dummy = data.find_all('span', {'class': 'desc'})
    desc = dummy[0].text
    return desc

    """here salary if not specified is retuned as none"""


def get_salary(data):
    compare_salary = re.compile('/d+')
    compare_lpa = re.compile('l.p.a')
    salary = data.find_all('span', {'class': 'salary'})
    salary = (dummy[0].text).split('\w+[-]+')
    mx = 0
    fl = 0
    int_check = 0
    for i in range(len(salary)):
        if re.search(compare_salary, salary[i]) is not None:
            int_check = 1
        if int(salary[i]) > mx:
            mx = int(salary[i])
    if re.search(compare_lpa, salary[i].lower()) is not None:
        fl = 1
    if fl == 1:
        mx = mx * (100000)
    if int_check == 1:
        return mx
    else:
        return None


def get_info_from_each_tuple(data):
    dummy_dict = dict()
    dummy_dict['salary'] = get_salary(data)
    dummy_dict['company'] = get_org_name(data)
    dummy_dict['loc'] = get_loc(data)
    dummy_dict['skills'] = get_skills(data)
    dummy_dict['description'] = get_job_desc(data)
    dummy_dict['exp'] = get_exp(data)
    return dummy_dict


"""here pass the bsobj as an argument"""


def get_jobs_count(bsobj):
    dummy_regex = re.compile('\d+')
    data = bsobj.find_all('span', {'class': 'cnt'})
    count_first = data[0].text
    count = count.split(" ")
    index = 0
    if re.search(dummy_regex, count_first) is not None:
        for i in count:
            if i == 'of':
                break
            else:
                index += 1
        count = int(count[index + 1])
        return count
    else:
        return 0


""" here main function starts for searching the jobs """

"""here there may be error"""


def prepare_parameters(data, cnt):  # this prepares parameters for the given options
    data = data.split('\w+')
    dummy_str = "-"
    for i in range(len(data)):
        data[i] = data[i].lower()
    dummy_str = dummy_str.join(data)
    dummy_str += '-jobs'
    cnt = str(cnt)
    if int(cnt) > 0: dummy_str += '-%s' % (cnt)
    return dummy_str


# to get pages pass the url  here there is exception needed
def make_obj(paramet, cnt):
    paramet = prepare_parameters(paramet, cnt)
    url = requests.get(base_url + '%s' % (paramet))
    bsobj = BeautifulSoup(url.text)
    return bsobj


"""here pass the job specification of the containing individual jobs """


def run_scraper(paramet):
    bsobj = make_obj(paramet, 0)
    count = 0
    check = bsobj.find_all('div', {'type': 'tuple'})
    if len(check) == 0:
        return [], False
    else:
        count = get_jobs_count(bsobj)
        for i in range(int(count / 50)):
            bsobj = make_obj(paramet, int(i))
            bsobj_len = bsobj.find_all('div', {'type': 'tuple'})
            for j in range(len(bsobj_len)):
                total_list_fetched.append(get_info_from_each_tuple(bsobj_len[j]))
    return total_list_fetched


