
import matplotlib.pyplot as plt
#working fine
import facebook
import textblob
from datetime import datetime
import requests
from textblob import TextBlob
message=['Nice☺️', 'True', 'Worst', 'Really!!!','Nice','Nice☺️', 'True', 'Worst', 'Really!!!','Nice','Looks are awesome.','Battery backup is excellent.',' Camera is good.The display light quality is good.',
        'Although this is good mobile, looks good, but Problem is that it doesn’t provide separate Space for dual SIM & memory card together.',
         'Not good one as expected.',' Camera quality very poor.','today is a rainy day','ok','yes please,but promote whole newsdn']


positive_pol=0
negative_pol=0
neutral_pol=0

for m in message:
    print(m)
    analysis=TextBlob(m)
    x=analysis.sentiment.polarity
    if(x>0):
        positive_pol+=x
        print("pos***")

    elif(x<0):
        negative_pol+=x
        print("neg***")
    else:
        neutral_pol+=1
        print(neutral_pol)
        print("neut***")
print(positive_pol)
print(negative_pol)
print(neutral_pol)

data=[]
data.append(positive_pol)
data.append(abs(negative_pol))
data.append(neutral_pol)
result=["Positive","Negative","Neutral"]
plt.pie(data, labels=result ,startangle=90, autopct='%.1f%%')
plt.show()