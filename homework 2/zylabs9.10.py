#2065973
#Maimuna Murad

import csv

fileName = input()

wordsFrequency = {}

with open(fileName, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for word in row:
            word = word.strip()
            x = word.split(" ")
            for stri in x:
                if stri in wordsFrequency:
                    wordsFrequency[stri] = wordsFrequency[stri] + 1
                else:
                    wordsFrequency[stri] = 1
for key in wordsFrequency.keys():
    print(key + " " + str(wordsFrequency[key]))