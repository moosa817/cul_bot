import requests
from bs4 import BeautifulSoup
import random

def download_images(data,no,num_images=15):
    # user can input a search keyword and the count of images required
# download images from google search image
    Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&safe=active&'

    u_agnt = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',
        } #write: 'my user agent' in browser to get your browser user agent details
    # data = input('Enter your search keyword: ')
    # num_images = int(input('Enter the number of images you want: '))

    # print('Searching Images....')

    search_url = Google_Image + 'q=' + data
    #'q=' because its a  request url, without u_agnt the permission gets denied
    response = requests.get(search_url, headers=u_agnt)
    html = response.text #To get actual result i.e. to read the html data in text mode

            # find all img where class='rg_i Q4LuWd'
    b_soup = BeautifulSoup(html, 'html.parser') #html.parser is used to parse/extract features from HTML files
    results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})

    #extract the links of requested number of images with 'data-src' attribute and appended those links to a list 'imagelinks'
            #allow to continue the loop in case query fails for non-data-src attributes
    count = 0
    imagelinks= []
    for res in results:
        try:
            link = res['data-src']
            imagelinks.append(link)
            count = count + 1
            if (count >= num_images):
                        break

        except KeyError:
                    continue

    # print(f'Found {len(imagelinks)} images')
    # print(f'Searching {data}')

    random.shuffle(imagelinks)

    return imagelinks[:no-1]

