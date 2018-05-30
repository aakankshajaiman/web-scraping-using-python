# -*- coding: utf-8 -*-
__author__ = 'Aakanksha Jaiman' 

import urllib2
from bs4 import BeautifulSoup
import csv
def read_m_by_rating(first_year, last_year, num_of_m=50):
    # This method takes two years and a number as inputs. If we have first year = 2015, and
    # last_year =2016, and num_of_m =40, we want to retrieve top 40 movies that were released between 2015 and 2016. num_of_m has the default value of 50.
    # In this assignment, your program will extract <=50 top movies.
    if num_of_m > 50:
        print "Error: my program can extract at most 50 movies!"
        return
    # Below is the code for reading html and create a beautifulsoup object
    url = "http://www.imdb.com/search/title?at=0&sort=user_rating&start=1&title_type=feature&year="+first_year+","+last_year+"&view=simple"
    test_url = urllib2.urlopen(url)
    readHtml = test_url.read()
    soup = BeautifulSoup(readHtml, "html.parser")
    # Unfortunately, a list of movies you want to extract are not
    # contained in a table. They are actually enclosed in a <div class="lister-list"> tag. Then within this div tag, you can find a number of
    # <div class="lister-item mode-simple">, each of which represents a movie
    movies_div = soup.find('div', attrs={'class':'lister-list'})
    movies = movies_div.find_all('div', attrs={'class':'lister-item mode-simple'})
    list_movies = [] # initialize the return value, a list of movies
    
    # Using count track the number of movies processed. now it's 0 - No movie has been processed yet.
    count = 0
    
    #for m in movies: # each row represents information of a movie
        #dict_each_movie = {} # create an empty dictionary. You need to extract 4 pieces of information regarding a movie: rank, title, year, and rating.
        #title = soup.find('span', attrs={'class':'lister-item-index unbold text-primary'})
    for movie in movies:
        dict_each_movie = {} 
        
        """ code to fetch year rank. """
        ranks = movie.find('span', attrs={'class': 'lister-item-index unbold text-primary'})
        for r in ranks:
            rank = r.string
            rank = rank.encode("ascii","ignore")
            dict_each_movie["rank"] = rank
        
        title_dictionary = movie.find('span', attrs={'class': 'lister-item-header'})
        title = title_dictionary.find('a').get_text().encode("ascii","ignore")
        dict_each_movie["title"] = title
        
        years = movie.find('span', attrs={'class': 'lister-item-year text-muted unbold'})
        for y in years:
            year= y.string
            year = year.encode("ascii","ignore")
            dict_each_movie["year"] = year

        rating_dictionary = movie.find('div', attrs={'class': 'col-imdb-rating'})  
        rating = rating_dictionary.find('strong').get_text().strip().encode("ascii","ignore")
        dict_each_movie["rating"] = rating
        
        list_movies.append(dict_each_movie)
        count = count + 1
        if count == num_of_m:
            break
    return list_movies


def write_movies_csv(list_movies, filename):
    # write the movies to a csv file ; each row represents a movie. The parameter list_movies includes a number of movies, which is the output of the function read_m_by_rating. The filename represents the output file name
    lis = [] # to write the file, we create a list of strings
    header = "rank,"+"title,"+"year,"+"rating"
    lis.append(header) # add the header to the list
    for movie in list_movies:
        string = movie["rank"] +","+ movie["title"] +","+movie["year"] + ","+movie["rating"]
        lis.append(string)# add the string to the list
    
    thelist = lis        
    f = open(filename, "wb")
        
    for item in thelist:
            #string = ",".join(item)
            print item 
            f.write("%s\n" % item)
    f.close()
    '''
    Your code here: write lis (a list of strings) to a file with filaname. Please remember to close the file when you are done
    '''


def main():
    #print read_m_by_rating('2005','2015',11) # Output: [{'rating': '10', 'year': '2015', 'rank': '1', 'title': 'Captives'}, {'rating': '10', 'year': '2015', 'rank': '2', 'title': 'In the Park'}, {'rating': '10', 'year': '2014', 'rank': '3', 'title': 'Lacrimosa'}, {'rating': '9.8', 'year': '2015', 'rank': '4', 'title': 'Till We Meet Again'}, {'rating': '9.8', 'year': '2015', 'rank': '5', 'title': 'Beneath the Old Dark House'}, {'rating': '9.8', 'year': '2013', 'rank': '6', 'title': 'Bestie!'}, {'rating': '9.8', 'year': '2015', 'rank': '7', 'title': "Sizzler '77"}, {'rating': '9.8', 'year': '2015', 'rank': '8', 'title': 'Defenders of Life'}, {'rating': '9.8', 'year': '2011', 'rank': '9', 'title': 'Walk a Mile'}, {'rating': '9.8', 'year': '2010', 'rank': '10', 'title': 'Brente popcorn'}, {'rating': '9.8', 'year': '2014', 'rank': '11', 'title': 'Circa Survive: Live at the Shrine'}]
                                             # You don't need to have the exact same output, but should have similar results
    li= read_m_by_rating("2005", "2016", 45)
    write_movies_csv(li,"movies.csv") # your movie.csv file should look like the following
    """
    rank,title,year,rating
    1,Jackals,2016,10
    2,Captives,2015,10
    3,All She Wrote,I) (2016,10
    4,Reins of Hope Movie,2016,10
    5,Still Waters,II) (2016,10
    6,Who Will Move the Stone,2016,10
    7,The Parricidal Effect,2016,10
    8,Loud Places,2016,10
    9,In the Park,2015,10
    10,Second Life,2016,10
    11,Codename: Watermelon,2016,10
    12,Anywhere But Here,I) (2016,10
    13,Lacrimosa,2014,10
    14,Temuan Takdir,2016,10
    15,makrina monopatia,2016,10
    16,Last Call,VI) (2016,10
    17,Uno: The Movie,2016,9.9
    18,Dag II,2016,9.9
    19,Garroter,2016,9.9
    20,Regrets of the Past,2016,9.9
    21,Luces,2016,9.9
    22,Till We Meet Again,2015,9.8
    23,The Best Thanksgiving Ever,2016,9.8
    24,Beneath the Old Dark House,2015,9.8
    25,Death Beach,2016,9.8
    26,Blue Line Station,2016,9.8
    27,Eradication Code 6,2016,9.8
    28,Bestie!,2013,9.8
    29,The 12 Slays of Christmas,2016,9.8
    30,Sizzler '77,2015,9.8
    31,Defenders of Life,2015,9.8
    32,Spin the Plate,2016,9.8
    33,Walk a Mile,2011,9.8
    34,Brente popcorn,2010,9.8
    35,Circa Survive: Live at the Shrine,2014,9.8
    36,Get Rich Free,2016,9.7
    37,Empty Space,II) (2016,9.7
    38,Gold Star,I) (2016,9.7
    39,Joanna, Gone Girl,2007,9.7
    40,Apocalypse Will Not Happen,2015,9.7
    41,Vidas Em Paralelo,2010,9.7
    42,The Breakout: A Rock Opera,2016,9.7
    43,Amanat,2016,9.7
    44,The Polar Bear Club,2014,9.7
    45,Savior of none,2013,9.7
    """

if __name__ == '__main__':
    main()
