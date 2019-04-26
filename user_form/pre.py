import os
import pandas as pd
from operator import itemgetter

checker_list=[',','.','[',']','\\','\'','\"'] 


def parser_text(s): 
    s=str(s).split()
    string_one=''
    lo=[]
    l=0
    for i in range(len(s)):
        i=list(s[i])
        for j in i:
            if j not in checker_list:
                string_one+=j
            else:
                continue
        string_one=string_one.lower()
        lo.append(string_one)
        string_one=''
    return lo

def get_element(data,index):
    data_dummy=data.iloc[:,5:6]
    return data_dummy.values

def prediction_engine(skills,file_name):
    data1=skills
    path = os.getcwd()
    #data1 = input().split()
    os.chdir('/home/hyperion/Desktop/datsets/')
    data = pd.read_excel('%s.xlsx' % (file_name))
    list_data=[]
    data_dummy = data.iloc[:100,5:6]
    data_dummy = data_dummy.values.tolist()
    for i in range(len(data_dummy)):
        string_to_work = (parser_text(data_dummy[i]))
        count = 0
        count_dict=dict()
        count_dict['index']=i
        for j in data1:
            if j in string_to_work:
                count+=1
        count_dict['count']=count
        list_data.append(count_dict)
    list_data = sorted(list_data,key=itemgetter('count'),reverse=True)
    new_list = []
    for i in range(3):
        new_list.append(get_element(data,list_data[i].get('index')))
    os.chdir(path)
    return new_list

#pass do work as lis



