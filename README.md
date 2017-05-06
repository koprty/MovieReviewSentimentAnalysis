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
* Analysis_Notebook.ipynb
* tiniest_movies.txt - truncated file of our data for testing function correctness and "bug-freeness"
* output.txt - sample output from transformData using tiniest_movies
  * this is used in Analysis_Notebook for now

# TO DO LIST 
* Clean Data [ ] 
* Divide the Data into 2/3 (training) and 1/3 (testing)    (RANDOM VERSUS STRATIFICATION) 
    * Validate the training data with (maybe) cross validation
* Create classifier for data [ ]
* Testing Data [ ]
* Repeat from step 2 until we find a good classifier with a decent accuracy


# Technologies to Use
* Spark 
* Python 
* Look into python libraries for this 






