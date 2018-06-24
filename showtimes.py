import csv
import json
import os
import pdb
import requests
from bs4 import BeautifulSoup
import datetime
import pytest
import tkinter
from lxml import html
from IPython import embed

## Movie Showtimes Application
welcome = """

Welcome to Movie Showtimes!

"""
print(welcome)

request_url = "https://www.imdb.com/showtimes/US/10003/2018-06-26"

movie_listings = []

#https://www.fandango.com/theaterlistings-prn.aspx?location=10003&pn=1&sdate=6-18-2018&tid=AAECF,AABQF,AAJNK,AABQG,AAEFP,AAECI,AAEFN,AANWY,AATNT,AAEFO
#https://www.fandango.com/theaterlistings-prn.aspx?location=10012&pn=1&sdate=6-19-2018&tid=AAECI,AAYHN,AABQF,AAECF,AAJNK,AAEFP,AANWY,AAEFO,AATNT,AAEFN
response = requests.get(request_url)
#print(response.text)
soup_response = BeautifulSoup(response.text, 'lxml')
#print(type(soup_response))
#print(soup_response.prettify())

 ## TODO: isolate showtime details for a movie

#with help from url: https://www.dataquest.io/blog/web-scraping-beautifulsoup/
#soup_div = soup_response.find_all('div', class_ = "info")
soup_div = soup_response.find_all('div', class_ = "list_item odd")
#print(soup_div[0])

#print(soup_div)
#print(type(soup_div))
#print(len(soup_div))
#print(soup_div[0])

#showtimes = soup_div[0]
#
##FIRST THEATER NAME
#first_theater = showtimes.find_all('div', class_ = "fav_box")
##print(first_theater)
##print(first_theater[0])
#first_theater = first_theater[0]
##print(first_title)
##print(first_theater.h3.a.text)
#first_theater = first_theater.h3.a.text
#
##FIRST THEATER ADDRESS
#first_address = showtimes.find_all('div', class_ = "address")
##print(first_address[0].span.text)
##print(first_address[0])
#first_address = first_address[0]
##print(first_address)
#first_street = first_address.find('span', attrs = {'itemprop' : 'streetAddress'})
#first_city = first_address.find('span', attrs = {'itemprop' : 'addressLocality'})
#first_state = first_address.find('span', attrs = {'itemprop' : 'addressRegion'})
#first_zip = first_address.find('span', attrs = {'itemprop' : 'postalCode'})
#first_street = first_street.text
#first_city = first_city.text
#first_state = first_state.text
#first_zip = first_zip.text
#
##FIRST MOVIE TITLE
#first_movie = showtimes.find_all('div', class_ = "info")
#first_movie = first_movie[0]
#first_movie_title = first_movie.a.text
#
##FIRST MOVIE SHOWTIMES
##print(first_movie)
#
#first_movie_times = first_movie.find('div', class_ = "showtimes")
##print(type(first_movie_times))
##print(first_movie_times.a)
#first_movie_times = first_movie_times.a
##print(first_movie_times["data-displaytimes"])
#first_movie_times = first_movie_times["data-displaytimes"]
##print(first_movie_times)
#
##first_movie_times = first_movie.find('div', class_ = "btn_float")
##first_movie_times = first_movie.find_all(attrs = {"target" : "_target"})
###print(first_movie_times[1].text)
##first_movie_times = str(first_movie_times[0].text) + " | " + str(first_movie_times[1].text)
##print(first_movie_times)
#
##FULL FIRST SHOWTIME PRINTOUT
##print(welcome)
##print(f"""{first_theater}
##{first_street}
##{first_city}, {first_state} {first_zip}
##
##    {first_movie_title}
##    {first_movie_times}
##            """)
#
##print(len(soup_div))
##print(soup_div[10].h3)

##COLLECT ALL THEATERS
theater_names = []
theater_streets = []
theater_cities = []
theater_states = []
theater_zips = []

for t in soup_div:
    if t.find('div', class_ = "fav_box") is not None:
        theater_data = t.find('div', class_ = "fav_box")
        theater = theater_data.h3.a.text
        theater_names.append(theater)

    if t.find('span', attrs = {'itemprop' : 'streetAddress'}) is not None:
        street_data = t.find('span', attrs = {'itemprop' : 'streetAddress'})
        street = street_data.text
        theater_streets.append(street)

    if t.find('span', attrs = {'itemprop' : 'addressRegion'}) is not None:
        city_data = t.find('span', attrs = {'itemprop' : 'addressRegion'})
        city = city_data.text
        theater_cities.append(city)

    if t.find('span', attrs = {'itemprop' : 'addressLocality'}) is not None:
        state_data = t.find('span', attrs = {'itemprop' : 'addressLocality'})
        state = state_data.text
        theater_states.append(state)

    if t.find('span', attrs = {'itemprop' : 'postalCode'}) is not None:
        zip_data = t.find('span', attrs = {'itemprop' : 'postalCode'})
        zip = zip_data.text
        theater_zips.append(zip)

print(len(theater_names))
print(len(theater_streets))
print(len(theater_cities))
print(len(theater_states))
print(len(theater_zips))


#first_zip = first_address.find('span', attrs = {'itemprop' : 'postalCode'})




#print(first_showtime)

#print(first_showtime.h3.a.text)


#print(first_showtime.h4.a.text)

#first_title = first_showtime.h4.a.text
#print(first_title)

#for n in soup_div:
#    title = soup_div[n]
#    movie_title = {
#        "title": title.h4.a.text
#    }
#
#print(movie_title)

#print(soup_div2)

#css_soup = BeautifulSoup('<a class="btn2 btn2_simple medium"></a>')

#for m in soup_response.find_all('a'):
#    if m.get("data-times") != "None":
#        print(m.get("data-times"))

showtime_data = []

#for m in soup_response.a:
#    showtime_data.append(m)

#print(showtime_data)

#print(type(response))
#response_html = json.loads(response.text)
#print(type(response_html))

#response_data = BeautifulSoup(response_html)
#print(type(response_data))
#print(response.cookies)
#print(response.error) - no Error
#print(response.history)
#print(response.url)
##leads to correct url
#print(response.data)

#link = "https://www.fandango.com/10003_movietimes?mode=general&q=10003"
#response = requests.get(link) #get page data from server, block redirects
#sourceCode = response.content #get string of source code from response
#htmlElem = html.document_fromstring(sourceCode) #make HTML element object
#print(htmlElem)


##url for data tree: https://www.fandango.com/rss/moviesnearme_10003.rss


##zip = 10003
## TODO: add input for zip code
##zip = input("Please enter the 5-digit zip code for your area")

## TODO: add date functionality

## TODO: add request to web

## TODO
