# information-retrieve-nlp-project
Step I
First converted the Json file into CSV
Created the df1.csv file which contains all the data.

Step II

Create the df2.csv file which contains data before partition. 

The questiontype, answertype, unixtime, asin id, answertime columns are removed.

Created two new columns Q_and_A and keywords. 
Q_and_A contains combined data from question and answer column
keywords column is empty, used for next step.

Step III

Created four csv fils from one df2.csv file so that it is easy for data handling, as with whole data the algorithm shows memory error. df2_1.csv , df2_2.csv ,df2_3.csv ,df2_4.csv . each file contains around 80000 data points.

Step IV

Now all four files are cleaned using NLTK library package and named as df3_1.csv , df3_2.csv ,df3_3.csv ,df3_4.csv.
The cleaning process includes removing stop words, removing non-English words, removing urls, punctuation symbols, numbers, white spaces, lemmatization and converting into lower case.

Step V

Created tfidf model and cosine similarity matrix by using Gensim library.
The four data file are used to create four models and similarity matrix. Compared the keyword given by user. Cosine similarity between user keyword and data is compared and collected top 5 questions and answer for all 4 different data. The top 5 questions and answers will have highest similarity score.
So in turn there will be top 20 questions and answers will be available from 4 different data sets. So these top 20 data points will be stored in file. These top 20 questions and answers will be finally sorted based on similarity score and out of that top 5 will be shown as final output.
  
            
