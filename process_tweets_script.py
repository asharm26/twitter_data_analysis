#!/usr/bin/env python
# coding: utf-8

# In[4]:


# script to download data periodically for the past hour and process data


# In[80]:


import tweepy
import pandas as pd
import numpy as np
import requests
import os
import connection
import configs
from datetime import datetime, timedelta
import pytz
import re
from collections import Counter


# In[92]:


# search query (can be changed easily)

# search_query = 'covid -is:retweet'
search_query = 'covid'


# In[93]:


# make call to Twitter API for results

previous_hour = (datetime.now() - timedelta(hours = 1)).astimezone(pytz.utc)

paginator_tweets = tweepy.Paginator(
    connection.tweepy_client.search_recent_tweets,
    query=search_query,
    tweet_fields=['created_at', 'lang', 'author_id', 'entities'], 
    start_time=previous_hour,
    max_results=100,
).flatten(limit=50000)


# In[94]:


# Process tweets.txt file

df = pd.DataFrame(paginator_tweets)
df = df.replace(r'\n','\t', regex=True)
df['json'] = df.apply(lambda x: x.to_json(), axis=1)


# In[95]:


# make directory for current hour processing and save processed files there

dir = os.path.join(str(previous_hour))
os.makedirs(dir)
np.savetxt(f'{dir}/tweets.txt', df['json'], fmt='%s', delimiter='\t')


# In[96]:


# Process tweets_text.txt file

tweets_read = pd.read_json(f'{dir}/tweets.txt', lines=True)
df = pd.DataFrame(tweets_read)
df = df.replace(r'\t','\n', regex=True)
np.savetxt(f'{dir}/tweets_text.txt', df.text, fmt='%s', delimiter='\n')


# In[97]:


# Process Hashtags

hashtags = []
i=0
file_reader = open(f'{dir}/tweets_text.txt','r')
for line in file_reader:
    hashtags += re.findall(r'#(\w+)', line)
counter_dict = dict(Counter(hashtags))
sorted_hashtags = dict(sorted(counter_dict.items(), key=lambda item: item[1], reverse=True))

file_name=f'{dir}/hashtags.txt'
with open(file_name, 'a+') as file_writer:
    for item in sorted_hashtags:
        file_writer.write("%s %s\n" % (item, sorted_hashtags[item]))


# In[98]:


# Process Mentions

import re
from collections import Counter
mentions = []
i=0
file_reader = open(f'{dir}/tweets_text.txt','r')
for line in file_reader:
    mentions += re.findall("@([a-zA-Z0-9_]{1,50})", line)
counter_dict = dict(Counter(mentions))
sorted_mentions = dict(sorted(counter_dict.items(), key=lambda item: item[1], reverse=True))

file_name=f'{dir}/mentions.txt'
with open(file_name, 'a+') as file_writer:
    for item in sorted_mentions:
        file_writer.write("%s %s\n" % (item, sorted_mentions[item]))


# In[ ]:




