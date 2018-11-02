import praw
import pandas as pd
import datetime as dt
import datetime
from datetime import timezone
import re
import re
from credentials import *
import sys
from slacker import Slacker
 
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')
slack = Slacker('xoxb-656-67756-hfjfjjjhjhfhj')
dff = pd.read_csv("reddit.csv")
for index, row in dff.iterrows():
    rdt = row['reditname']
    domain = row['domain']
    print(rdt)
    print(domain)
    subreddit = reddit.subreddit(rdt)
    top_subreddit = subreddit.new(limit=1000)
    topics_dict = {"title": [],
                   "score": [],
                   "id": [], "url": [],
                   "comms_num": [],
                   "created": [],
                   "body": []}
    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)
 
    topics_data = pd.DataFrame(topics_dict)
 
    def get_date(created):
        return dt.datetime.fromtimestamp(created)
    _timestamp = topics_data["created"].apply(get_date)
    topics_data = topics_data.assign(
        timestamp=_timestamp).sort_values(by=['timestamp'])
    created_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=15)
 
    topics_data = topics_data[(topics_data['timestamp'] > created_time) & (
        topics_data['timestamp'] < datetime.datetime.utcnow())]
    my_list = ['Maintenance', 'Scheduled', 'downtime', 'Voice',
                'Outage', 'Interruption', 'microphone','chat']
    ndata = topics_data[topics_data['title'].str.contains(
        "|".join(my_list), regex=True, flags=re.IGNORECASE)].reset_index(drop=True)
 
    print(ndata)
    if len(ndata['title']) > 0:
        slack.chat.post_message(
            '#reddit', domain + ': ' + ndata['title'] + ndata['url'])
    else:
        print('hi')
