# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:15:10 2022

@author: user
"""



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


import warnings
warnings.filterwarnings("ignore")

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 30)

path = r"C:\Users\user\Desktop\adult.csv"


df=pd.read_csv(path)




# =============================================================================
#                              CLEANING 
# =============================================================================
df.isnull().sum()

df.head()

df.isin(['?']).sum()

df["workclass"]=df["workclass"].replace("?", df["workclass"].mode()[0])

df["occupation"]=df["occupation"].replace("?", df["occupation"].mode()[0])

df["native-country"]=df["native-country"].replace("?", df["native-country"].mode()[0])


df=df.drop(columns=["fnlwgt","educational-num","capital-gain",'capital-loss'])

df.head()

df.duplicated().all()

df.shape

df["income"] = df.income.map({'<=50K': 0, '>50K': 1, '<=50K.': 0, '>50K.': 1})

df["income2"] = df["income"].map({0 : "<=50k", 1 : ">=50k"})

df["marriage-status"]=df["marital-status"].map({'Never-married':'Single', "Widowed" : "Single", "Divorced":"Single", "Separated":"Single",'Married-civ-spouse':"Married",'Married-spouse-absent':"Married", 'Married-AF-spouse':"Married"  })

df["marital-status"].unique()
 

# =============================================================================
df.describe()

# =============================================================================
# Mean value of Age is 39.5, std 13.86. 
# Age values are between 17 and 90.
# %75 observations the value of age is less than 49.
# hours-per-week mean value is 40.59 , std 13.
# Difference between mean and median is not significantly high. 
# However Difference between 3rd quartile and max show us distirbution is right skewed.
# =============================================================================


# =============================================================================
# hours-per-week mean value is 40.59, std.dev. 13
# hours-per-week range are between  1 and 99 
# hours-per-week IQR is between 38 and 45. Which tell us %50 obvervation values concentrated >
# > between 38 and 45
# Difference between mean and median is not significantly high. 
# However Difference between 3rd quartile and max show us distirbution is right skewed.
# =============================================================================


df.describe(include=["O"])


# =============================================================================
#
# =============================================================================







df.head()

#%%

fig = plt.figure(figsize=(10,8)) 
sns.boxplot(x="income2", y="age", data=df)
plt.show()



#%% 

plt.figure(figsize=(10,6))
total = float(len(df) )

ax = sns.countplot(x="income", data=df)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 200,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 
plt.show()


# 76% of data earns under 50k


#%%

plt.figure(figsize=(10,6))
total = float(len(df) )

ax = sns.countplot(x="gender", data=df)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 200,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 
plt.show()



#%%
plt.figure(figsize=(10,6))
total = float(len(df) )

ax = sns.countplot(x="gender", hue="income2", data=df)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 200,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 
plt.show()

# %33 of the data are female.
# Only 3% of Female earn more than 50k  




#%%
plt.figure(figsize=(14,5.5))
total = float(len(df) )

ax = sns.countplot(x="marriage-status", data=df)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 200,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 
plt.show()




#%%



plt.figure(figsize=(12,5))
total = float(len(df["income"]) )

ax = sns.countplot(x="marriage-status", hue="income", data=df,)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 

plt.legend(loc='upper right')
plt.show()

# Intresting detection : Only %3.34 of the Single Adult earn more than 50k 
# But on the marriage side ; It is too close each other 

#%%



plt.figure(figsize=(14,6))
total = float(len(df["income"]) )

ax = sns.countplot(x="marital-status", hue="income", data=df)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 

plt.legend(loc='upper right')
plt.show()


#%%
plt.figure(figsize=(12,5))
total = float(len(df) )

ax = sns.countplot(x="workclass", data=df)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 200,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 
plt.show()

# 75% of the Data work at Private sector. 


#%%
plt.figure(figsize=(12,5))
total = float(len(df["income"]) )

ax = sns.countplot(x="workclass", hue="income", data=df)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 

plt.legend(loc='upper right')
plt.show()

 
# With 15 percent earn more than 50k , private sector still leader. 
# Only at Self-employement inc over than 50k earner is more than  under 50k earner




#%%

plt.figure(figsize=(8,5))
total = float(len(df) )

ax = sns.countplot(y="occupation", data=df)
for p in ax.patches:

    ax.text(p.get_x()+p.get_width()/2.,

            '{:1.2f}'.format((height/total)*100),
            ha="center") 
    
    
plt.show()



#%%

plt.figure(figsize=(12,6))
total = float(len(df) )

ax = sns.countplot(y="occupation", hue="income2" , data=df)
for p in ax.patches:
    ax.text(p.get_x()+p.get_width()/2.,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 
    

plt.show()



#%%

plt.figure(figsize=(12,5))
total = float(len(df) )

ax = sns.countplot(x="race", data=df, order = df["race"].value_counts().index )
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 200,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 
    
    
plt.show()


#%%

plt.figure(figsize=(12,5))
total = float(len(df["income2"]) )

ax = sns.countplot(x="race", hue="income2", data=df, order = df["race"].value_counts().index )
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 

plt.legend(loc='upper right')
plt.show()

#%%
plt.figure(figsize=(12,5))
total = float(len(df) )

ax = sns.countplot(x="education", data=df, order =  df["education"].value_counts().index )
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 200,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 
    
plt.xticks(rotation=90) 
plt.show()



#%%

plt.figure(figsize=(12,5))
total = float(len(df["income2"]) )

ax = sns.countplot(x="education", hue="income2", data=df,  order = df["education"].value_counts().index )
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/1.6,
            height + 100,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 

plt.legend(loc='upper right')
plt.show()




