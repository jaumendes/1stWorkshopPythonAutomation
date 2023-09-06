#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %% [code]
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

# LIBRARIES #
import time
import calendar 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Any results you write to the current directory are saved as output.
import sys
#with open('emailbody.txt') as myf:
 #   myf.write("hello Friend!\n")#' newline='', encoding="utf16")

import re
from decimal import *

import collections
from collections import OrderedDict
from math import *


# START VARS #

tempoinit = time.time()

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

myday = ''
mymonth = ''
cost_total = 0

months = ["JAN",  "FEV", "MAR",  "APR",  "MAY", "JUN",    "JUL",      "AGO",     "SET",     "OCT",     "NOV",    "DEC"          ]


dic_inputs = {}
cof   = 0
lunch = 0
tab   = 0
joi   = 0
shops = 0
dinner = 0
drink = 0

outros = []
err = []
diffs = []

# CALCULATE PERCENTAGE #

def percentage(part, whole):
    #return (percent * whole) / 100.0
    try:        
        return str(100 * float(part)/float(whole))[0:4] + ' %'
    except:
        return '0.00'

# GET INTEGRATION #

def integ(textfile,adata):
    bodymail = "emailbody_"+adata+".txt"
    sys.stdout = open(bodymail,'w')


    dic_inputs = {}
    cost_dict = {}
    cof   = 0
    lunch = 0
    tab   = 0
    joi   = 0
    shops = 0
    dinner = 0
    drink = 0
    outros = []
    err = []
    mymonth = ''
    err = []
    cost_br  = 0
    cost_tab = 0
    cost_din = 0
    cost_cof = 0
    cost_joi = 0
    cost_dri = 0
    cost_shop  = 0
    cost_port  = 0
    cost_food  = 0
    cost_gift = 0
    cost_lunch = 0
    cost_metro = 0
    cost_gas   = 0
    cost_ecool = 0
    cost_fun = 0
    cost_car = 0
    cost_trf   = 0
    cost_trp   = 0
    cost_spor   = 0
    cost_heal   = 0
    cost_rent = 0
    cost_incom = 0
    cost_total = 0
    lasttotalday = 0
    total_incoming = 0
    afile = open(textfile,"r")
    #with open(textfile,'rb') as afile:
    #        thelines = afile.read()
    thelines = afile.readlines()
    month_keys = []
    total_acc = 0
    counter = 0
    print ('>------------------------------------------------------------------<')
    print ('month', '\t','spent', '\t', 'difflast' , '\t', 'AVG', '\t',' ACC' , '\n')
    for i in thelines:
        #print (i)
        li = i.strip()
        if li in months:
            # print (li)
            mymonth=li
        #print type(li.split(".")[0])
        elif len(li.split("."))> 1 :
            
            #print li.split(".")[0]
            myday = li.split(".")[0]
            my_vals = li.split(".")[1:]
            
            my_key = str(mymonth)+ str(myday)
            # CRIAR VARIAVEL DE DO PARA RETORNAR WEEKDAY
           # my_weekday = 
            month_keys.append(my_key)

            dic_inputs[my_key] = my_vals # INPUT VALUES BY DAY OF MONTH #
            #print (type(my_vals))
            # print(my_key, my_vals) = 27 ["dcx","adczx","efdc"]
#            get_items = my_vals.split('+')
#           get_values = my_vals[0].split(' ')
 #          get_descriptions = my_vals[1:].split('+') # return list 
           
            
            totalday=0
             
#           dictionary_values = dict(zip(get_values, get_descriptions))
            for item in my_vals: # for string in list 
                #print (item)
                pvalues = item[1:].split(" +")# lista de " value key "
                for i in pvalues:
#                   vv = i.split(' ')[0]
 #                  kk = i.split(' ')[1]  
                    #print (kk, vv)
                    #for i,j in vv.strip.split(' '):
                    #print (i)
                    i = i.strip()
                    #print (i)
                    if i == '':
                        continue
                    elif re.search(r"inc", i):
                        #print (i)
                        total_incoming +=int(i.split(' ')[0])
                    else:
                        #print (i)
                        totalday  += int(i.split(' ')[0])
                        total_acc += int(i.split(' ')[0])
##          for i in get_values: # 
  #             if i.isdigit() :
   #                ax = int(i) #totalday=0
    #               totalday+=int(i)
     #              total_acc += int(i)
                    
            
            print  (my_key,'\t ', totalday,'\t', lasttotalday-totalday, '\t', int(total_acc/len(month_keys)),'\t', total_acc , '\t' , 1200 - total_acc , '\t', totalday//4 * '|')
            lasttotalday = totalday
            time.sleep(1)
            
        elif li.startswith('#'):
                diffs.append(li)
            
        else:
            print (li.split("+") , '-------------------')
            my_vals = li
    #my_key = str(mymonth)+ str(myday)
    #dic_inputs[my_key] = my_vals
    #trf_dic_to_tables(dic_inputs)

    # DEF
    for key, value in sorted(dic_inputs.items()):
                    # MAY31 ' 5 lunch-brazind + 1 drink + 1 paper + 5 joi'
        counter +=1
        try: #if len(value) > 0: #try:
            #print (values)
            values = value[0].split("+ ") 

            #print key, values # MAY31  [ ' 2 cof ', ' 1 br ', ' 4 lunch ', ' 22 mini' ]
            for i in values: 
                # print (key, i)
                           
                if re.search(r"br", i.strip()):
                    cost = i.strip().split(" ")[0]
                    
                    cost_br += int(cost)
                    cost_total += int(cost)
                elif re.search(r"tab", i.strip()) or re.search(r"paper", i.strip()):
                    cost = i.strip().split(" ")[0]
                    
                    cost_tab += int(cost)
                    cost_total += int(cost)
                elif re.search(r"trf", i.strip()) or re.search(r"tlm", i.strip()) or re.search(r"bet", i.strip()):
                    cost = i.strip().split(" ")[0]
                    
                    cost_trf += int(cost)
                    cost_total += int(cost)
                elif re.search(r"rent", i.strip()) :
                    cost = i.strip().split(" ")[0]
                    
                    cost_rent += int(cost)
                    cost_total += int(cost)
                elif re.search(r"lunch", i.strip())  : #r"^dinner",
                    cost = i.strip().split(" ")[0]
                    
                    cost_lunch += int(cost)
                    cost_total += int(cost)
                elif re.search(r"dinner", i.strip())  : #r"^dinner",
                    cost = i.strip().split(" ")[0]                    
                    cost_din += int(cost)
                    cost_total += int(cost)
                    
                elif re.search(r"metro", i.strip()): #r"^dinner",
                    cost = i.strip().split(" ")[0]                    
                    cost_metro += int(cost)
                    cost_total += int(cost)
                    
                elif re.search(r"ecool", i.strip()) or re.search(r"parq", i.strip())  or re.search(r"portag", i.strip()) : #r"^dinner",
                    cost = i.strip().split(" ")[0]                    
                    cost_ecool += int(cost)
                    cost_total += int(cost)
                    
                elif re.search(r"fun", i.strip()) :
                    cost = i.strip().split(" ")[0]                    
                    cost_fun += int(cost)
                    cost_total += int(cost)
                    
                elif re.search(r"sport", i.strip()): #SPORT
                    cost = i.strip().split(" ")[0]                    
                    cost_spor += int(cost)
                    cost_total += int(cost)
                    
                elif re.search(r"heal", i.strip()): #HEALTH
                    cost = i.strip().split(" ")[0]
                    cost_heal += int(cost)
                    cost_total += int(cost)
                    
                elif re.search(r"cof", i.strip()): #r"^dinner",
                    cost = i.strip().split(" ")[0]                    
                    cost_cof += int(cost)
                    cost_total += int(cost)
                elif re.search(r"joi", i.strip()): #r"^dinner",
                    cost = i.strip().split(" ")[0]                    
                    cost_joi += int(cost)
                    cost_total += int(cost)
                    
                elif re.search(r"food",  i.strip()): #.split("-")): #r"^dinner",
                    cost = i.strip().split(" ")[0]
                    cost_food += int(cost)
                    cost_total += int(cost)
                elif re.search(r"port", i.strip()): #.split("-")): #r"^dinner",
                    cost = i.strip().split(" ")[0]
                    cost_port += int(cost)
                    cost_total += int(cost)
                elif re.search(r"gift", i.strip()): #.split("-")): #r"^dinner",
                    cost = i.strip().split(" ")[0]
                    cost_gift += int(cost)
                    cost_total += int(cost)
                    
                elif re.search(r"shops", i.strip()) or re.search(r"bag", i.strip()): #.split("-")): #r"^dinner",
                    cost = i.strip().split(" ")[0]
                    cost_shop += int(cost)
                    cost_total += int(cost)
                elif re.search(r"drink", i.strip()) or re.search(r"beer", i.strip()): #r"^dinner",
                    cost = i.strip().split(" ")[0]                    
                    cost_dri += int(cost)
                    cost_total += int(cost)
                elif re.search(r"gas", i.strip()) : #or re.search(r"beer", i.strip()): #r"^dinner",
                    cost = i.strip().split(" ")[0]                    
                    cost_gas += int(cost)
                    cost_total += int(cost)
                elif re.search(r"trp", i.strip()) : #or re.search(r"beer", i.strip()): #r"^dinner",
                    cost = i.strip().split(" ")[0]                    
                    cost_trp += int(cost)
                    cost_total += int(cost)
                elif re.search(r"car", i.strip()) : #or re.search(r"beer", i.strip()): #r"^dinner",
                    cost = i.strip().split(" ")[0]                    
                    cost_car += int(cost)
                    cost_total += int(cost)
                elif re.search(r"inc", i.strip()) : #or re.search(r"beer", i.strip()): #r"^dinner",
                    cost = i.strip().split(" ")[0]                    
                    cost_incom += int(cost)
                    #cost_total += int(cost)    NOT A COST            
                    
                else:
                    outros.append(key+i)
                    #print i.strip(), ' NAO DEU!!'
                    
                    
        except:
            print ("olha", value )
            err.append(value)
    print (mymonth, '\n>-----------------------------------------<'    )
    print (outros , '\n', err)
    print ('number of days = ' , len(dic_inputs.keys()) , ' days.\n\n')
    cost_dict['BR'] = cost_br
    cost_dict['TAB'] = cost_tab
    cost_dict['DIN'] = cost_din
    cost_dict['JOI'] = cost_joi
    cost_dict['DRI'] = cost_dri
    cost_dict['COF'] = cost_cof
    cost_dict['SHOP'] = cost_shop
    cost_dict['LUNCH'] = cost_lunch
    cost_dict['GAS'] = cost_gas
    cost_dict['TRF'] = cost_trf
    cost_dict['CAR'] = cost_car
    cost_dict['SPORT'] = cost_spor
    cost_dict['HEAL'] = cost_heal
    cost_dict['RENT'] = cost_rent
    cost_dict['SPENT'] = cost_total    
    cost_dict['METRO'] = cost_metro
    cost_dict['FUN'] = cost_fun
    cost_dict['INCOM'] = cost_incom

    sorted_my_dict = OrderedDict(sorted(cost_dict.items(), key=lambda t: t[1])) 
    # WantedOutput = sorted(MyDict, key=lambda x : MyDict[x])
    # OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    print ('\nDESCRIPT \t'   ,  'EUR'  ,  '\t',  ' % '   ,   '\t', 'Eur/Day')
    
    ###for k,v in sorted_my_dict: #.items{()}[::-1]:
       #### print (k, '\t', v, '\t', percentage(int(v),cost_total), '\t' ,'\t', float(v/int(myday.strip())), '\t', int(v/10) * '|')
    #print counter #int(myday), type(myday)
    print ('\nDIFF \t'  , cost_incom-cost_total,'\t', 'Preview = ',int( ((cost_incom-cost_total)/(32 - counter))), ' Eur / Day')
    for i in diffs:
            print (i)
    print ('\nSPENT \t' , cost_total , '\t', int(float(cost_total/len(dic_inputs.keys()))), '\n')
    #f.write(str('\nSPENT \t\t' + str( cost_total) + '\t\t' + str(float(cost_total/len(dic_inputs.keys()))) +  '\n'))

    # CREATE EPORT STEP 1
    
    for i, j in sorted_my_dict.items():
        print (i,'\t', j,'\t', j/cost_total,'\t', '|' * (int(j/4)+1))

       

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def main():
        script = sys.argv[0]
        filename = sys.argv[1]
        
        adata = filename.split(".")[0]
        adata = adata.split("_")[1]
       
        integ(filename,adata)

main()





#--------------------------------------
# Python program to Find day of  
# the week for a given date 
import datetime 
import calendar 
  
def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    print (calendar.day_name[born]) 
  
# Driver program 
# date = '03 02 2019'
# print(findDay(date))

#--------------------------------------------
# Python program to Find day of  
# the week for a given date 
import calendar 
  
def findDay(date): 
    day, month, year = (int(i) for i in date.split(' '))     
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 
  
# Driver program 
date = '03 02 2019'
print(findDay(date))


tempofim=time.time()

# ENCONTRA O DIA # 
from datetime import datetime
my_wk_day = datetime.today().strftime('%A')
print (my_wk_day)

print(tempofim, " SECONDS ELAPSED!\nFIN!")

# CLOSE LOG FILE
sys.stdout.close()
#myf.close()
