# Mission to Mars - Web Scraping

## Background
This project scrapes information from three separate websites. The latest Mars News comes from [NASA Mars News](https://mars.nasa.gov/news/), Mars' Facts comes from [Space Facts](https://space-facts.com/mars/), and the images of Mars' Hemispheres come from [Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

To update or run the site for the first time, the user will need to click on "Scrape New Data," this will automatically update the latest Mars news. 


## Contents
### Resources

* [mission_to_mars.ipynb](Missions_to_Mars/mission_to_mars.ipynb) - This script that does the initial scrape. Note: NASA Mars News is slow to connect and may need to be ran twice. 
* [mars_table.html](Missions_to_Mars/mars_table.html) - HTML file of Mars' Facts. This table is create in mission_to_mars.ipynb . 
* [scrape_mars.py](scrape_mars.py) - The same code from mission_to_mars.ipynb, but with a few functions that will connect to app.py . 
* [app.py](app.py) - Uses Mongo and Flask to create HTML webpage that displays all the scraped information. 
* [index.html](Templates/index.html) - HTML file uses Bootstrap to design webpage. 

### Images

* [mission_to_mars.png](Images/mission_to_mars.png)


