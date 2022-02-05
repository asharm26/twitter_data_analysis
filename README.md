# twitter_data_analysis

A twitter data processor for finding popular hashtags and mentions from the tweets within every past hour.


Steps to get the project running:
1. Run: https://github.com/asharm26/twitter_data_analysis/blob/main/Installations.py
    This is to install the required Python packages.
2. Run: https://github.com/asharm26/twitter_data_analysis/blob/main/configs.py
    This is a file containing config information for connecting to tweepy API. It has all the required fields and they are masked
    Visit https://developer.twitter.com/en to generate the required keys
3. Run: https://github.com/asharm26/twitter_data_analysis/blob/main/connection.py
    This is for getting a Twitter API client to talk to Twitter APIs
4. Run: https://github.com/asharm26/twitter_data_analysis/blob/main/process_tweets_script.py
    This is the main script to extract data, process it for popular trends (tweets, hashtags and mentions)
    The `search_query` param can be changed to whatever suits the needs
    Everytime this script is run, it will generate a new directory with the timestamp and have raw and processed data for the past hour to when it was run.
    
 Hope these instructions help.
 
 This is the overall architecture of the system designed:
 https://github.com/asharm26/twitter_data_analysis/blob/main/system_design.png
