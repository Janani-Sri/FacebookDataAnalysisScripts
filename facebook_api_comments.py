#working fine
import facebook
page_token='XXX' #Facebook page access token
page_id='12345' #Facebook page id
graph = facebook.GraphAPI(page_token)
profile = graph.get_object(page_id)
print(profile)
posts = graph.get_connections(profile['id'], 'posts')
print(posts)
comments = []
message=[]
c=[]
for post in posts["data"]:
    first_comments = graph.get_connections(id=post["id"], connection_name="comments")
    comments.extend(first_comments["data"])
for comment in comments:
    message.append(comment["message"])
print(message)
