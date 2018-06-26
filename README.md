#Movie Showtime application

Prompts the user for a zip code and date and outputs showtime listings for nearby movie theaters.

##Prerequisites
Requires Git and Python 3.x.

##Installation
Install the source code from Github:

```sh
git clone https://github.com/matthewjahns/movie-showtimes-app.git
cd movie-showtime-app/
```

Install required packages:

```sh
# For Pipenv users:
pipenv install # then run `pipenv shell`

# For Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

# All others:
pip install -r requirements.txt
```

## Usage
Run the application:

```sh
python3 app/showtimes.py
```

## Testing
To run the tests successfully, first update the test_url() and test_date() functions with the current date.

Run the test:
```sh
pytest test/
```

## [License](LICENSE.md)
