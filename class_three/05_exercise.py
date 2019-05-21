"""
Filter out the "NO STOP/STAND PM" citations from a list of dictionaries regarding citations

Exercise: Modify `check_citation_type()` to return the citation if it matches the violation_description

"""
list_of_citations = [
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6427650.9', 'Longitude': '1844147.1'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6427650.9', 'Longitude': '1844147.1'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6427650.9', 'Longitude': '1844147.1'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6427650.9', 'Longitude': '1844147.1'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6426779.5', 'Longitude': '1843759.2'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6426779.5', 'Longitude': '1843759.2'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6426732.3', 'Longitude': '1843915.2'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '99999', 'Longitude': '99999'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '99999', 'Longitude': '99999'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6426057.7', 'Longitude': '1843690'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6427650.4', 'Longitude': '1843440.1'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '99999', 'Longitude': '99999'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6427650.4', 'Longitude': '1843440.1'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6427650.4', 'Longitude': '1843440.1'},
    {'Violation Description': '5200', 'Latitude': '99999', 'Longitude': '99999'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6427650.4', 'Longitude': '1843440.1'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6431745.3', 'Longitude': '1837410.7'},
    {'Violation Description': 'NO STOP/STAND PM', 'Latitude': '6431745.3', 'Longitude': '1837410.7'},
    {'Violation Description': 'RED ZONE', 'Latitude': '99999', 'Longitude': '99999'},
    {'Violation Description': 'PREF PARKING', 'Latitude': '6431043.1', 'Longitude': '1837811'},
    {'Violation Description': 'PREF PARKING', 'Latitude': '6431369.8', 'Longitude': '1837351.9'},
    {'Violation Description': 'PREF PARKING', 'Latitude': '6431393.1', 'Longitude': '1837319.1'},
    {'Violation Description': 'WHITE ZONE', 'Latitude': '6431486.4', 'Longitude': '1837187.9'},
    {'Violation Description': 'PREF PARKING', 'Latitude': '6431087.4', 'Longitude': '1837179.4'}
]


def filter_citations_by_type(list_of_citations, violation_description):
    """Gets a list of the citations for a particular violation_description.
    """

    citations = []
    for citation in list_of_citations:

        filtered_citation = check_citation_type(citation, violation_description)

        if filtered_citation:
            citations.append(filtered_citation)

    return citations


def check_citation_type(citation, violation_description):
    """A helper function used in filter_citations_by_type to extract the citation by desciprtion.

    """
    #### EXERCISE: Implement boolean conditional checking against violation_description here
    if citation['Violation Description']:
        return citation
    else:
        return {}


if __name__ == "__main__":
    type_of_citations = filter_citations_by_type(list_of_citations, "NO STOP/STAND PM")    

    print(type_of_citations)


