# RedditBot_for_slack
 setting up a Reddit bot to monitor realtime subreddit headlines about user sentiments and getting that into slack channel and visualizing as a time series graph.
![logo](https://user-images.githubusercontent.com/8762047/47928585-1ea28800-de9d-11e8-87a0-afa984d06e2d.png)
Hello Everyone, Reddit is one of the biggest social news aggregation in United states. All the members can post about anything in related subreddit. If you are having a product which lots of people are using then getting to know what they are feeling about the product is really important. Social media platforms like facebook, Twitter, reddit etc. are one of the most widely used by people. Reddit is also a discussion forum where people can talk and discuss about anything. Almost all products whether its microsoft Azure or AWS are having their subreddits on which they communicate with their users. So, What if you want to know about the sentiments of users and get all the negative headlines from a subreddit so that you can improve the product accordingly or if you want to interact with user in real time. Here I will be explaining that how you can get notification in slack with the URL link of the headlines if any user is starting a negative discussion about a product related to you in real time.
Now, apart from that suppose you also want to see a time series graph that how frequent users are talking negative for your product and you want to visualize that in some form so that you can see how many negative headlines are there and how many people have up-voted on those headlines and how many people are engaged on those headlines. 
I guess by now you must have got an idea what i am trying to achieve. Suppose you are a company who provide voice services to big games like PUBG, Fortnite, Call of Duty, World of tanks etc and you want to see what people are talking about online about the voice services. If lots of people are up-voting a headline then it means its a generic issue and you can work on that in real time. But if there are few upvotes then may be the problem is at user end like low speed or something.
So, Lets start.
1.) First we need few details like below which can be created by going on twitter and follow the instruction on https://redditclient.readthedocs.io/en/latest/oauth/
you can use your own reddit account for that there is not need of using official vivox account and i am not aware if we even have any official reddit account or not.
client_id='client_id', \
client_secret='client_secret', \
user_agent='user_agent', \
username='username', \
password='password'
2.) To interact with slack we need to create a slack bot API which you can create by following instruction on the below you tube:-
SLACK API = 'xoxb-44323424–234324243-dfsdfdsfsf'

3.)we will also be maintaining a csv file in which we will be maintaining client twitter name information in the format like below:-

![1 8o9w-ctbjnjx3y1hj7a2ha](https://user-images.githubusercontent.com/8762047/47929248-dbe1af80-de9e-11e8-801d-84f9a57e5887.png)

4.) we need some libraries to set up the whole process. So, please install the below libraries into your environment:-

<img width="494" alt="screen shot 2018-11-02 at 12 43 16 pm" src="https://user-images.githubusercontent.com/8762047/47928586-1ea28800-de9d-11e8-8a23-4218c63d4eac.png">

5.)After that we will setup setup the reddit with praw method as praw is the api to interact with reddit data. if you want to read more about praw please go here https://praw.readthedocs.io/en/latest/.

<img width="559" alt="screen shot 2018-11-02 at 12 43 23 pm" src="https://user-images.githubusercontent.com/8762047/47928587-1ea28800-de9d-11e8-9a6e-7316dddd919f.png">

6.)Then we will read the CSV file into a panda's dataframe. The CSV file is having all the details of the subreddit and if you need to add or delete any subreddit, you can do that in the CSV file and there will be no need to edit the python script.

<img width="357" alt="screen shot 2018-11-02 at 12 43 29 pm" src="https://user-images.githubusercontent.com/8762047/47928588-1ea28800-de9d-11e8-94fc-7e84ef9ee1c5.png">

7.)After that as we are doing this dynamically so we will be creating two variables one is to read the subreddit name and the other will be client name.

<img width="425" alt="screen shot 2018-11-02 at 12 43 36 pm" src="https://user-images.githubusercontent.com/8762047/47928589-1ea28800-de9d-11e8-94fe-e60ee53f4529.png">

8.) Now, we will read the headlines from the subreddit. As we are building a dynamic bot here so we will be reading just the new headlines and to do that we will follow the below line of code. Here first we are taking the subreddit name into a variable subreddit and then we are reading just the new comments here. I have passed here limit = 1000 which you can pass as None as well but you won't be able to get more than 1000 headlines and by default its 100.

<img width="486" alt="screen shot 2018-11-02 at 12 43 44 pm" src="https://user-images.githubusercontent.com/8762047/47928590-1ea28800-de9d-11e8-8dc8-7bf7233e354b.png">

9.) So, what if you need all the historic headlines. We don't need it here but if you want to download all of that you can use the pushshiftapi ( https://github.com/pushshift/api) for that :-

<img width="1449" alt="screen shot 2018-11-02 at 12 43 53 pm" src="https://user-images.githubusercontent.com/8762047/47928591-1ea28800-de9d-11e8-9bf7-ba36eb460795.png">

10.) Now we will create a dictionary for they keys which we will be reading from reddit. there are 95 different values reddit provides but we don't need all of them. As per our requirement i am using the below.

<img width="589" alt="screen shot 2018-11-02 at 12 44 01 pm" src="https://user-images.githubusercontent.com/8762047/47928592-1ea28800-de9d-11e8-9c61-e3308f694669.png">

11.) Once we declare the structure of the dictionary now its time to read the data into that dictionary from the reddit:-

<img width="709" alt="screen shot 2018-11-02 at 12 44 08 pm" src="https://user-images.githubusercontent.com/8762047/47928593-1f3b1e80-de9d-11e8-8e7f-d433fa2b6437.png">

12.) Finally, we have the data and now we will convert that into a pandas data frame to perform further operation on that:-
<img width="511" alt="screen shot 2018-11-02 at 12 44 14 pm" src="https://user-images.githubusercontent.com/8762047/47928594-1f3b1e80-de9d-11e8-89ad-c9a816d78072.png">

13.) Reddit always give time in epoch format and we need a general time stamp to read perform manipulation on that:-

<img width="857" alt="screen shot 2018-11-02 at 12 44 20 pm" src="https://user-images.githubusercontent.com/8762047/47928596-1f3b1e80-de9d-11e8-8060-56270c0509c5.png">

14.) Now, its time to decide what should be the time interval of our bot, lets say you want to do this every 15 minutes. Also, as reddit and yor timezone could be different so its always a wise thing to go for a common timezone and that is why i am converting both into UTC.

<img width="1144" alt="screen shot 2018-11-02 at 12 44 27 pm" src="https://user-images.githubusercontent.com/8762047/47928597-1f3b1e80-de9d-11e8-9207-71a5a70a86f2.png">

15.) Now, its time to filter out the headlines which you can do by following the below code:-

<img width="1254" alt="screen shot 2018-11-02 at 12 44 33 pm" src="https://user-images.githubusercontent.com/8762047/47928600-1f3b1e80-de9d-11e8-9727-dcb32499c1d4.png">

16.) post it in the slack channel:-

<img width="917" alt="screen shot 2018-11-02 at 12 44 38 pm" src="https://user-images.githubusercontent.com/8762047/47928601-1f3b1e80-de9d-11e8-840f-d2fca52ac07b.png">

17.) Now, What if we want to store the data into some DB and visualize that on grafana. I am using InfluxDB here so just replace the step 15 with below code and the data will be stored in InfluxDB.

<img width="1187" alt="screen shot 2018-11-02 at 12 44 44 pm" src="https://user-images.githubusercontent.com/8762047/47928602-1f3b1e80-de9d-11e8-8f13-063214778597.png">

18.) Setup Grafana for time series visualization and you will get the graph liek below .In the above graph we can see that at midnight some posted a headline and 247 people upvoted it and 115 people commented on it in just 15 minutes. So, that's a concern. The grafana dashboard will be looking like below :-

<img width="1281" alt="screen shot 2018-11-02 at 12 57 03 pm" src="https://user-images.githubusercontent.com/8762047/47929247-dbe1af80-de9e-11e8-8389-23b48e7ecdc5.png">
