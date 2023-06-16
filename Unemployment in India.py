# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 02:33:27 2023

@author: Manu Singh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
print(data.head())

#Let’s see if this dataset contains missing values or not:

print(data.isnull().sum())


#While analyzing the missing values, It was found that the column names are not correct. So, for a better understanding of this data, we will rename all the columns:

#While analyzing the missing values, It was found that the column names are not correct. So, for a better understanding of this data, we will rename all the columns:

data.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]

#Now let’s have a look at the correlation between the features of this dataset:

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
sns.heatmap(data.corr())
plt.show()


#Unemployment Rate Analysis: Data Visualization

#While analyzing the missing values, It was found that the column names are not correct. So, for a better understanding of this data, we will rename all the columns:

data.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=data)
plt.show()


#Now let’s see the unemployment rate according to different regions of India:

plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=data)
plt.show()