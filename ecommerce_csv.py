import json
import csv
import ast
import os
import pandas as pd

#Setting up the workimg directory

os.chdir('D:\\Data_science\\Projects\\Excelr_project\\project1_NLP\\Output')

# Opening the JSON file and loading the data into variable

data=[]
with open("qa_Electronics.json",encoding='utf-8') as json_file:
   for i in json_file:
       c=ast.literal_eval(i)
       data.append(c)
#type(data)   

#writing the data into csv file
       
data_file=open('data_file.csv','w')

#create the CSV writer Object

csv_writer=csv.writer(data_file)

#Counter variable used for writing variables into csv file

header=['questionType','asin','answerTime','unixTime','question','answerType','answer']
csv_writer.writerow(header)

#looping the data line by line
for line in data:
    default_list=['NAN','NAN','NAN','NAN','NAN','NAN','NAN'] 
    # if column data is unavilable insert NAN
    if len(line)!=0:    #cheking row is empty of not
        for j in line:
            if j== "questionType":
                default_list[0]=line[j]
            if j== "asin":
                default_list[1]=line[j]
            if j== "answerTime":
                default_list[2]=line[j]
            if j== "unixTime":
                default_list[3]=line[j]
            if j== "question":
                default_list[4]=line[j]
            if j== "answerType":
                default_list[5]=line[j]
            if j== "answer":
                default_list[6]=line[j]
            
        csv_writer.writerow(default_list)      
data_file.close() # Closing the file and will save it at the project current working directory

#Reading the csv file
df=pd.read_csv('data_file.csv')

df_asin = df.groupby("asin").count()
df_asin.head(5) 
df.describe
df.info
df.shape
df.columns
df.sort_index()
product_id= "0594033926"

df_asin_pid=df.loc[df["asin"] == "0594033926"]

