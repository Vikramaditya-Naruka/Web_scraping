#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[35]:


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
webpage = requests.get('https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=1',headers = headers).text


# In[36]:


soup = BeautifulSoup(webpage,'lxml')


# In[37]:


company = soup.find_all('div',class_="companyCardWrapper")


# In[38]:


len(company)


# In[39]:


name = []
rating = []
rating_count = []
about = []
for i in company:
    name.append(i.find('h2').text.strip())
    rating.append(i.find('span',class_="companyCardWrapper__companyRatingValue").text.strip() )
    rating_count.append(i.find('span',class_="companyCardWrapper__companyRatingValue").text.strip() )
    about.append(i.find('span',class_="companyCardWrapper__interLinking").text.strip() )


# In[40]:


df = pd.DataFrame(name)
df 


# In[9]:


d = {'Name':name ,'Rating': rating,'Reviews':rating_count,'About':about}
df = pd.DataFrame(d)


# In[ ]:





# In[10]:


s = df['About'].str.split(pat = '|',n =5,expand = True)


# In[11]:


df['Service'] = s[0]
df['Employees'] = s[1]
df['public'] = s[2]
df['old'] = s[3]
df['Located'] = s[4]


# In[12]:


df = df.drop(columns = ['About'])
df


# In[31]:


final = pd.DataFrame()
for j in range(1,501):
    url = 'https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={}'.format(j)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage = requests.get(url,headers = headers).text
    
    soup = BeautifulSoup(webpage,'lxml')
    company = soup.find_all('div',class_="companyCardWrapper")
    name = []
    rating = []
    rating_count = []
    About = []
    for i in company:
        name.append(i.find('h2').text.strip())
        rating.append(i.find('span',class_="companyCardWrapper__companyRatingValue").text.strip() )
        rating_count.append(i.find('span',class_="companyCardWrapper__companyRatingValue").text.strip() )
        about.append(i.find('span',class_="companyCardWrapper__interLinking").text.strip() )
        d = {'Name':name ,'Rating': rating,'Reviews':rating_count}
        df = pd.DataFrame(d)
    final = final.append(df,ignore_index = True)
    


final
    


# In[41]:


Result = pd.DataFrame()
for j in range(1,501):
    url = 'https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={}'.format(j)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage = requests.get(url,headers = headers).text
    
    soup = BeautifulSoup(webpage,'lxml')
    company = soup.find_all('div',class_="companyCardWrapper")
    About = []
    for i in company:
        About.append(i.find('span',class_="companyCardWrapper__interLinking").text.strip() )
        
        df = pd.DataFrame(About)
    Result = Result.append(df,ignore_index = True)    


# In[79]:


final['About'] = Result


# In[80]:


final.head()


# In[81]:


s = final['About'].str.split(pat = '|',n =5,expand = True)


# In[82]:


s


# In[83]:


final['Service'] = s[0]
final['Employees'] = s[1]
final['public'] = s[2]
final['old'] = s[3]
final['Located'] = s[4]


# In[84]:


final = final.drop(columns = ['About','Reviews'])


# In[85]:


final.head()


# In[86]:


final.shape


# In[88]:


final.to_csv('companies_detail.csv')


# In[ ]:




