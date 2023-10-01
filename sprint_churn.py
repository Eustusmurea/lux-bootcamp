#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing dependencies
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas_profiling
import plotly.offline as po
import plotly.graph_objs as go
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Perform Exploratory Data Analysis in just one line of code
pandas_profiling.ProfileReport(pd.read_csv('Tel_Customer_Churn_Dataset.csv'))


# In[3]:


#Import Customer Churn Dataset
churn_dataset = pd.read_csv('Tel_Customer_Churn_Dataset.csv')


# In[4]:


# Number of Columns and Rows in the Dataset
churn_dataset.shape


# In[6]:


# Convert String values (Yes and No) of Churn column to 1 and 0
churn_dataset.loc[churn_dataset.Churn=='No','Churn'] = 0 
churn_dataset.loc[churn_dataset.Churn=='Yes','Churn'] = 1


# In[7]:


# Replace all the spaces with null values
churn_dataset['TotalCharges'] = churn_dataset["TotalCharges"].replace(" ",np.nan)

# Drop null values of 'Total Charges' feature
churn_dataset = churn_dataset[churn_dataset["TotalCharges"].notnull()]
churn_dataset = churn_dataset.reset_index()[churn_dataset.columns]

# Convert 'Total Charges' column values to float data type
churn_dataset["TotalCharges"] = churn_dataset["TotalCharges"].astype(float)


# In[8]:


# Visualize Total Customer Churn
plot_by_churn_labels = churn_dataset["Churn"].value_counts().keys().tolist()
plot_by_churn_values = churn_dataset["Churn"].value_counts().values.tolist()

plot_data= [
    go.Pie(labels = plot_by_churn_labels,
           values = plot_by_churn_values,
           marker = dict(colors =  [ 'Teal' ,'Grey'],
                         line = dict(color = "white",
                                     width =  1.5)),
           rotation = 90,
           hoverinfo = "label+value+text",
           hole = .6)
]
plot_layout = go.Layout(dict(title = "Customer Churn",
                   plot_bgcolor  = "rgb(243,243,243)",
                   paper_bgcolor = "rgb(243,243,243)",))


fig = go.Figure(data=plot_data, layout=plot_layout)
po.iplot(fig)


# In[ ]:




