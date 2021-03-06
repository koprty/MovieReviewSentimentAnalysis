# Our Data file is not in a format that is easily ready by the sc.textFile default command in spark
# Thus, this file attempts to reconvert the file into a file easily read by spark (a one time use file) 

#USAGE: 
# 1) change the call parameters on the bottom of this file
# 2) run the following command: (change the last name as desired)
# python transformData.py > outputFileName.txt



# turns movies.txt data file into a rdd readable file
# sc.textFile() makes an entry for every line it sees in the file
# there are several parameters in the original file: (all printed on different lines) 
# productId, userId, profilename, helpfulness, score, time, summary, text
# note, this is a really fast implementation and not the cleanest, so if there are bugs, PLEASE REPORT THEM
def outputRDD_readable(filename):
    f = open(filename, 'r')
    data = f.readlines()
    L = [] # 8 max elements
    maxE = 8
    #initializing first line to have all the headers just for clarity
    #TODO: remove as needed
    str_ans = "" #"productId///userId///profileName///helpfulness///score///time///summary///text\n" 
    for line in data: # check each line
        if (len(line.split()) > 0):# if empty, dont do anything
            L.append(" ".join(line.replace("\n"," ").split(" ")[1:]).strip()) #get rid of preceding category descriptions
        
            if (len(L) == maxE): #clear temp holder after adding to things string to print
                str_ans+= "///".join(L)
                str_ans+= "\n"
                L=[]
    print "\n".join(str_ans.split("\n")[:-2]) # remove last  two elements just because they might be flawed data
    # text files on my local machine are very poorly cut... using the head command lolz

#outputRDD_readable("movies.txt");
#outputRDD_readable("smaller_movies.txt");
#outputRDD_readable("50k_parsed.txt");
#outputRDD_readable("100k_parsed.txt");
#outputRDD_readable("tiniest_movies.txt");
outputRDD_readable("prediction_data.txt");
