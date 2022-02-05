#!/usr/bin/env python
# coding: utf-8

# In[1]:


# make connection to twitter API and get client


# In[ ]:

import tweepy
import configs

tweepy_client = tweepy.Client(
    bearer_token=configs.bearer_token,
)

