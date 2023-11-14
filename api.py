import facebook
from datetime import datetime

page_token='XXX' #Facebook page access token
page_id='123456' #Facebook page id
graph=facebook.GraphAPI(access_token=page_token,version="3.0")
# posts_2019 = graph.get_all_connections(id=page_id,
#                                        connection_name='posts',
#                                        fields='comments',
#                                        )
# # print(posts_2019)
# for ind, post in enumerate(posts_2019):
#     print(ind, post)
# default_info = graph.get_object(id="2033255143590275",fields="posts")
# # for p in default_info:
# #     print(p.get_object(fields))
# print(default_info)

p=graph.get_object(id=page_id)
                   # fields='posts.fields(comments.fields(data.fields(id)))')

print(p)
post_1=p['posts']['data'][0]
post_2=p['posts']['data'][1]
post_3=p['posts']['data'][2]
post_4=p['posts']['data'][3]
post_5=p['posts']['data'][4]

print(post_1)

