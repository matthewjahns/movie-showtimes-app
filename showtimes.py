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
powered by the Internet Movie Database
(https://www.imdb.com/)

"""

        ##FIRST THEATER DETAILS
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

zip_error = "The zip code entered does not appear to be valid. Please check your entry and try again."

zip_url_error = "We were unable to find any showtimes near the entered zip code. Please check your entry and try again."

#Dates with help from URL: https://stackoverflow.com/questions/1506901/cleanest-and-most-pythonic-way-to-get-tomorrows-date

day_one = datetime.date.today()
day_two = datetime.date.today() + datetime.timedelta(days=1)
day_three = datetime.date.today() + datetime.timedelta(days=2)
day_four = datetime.date.today() + datetime.timedelta(days=3)
day_five = datetime.date.today() + datetime.timedelta(days=4)
day_six = datetime.date.today() + datetime.timedelta(days=5)
day_seven = datetime.date.today() + datetime.timedelta(days=6)



#print(welcome)
if __name__ == '__main__':

    window = tkinter.Tk()

    welcome_message = tkinter.Message(text="\nWelcome to Movie Showtimes!\nPowered by the Internet Movie Database \n (https://www.imdb.com/) \n")

    zip_label_prompt = tkinter.Label(text="Please enter a 5-digit postal code (US only): ")
    z_entry = tkinter.StringVar()
    zip_entry = tkinter.Entry(textvariable=z_entry)

    date_radio_label = tkinter.Label(text="\n\nPlease select a show date: ")
    date_radio_value = tkinter.StringVar()
#    date_radio_a = tkinter.Radiobutton(text="2018-06-27", value="2018-06-27", variable=date_radio_value)

    date_radio_a = tkinter.Radiobutton(text=day_one.strftime("%B %d, %Y "), value=day_one.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_b = tkinter.Radiobutton(text=day_two.strftime("%B %d, %Y "), value=day_two.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_c = tkinter.Radiobutton(text=day_three.strftime("%B %d, %Y "), value=day_three.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_d = tkinter.Radiobutton(text=day_four.strftime("%B %d, %Y "), value=day_four.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_e = tkinter.Radiobutton(text=day_five.strftime("%B %d, %Y "), value=day_five.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_f = tkinter.Radiobutton(text=day_six.strftime("%B %d, %Y "), value=day_six.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_g = tkinter.Radiobutton(text=day_seven.strftime("%B %d, %Y "), value=day_seven.strftime("%Y-%m-%d"), variable=date_radio_value)

    def handle_button_click():
        print("Submitting your entry...")
        print("Searching for movie showtimes")
        zip_url = str(zip_entry.get())
        date_url = str(date_radio_value.get())

        #    try:
        #        float(zip_url)
        #        pass
        #    except ValueError as e:
        #        quit("The entry does not appear to be a valid zip code. Please try again.")

        #if len(zip_url) != 5:
        #    quit("The entry does not appear to be a valid zip code. Please try again with a five-digit postal code.")

        #request_url = "https://www.imdb.com/showtimes/US/10003/2018-06-26"
        request_url = f"https://www.imdb.com/showtimes/US/{zip_url}/{date_url}"

        response = requests.get(request_url)
        soup_response = BeautifulSoup(response.text, 'lxml')

        if soup_response.find('div', class_ = "alert") is not None:
            print(zip_url_error)
            quit("Stopping the program.")

        #with help from url: https://www.dataquest.io/blog/web-scraping-beautifulsoup/
        soup_div = soup_response.find_all('div', class_ = "list_item odd")
        soup_div_even = soup_response.find_all('div', class_ = "list_item even")


        ##COLLECT ALL THEATERS
        theater_names = []
        theater_streets = []
        theater_cities = []
        theater_states = []
        theater_zips = []
        movie_titles = []
        movie_times = []

        theater_directory = {
                "theater": "",
                "address": ""
                }

        movie_directory = {
                "title": "",
                "times": ""
                }

        movie_showtimes = []

        for t in soup_div:

            if t.find('div', class_ = "fav_box") is not None:
                theater_data = t.find('div', class_ = "fav_box")
                theater = theater_data.h3.a.text
                theater_names.append(theater)

            if t.find('span', attrs = {'itemprop' : 'streetAddress'}) is not None:
                street_data = t.find('span', attrs = {'itemprop' : 'streetAddress'})
                street = street_data.text
                theater_streets.append(street)

            if t.find('span', attrs = {'itemprop' : 'addressLocality'}) is not None:
                city_data = t.find('span', attrs = {'itemprop' : 'addressLocality'})
                city = city_data.text
                theater_cities.append(city)

            if t.find('span', attrs = {'itemprop' : 'addressRegion'}) is not None:
                state_data = t.find('span', attrs = {'itemprop' : 'addressRegion'})
                state = state_data.text
                theater_states.append(state)

            if t.find('span', attrs = {'itemprop' : 'postalCode'}) is not None:
                zip_data = t.find('span', attrs = {'itemprop' : 'postalCode'})
                zip = zip_data.text
                theater_zips.append(zip)

            theater_details = f"""

{theater}
{street}
{city}, {state} {zip}"""

            print(theater_details)

            if t.find_all('div', class_ = "info") is not None:
                showtime_data = t.find_all('div', class_ = "info")

                for m in showtime_data:

                    if m.h4.span.a.text is not None:
                        title = m.h4.span.a.text
                        movie_titles.append(title)

                    if m.div.div is not None:
                        time_data = m.div.div
                        time = time_data.a["data-displaytimes"]
                        movie_times.append(time)

                    movie_showtime = f"""
            {title}
            {time}
            """

                    print(movie_showtime)

        #            movie_showtimes.append(movie_showtime)

        for t in soup_div_even:

            if t.find('div', class_ = "fav_box") is not None:
                theater_data = t.find('div', class_ = "fav_box")
                theater = theater_data.h3.a.text
                theater_names.append(theater)

            if t.find('span', attrs = {'itemprop' : 'streetAddress'}) is not None:
                street_data = t.find('span', attrs = {'itemprop' : 'streetAddress'})
                street = street_data.text
                theater_streets.append(street)

            if t.find('span', attrs = {'itemprop' : 'addressLocality'}) is not None:
                city_data = t.find('span', attrs = {'itemprop' : 'addressLocality'})
                city = city_data.text
                theater_cities.append(city)

            if t.find('span', attrs = {'itemprop' : 'addressRegion'}) is not None:
                state_data = t.find('span', attrs = {'itemprop' : 'addressRegion'})
                state = state_data.text
                theater_states.append(state)

            if t.find('span', attrs = {'itemprop' : 'postalCode'}) is not None:
                zip_data = t.find('span', attrs = {'itemprop' : 'postalCode'})
                zip = zip_data.text
                theater_zips.append(zip)

            theater_details = f"""

{theater}
{street}
{city}, {state} {zip}"""

            print(theater_details)

            if t.find_all('div', class_ = "info") is not None:
                showtime_data = t.find_all('div', class_ = "info")

                for m in showtime_data:

                    if m.h4.span.a.text is not None:
                        title = m.h4.span.a.text
                        movie_titles.append(title)

                    if m.div.div is not None:
                        time_data = m.div.div
                        time = time_data.a["data-displaytimes"]
                        movie_times.append(time)

                    movie_showtime = f"""
            {title}
            {time}
            """

                    print(movie_showtime)

    submit_button = tkinter.Button(text="Submit", command=handle_button_click)

    welcome_message.pack()

    zip_label_prompt.pack()
    zip_entry.pack()

    date_radio_label.pack()

    date_radio_a.pack()
    date_radio_b.pack()
    date_radio_c.pack()
    date_radio_d.pack()
    date_radio_e.pack()
    date_radio_f.pack()
    date_radio_g.pack()

    submit_button.pack()
    window.mainloop()




## TODO: add input for zip code
##zip = input("Please enter the 5-digit zip code for your area")

## TODO: add date functionality

## TODO: add request to web

## TODO
