#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


from sklearn.svm import SVC

clf = SVC(C=10000, kernel="rbf")

t0 = time()
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
prediction = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"
print(clf.score(features_test,labels_test))

Chris = 0

for i in prediction:
    if i == 1:
        Chris = Chris + 1
print Chris


#########################################################
### your code goes here ###

#########################################################


