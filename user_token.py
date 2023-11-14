import facebook
from datetime import datetime

# page_token='XXX'
user_token='XXX'

user_id='12345'
graph=facebook.GraphAPI(access_token=user_token,version="3.0")
p=graph.get_object(id=user_id,fields='accounts')
print(p)
po = graph.get_connections(user_id,'accounts')
print(po)
for i in po["data"]:
    first_comments = i['access_token']
    print(i['id'])
    print(i['name'])
    print(first_comments)

xx=graph.get_all_connections(id=user_id,connection_name='accounts',
                                       fields='access_token,id',
                                       )

print(xx)
