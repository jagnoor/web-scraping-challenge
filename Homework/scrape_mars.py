# Importing Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time as tm
import pandas as pd

def init_browser():
    # Setting Up Splinter
    executable_path = {'executable_path': "C:/Windows/chromedriver"}
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    # URL to NASA Mars News Site
    url_NASA_News = 'https://mars.nasa.gov/news/'
    browser.visit(url_NASA_News)
    # Visiting the URL Takes Some Time, Using the Time Module to Slow Down the Run
    tm.sleep(5)
    # HTML Object
    html = browser.html
    # Parse with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')


    # Scraping for Latest Title
    slidebar = soup.find('li', class_='slide')
    categories = slidebar.find_all('div', class_='content_title')
    for category in categories:
        news_title = category.text.strip()

    # Scraping for Latest Paragraph
    slidebar = soup.find('li', class_='slide')
    categories = slidebar.find_all('div', class_='article_teaser_body')
    for category in categories:
        news_p = category.text.strip()


    # Creating Mars Data Table
    # URL Path to Mars Facts
    url_Mars_Facts = 'https://space-facts.com/mars/'

    # Creating Table with Pandas
    tables = pd.read_html(url_Mars_Facts)

    # Grabbing Mars Data and Putting in DataFrame
    df = tables[0]
    df = df.rename(columns={1:'Mars', 0:' '})

    # Converting DataFrame to HTML Table String
    html_table = df.to_html()

    #Stripping Unwanted Newlines
    html_table.replace('\n', '')


    # URL Path to USGS Astrogeology
    URL_USGS_Astrogeology = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(URL_USGS_Astrogeology)

    # HTML Object
    html = browser.html
    # Parse with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Visiting the URL Takes Some Time, Using the Time Module to Slow Down the Run
    tm.sleep(5)
    # URL Path to USGS Home Page
    URL_USGS_HomePage = 'https://astrogeology.usgs.gov'

    # Scraping
    field_item = soup.find_all('a', class_='itemLink product-item')

    # Creating List of hrefs and Dropping Duplicates
    hrefs_list = [item.get('href') for item in field_item]
    hrefs_list = list(set(hrefs_list))

    # Creating Dictionary of hemisphere_image_urls
    hemisphere_image_urls = []

    # For Loop Grab the Title and Image Path
    for href in hrefs_list:
        # Creating URL for Mars Hemispheres Page
        URL_Hemis = URL_USGS_HomePage + href
        browser.visit(URL_Hemis)
        
        # HTML Object
        html = browser.html
        
        # Parse with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        
        #Scraping Title
        img_title = soup.find_all('h2', class_='title')
        for t in img_title:
            img_title_clean = t.text.strip()
        
        # Scraping img URL
        img_download_thumb = soup.find('div', class_='downloads')
        img_url = img_download_thumb.find_all('a')[0]['href']

        # Appending Dictionary to List
        hemisphere_image_urls.append({"Title": img_title_clean, "img_url": img_url})

    # Storing Data into Dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "hemisphere_image_one": hemisphere_image_urls[0]['img_url'],
        "hemisphere_image_two": hemisphere_image_urls[1]['img_url'],
        "hemisphere_image_three": hemisphere_image_urls[2]['img_url'],
        "hemisphere_image_four": hemisphere_image_urls[3]['img_url'],
        "hemisphere_title_one": hemisphere_image_urls[0]['Title'],
        "hemisphere_title_two": hemisphere_image_urls[1]['Title'],
        "hemisphere_title_three": hemisphere_image_urls[2]['Title'],
        "hemisphere_title_four": hemisphere_image_urls[3]['Title'],
    }

    # Closing Browser
    browser.quit()

    # Return Results
    return mars_data
