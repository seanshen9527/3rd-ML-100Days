#!/usr/bin/env python
# coding: utf-8

# In[11]:


target_url = 'https://raw.githubusercontent.com/vashineyu/slides_and_others/master/tutorial/examples/imagenet_urls_examples.txt'

import requests
response = requests.get(target_url)
data = response.text

split_tag = '\n'
data = data.split(split_tag)

def split_data(data):
    name=[]
    url=[]
    for i in data:
        name.append(i.split("\t")[0])
        try:    
            url.append(i.split("\t")[1])
        except :
            url.append("")
    data_dict = {'name': name,
                'url':url}
    return data_dict

import pandas as pd
data=split_data(data)
df_data = pd.DataFrame(data)

from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

first_link = df_data.iloc[0,1]
#first_link = df_data.loc[0][1]

response = requests.get(first_link)
img = Image.open(BytesIO(response.content))

plt.imshow(img)
plt.show()


# In[6]:


def img2arr_fromURLs(url_list, resize = False):
    img_list=[]
    for url in url_list:
        response = requests.get(url)
        try:
            img=Image.open(BytesIO(response.content))
        except :
            pass
        else:
            img_list.append(img)
    return img_list

result = img2arr_fromURLs(df_data['url'][0:5])
print("Total images that we got: %i " % len(result)) # 如果不等於 5, 代表有些連結失效囉

for im_get in result:
    plt.imshow(im_get)
    plt.show()

