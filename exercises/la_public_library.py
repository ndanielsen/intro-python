"""
    "Counting LA Library Circulation"

    Data source: County of Los Angeles Open Data Portal
    https://data.lacounty.gov/Arts-and-Culture/Public-Library-Monthly-Circulation/gf6j-sjun

    Nathan @nate_somewhere

    Class notes:

    Python3 required, python2 not guaranteed to work completely
    Internet connection required
    Text editor required
"""

# EXERCISE

# Count the total ciruclation in 2015.

import csv
import os


try:
    # python3 functionality
    from urllib.request import urlretrieve
except ImportError as ex:
    from urllib import urlretrieve  # python2 compability


def file_downloader(url, filename):
    """Downloads and names a file given a filename and download_url"""

    if not os.path.isfile(filename):
        urlretrieve(url, filename)
        print("File: %s downloaded" % filename)
    if os.path.isfile(filename):
        print("File: %s present and ready to go!" % filename)

    return os.path.abspath(filename)


def open_file(file_path):
    """Opens a file and returns the data"""
    with open(file_path, "r", encoding="utf-8") as csvfile:
        # TODO = What is a csv DictReader?
        data = list(csv.reader(csvfile))
    return data


if __name__ == "__main__":
    url = "https://data.lacounty.gov/api/views/gf6j-sjun/rows.csv?accessType=DOWNLOAD"
    filename = "library_monthly_circulation.csv"

    file_location = file_downloader(url, filename)
    file_data = open_file(file_location)

    counter = 0

    for row in file_data[1:]:
        supply_dist, cost_code, library, city, zipname, month, year, month_year, circulation = (
            row
        )
        # TODO - Look for the year in each row and if the year that matches then add that circulation

        counter += int(circulation)

    print(counter)
