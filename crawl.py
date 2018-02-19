from bs4 import BeautifulSoup
import requests
import csv

#This python file will scrape the h2 from the nytimes website and save 
#the clean h2 in a csv file

url = 'http://nytimes.com'


source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)



    csv_writer.writerow([headline])

csv_file.close()