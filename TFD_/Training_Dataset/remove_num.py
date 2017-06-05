import string
import csv
import regex as re

def removeNums(tweet):

     out = tweet.translate(None, '0123456789')
     return out

if __name__ == "__main__":

    tweets = []

    with open("2500_training_data.csv",'r') as r, open("2500_training_data_2.csv", 'a') as w:
        reader = csv.DictReader(r)

        fieldnames = ['tweet','label']
        writer = csv.DictWriter(w, fieldnames=fieldnames)

        for row in reader:
            tweets.append(row)
        writer.writeheader()

        for t in tweets:
            ar = t['tweet'].lower()
            writer.writerow({'tweet': removeNums(ar), 'label':t['label']})
