import GetOldTweets3 as got
import csv

startDate="2017-01-20"
endDate="2019-11-16"



csvFile = open(startDate+'_'+endDate+'.csv','w',newline='',encoding='utf_8_sig')
csvWriter = csv.writer(csvFile)


tweetCriteria = got.manager.TweetCriteria().setUsername("realDonaldTrump")\
                                           .setSince(startDate)\
                                           .setUntil(endDate)
                                           
tweets = got.manager.TweetManager.getTweets(tweetCriteria);

for tweet in tweets:
    
    csvWriter.writerow([tweet.date,tweet.text])
    
   

csvFile.close()
                             





