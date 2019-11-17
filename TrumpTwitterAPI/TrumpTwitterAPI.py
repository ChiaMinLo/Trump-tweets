import GetOldTweets3 as got
import csv
import datetime
import re

startDate="2017-01-20"
endDate=(datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")

def remove_picture(sample):
    return re.sub(r'pic.twitter.com\S+', "", sample)


csvFile = open(startDate+'_'+datetime.datetime.now().strftime("%Y-%m-%d")+'.csv','w',newline='',encoding='utf_8_sig')
csvWriter = csv.writer(csvFile)


tweetCriteria = got.manager.TweetCriteria().setUsername("realDonaldTrump")\
                                           .setSince(startDate)\
                                           .setUntil(endDate)
                                           
tweets = got.manager.TweetManager.getTweets(tweetCriteria);

for tweet in tweets:
    tweet.text=remove_picture(tweet.text)
    tweet.text=tweet.text.partition("https")[0]
    csvWriter.writerow([tweet.date,tweet.text])
   

   

csvFile.close()
                             





