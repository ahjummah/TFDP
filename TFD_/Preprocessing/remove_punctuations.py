import string
import csv

def removePunctuations(tweet):

     out = tweet.translate(None, r"!\"#$%&'()*+,./:;<=>?-[\]^_`{|}~")
     out = out.translate(None, '0123456789')
     tweet = out.split(" ")
     for word in tweet:
         if "@" in word:
             tweet.remove(word)

     return ' '.join(tweet)




if __name__ == "__main__":

    tweets = []

    with open("../Training_Dataset/2500_training_data_2.csv",'r') as r, open("../Training_Dataset/2500_training_data_3.csv", 'a') as w:
        reader = csv.DictReader(r)

        fieldnames = ['tweet','label']
        writer = csv.DictWriter(w, fieldnames=fieldnames)

        for row in reader:
            tweets.append(row)
            
        writer.writeheader()

        for t in tweets:
            ar = t['tweet'].lower()
            writer.writerow({'tweet': removePunctuations(ar), 'label':t['label']})
