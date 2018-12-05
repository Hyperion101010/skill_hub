import os
from operator import itemgetter
import sys
import pandas as pd
import datetime as dt
import re

if "__name__" == "__main__":
    current_dir = os.getcwd()
    now = dt.datetime.now()
    os.chdir('/util_file')
    data = pd.read_csv('data')
    data1 = set()
    current_date = str(now.strftime("%d")) + str((now.strftime("%m"))) + str(
        niow.strftime("%y"))  # here %A is for day,%x is for month
    print ("1)for total display \n2)for entering the query \n3)modifying task \n4)today's task")
    while True:
        q = int(input("\nquery:"))
        if q == 1:
            print (data)
        elif q == 2:
            org_name = input("\norg_name:")
            try:
                dum = set()
                dum['link'] = input('\nenter the link:')
                dum['bugid'] = input('\nthe bug id:')
                dum['dt'] = current_date
                dum['check'] = int(current_date[:2])
                dum['progress'] = input("\nselect among 1)completed 2)later 3)patch for review")
                data1[str(org_name)].append(dum)
            except:
                print ('\nerror incorrect org name')
        elif q == 3:
            query = input('\nenter the org_name')
            dummy = input("enter the change  \n1)date(enter as dd+mm+yy) \n2)progress update")
            dr = input(input("enter the bug id:"))
            ind = 0
            for i in dummy[str(org_name)]:
                if i.get(str(dr)):
                else:
                    ind += 1
            if dummy == 1:
                date_new = str(input("\nenter the date:"))
                ((data1[str(org_name)])[ind])['dt'] = int(date_new)
                ((data1[str(org_name)])[ind])['check'] = int(date_new[:2])
            elif dummy == 2:
                ((data1[str(org_name)])[ind])['progress'] = str(input("\nenter the bugid:"))
# answer = sorted(duml,key = itemgetter('check'),reverse=True)
        else:
            choice = input("\nenter the org:")
            new_set = data1[str(org_name)]
            new_set = sorted(new_set, keys=itemgetter('check'))
            print (new_set[0])
            print (new_set)
            print (data)
