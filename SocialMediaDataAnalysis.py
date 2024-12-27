#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[2]:



'/opt/conda/bin/python3 -m pip install --upgrade pip'


# In[10]:


import pandas as pd
import random
import numpy as np

# Define the list of categories
categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']

# Generate random data with 500 entries
n = 500

# Create a dictionary to store the data
data = {
    'Date': pd.date_range('2021-01-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

print(df.head())


# In[11]:


df.describe()
#THis command ignores non numerial values


# In[12]:


df.describe(include='all')


# In[13]:


df.dtypes
#to check the data types in dataset


# In[14]:


df.info()


# In[15]:


df.loc[df['Category'] == "Health"] 


# In[16]:


df.isnull().sum()
#to check missing values.


# In[17]:


unique_categories = df['Category'].unique() 
print(unique_categories)


# In[18]:


category_counts = df['Category'].value_counts()
print(category_counts)
#This code is to determine the occurrence of each category


# In[21]:


# Group by 'Category' and aggregate the counts and sum of likes
category_stats = df.groupby('Category').agg(
    count_of_tweets=('Category', 'count'),
    total_likes=('Likes', 'sum')
).reset_index()

# Display the result
print(category_stats)


# In[23]:


import matplotlib.pyplot as plt

# Plotting the bar chart
fig, ax1 = plt.subplots()

# Bar chart for count of tweets
ax1.bar(category_stats['Category'], category_stats['count_of_tweets'], color='b', alpha=0.7)
ax1.set_xlabel('Category')
ax1.set_ylabel('Count of Tweets', color='b')
ax1.tick_params('y', colors='b')

# Create a second y-axis for the likes data
ax2 = ax1.twinx()
ax2.plot(category_stats['Category'], category_stats['total_likes'], color='r', marker='o', linestyle='dashed')
ax2.set_ylabel('Total Likes', color='r')
ax2.tick_params('y', colors='r')

plt.title('Counts of Tweets and Total Likes by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:


# Based on the barplot above,fitness has most likes with 65 tweets,travel is second most likes with only 62 tweets 
#compared to music with highest tweets but lesser likes.However the most engaged category based on likes is fitness,followed by
#Travel category,third is Music and Family.


# In[115]:


plt.figure(figsize=(12, 8))
sns.boxplot(x='Category', y='Likes', data=df)
plt.title('Box Plot of Likes by Category')
plt.xlabel('Category')
plt.ylabel('Likes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[118]:


plt.figure(figsize=(12, 8))
plt.scatter(df['Date'], df['Likes'], c=df['Category'].astype('category').cat.codes, cmap='viridis')
plt.colorbar(label='Category')
plt.title('Scatter Plot of Likes by Date')
plt.xlabel('Date')
plt.ylabel('Likes') 
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()


# In[ ]:


# This scatter plot shows a very weak relationship between category,likes and date.All variables are independent of each other.


# In[28]:


Category =['Culture','Family','Fashion','Fitness','Food','Health','Music','Travel']
count_of_tweets =[69,41,67,55,63,76,67,62]
plt.bar(Category,count_of_tweets)
plt.xlabel('category')
plt.ylabel('count_of_tweets')
plt.title('Category and count of tweets')
plt.show()


# In[ ]:


#Health is the most engaged category based on number of tweets,followed by culture and fashion.


# In[121]:


plt.figure(figsize=(12, 8))
sns.boxplot(x='Category', y='Likes', data=df)
plt.title('Box Plot of Likes by Category')
plt.xlabel('Category')
plt.ylabel('Likes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:


#No outlier found in category and likes.


# In[126]:


categories = df['Category'].unique()

# Set up the figure and axes
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(16, 10), sharey=True)
axes = axes.flatten()

# Plot histograms for each category
for i, category in enumerate(categories):
    ax = axes[i]
    subset = df[df['Category'] == category]
    ax.hist(subset['Likes'], bins=30, edgecolor='black')
    ax.set_title(category)
    ax.set_xlabel('Likes')
    ax.set_ylabel('Frequency')

# Add a main title
fig.suptitle('Histograms of Likes by Category', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to fit the main title

plt.show()


# In[57]:


df.loc[df['Category'] == "Health"].mean()


# In[60]:


round(5342.289474,0)


# In[58]:


df.loc[df['Category'] == "Family"].mean()


# In[68]:


round(4861.926829,0)


# In[63]:


df.loc[df['Category'] == "Fitness"].mean()


# In[64]:


round(4577.672727,0)


# In[66]:


df.loc[df['Category'] == "Food"].mean()


# In[67]:


round(4857.84127,0)


# In[69]:


df.loc[df['Category'] == "Culture"].mean()


# In[70]:


round(5481.101449,0)


# In[71]:


df.loc[df['Category'] == "Music"].mean()


# In[72]:


round(5538.253731,0)


# In[73]:


df.loc[df['Category'] == "Travel"].mean()


# In[74]:


round(4902.774194,0)


# In[75]:


df.loc[df['Category'] == "Fashion"].mean()


# In[76]:


round(5429.38806,0)


# In[ ]:


#Based on the average total likes of category,music has the most likes,followed by Culture and Fashion with
#very little difference.Health has the fourth position of average total likes,followed by Travel, Family,Food
#and fitness has least total average likes.


# In[ ]:


# To conclude from the above charts and statistical analysis,the number of tweets does not guarantee or determine the likes 
#of the tweet irrespective of the date.Therefore,I recommend for example heath has the highest tweets but lesser likes compare
#to other categories,could be improve by focus on interesting topics or general presentation of the tweet like design and colors.

