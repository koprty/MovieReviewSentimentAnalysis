# MovieReviewSentimentAnalysis
Project for COMP4651- 
Goal: An accurate classifier that will analyze the sentiment of the movie (positive and negative) 

## Team Members 
* Lise
* Kiki
* Sam

## Data
* The Data we used in this project was taken from the Snap project of Stanford
  * https://snap.stanford.edu/data/web-Movies.html

## Current Code/Files
* transformData.py
  * transform the movies.txt data format into the single line format we can use in RDD's in spark
  * uses "\\\" to differentiate different categories in each line
  * example: product_id\\\user_id\\\score...etc
* Analysis_Notebook s .ipynb
  * there are 3 of these files that you should pay attention to 
  * 6k_Analysis.ipynb, 50k_Analysis.ipynb, 100k_Analysis.ipynb 
    * number refers to approximate amount of data *.7 used in classifier
  * All three of these files create three classifiers, a SVM, logarithmic regression classifier, and naive bayes 
  * The Three classifiers are built using the same procedure, but just for easy comparision of the results
  * These three classifiers classify our datapoints by doing a binary classfication (positive and negative) 


* NOTE: All large data files have been removed due to GitHub file limits
* output.txt and 6k_parsed.txt are examples of the result from transformData.py on the snap data formats

# Technologies to Use
* Spark 
* Python 
* pyspark.mllib library/module

  
## Future Ideas
* Probabilities instead of binary classification
* Use a more powerful machine to run and test on more data
* Parameter Optimization
* Individual words to different sentiment scores instead of classifying all words in one review to one score






