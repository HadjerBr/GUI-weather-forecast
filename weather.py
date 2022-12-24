from bs4 import BeautifulSoup
import requests
import urllib.request

city_name = ""
temperature = ""
date_and_time= ""
sky = ""
precipitation = ""
humidity = ""
wind = ""



def get_weather(city):
    global city_name, temperature, date_and_time, sky, precipitation, humidity, wind
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    result = requests.get(f"https://www.google.com/search?q=weather+in+{city}&ei=-yynY8_TLtODxc8Pkr6kwAE&oq=weather+in+&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgoIABCRAhBGEIACMgUIABCRAjIFCAAQkQIyBQgAEJECMgUIABCRAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOhIILhDHARDRAxDqAhC0AhBDGAE6DAgAEOoCELQCEEMYAToECAAQQzoLCC4QgAQQxwEQ0QM6CAguEIAEENQCOgkIABBDEEYQgAI6BwgAEMkDEENKBAhBGABKBAhGGABQjghYjiJg2DRoAXAAeACAAbwBiAGqDpIBBDAuMTGYAQCgAQGwAQrAAQHaAQQIARgH&sclient=gws-wiz-serp", headers = headers).content
    soup = BeautifulSoup(result, "lxml")
    city_name = soup.find("div", class_ = "wob_loc q8U8x").text
    temperature = soup.find("span", class_ = "wob_t q8U8x").text
    date_and_time = soup.find("div", class_ = "wob_dts").text
    sky = soup.find("span", {"id": "wob_dc"} ).text
    precipitation = soup.find("span", {"id": "wob_pp"}).text
    humidity = soup.find("span", {"id": "wob_hm"}).text
    wind = soup.find("span", {"id": "wob_ws"}).text
    # image = soup.find("img", {"class" : "wob_tci"})
    # url = image["src"]
    # link = ("C:\\Users\\orange\\OneDrive\\Documents\\3rd year computer engineering\\weather forecast python\\image.png")
    # urllib.request.urlretrieve(url, link)