from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


message=['Nice☺️', 'True', 'Worst', 'Really!!!','Nice','Nice☺️', 'True', 'Worst', 'Really!!!','Nice.looking awesome.do something better.best dale ever.wow.hfgxcbjchfdhkdfhih','Looks are awesome.','Battery backup is excellent.',' Camera is good.The display light quality is good.',
        'Although this is good mobile, looks good, but Problem is that it doesn’t provide separate Space for dual SIM & memory card together.',
         'Not good one as expected.',' Camera quality very poor.','today is a rainy day','ok','yes please,but promote whole newsdn']
#tagcloud
comment_words = ' '
stopwords = set(STOPWORDS)
for words in message:
    comment_words = comment_words + words + ' '

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
