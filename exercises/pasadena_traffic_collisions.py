"""
    "Counting Car Accidents"

    Data source: Pasadena Open Data Portal
    http://data.cityofpasadena.net/datasets/traffic-collisions/data

    Nathan @nate_somewhere

    Class notes:

    Python3 required, python2 not guaranteed to work completely
    Internet connection required
    Text editor required
"""

# EXERCISE

# Count the number of acidents by day of the week in the data set.
# Finish implementing the 'weekday_counter' function to do this


import csv
import os


try:
    # python3 functionality
    from urllib.request import urlretrieve
except ImportError as ex:
    from urllib import urlretrieve # python2 compability


def file_downloader(url, filename):
    """Downloads and names a file given a filename and download_url"""

    if not os.path.isfile(filename):
        urlretrieve(url, filename)
        print('File: %s downloaded' % filename)
    if os.path.isfile(filename):
        print('File: %s present and ready to go!' % filename)

    return os.path.abspath(filename)

def open_file(file_path):
    """Opens a file and returns the data"""
    with open(file_path, 'r', encoding='utf-8',) as f:
        # TODO = What is a csv DictReader?
        data = list(csv.DictReader(f))
    return data

def weekday_counter(list_o_dicts):
    """Counts each weekday in the data set and returns the count

    Arguments
    ---------

    list_o_dicts : list of dictionaries
        a list of dictionaries from a data source

    Returns
    -------

    counter : dict
        counts of each day of the week

    """
    counter = {}

    counter['day'] = 0
    for row in list_o_dicts:
        # TODO - Look for the day in each row and add it to the counter
        counter['day'] += 1

    return counter


if __name__ == '__main__':
    url = "https://opendata.arcgis.com/datasets/85f49ea583c24056968bee6e28162da4_0.csv"
    filename = 'pasadena_traffic_collisions.csv'

    file_location = file_downloader(url, filename)
    file_data = open_file(file_location)

    weekday_counts = weekday_counter(file_data)

    print(weekday_counts)