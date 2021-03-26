### Mach Eight Sample Project

Take a look here [Nba Players Project](https://nbaplayers-project.herokuapp.com/)


## Quick Start

To get this project up and running locally on your computer:
1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
   It is recommended to use a Python virtual environment.
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   git clone https://github.com/jaumemy/macheight-sampleproject.git
   pip3 install -r requirements.txt
   python3 manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/` to open the  site


## Here is how it should work

  ![](macheight_sampleproject.gif)

## Project

The project is to create a simple web front end to display data about NBA
players' heights. The raw data is taken from
[here](https://www.openintro.org/data/index.php?data=nba_heights).  The data is
served in json format by the endpoint
[here](https://mach-eight.uc.r.appspot.com/).

The task is to create a single page webapp with 3 different pages described
below. The app must load the data in JSON format from the mach-eight url above.
The URL is not paginated, and it's ok to load the entire dataset into memory at
once. All pages include a navbar with 2 items: "Player List" and "Player
Matches"


# Player List Page

The player list page is the default page that is shown when the app is loaded.
It includes a tabular view of all players in the dataset, including first name,
last name, height in meters, and height in inches. Clicking on column headers
will sort by that column. Clicking on the row for a player will open that
player's detail page.


# Player detail page

The player detail page includes the player's name and height. It also lists the
names of all players that have the same height in inches. The detail page will
have "Player List" as the active link in the navbar.

# Matches page

The matches page is accessible through the navbar link. The matches page
prompts the user to input a number of inches. It will then display all pairs of
players whose heights in inches add up to the input number. For example, if the
user enters 153, the page will display Alex Acker and Hassan Adams as one of
the pairs (there may be other pairs as well).

The algorithm to find the pairs must be faster than O(n^2).
