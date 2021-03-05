### Mach Eight Sample Project

Thank you for taking the time to complete this sample project. We're a tech
first company and we value our engineers tremendously. We're are looking for
hard working, smart engineers with either excellent experience or lots of
potential.


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

It is expected that this can be completed in 1-3 hours. If it's taking longer
than that, please reach out. It's possible we mis-scoped it, and I don't want
anyone spending a full day on this.


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

## Evaluation

The project will be evaluated on its correctness, i.e., all features work as
specified. The cleanliness of the code will also be evaluated, as well as the
architecture of the components. The matches page must work in a reasonable
amount of time and memory usage. Best practices and unit tests are looked upon
very kindly.

This is _not_ a closed book test. You are encouraged to reach out with any
questions that you come across.

## Submission

The preferred form of submission is by publishing a public repo on github with
your code and a README file explaining how to run the code. I also can accept
an emailed zip file with the same contents.
