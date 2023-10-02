
Customer churn is a critical issue for businesses, including telecom companies, subscription services, and more. Identifying and understanding the factors that lead to churn can help businesses take proactive measures to retain their customers. In this data science project, we will use historical data to predict customer churn rate. The objective is to build a machine learning model that can predict whether a customer is likely to churn based on their historical behavior and characteristics.

Project - Option 2: Imagine you're working with Sprint, one of the biggest telecom companies in the USA. They're really keen on figuring out how many customers might decide to leave them in the coming months. Luckily, they've got a bunch of past data about when customers have left before, as well as info about who these customers are, what they've bought, and other things like that. So, if you were in charge of predicting customer churn, how would you go about using machine learning to make a good guess about which customers might leave? What steps would you take to create a machine learning model that can predict if someone's going to leave or not?

### Data collection

Generate the data you need to run the project by describing the data on sites such as *<https://www.mockaroo.com/>*

### Initialize a Jupyter file

```
jupyter notebook churn_rate_measurement.ipynb
```

### Installing dependences

Import the dependences you need to run and complete this project on Jupyter notebook

```python
#importing dependencies
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas_profiling
import plotly.offline as po
import plotly.graph_objs as go
%matplotlib inline
```

### Import Customer Churn Dataset

```python
churn_dataset = pd.read_csv('Tel_Customer_Churn_Dataset.csv')
```

### Perform Exploratory Data Analysis in just one line of code

```python
pandas_profiling.ProfileReport(pd.read_csv('Tel_Customer_Churn_Dataset.csv'))
```

### Number of Columns and Rows in the Dataset

churn_dataset.shape

### Convert String values (Yes and No) of Churn column to 1 and 0

churn_dataset.loc[churn_dataset.Churn=='No','Churn'] = 0
churn_dataset.loc[churn_dataset.Churn=='Yes','Churn'] = 1

### Replace all the spaces with null values

```python
churn_dataset['TotalCharges'] = churn_dataset["TotalCharges"].replace(" ",np.nan)
```

### Drop null values of 'Total Charges' feature

```python
churn_dataset = churn_dataset[churn_dataset["TotalCharges"].notnull()]
churn_dataset = churn_dataset.reset_index()[churn_dataset.columns]

```

### Convert 'Total Charges' column values to float data type

```python
churn_dataset["TotalCharges"] = churn_dataset["TotalCharges"].astype(float)
```

### Visualize Total Customer Churn

```python
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
```

Predicting customer churn is a valuable use case in data science that can help businesses reduce customer attrition and increase customer retention. By following this project's Jupyter notebook, you will learn how to preprocess data, build predictive models, and deploy a churn rate prediction system using historical customer data.
