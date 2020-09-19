import csv
import requests
import re
import datetime
from bs4 import BeautifulSoup

def scrape_data(url):

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'lxml')
    content  = soup.find_all("script")[2].string

    # Get the count from the website
    data = content.split('var data = ')
    AAA = data[1].rsplit('count')
    count = AAA[1].rsplit(',')[0][3:]

    #get the current timestamp for the data
    timestamp = datetime.datetime.now()

    # write to csv
    with open('climbers.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, count])


if __name__=="__main__":
    url = "https://portal.rockgympro.com/portal/public/c517f311383a69209b2d00e4698bf8e7/occupancy?&iframeid=occupancyCounter&fId="
    scrape_data(url)
