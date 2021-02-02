#!/usr/bin/env python
# coding: utf-8

# ## scrapping the customer review data from online shopping website
# ## 1. Customer name
# ## 2. Review Title
# ## 3. No. of Stars
# ## 4.Review Content
# 

# In[12]:


from bs4 import BeautifulSoup as bs #importing the beautifulSoup librabry
import requests  #importing the Request librabry


# In[26]:


#getting the url of the site
link = "https://www.flipkart.com/sjcam-sj-4000-air-4k-full-hd-wifi-30m-waterproof-sports-action-camera-dv-camcorder-16mp/p/itm3f81a086c29fd?pid=SAYF956CJMBUUJFK&lid=LSTSAYF956CJMBUUJFKNMENUA&marketplace=FLIPKART&srno=b_1_1&otracker=hp_omu_Best%2Bof%2BElectronics_1_11.dealCard.OMU_N5LH0EUR1TXS_6&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_1_NA_view-all_6&fm=neo%2Fmerchandising&iid=eea52af7-f3bc-48a7-aa5a-1fa494c8576d.SAYF956CJMBUUJFK.SEARCH&ppt=browse&ppn=browse&ssid=vvmyj8uqww0000001612243045876"


# In[27]:


#fetching the whole content of the page
page = requests.get(link) 
page.content


# In[28]:


page #getting the status code


# In[29]:


#creating a soup variable to get data in proper html format
soup = bs(page.content,"html.parser") 


# In[30]:


#prettify organises the data in more easy to visualise way
print(soup.prettify()) 


# In[31]:


#finding the names of the customer
name = soup.find_all('p',class_='_2sc7ZR _2V5EHH') 


# In[36]:


print(name)


# In[38]:


len(name)


# In[40]:


#getting the data from the fetched customer name section
cust_name = [] 
for x in range(0,len(name)):
    cust_name.append(name[x].get_text())


# In[41]:


cust_name


# In[43]:


#getting the review name
name2 = soup.find_all('p',class_='_2-N8zT')
print(name2)


# In[44]:


##getting the data from the fetched customer name section
review_name = [] 
for x in range(0,len(name2)):
    review_name.append(name2[x].get_text())
    
review_name


# In[46]:


#getting the no. of stars
stars = soup.find_all('div',class_='_3LWZlK _1BLPMq')
print(stars)


# In[47]:


##getting the data from the fetched no. of stars
no_of_strs = [] 
for x in range(0,len(stars)):
    no_of_strs.append(stars[x].get_text())
    
no_of_strs


# In[49]:


#getting the review content
content = soup('div',class_='t-ZTKy')
print(content)


# In[50]:


##getting the data from the fetched no. of stars
review_content = []
for x in range(0,len(content)):
    review_content.append(content[x].get_text())
    
review_content


# In[51]:


import pandas as ps


# In[56]:


#saving the extracted data in csv format
df = ps.DataFrame()
df['cust_name']=cust_name
df['review_name']=review_name
df['no_of_strs']=no_of_strs
df['review_content']=review_content
df.to_csv(r'd:\scrapped_data.csv',index=True)
df


# In[53]:





# In[ ]:




