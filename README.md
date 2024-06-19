# Yallakora-web-scrapt

Overview
This script scrapes match details from the Yallakora website for a specified date, parses the relevant information, and saves it into an Excel file. The script extracts the championship title, teams, match time, and score.

Requirements
Python 3.x
Libraries: requests, BeautifulSoup, pandas.

Script Description
User Input
The script prompts the user to enter a date in the format MM/DD/YYYY.

URL Construction
The script constructs the URL for the Yallakora Match Center page based on the provided date and sends a GET request to fetch the webpage content.

Data Extraction
Page Download and Parsing:
The script downloads the webpage content and parses it using BeautifulSoup.

Selecting Relevant Data:
The script identifies HTML elements containing championship details and matches.

Parsing Match Data:

Extracts the championship title.
Iterates through each match to extract:
Teams: Names of the competing teams.
Score: The match score.
Match Time: The time the match took place.
Compiles all the match details into a structured format.
Saving Data to Excel
The script converts the extracted match details into a Pandas DataFrame and saves it to an Excel file named matches.xlsx.
