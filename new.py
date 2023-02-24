from heapq import merge
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
import time
import csv
from bs4 import BeautifulSoup
import csv
import pandas as pd
driver = webdriver.Chrome(ChromeDriverManager().install())

# url = "https://qoruz.com/find-influencers/top-fashion-vloggers-india"
# print(url)
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')
# url = "https://qoruz.com/find-influencers/top-fashion-vloggers-india"
# print(url)
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')

with open('all_url.txt') as f:
    lines = f.readlines()
    for i in lines:
        url = i
        driver.get(url) 
        time.sleep(5) 
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        # page = requests.get(url)
        # soup = BeautifulSoup(page.content, 'html.parser')
        file_creator_name = url.split('/')[-1:]
        file_creator_name_= file_creator_name[0].strip('\n')
        file_creator_name_csv = file_creator_name_+'.csv'
        channel_type ="instagram"
        #print(soup)
        table2 = soup.find('td.text-center')
        #print(table2)
        #tables = soup.find('table',class_='table table-bordered')
        items = []
        products = soup.select('div.table-name-details')
        #print(products)
        tables = soup.find('table',class_='table table-bordered')
        #print(tables)

        for row in tables.find_all('tr')[1:]:
            name = row.select('p > a')[0].text
            handle = row.select('span')[0].text
            img = row.select('p > img')
            for im in img:
                imgs = im.get('src')
            imgs_o = row.select('p > a')

            for img in imgs_o:
                imgd = img.get('href')
                url = imgd
                driver.get(url) 

                time.sleep(10) 

                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                new_divs = soup.find('div', {'class' : 'profile-info'})
                name = new_divs.select('h5')[0].text
                img = soup.find('img',{'class':'img-fluid'})
                src = img.get('src')
                email = soup.find('span',{'class':'about'}).text
                try:
                    location = soup.find('span',{'class':'location'}).text
                except:
                    location = 'Not available'
                desc = soup.find('ul',{'class':'tag-list success'}).text
                social = soup.find('div',{'class':'block box social-profile'})
                head_social = social.select('ul')
                list2 =[]
                list2.append(name)
                list2.append(src)
                list2.append(email)
                list2.append(location)
                list2.append(desc)
                list1=[]
                list1.append('name')
                list1.append('img')
                list1.append('email')
                list1.append('location')
                list1.append('desc')





                for ul in head_social:
                    for li in ul.find_all('li'):
                        new = li.find('h6').text
                        span = li.findAll('div',{'class':'user-status noselect'})
                        for s in span:
                            ns = li.findAll('h6')
                        
                            for i in ns:
                                nre = i.text
                                list1.append(nre)
                            nn = li.findAll('span')
                            for i in nn:
                                nrn = i.text
                            # print(nrn)
                                list2.append(nrn)
                # del list2[5]
                # del list2[10]
                # del list2[15]
                # del list2[20]
                # print(list2)
                # print(list1)
                dict1 ={}
                key= ['creator1_name','image_url1','description','locaiton','desc','insta_username','score1', 'insta_followersc', ' insta Average Likes', 'insta Average Comments', ' insta Average Video Views','twitter_username', 'Score2', 'fb_followers', 'tw Total Tweets', 'tw Average Favourites', 'tw Average Retweets','fb_username', 'Score3', 'fb Page Likes', 'fb Average Likes', 'fb Average Comments', 'fb Average Shares', 'youtube_username','Score4', 'youtube_followers', 'youtube Total Videos', 'youtube Average Likes', ' youtube Average Views']
                key2= ['creator1_name','image_url1','description','locaiton','desc','insta_username','score1', 'insta_followersc', ' insta Average Likes', 'insta Average Comments', ' insta Average Video Views','twitter_username', 'Score2', 'fb_followers', 'tw Total Tweets', 'tw Average Favourites', 'tw Average Retweets', 'fb_username','Score3', 'fb Page Likes', 'fb Average Likes', 'fb Average Comments', 'fb Average Shares']
                key3= ['creator1_name','image_url1','description','locaiton','desc','insta_username','score1', 'insta_followersc', ' insta Average Likes', 'insta Average Comments', ' insta Average Video Views','twitter_username', 'Score2', 'fb_followers', 'tw Total Tweets', 'tw Average Favourites', 'tw Average Retweets']
                key4= ['creator1_name','image_url1','description','locaiton','desc','insta_username','score1', 'insta_followersc', ' insta Average Likes', 'insta Average Comments', ' insta Average Video Views']


                if len(list1)==25:
                    list1.insert(5,'insta_username')
                    list1.insert(11,'twitter_username')
                    list1.insert(17,'fb_username')
                    list1.insert(23,'youtube creator_name')
                    #print(list1)
                if len(list1)==20:
                    list1.insert(5,'insta_username')
                    list1.insert(11,'twitter_username')
                    list1.insert(17,'fb_username')
                if len(list1)==15:
                    list1.insert(5,'insta_username')
                    list1.insert(11,'twitter_username')
                if len(list1)==10:
                    list1.insert(5,'insta_username')

                #     print(list1)
                if len(list1) == len(key):
                    for i in range(len(key)):
                        dict1[key[i]]=list2[i]
                    print(len(key))
                elif len(list1)==len(key2):
                    for i in range(len(key2)):
                        
                        dict1[key2[i]]=list2[i]
                    print(len(key2))
                elif len(list1)==len(key3):
                    for i in range(len(key3)):
                        dict1[key3[i]]=list2[i]
                    print(len(key3))

                elif len(list1)==len(key4):
                    for i in range(len(key4)):
                        dict1[key4[i]]=list2[i]
                    print(len(key4))
                else:
                    print('The key and value not same')
                    print()
                data = row.find_all('td')[1:5]
                row_data = [td.text.strip() for td in data]
        # print(row_data)  
                dicup = {
                    "creator_name": name,
                    "channel_type":"Instagram",
                    "handle_name": handle,
                    "blog_url":imgd,
                    "image_url":imgs,
                    "insta_followers":row_data[0],
                    'avg_ngagement':row_data[1],
                    'engagement_rate':row_data[2],
                    'avg_video_views':row_data[3]
                    }
                
                final = {**dicup,**dict1}
                items.append(final) 
                #print(dict1)
            # print(final)
                time.sleep(0.1) 
        #key = items[0].keys() 
        #print(key) 
        # with open(file_name_csv, 'w', newline='') as output_file:
        #     dict_writer = csv.DictWriter(output_file, key)
        #     dict_writer.writeheader()
        #     dict_writer.writerows(items) 
        #print(items)


        dict_key = ['creator_name','channel_type','handle_name','blog_url','image_url','insta_followers','avg_ngagement','engagement_rate','avg_video_views','creator1_name','image_url1','description','locaiton','desc','insta_username','score1', 'insta_followersc', ' insta Average Likes', 'insta Average Comments', ' insta Average Video Views','twitter_username', 'Score2', 'fb_followers', 'tw Total Tweets', 'tw Average Favourites', 'tw Average Retweets','fb_username', 'Score3', 'fb Page Likes', 'fb Average Likes', 'fb Average Comments', 'fb Average Shares', 'youtube_username','Score4', 'youtube_followers', 'youtube Total Videos', 'youtube Average Likes', ' youtube Average Views']

        with open(file_creator_name_csv, 'w',encoding="utf-8", newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, dict_key)
            dict_writer.writeheader()
            dict_writer.writerows(items)  




        # dict_key = ['creator_name','channel_type','handle_name','blog_url','image_url','insta_followers','avg_ngagement','engagement_rate','avg_video_views','creator1_name','image_url1','description','locaiton','desc','insta_username','score1', 'insta_followersc', ' insta Average Likes', 'insta Average Comments', ' insta Average Video Views','twitter_username', 'Score2', 'fb_followers', 'tw Total Tweets', 'tw Average Favourites', 'tw Average Retweets','fb_username', 'Score3', 'fb Page Likes', 'fb Average Likes', 'fb Average Comments', 'fb Average Shares', 'youtube_username','Score4', 'youtube_followers', 'youtube Total Videos', 'youtube Average Likes', ' youtube Average Views']

        # with open(file_creator_name_csv, 'w', newline='') as output_file:
        #     dict_writer = csv.DictWriter(output_file, dict_key)
        #     dict_writer.writeheader()
        #     dict_writer.writerows(items) 
        # with open(file_name_csv, 'w',newline='') as csvfile:
        #     writer = csv.DictWriter(csvfile, fieldnames=dict_key)
        #     writer.writeheader()
        #     for data in items:
        #         writer.writerow(data)
            # with open(file_name_csv, 'w') as csvfile:
            #     writer = csv.writer(csvfile, delimiter=',')
            #     writer.writerows(items)
        
            # import pandas as pd
            # dic = items
            # df = pd.DataFrame.from_dict(dic, orient='index') #Convert dict to df
            # print(df)
            # df.to_csv(file_name_csv,header=False)
        