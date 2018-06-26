import pytest
import requests
import datetime
import lxml
from bs4 import BeautifulSoup

def url(zip, date):
     return f"https://www.imdb.com/showtimes/US/{zip}/{date}"

#Set up for date variable:
today = datetime.date.today()
date_url = today.strftime("%Y-%m-%d")

#Test zip code variable:
zip_url = "10003"

#test of date variable for compatibility with url:
def test_date():
    assert date_url == "2018-06-26"

#test of zip code variable for proper number of digits:
def test_zip_len():
    assert len(zip_url) == 5

#test of zip code variable for composition of digits:
def test_zip_float():
    assert zip_url.isdigit() == True

#test of url:
def test_url():
    assert url(zip_url, date_url) == "https://www.imdb.com/showtimes/US/10003/2018-06-26"

#test of good url:
def test_good_url():
    request_url = url(zip_url, date_url)
    response = requests.get(request_url)
    soup_response = BeautifulSoup(response.text, 'lxml')
    assert soup_response.find_all('div', class_ = "list_item odd") is not None

#test of bad url:
def test_bad_url():
    zip_url = "00000"
    request_url = url(zip_url, date_url)
    response = requests.get(request_url)
    soup_response = BeautifulSoup(response.text, 'lxml')
    assert soup_response.find('div', class_ = "alert") is not None
