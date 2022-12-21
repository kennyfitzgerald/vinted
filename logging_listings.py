import os

def log_seen_listings(list):
    """ Takes a dataframe with an 'id' column name and saves the IDs of listings that have been sent out in a text file.
    """
    filepath = 'seen_listings.txt'
    
    textfile = open(filepath, "a")

    for element in list:
        textfile.write(str(element) + "\n")

    textfile.close()


def read_seen_listings():
    """ Checks if the 'seen_listings.txt' file exists and if it does returns a list of IDs that have previously been seen
        in search results.
    """

    seen_listings = []

    if os.path.exists('seen_listings.txt'):
        with open('seen_listings.txt', 'r') as f:
            seen_listings = [int(line.strip()) for line in f]

    return seen_listings
