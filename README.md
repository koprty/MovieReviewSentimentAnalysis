# MovieReviewSentimentAnalysis
Project for COMP4651- 
Idea we will attempt to build an accurate classifier that will analyze the sentiment of the movie (positive and negative) 

## Team Members 
* Lise
* Kiki
* Sam

# Current Code/Files
* transformData.py
  * transform the movies.txt data format into the single line format we can use in RDD's in spark
  * uses "\\\" to differentiate different categories in each line
  * example: product_id\\\user_id\\\score...etc
* Analysis_Notebook s .ipynb
* there are 3 of these files that you should pay attention to 
* 6k, 50k, 100k <- these endings refer to the approximate number of data points used for the file
* All three of these files create three classifiers, a SVM, A Log based classifier, and naive bayes 
* we just kept three files so we could display the different results from each classifier


# Technologies to Use
* Spark 
* Python 
* Look into python libraries for this 






