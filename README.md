# Explore US Bikeshare Data
_Created 6/15/2020_

Interactive Python script to analyze bikeshare data from Chicago, NYC, and Washington, DC.

This project was completed as part of Udacity's "[Programming for Data Science with Python](https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104)" Nanodegree Program.

## Files used
* `bikeshare.py`
* CSV data files (not tracked in Git). Bikeshare data needs to follow the [General Bikeshare Feed Specification (GBFS)](https://nabsa.net/resources/gbfs/).

## Extend
Currently this program handles data for Chicago, NYC, and Washington, DC. To add a city, follow these steps:

1. Find bikeshare data in CSV format for your desired city. GBFS lists these on [GitHub](https://github.com/NABSA/gbfs/blob/master/systems.csv).
2. Download the city bikeshare data CSV to this project directory, then modify the `CITY_DATA` dictionary and `get_filters` function to include the new city option.

_Note: Column headers and data formats may vary slightly from city to city. You may need to manually edit the CSV or modify more code to make this work._

## Run the program

- Clone this repository to your local machine.
- Download datasets in CSV format to the project directory. Make sure the CSV files name match the expected values in the `CITY_DATA` dictionary.
- Run bikeshare.py in your terminal: `cd /path/to/project && python bikeshare.py`

## References/credits

These StackOverflow posts and docs were used to complete this project.

Raising error if string not in one or more lists
https://stackoverflow.com/q/35246467/1940172

AttributeError: 'int' object has no attribute 'index' (python)
https://stackoverflow.com/a/34520956/1940172

how can I suppress the “dtype” line when printing a pandas dataframe?
https://stackoverflow.com/a/55815338/1940172

Convert numpy, list or float to string in python
https://stackoverflow.com/a/24915798/1940172

Calendar and Pandas docs
https://docs.python.org/3/library/calendar.html
https://pandas.pydata.org/docs/reference/index.html#api
