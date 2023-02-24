import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set up the browser driver
driver = webdriver.Chrome(ChromeDriverManager().install())


url ="https://in.hotels.com/Hotel-Search?GOTO=HOTSEARCH&SearchArea=City&SearchType=Place&adults=2&children=&destination=India&endDate=2023-02-25&lang=16393&latLong=&needUTF8Decode=true&regionId=80&rfrr=hotel.search&selected=&semdtl=&sort=RECOMMENDED&startDate=2023-02-21&theme=&useRewards=false&userIntent="
driver.get(url) 
time.sleep(5) 
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
#uitk-card-link
name = soup.find('div', {'class' : 'uitk-spacing uitk-spacing-padding-blockend-three uitk-layout-flex-item'}).text
rating = soup.find('div', {'class' : 'is-visually-hidden'})
data = soup.find('div', {'class' : 'uitk-layout-grid uitk-layout-grid-has-columns-by-small uitk-layout-grid-has-columns-by-medium uitk-layout-grid-has-columns-by-large uitk-layout-grid-has-columns uitk-layout-grid-has-space uitk-layout-grid-display-grid uitk-layout-flex-item'}).text
link = soup.find('div', {'class' : 'uitk-card uitk-card-roundcorner-all uitk-card-has-primary-theme'})


link2 = link.find('a')

link3 = link2.get("href")
sicret_key = str(link3)
#print(link3)
new_link = "https://in.hotels.com"+sicret_key
driver.get(new_link) 
time.sleep(5) 

html = driver.page_source
soup2 = BeautifulSoup(html, "html.parser")
#animities =soup.find('div', {'class' : 'uitk-spacing SimpleContainer'})

#uitk-card-content-section uitk-card-content-section-padded uitk-spacing uitk-spacing-margin-blockend-three uitk-spacing-padding-inline-six uitk-spacing-padding-block-six uitk-card uitk-card-roundcorner-all uitk-card-has-primary-theme
#for location
data3 = soup2.find('div', {'class' : 'uitk-text uitk-type-300 uitk-text-default-theme uitk-layout-flex-item uitk-layout-flex-item-flex-basis-full_width'})

#animities1 = soup2.find_all('div', {'class' : 'lazyload-wrapper'})
# wait = WebDriverWait(soup2, 10)
# div_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="Amenities"]')))
animities1 = soup2.find_all('div', {'class' : 'uitk-spacing uitk-spacing-margin-block-six'})
#uitk-text uitk-type-300 uitk-text-default-theme uitk-layout-flex-item uitk-layout-flex-item-flex-basis-full_width
# print(data)
# print(name)
print(rating)
# print(animities1)
