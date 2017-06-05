
# coding: utf-8

# In[1]:


import pickle
import sys
from Preprocessing import remove_punctuations
from Preprocessing import remove_stopwords
from sklearn.utils import compute_class_weight
from sklearn.preprocessing import LabelEncoder
import numpy as np


# In[2]:


with open('Models/classifier.pkl', 'rb') as f:
    clf = pickle.load(f)
    
with open('Models/vectorizer.pkl', 'rb') as g:
    vectorizer = pickle.load(g)
    
with open('Models/lsa.pkl', 'rb') as h:
    lsa = pickle.load(h)
        


# In[3]:


a = raw_input("Enter:\n")
# a = "@ice you are so fucking stupid dude!"
a = remove_punctuations.removePunctuations(a)
a = remove_stopwords.remove_words(a)
print a
X = vectorizer.transform([a]) 
tfidf = X.toarray()
lsa_ = lsa.transform(X)
final_representation = np.concatenate((tfidf,lsa_),axis=1)
print "output",clf.predict(final_representation)

label = []
_input = raw_input("Do you feel like you are being bashed?[0/1]:\n")
label.append(_input)


# In[4]:


# b = "you are just beautiful"
# b = remove_punctuations.removePunctuations(b)
# b = remove_stopwords.remove_words(b)

# X1 = vectorizer.transform([b])
# tfidf = X1.toarray()
# lsa_ = lsa.transform(X1)
# final_representation = np.concatenate((tfidf,lsa_),axis=1)
# print "output",clf.predict(final_representation)
# _input = raw_input("Do you feel like you are being bashed?[0/1]:\n")
# label.append(_input)


# In[5]:


new_feed = []
new_feed.append(a)
# new_feed.append(b)
c = []

for tweet in new_feed:
    c.append(remove_stopwords.remove_words(remove_punctuations.removePunctuations(tweet)))
    
X_new = np.array(c)   
y_new = np.array(label)
le = LabelEncoder()
y_encoded = le.fit_transform(y_new)
print X_new.shape
print y_new.shape


# In[6]:


X2 = vectorizer.transform(X_new)
tfidf = X2.toarray()
lsa_ = lsa.transform(X2)
final_representation = np.concatenate((tfidf,lsa_),axis=1)


# In[7]:


# class_weights = compute_class_weight('balanced', [0, 1], y_new)
# class_weight_dictionary = {1:class_weights[0], 1:class_weights[1]}
clf.partial_fit(final_representation,y_encoded)


# In[8]:


# save to pickle
import pickle

with open('Models/classifier.pkl', 'wb') as f:
    pickle.dump(clf, f)

