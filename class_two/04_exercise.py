"""
Extracting city names from a list of addresses

Exercise: Modify `extract_city_name()` to get the city name out of the address_string


"""

list_of_addresses = [
    "Austin, TX 78701",
    "Washington, DC 20001",
    "Whittier, CA 90602",
    "Woodland Hills, CA 91371",
    "North Hollywood, CA 91601"
    "Baltimore, MD 21201",
    "Woodland Hills, CA 91365",
    "Brea, CA 92821",
    "Whittier, CA 90601",
    "Studio City, CA 91604",
    "Woodland Hills, CA 91364",
    "Reseda, CA 91335"
]

def get_list_cities(addresses):
    """Gets a list of the cities from the addresses given to it.
    """

    cities = []
    for address in list_of_addresses:

        city_name = extract_city_name(address)

        cities.append(city_name)

    return cities


def extract_city_name(address_string):
    """A helper function used in get_list_cities to extract the city name from the address_string.

    Look at "02_strings" for hints
    """
    #### EXERCISE: Implement extract city from string here

    return address_string


if __name__ == "__main__":
    cities = get_list_cities(list_of_addresses)    

    print(cities)


