"""
    "Exploring Los Angeles Parking Citations Data"

    Data source: City of Los Angeles Open Data Portal
    https://data.lacity.org/A-Well-Run-City/Parking-Citations/wjz9-h9np

    Nathan @nate_somewhere

    Warning:

    The dataset downloaded has 9.5 million plus rows 
    and takes several minutes to download.

    By default, a smaller dataset is in the exercises/data folder that you should
    use for development until you are ready to run the whole batch.

    Class notes:

    Python3 required, python2 not guaranteed to work completely
    Internet connection required
    Text editor required
"""

# EXERCISE

# Calculate the total fines for each type of citation in January 2019.


import csv
import os
from datetime import datetime

try:
    # python3 functionality
    from urllib.request import urlretrieve
except ImportError as ex:
    from urllib import urlretrieve  # python2 compability

CURRENT_DIR_PATH = os.path.dirname(__file__)

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
    with open(file_path, "r", encoding="utf-8-sig") as csvfile:
        # TODO = What is a csv DictReader?
        csv_file_data = csv.DictReader(csvfile)

        # ADVANCED EXERCISE - Can you think of a way to filter the data returned here?
        # Currently it is loading the entire 9.5+ million records.
        # HINT - What is list() doing to the csv_file_data object?
        # DEEPER HINT - what is a python generator? 
        data = list(csv_file_data)
    return data

def filter_by_date_range(citation_row, start, end):
    """Filters a citation by the issue date in a date range.

    Returns True or False if date falls in the range.

    # TODO - What is a function keyword arguments?
    """
    # HINT - corresponds to "10/31/2018" format
    date_format = "%m/%d/%Y"

    # TODO - What is strptime doing?
    date_start = datetime.strptime(start, date_format)
    date_end = datetime.strptime(end, date_format)

    try:
        citation_date_str = citation_row['Issue Date']
        citation_date_obj = datetime.strptime(citation_date_str, date_format)

        # HINT - the citation falls between the start and end date.
        if date_start <= citation_date_obj <= date_end:
            return True
        else:
            return False
    except: 
        # TODO - What is try-except in python?
        # Why is this necessary here?
        return False

def calculate_total_fine_by_citation(file_data, start="12/1/2015", end="12/31/2015"):

    # Store the fine amount format - key: violation description & value: fine_amount
    total_fine_by_citation = {}

    # HINT - citation_row is a dictionary
    for citation_row in file_data:
        if filter_by_date_range(citation_row, start, end) is True:
            violation_desciption = citation_row["Violation Description"]

            # TODO - Get the fine amount from the citation row and add it to the total
            # HINT - the key is called "Fine amount" in citation_row and value is a string
            fine_amount = 0

            # If the violation_desciption doesn't exist, then add it
            if total_fine_by_citation.get(violation_desciption) is True:

                # TODO - What is this doing here?
                total_fine_by_citation[violation_desciption] += fine_amount
            else:
                total_fine_by_citation[violation_desciption] = fine_amount    
    
    return total_fine_by_citation

if __name__ == "__main__":
    url = "https://data.lacity.org/api/views/wjz9-h9np/rows.csv?accessType=DOWNLOAD"
    

    # this is a smaller, faster, abbreviated data set you can develop with
    data_file_path = os.path.join(CURRENT_DIR_PATH, "data/la_parking_citations_abbr.csv")

    ### UNCOMMENT THIS TO DOWNLOAD FULL DATASET ###
    ### WARNING: It is slow!!!!
    # data_file_path = os.path.join(CURRENT_DIR_PATH, "data/la_parking_citations_full.csv")

    file_location = file_downloader(url, data_file_path)
    file_data = open_file(file_location)

    # TODO - Set the Dates from Feb 1 to Feb 28, 2019
    start_date = "3/1/2019"
    end_date = "3/31/2019"

    total_fine_by_citation = calculate_total_fine_by_citation(file_data, start=start_date, end=end_date)

    print(total_fine_by_citation)

# EXTRA CREDIT
# 
# - Can you create another function named `count_by_citation` that simply counts the number of
#     citations by type for Jan 1 to Jan 31, 2019?
# - What other intersting attributes that you count?
# 
# ADVANCED EXTRA CREDIT
# 
# See the open_file() for one method of optimizing / speeding this up.
#
# Can you think of any other ways of preprocessing the data to speed things up?
