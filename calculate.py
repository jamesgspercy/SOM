#Importing python libraries and defining functions

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def radose_func():
    ralist = []
    ralist2 = []
    ralist3 = []
    ralist4 = []

    for A in dose:
        ralist.append(round((F*Rt*E*(A/(A+Kd))),2))
    for A in dose2:
        ralist2.append(round((ex2_F*ex2_Rt*ex2_E*(A/(A+ex2_Kd))),2))
    for A in dose3:
        ralist3.append(round((ex3_F*ex3_Rt*ex3_E*(A/(A+ex3_Kd))),2))
    for A in dose4:
        ralist4.append(round((ex4_F*ex4_Rt*ex4_E*(A/(A+ex4_Kd))),2))
    return ralist, ralist2, ralist3, ralist4

ralist, ralist2, ralist3, ralist4 = radose_func()

#print('RADose')
#print(ralist)
#print(ralist2)
#print(ralist3)
#print(ralist4)

#radose_list = radose_func()
#print(radose_list)

def log_dose_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    for A in dose:
        if type(A) == int or float:
            list.append(round(math.log(A,10),1))
        else:
            print('There is an error')
    for A in dose2:
        if type(A) == int or float:
            list2.append(round(math.log(A,10),1))
        else:
            print('There is an error')
    for A in dose3:
        if type(A) == int or float:
            list3.append(round(math.log(A,10),1))
        else:
            print('There is an error')
    for A in dose4:
        if type(A) == int or float:
            list4.append(round(math.log(A,10),1))
        else:
            print('There is an error')        
    return list, list2, list3, list4

ldlist, ldlist2, ldlist3, ldlist4 = log_dose_func()

#print('LogDose')
#print(ldlist)
#print(ldlist2)
#print(ldlist3)
#print(ldlist4)

def effect_ct_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    for A in ralist:
        list.append((A - threshold)/(capacity - threshold)*100) 
    for A in ralist2:
        list2.append((A - threshold)/(capacity - threshold)*100)
    for A in ralist3:
        list3.append((A - threshold)/(capacity - threshold)*100)
    for A in ralist4:
        list4.append((A - threshold)/(capacity - threshold)*100)
    return list, list2, list3, list4    
    
ectlist, ectlist2, ectlist3, ectlist4 = effect_ct_func()

#print('EffectCT')
#print(ectlist)
#print(ectlist2)
#print(ectlist3)
#print(ectlist4)

effect_ct_list = effect_ct_func()
#print(effect_ct_list)

def effect_assay_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    for A in ralist:
        if A <= 0:
            A = 0
        if A >= 100:
            A = 100
        list.append(round(A,2))
    for A in ralist2:
        if A <= 0:
            A = 0
        if A >= 100:
            A = 100
        list2.append(round(A,2))
    for A in ralist3:
        if A <= 0:
            A = 0
        if A >= 100:
            A = 100
        list3.append(round(A,2))
    for A in ralist4:
        if A <= 0:
            A = 0
        if A >= 100:
            A = 100
        list4.append(round(A,2))
    return list, list2, list3, list4 

ealist, ealist2, ealist3, ealist4 = effect_assay_func()

#print('EffectAssay')
#print(ealist)
#print(ealist2)
#print(ealist3)
#print(ealist4)

    
zippedList = list(zip(dose, ldlist, ectlist))
zippedList2 = list(zip(dose2, ldlist2, ectlist2))
zippedList3 = list(zip(dose3, ldlist3, ectlist3))
zippedList4 = list(zip(dose4, ldlist4, ectlist4))

calculations_zl = list(zip(ralist, ectlist, ealist))
calculations_zl2 = list(zip(ralist2, ectlist2, ealist2))
calculations_zl3 = list(zip(ralist3, ectlist3, ealist3))
calculations_zl4 = list(zip(ralist4, ectlist4, ealist4))

# Creating the DataFrame 

df = pd.DataFrame(zippedList, columns = ['Dose','log(Dose)','effect_assay'])
df2 = pd.DataFrame(zippedList2, columns = ['Dose','log(Dose)','effect_assay'])
df3 = pd.DataFrame(zippedList3, columns = ['Dose','log(Dose)','effect_assay'])
df4 = pd.DataFrame(zippedList4, columns = ['Dose','log(Dose)','effect_assay'])

# Display Calculations
#
# Effect(C-T) determines gross effect as %MPE in assay given Threshold T and Ceiling C as Effect=((RA-T)/(C-T))*100
#
#

#print("Calculations")

calculations1 = pd.DataFrame(zippedList, columns =  ['RA(Dose)','Effect(C-T)', 'Effect(Assay)'])
calculations2 = pd.DataFrame(zippedList, columns =  ['RA(Dose)','Effect(C-T)', 'Effect(Assay)'])
calculations3 = pd.DataFrame(zippedList, columns =  ['RA(Dose)','Effect(C-T)', 'Effect(Assay)'])
calculations4 = pd.DataFrame(zippedList, columns =  ['RA(Dose)','Effect(C-T)', 'Effect(Assay)'])

#display(calculations1,calculations2,calculations3,calculations4)

#display(df,df2,df3,df4)

from matplotlib import style # import style module
style.use("ggplot")

fig = plt.figure()

plt.figure(figsize=(10,8)) 
plt.plot(df['log(Dose)'], df['effect_assay'])
plt.scatter(df['log(Dose)'], df['effect_assay'], label = "EXP1")

plt.plot(df2['log(Dose)'], df2['effect_assay'])
plt.scatter(df2['log(Dose)'], df2['effect_assay'], label = "EXP2")

plt.plot(df3['log(Dose)'], df3['effect_assay'])
plt.scatter(df3['log(Dose)'], df3['effect_assay'], label = "EXP3")

plt.plot(df4['log(Dose)'], df4['effect_assay'])
plt.scatter(df4['log(Dose)'], df4['effect_assay'], label = "EXP4")

plt.xlim(-3.0,3.0)
plt.ylim(0,100)
plt.title("Log(Dose) Effect Curve")
plt.xlabel("Log(Dose)")
plt.ylabel("Effect Assay")
plt.legend(loc = 2)

plt.show()

display(calculations1,calculations2,calculations3,calculations4)

#df2.plot(kind='scatter',x='log(Dose)',y='effect_assay',color='red',xticks=[-3.0,-2.5,-2.0,-1.5,-1.0,-0.5,0.5,1,1.5,2,2.5,3], xlim=[-3.0,3.0], ylim=[0,100])

#plt.plot(kind='scatter', df, df2, df3, df4)
#style.use("ggplot")


#plt.plot(df2['log(Dose)'], df['effect_assay'])

#fig = df.plot(kind='scatter',x='log(Dose)',y='effect_assay',color='red',xticks=[-3.0,-2.5,-2.0,-1.5,-1.0,-0.5,0.5,1,1.5,2,2.5,3], xlim=[-3.0,3.0], ylim=[0,100])

