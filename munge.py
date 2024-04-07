import csv
import os

platform_agnostic_file_path = os.path.join('data', 'listings.csv')


#This opens the file in read mode
f = open(platform_agnostic_file_path, 'r')

data = list(csv.DictReader(f))

listData = []
keys = []

for row in data:
    tempData =[]
    keys = row.keys() #not changing
    for k in keys:
        tempData += [row[k]]

    listData += [tempData]

indexNum = []
wordList = ['id', 'host_id', 'name', 'price', 'neighbourhood', 'host_name', 'host_is_superhost', 'beds', 'neighbourhood_group_cleansed', 'review_scores_rating']
wordline = ''

for word in wordList:
    num = list(keys).index(word)
    indexNum += [num]
    wordline += word + ','

#print(indexNum)
wordline = wordline[:-1]

cleanedLines = []

for item in listData:
    notempty = True
    tempList = []
    for l in range (0, len(indexNum)):
        if item[indexNum[l]] == '':
            notempty = False
            break
        else:
            tempList += [item[indexNum[l]]]
    if notempty == True and len(tempList) == 10:
        cleanedLines += [tempList]

newFile = os.path.join('data', 'listings_clean.csv')
newF = open(newFile, "w", newline='')

writer = csv.writer(newF)
writer.writerow(wordList)
for row in cleanedLines:
    writer.writerow(row)

newF.close()

