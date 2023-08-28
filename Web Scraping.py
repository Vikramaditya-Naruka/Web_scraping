#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests beautifulsoup4 pandas


# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[4]:


row_data=requests.get("https://www.flipkart.com/search?q=best+mobile+phone+5g&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1")


# # extract all Data from filpkard website¶

# In[6]:


soup=BeautifulSoup(row_data.content)

for i in range(2,248):
    row_data=requests.get("https://www.flipkart.com/search?q=best+mobile+phone+5g&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i))
    soup.append(BeautifulSoup(row_data.content))




# # step 1 extract price class and Create Dataframe

# In[10]:


x=soup.select("._4rR01T")
name=[]
for i in x:
#     print(i.contents[0])
    name.append((i.contents[0]))


# In[11]:


len(name)
# print(name)
df_name=pd.DataFrame(name,columns=["details"])


# In[9]:


df_name


# # step 2 extract price class and Create Dataframe

# In[12]:


x=soup.select("._30jeq3")
price=[]
for i in x:
    price.append((i.contents[0]))


# In[13]:


df_price=pd.DataFrame(price,columns=["price"])


# In[14]:


df_price.head()


# # step 3 Extract review class and Create Dataframe

# In[15]:


x=soup.select("._3LWZlK")
review=[]
for i in x:
    review.append((i.contents[0]))


# In[16]:


df_review = pd.DataFrame(review,columns=["review"])


# In[17]:


df_review.head()


# # step 4 Concat all DataFrame

# In[18]:


df=pd.concat((df_name,df_price,df_review),axis=1)


# In[21]:


df=df.dropna()


# In[22]:


df.head()


# # step 5 appling feature engineering technique for clean data

# In[23]:


# convert data in lower case

def lower_case(text):
    return text.lower()

columns=df.columns
# print(columns)
for i in columns:
    df[str(i)]=df[str(i)].apply(lower_case)

df.head()


# In[24]:


# extract company name from details column

df["company"]=df["details"].str.split(" ",expand=True)[0]


# In[25]:


# extract model name from details column

df["model"]=df["details"].str.split(" ",expand=True)[1] +" "+ df["details"].str.split(" ",expand=True)[2]


# In[26]:


df.head()


# In[27]:


# extract color  from details column

df["color"]=df["details"].str.split(" ",expand=True)[3]


# In[28]:


df.head()


# In[30]:


import re

# create function for extract only digit from text
def integer(text):
    a=re.findall("\d",text)
    b="".join(a)
    return int(b)

#create function for remove Punctuation
def Punctuation_remove(text):
    if text !=" ":
        a=re.findall("\w",text)
        b="".join(a)
    return b


# In[31]:


df["price"]=df["price"].astype(str)
df["color"]=df["color"].astype(str)


# In[32]:


# apply function

df["price"]=df["price"].apply(integer)
df["color"]=df["color"].apply(Punctuation_remove)


# In[33]:


df.head()


# In[34]:


color=["sunrise","midnight","purple","starlight","blue","black","red"]


# In[35]:


def remove_color(text):
    if text in color:
        return text
    else :
        return "White"


# In[36]:


df["color"]=df["color"].apply(remove_color)


# In[37]:


df.head()


# In[38]:


df["model"]=df["model"].astype(str)
df["model"]=df["model"].apply(Punctuation_remove)


# In[39]:


df.head()


# In[40]:


df=df.drop("details",axis=1)


# In[41]:


df


# In[42]:


df["company"]=df["company"].apply(Punctuation_remove)


# In[43]:


df


# In[44]:


df.info()


# In[45]:


df["price"]=df["price"].astype(str)
df["tag"]=df["company"] +" "+df["model"]+" "+df["color"]+" "+df["price"]+" "+df["review"]


# In[46]:


df.head()


# In[47]:


df.shape


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send an HTTP GET request to the website
url = "https://quotes.toscrape.com/"
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract quotes and authors from the HTML
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Create a list of dictionaries to store the data
data = []
for quote, author in zip(quotes, authors):
    data.append({"Quote": quote.text, "Author": author.text})

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[49]:





# In[ ]:




