#working fine
import facebook
import textblob
from datetime import datetime
import requests
from textblob import TextBlob

page_token='XXX' #Facebook page access token
page_id='12345' #Facebook page id

graph = facebook.GraphAPI(page_token)
profile = graph.get_object(page_id)
posts = graph.get_connections(profile['id'], 'posts')
comments = []
message=[]
c=[]
for post in posts["data"]:
    first_comments = graph.get_connections(id=post["id"], connection_name="comments")
    comments.extend(first_comments["data"])
    # while True:
    #     try:
    #         next_comments =  requests.get(post["paging"]["next"]).json()
    #         comments.extend(next_comments["data"])
    #         print("********************************************")
    #     except KeyError:
    #         break

for comment in comments:
    message.append(comment["message"])
# print(comments)
positive_pol=0
negative_pol=0
neutral_pol=0
print(message)
for m in message:
    analysis=TextBlob(m)
    x=analysis.sentiment.polarity
    if(x>0):
        positive_pol+=x
    elif(x<0):
        negative_pol+=x
    else:
        neutral_pol+=x
    print(x)
print("**********")
print(positive_pol)
print(negative_pol)
print(neutral_pol)
