(An extension was used for the assignment, and extra credit is at the end)
# AirBnB MongoDB Analysis

## MongoDB Commands

MongoDB Command 1:

`mongo
db.listings.find({}).limit(2)
`

Output: 
`
[
  {
    _id: ObjectId('6611a42bc34b7fbd6a5a648b'),
    id: 9419,
    host_id: 30559,
    name: 'Rental unit in Seattle · ★4.72 · 1 bedroom · 1 bed · 3 shared baths',
    price: '$67.00',
    neighbourhood: 'Seattle, Washington, United States',
    host_name: 'Angielena',
    host_is_superhost: 't',
    beds: 1,
    neighbourhood_group_cleansed: 'Other neighborhoods',
    review_scores_rating: 4.72
  },
  {
    _id: ObjectId('6611a42bc34b7fbd6a5a648c'),
    id: 9531,
    host_id: 31481,
    name: 'Home in Seattle · ★4.97 · 2 bedrooms · 3 beds · 1 bath',
    price: '$184.00',
    neighbourhood: 'Seattle, Washington, United States',
    host_name: 'Cassie',
    host_is_superhost: 't',
    beds: 3,
    neighbourhood_group_cleansed: 'West Seattle',
    review_scores_rating: 4.97
  }
]
`

This query found the first 2 entries of the collection in any other. Both airbnb listings have relatively high review scores, but it does seem like (with only one sample from each section) there may be an interesting relationship between the number of beds and the review score.



MongoDB Command 2:

`mongo
db.listings.find().pretty().limit(10)
`

Output:
`
[
  {
    _id: ObjectId('6611a42bc34b7fbd6a5a648b'),
    id: 9419,
    host_id: 30559,
    name: 'Rental unit in Seattle · ★4.72 · 1 bedroom · 1 bed · 3 shared baths',
    price: '$67.00',
    neighbourhood: 'Seattle, Washington, United States',
    host_name: 'Angielena',
    host_is_superhost: 't',
    beds: 1,
    neighbourhood_group_cleansed: 'Other neighborhoods',
    review_scores_rating: 4.72
  },
  {
    _id: ObjectId('6611a42bc34b7fbd6a5a648c'),
    id: 9531,
    host_id: 31481,
    name: 'Home in Seattle · ★4.97 · 2 bedrooms · 3 beds · 1 bath',
    price: '$184.00',
    neighbourhood: 'Seattle, Washington, United States',
    host_name: 'Cassie',
    host_is_superhost: 't',
    beds: 3,
    neighbourhood_group_cleansed: 'West Seattle',
    review_scores_rating: 4.97
  },
  {
    _id: ObjectId('6611a42bc34b7fbd6a5a648d'),
    id: 9534,
    host_id: 31481,
    name: 'Guest suite in Seattle · ★4.99 · 2 bedrooms · 2 beds · 1 bath',
    price: '$155.00',
    neighbourhood: 'Seattle, Washington, United States',
    host_name: 'Cassie',
    host_is_superhost: 't',
    beds: 2,
    neighbourhood_group_cleansed: 'West Seattle',
    review_scores_rating: 4.99
  }
]
`

This query found the 10 documents that organizes it in a good looking way using the pretty function. Something interesting to note is that super hosts have very high ratings. If I were booking an airbnb, having a rating of 4.5 or above is good enough, hence these superhosts status might play a role in the quality of the housing and hence the rating. 


 MongoDB Command 3:

`mongo
 db.listings.find({host_is_superhost: 't', $or:[{host_id: 30559}, {host_id : 31481}]}, {name: 1, price: 1, neighbourhood: 1, host_name: 1, host_is_superhost: 1, _id : 0})
 `

Output:
`
[
  {
    name: 'Rental unit in Seattle · ★4.72 · 1 bedroom · 1 bed · 3 shared baths',
    host_name: 'Angielena',
    host_is_superhost: 't',
    neighbourhood: 'Seattle, Washington, United States',
    price: '$67.00'
  },
  {
    name: 'Home in Seattle · ★4.97 · 2 bedrooms · 3 beds · 1 bath',
    host_name: 'Cassie',
    host_is_superhost: 't',
    neighbourhood: 'Seattle, Washington, United States',
    price: '$184.00'
  },
  {
    name: 'Guest suite in Seattle · ★4.99 · 2 bedrooms · 2 beds · 1 bath',
    host_name: 'Cassie',
    host_is_superhost: 't',
    neighbourhood: 'Seattle, Washington, United States',
    price: '$155.00'
  }
]
`

This query found 2 hosts that are super hosts and shows the name, price, neighbourhood, and superhost status. Something interesting is that Cassie (perhaps not the same one, but for simplicity of this analysis I will assume that these two Cassies are the same one) is a very expensive host, serving houses above $150 per night.

MongoDB Command 4:

`mongo
db.listings.distinct('host_name')
`

Output (First 3):
`'A-Team',         'Aaron',            'Abe',
`

This query found all unique host names. 

MongoDB Command 5: 

`mongo
db.listings.find({neighbourhood_group_cleansed: 'Cascade', beds: {$gt: 2}}, {name: 1, beds: 1, review_scores_rating : 1, price: 1, _id : 0}).sort({review_scores_rating: -1})
`

Output:
`
{
    name: 'Townhouse in Seattle · ★5.0 · 3 bedrooms · 3 beds · 2.5 baths',
    price: '$317.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Serviced apartment in Seattle · 2 bedrooms · 3 beds · 2 baths',
    price: '$260.00',
    beds: 3,
    review_scores_rating: 5
  },
  {
    name: 'Townhouse in Seattle · ★5.0 · 2 bedrooms · 3 beds · 2 baths',
    price: '$195.00',
    beds: 3,
    review_scores_rating: 5
  }
`

This query finds all places that have more than 2 beds in the Cascade neighbourhood and orders by the review score rating in descending order. The output will include the name, beds, review scores rating, and the price. Something to note is that 3 bed apartments have a large range of different prices even though they are all 5 star ratings and around the same number of baths (unless 0.5 baths really makes that big of a difference in the price of rental per night).

MongoDB Command 6: 

show the number of listings per host

`mongo
db.listings.aggregate([
    {
        $group: {
            _id: "$host_id",
            listingCount: {$sum: 1}
        }
    }
])
`

Output:
`
[
  { _id: 11818709, listingCount: 1 },
  { _id: 198859968, listingCount: 1 },
  { _id: 9486318, listingCount: 1 },
  { _id: 1214369, listingCount: 1 },
  { _id: 179687197, listingCount: 1 },
  { _id: 546224064, listingCount: 1 },
  { _id: 95147638, listingCount: 1 },
  { _id: 32290113, listingCount: 1 },
  { _id: 542173718, listingCount: 1 },
  { _id: 4202600, listingCount: 1 },
  { _id: 114258495, listingCount: 1 },
  { _id: 233534137, listingCount: 1 },
  { _id: 542441283, listingCount: 2 },
  { _id: 365820430, listingCount: 1 },
  { _id: 540655866, listingCount: 1 },
  { _id: 174096725, listingCount: 1 },
  { _id: 429381332, listingCount: 1 },
  { _id: 2887279, listingCount: 1 },
  { _id: 42230885, listingCount: 1 },
  { _id: 40983081, listingCount: 1 }
]
`

This query shoulds the number of listsings by host. With the small sample size we have here (could press 'it' command to get a better idea), we can see that most hosts only have only place in seattle that is open for rental through Airbnb. 

MongoDB Command 7:

`mongo
db.listings.aggregate([
    {
        $group: {
            _id : '$neighbourhood',
            average : {$avg: '$review_scores_rating'}
        }
    },

    {
        $match: {
            average : {$gte:4}
        }
    },

    {
        $sort: {'average' : -1}
    }

])
`

Output:
`
{
    _id: 'West Seattle, Washington, Washington, United States',
    average: 5
  },
  {
    _id: 'Capitol Hill, Seattle, Washington, United States',
    average: 4.94
  },
  { _id: 'Seattle, Wa, United States', average: 4.91 }

`

This query is finding the average review scores rating but only shows the groups that have average rating 4 or above and then show the average ratings by descending order. It seems like there are only 3 regions in seattle that have more than 4.91 average rating, and hence we can conclude that Airbnb listings are the best in these regions.



## Data set Details 
The origin of the data set is from the [Airbnb Data](https://insideairbnb.com/get-the-data/). The city I chose is Seattle, United States. 

The orinal form of the data was in a zip file stores as a csv file. 

The frist 20 rows of the data set is shown here. 

id | host_id | name | price | neighbourhood | host_name | host_is_superhost | beds | neighbourhood_group_cleansed | review_scores_rating |
|-|-|-|-|-|-|-|-|-|-|
| 6606 | 14942 | Guesthouse in Seattle · ★4.60 · 1 bedroom · 1 bed · 1 bath | $99.00 | Seattle, Washington, United States | Joyce | f | 1 | Other neighborhoods | 4.6 |
| 9419 | 30559 | Rental unit in Seattle · ★4.72 · 1 bedroom · 1 bed · 3 shared baths | $67.00 | Seattle, Washington, United States | Angielena | t | 1 | Other neighborhoods | 4.72 |
| 9531 | 31481 | Home in Seattle · ★4.97 · 2 bedrooms · 3 beds · 1 bath | $184.00 | Seattle, Washington, United States | Cassie | t | 3 | West Seattle | 4.97 |
| 9534 | 31481 | Guest suite in Seattle · ★4.99 · 2 bedrooms · 2 beds · 1 bath | $155.00 | Seattle, Washington, United States | Cassie | t | 2 | West Seattle | 4.99 |
| 9909 | 33360 | Home in Seattle · ★4.80 · 2 bedrooms · 2 beds · 1 bath | $228.00 | Seattle, Washington, United States | Laura | t  | 2 | West Seattle | 4.8 |
| 25002| 102684 | Guest suite in Seattle · ★4.93 · 1 bedroom · 2 beds · 1 bath | $94.00 | Seattle, Washington, United States | Amanda | t | 2 | Ballard | 4.93 |
| 37234| 160789 | Home in Seattle · ★4.17 · 1 bedroom · 2 beds · 1 bath | $130.00 | Seattle, Washington, United States | Darrell | f | 2 | Ballard | 4.17 |
| 68508  | 340192 | Rental unit in Seattle · ★4.63 · 2 bedrooms · 2 beds · 1 bath | $225.00 | Seattle, Washington, United States | Angela | f | 2 | Cascade | 4.63 |
| 119103 | 601600 | Guesthouse in Seattle · ★4.94 · 2 bedrooms · 2 beds · 1 bath | $108.00 | Seattle, Washington, United States | Hal | t | 2 | Other neighborhoods | 4.94 |
| 132120 | 378445 | Rental unit in Seattle · ★4.68 · 1 bedroom · 1 bed · 1 bath | $75.00 | Seattle, Washington, United States | Ralph | f | 1 | Other neighborhoods | 4.68 |
| 132160 | 558743 | Guest suite in Seattle · ★4.87 · 2 bedrooms · 2 beds · 1 bath | $173.00 | Seattle, Washington, United States | Natalie | t | 2 | Other neighborhoods | 4.87 |
| 151545 | 306615 | Rental unit in Seattle · ★4.93 · 3 bedrooms · 3 beds · 1.5 baths | $299.00 | Seattle, Washington, United States | Tara | t | 3 | Capitol Hill | 4.93 |
| 202251 | 601266 | Home in Seattle · ★4.45 · 3 bedrooms · 3 beds · 1 bath | $125.00 | Seattle, Washington, United States | Tim And Pam | f | 3 | Other neighborhoods | 4.45 |
| 210316 | 2438665 | Home in Seattle · ★4.76 · 1 bedroom · 1 bed · 4 shared baths  | $60.00 | Seattle, Washington, United States | Flor | f | 1 | Other neighborhoods | 4.76 |
| 226536 | 209571 | Cottage in Seattle · ★4.83 · 1 bedroom · 1 bed · 1 shared bath | $63.00 | Seattle, Washington, United States | Cheryl | t | 1 | Magnolia | 4.83 |
| 226677 | 30559  | Rental unit in Seattle · ★4.81 · 1 bedroom · 1 bed · 3 shared baths | $60.00 | Seattle, Washington, United States | Angielena | t | 1 | Other neighborhoods | 4.81 |
| 240920 | 946910 | Home in Seattle · ★4.86 · 1 bedroom · 2 beds · 1 private bath | $80.00 | Seattle, Washington, United States | Nathan | f | 2 | Other neighborhoods | 4.86 |
| 254340 | 1336214 | Rental unit in Seattle · ★4.91 · 1 bedroom · 1 bed · 1 bath  | $95.00 | Seattle, Washington, United States | Kim | f | 1 | Other neighborhoods | 4.91 |
| 260613 | 1387754 | Guest suite in Seattle · ★4.91 · 1 bedroom · 1 bed · 1 bath | $125.00 | Seattle, Washington, United States | Dot & Lucy | t | 1 | Ballard | 4.91 |
| 261912 | 558743 | Home in Seattle · ★4.81 · 2 bedrooms · 2 beds · 1 bath | $186.00 | Seattle, Washington, United States | Natalie | t | 2 | Other neighborhoods | 4.81 |

The raw code of what I did in order to munge the data is located in [munging python file](/munge.py). What I did to munge the data was to remove all the rows that had empty elements in them (hence we cannot perform operations on those lines of data). Furthermore, there was a lot of columns of data that would not be useful for analysis in this assignment. The main reason I decided to remove most of the columns was for the display in the previous section. Since displaying 127 columns of 20 entries of data would be difficult, I decided to munge the data to only include the columns that pertained to commands of this assignment. Once I removed all the entries with empty elements and removed all other columns, I created a new csv file called [listings_clean](/data/listings_clean.csv) that will be operated on in the rest of my analysis. 


'python

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

'
This is the section of the code that would deal with removing empty rows and not important columns.


## Extra Credit:

The full file of the python code used to run the output is located is embedded [here](/extracredit.py).

Meaningful code snippet:
`python
#show exactly two documents from the `listings` collection in any order
rows = collection.find({}).limit(2)
for row in rows:
    print(row)
`

The query that I wanted to recreate was the first query to show any 2 of the documents in the collection. The code snippet above has one query on the second line of the snippet. This is the exact same command we would run directly in MongoDB (except for using the db.databasename we just use collection). 

In order to run this output, I had to save the python file into an external python file, upload it to i6 using cyberduck, open my mongodb database and use the command 'Python extracredit.py'. Then the corresponding output would appear, which is the same output as if I directly writed the command into the mongodb terminal line. 

I had to learn on my own how to work python into mongoDB and run the file. And because of the extra work here, I think some extra credit should be applied.