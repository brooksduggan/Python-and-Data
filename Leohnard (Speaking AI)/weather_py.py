from bs4 import BeautifulSoup as bs
import requests

city = input()
def getweather(city):
    url = "https://www.accuweather.com/en/us/{}/weather-forecast/".format(city)
    html = requests.get(url).content
    # print("html : " + str(html))
    # create a new soup
    soup = bs(html, 'html.parser')
    # print("SOUP     " + str(soup))
    cur_location = soup.select(".BNeawe tAd8D AP7Wnd")
    cur_temp = soup.find("span", {"id": "wob_dcp"})
    
    print(cur_location)
    
    #response = "The current temperature in " + cur_location + " is " + cur_temp + " degrees."
    #sys.stdout.write(response + "\n")
    #sys.stdout.flush()
    
getweather(city)