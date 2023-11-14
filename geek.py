#text blob polarity crct percentage & piechart

import matplotlib.pyplot as plt
import facebook
import re
import textblob
from datetime import datetime
import requests
from textblob import TextBlob

message=['Nice☺️', 'True', 'Worst', 'Really!!!','Nice','Nice☺️', 'True', 'Worst', 'Really!!!','Nice','Looks are awesome.','Battery backup is excellent.',' Camera is good.The display light quality is good.',
        'Although this is good mobile, looks good, but Problem is that it doesn’t provide separate Space for dual SIM & memory card together.',
         'Not good one as expected.',' Camera quality very poor.','today is a rainy day','ok','yes please,but promote whole newsdn']

# print(comments)
positive_pol=0
negative_pol=0
neutral_pol=0
print(message)
for m in message:
    print(m)
    ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", m).split())
    analysis=TextBlob(m)
    x=analysis.sentiment.polarity
    if(x>0):
        positive_pol+=1
        print("pos***")
    elif(x<0):
        negative_pol+=1
        print("neg***")
    else:
        neutral_pol+=1
        print("neutral**")


print("Positive percentage: {} %".format(100*positive_pol/len(message)))

print("Negative percentage: {} %".format(100*negative_pol/len(message)))
print("Neutral  percentage: {} % ".format(100*neutral_pol/len(message)))

print("**********")
print(positive_pol)
print(negative_pol)
print(neutral_pol)

#piechart
data=[]
data.append(positive_pol)
data.append(negative_pol)
data.append(neutral_pol)
result=["Positive","Negative","Neutral"]
plt.pie(data, labels=result ,startangle=90, autopct='%.1f%%')
plt.show()