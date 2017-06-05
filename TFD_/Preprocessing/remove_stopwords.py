from cStringIO import StringIO
import csv

stop = ['we','our','ours','ourselves','he','him','his','himself', 'she', 'her', 'hers', 'herself', 'it',
    'its', 'itself','they','them','their','theirs','themselves','what','which','who','whom','this',
    'that','these','those','am','is','are', 'was','were','be', 'been', 'being','have','has','had',
    'having','do','does','did','doing','a', 'an','the','and','but','if','or','because','as','until',
    'while','of','at','by','for','with','about', 'against','between','into','through','during',
    'before','after','above','below','to','from','up','down','in','out','on','off','over','under',
    'again','further','then','once','here','there','when','where','why','how','all','any','both',
    'each','few','more','most','other','some','such','no','nor','only','own','same','so','than',
    'too','very','can','will','just','dont','should','now'
    ];



def remove_words(tweet):
    new_tweet = ""
    for i in tweet.lower().split():
         if i not in stop:
             new_tweet += i + " "
    return new_tweet

if __name__ == "__main__":
    tweets = []
    # with open('tweets-removed-punctuations-test.csv','r') as r, open('../Training_ Dataset/2500_training_data.csv','a') as w:
    # with open('TEST_2.csv','r') as r, open('TEST_out.csv','a') as w:
    with open("../Evaluating_Dataset/dataset_1_no_punc.csv",'r') as r, open("../Evaluating_Dataset/dataset_1_no_stop.csv", 'a') as w:

        reader = csv.DictReader(r)

        fieldnames = ['tweet','label']
        writer = csv.DictWriter(w, fieldnames=fieldnames)

        for row in reader:
            tweets.append(row)


        writer.writeheader()

        for t in tweets:
            ar = t['tweet'].lower()
            writer.writerow({'tweet': remove_words(ar), 'label':t['label']})
