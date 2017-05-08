# MovieReviewSentimentAnalysis
Project for COMP4651- 
Idea we will attempt to build an accurate classifier that will analyze the sentiment of the movie (positive and negative) 

## Team Members 
* Lise
* Kiki
* Sam

# Current state of Python notebook
* [u'productid', u'score', u'summary', u'text'], 
* [u'b003ai2vga', u'30', u'there is so much darkness now  come for the miracle', u'synopsis on the daily trek from juarez mexico to el paso texas an ever increasing number of female workers are found raped and murdered in the surrounding desert investigative reporter karina danes minnie driver arrives from los angeles to pursue the story and angers both the local police and the factory owners who employee the undocumented aliens with her pointed questions and relentless quest for the truthher story goes nationwide when a young girl named mariela ana claudia talancon survives a vicious attack and walks out of the desert crediting the blessed virgin for her rescue her story is further enhanced when the wounds of christ stigmata appear in her palms she also claims to have received a message of hope for the virgin mary and soon a fanatical movement forms around her to fight against the evil that holds such a stranglehold on the areacritique possessing a lifelong fascination with such esoteric matters as catholic mysticism miracles and the mysterious appearance of the stigmata i was immediately attracted to the 05 dvd release virgin of juarez the film offers a rather unique storyline blending current sociopolitical concerns the constant flow of mexican migrant workers back and forth across the us/mexican border and the traditional catholic beliefs of the hispanic population i must say i was quite surprised by the unexpected route taken by the plot and the means and methods by which the heavenly message unfoldsvirgin of juarez is not a film that you would care to watch over and over again but it was interesting enough to merit at least one viewing minnie driver delivers a solid performance and ana claudia talancon is perfect as the fragile and innocent visionary mariela also starring esai morales and angus macfadyen braveheart']

   
* SAMPLE OF WHAT SPITS OUT NOW

# Current Code/Files
* transformData.py
  * transform the movies.txt data format into the single line format we can use in RDD's in spark
  * uses "\\\" to differentiate different categories in each line
  * example: product_id\\\user_id\\\score...etc
* Analysis_Notebook.ipynb
* tiniest_movies.txt - truncated file of our data for testing function correctness and "bug-freeness"
* output.txt - sample output from transformData using tiniest_movies
  * this is used in Analysis_Notebook for now

# TO DO LIST 
* Clean Data [--semi-done--] <- A DOUBLE CHECK WOULD BE NICE 
* Divide the Data into 2/3 (training) and 1/3 (testing) [MAYBE DEPENDING ON WHAT APPROACH WE USE]
    * Validate the training data with (maybe) cross validation   (RANDOM VERSUS STRATIFICATION) 
* Create classifier for data [ ]
* Testing Data [ ]
* Repeat from step 2 until we find a good classifier with a decent accuracy


# Technologies to Use
* Spark 
* Python 
* Look into python libraries for this 






