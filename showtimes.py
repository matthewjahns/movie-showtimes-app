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

zip_error = "The zip code entered does not appear to be valid. Please check your entry and try again."

zip_url_error = """We were unable to find any showtimes near the entered zip code. Please check your entry and try again.
"""

#Date variables with help from URL: https://stackoverflow.com/questions/1506901/cleanest-and-most-pythonic-way-to-get-tomorrows-date

day_one = datetime.date.today()
day_two = datetime.date.today() + datetime.timedelta(days=1)
day_three = datetime.date.today() + datetime.timedelta(days=2)
day_four = datetime.date.today() + datetime.timedelta(days=3)
day_five = datetime.date.today() + datetime.timedelta(days=4)
day_six = datetime.date.today() + datetime.timedelta(days=5)
day_seven = datetime.date.today() + datetime.timedelta(days=6)



if __name__ == '__main__':

    window = tkinter.Tk()

    welcome_message = tkinter.Message(text="\nWelcome to Movie Showtimes!\nPowered by the Internet Movie Database \n (https://www.imdb.com/) \n")

    zip_label_prompt = tkinter.Label(text="Please enter a 5-digit postal code (US only): ")
    z_entry = tkinter.StringVar(value="Enter Here")
    zip_entry = tkinter.Entry(textvariable=z_entry)

    date_radio_label = tkinter.Label(text="\n\nPlease select a show date: ")
    date_radio_value = tkinter.StringVar(value=day_one.strftime("%Y-%m-%d"))

    date_radio_a = tkinter.Radiobutton(text=day_one.strftime("%B %d, %Y "), value=day_one.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_b = tkinter.Radiobutton(text=day_two.strftime("%B %d, %Y "), value=day_two.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_c = tkinter.Radiobutton(text=day_three.strftime("%B %d, %Y "), value=day_three.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_d = tkinter.Radiobutton(text=day_four.strftime("%B %d, %Y "), value=day_four.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_e = tkinter.Radiobutton(text=day_five.strftime("%B %d, %Y "), value=day_five.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_f = tkinter.Radiobutton(text=day_six.strftime("%B %d, %Y "), value=day_six.strftime("%Y-%m-%d"), variable=date_radio_value)
    date_radio_g = tkinter.Radiobutton(text=day_seven.strftime("%B %d, %Y "), value=day_seven.strftime("%Y-%m-%d"), variable=date_radio_value)

    def handle_button_click():
        print("""
Submitting your entry...
""")

        zip_url = str(zip_entry.get())

        date_url = str(date_radio_value.get())

        if len(zip_url) == 5 and zip_url.isdigit() == True:
            pass
        else:
            print(f"""The zip code entered--"{zip_url}"--does not appear to be valid. Please check your entry and try again.
            """)
            quit("Stopping the program.")

        print("Searching for movie showtimes...")

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

        theater_details = {
                "theater": "",
                "address": ""
                }

        movie_showtime = {
                "title": "",
                "times": ""
                }

        theater_directory = []
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
                        time = "Sorry--No movie times found."

                    if m.div.div is not None:
                        movie_data = m.div.div
                        if movie_data.a["data-title"] is not None:
                            title = movie_data.a["data-title"]
                        else:
                            title = title

                        if movie_data.a["data-displaytimes"] is not None:
                            time = movie_data.a["data-displaytimes"]
                        else:
                            if m.find_all('div', class_ = "showtimes") is not None:
                                time = ""
                                time_data = m.find_all('div', class_ = "showtimes")
                                for s in time_data:
                                    times = s.text
                                    time.append(f"{times} | ")

                            else:
                                time = "Sorry--No movie times found."

                    movie_titles.append(title)
                    movie_times.append(time)

#                    if m.div.div is not None:
#                        title_data = m.div.div
#                        title = title_data.a["data-title"]
#                        movie_titles.append(title)

#                    if m.div.div is not None:
#                        time_data = m.div.div
#                        time = time_data.a["data-displaytimes"]
#                        movie_times.append(time)

                    movie_showtime = f"""
            {title}
            {time}
            """

                    print(movie_showtime)

                    movie_showtimes.append(movie_showtime)

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

                    if m.find('div', class_ = "showtimes") is not None:

#with help from URL: http://texthandler.com/info/remove-line-breaks-python/

                        time_data = m.find('div', class_ = "showtimes")
                        time = time_data.text
                        time = time.replace("\r","")
                        time = time.replace("\n","")
                        time = time.replace(" ","")
                        time = time.replace("0a","0 a")
                        time = time.replace("0p","0 p")
                    else:
                        time = "Sorry--No movie times found."

#                    if m.h4.span.a.text is not None:
#                        title = m.h4.span.a.text
#                        movie_titles.append(title)

                    if m.h4.span.a.text is not None:
                        title = m.h4.span.a.text
#                        time = "Sorry--No movie times found."

                    if m.div.div is not None:
                        movie_data = m.div.div
                        if movie_data.a["data-title"] is not None:
                            title = movie_data.a["data-title"]
                        else:
                            title = title

                        if movie_data.a["data-displaytimes"] is not None:
                            time = movie_data.a["data-displaytimes"]


                    movie_titles.append(title)
                    movie_times.append(time)

#                    if m.div.div is not None:
#                        movie_data = m.div.div
#                        title = movie_data.a["data-title"]
#                        movie_titles.append(title)
#                        time = movie_data.a["data-displaytimes"]
#                        movie_times.append(time)

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
