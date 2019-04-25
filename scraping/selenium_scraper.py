from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import json
import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.store

#TASK
# ADD ITEM TYPE [Later]
# USE TRY CATCH 
# CORRECT AMAZON'S CHOICE ITEMS [Done]
# USE DYNAMIC SEARCH TERMS TO GET ITEM



def collect_products(page, max, driver):
    elem=driver.find_elements_by_class_name('s-result-item')
    for a in range(len(elem)):
        item={'link':'' , 'rating': '', 'title':'' , 'price':'' , 'image': '' ,'type':''}
        item_name=elem[a].text.split('\n')[0].replace(' ','').replace('/','_')
        if item_name != 'Sponsored':
            #setting url for item
            links= elem[a].find_elements_by_class_name('a-link-normal ')
            #print links[0].get_attribute("href").split('/ref')[0]
            item['link'] = links[0].get_attribute("href").split('/ref')[0]
            temp_item=elem[a].text.split('\n')     
            if item_name != "Amazon'sChoice":
                item['title']=temp_item[0]
                item['price']=temp_item[2] 
            else:
                item['title']=temp_item[1]
                item['price']=temp_item[3] 
            spanList=elem[a].find_elements_by_class_name('a-icon-alt')
            #setting rating value
            item['rating']=spanList[0].get_attribute("innerHTML").split(' ')[0]
            #download image
            img = elem[a].find_elements_by_class_name('s-image')
            src = img[0].get_attribute('src')
            urllib.urlretrieve(src, 'img/' + item_name  +".png") 
            item['image']=src  
            #save to mongodb
            db.products.insert_one(item).inserted_id
            #print item    
    if page < max:
        pagin=driver.find_element_by_class_name('a-pagination')
        pages=pagin.find_elements_by_tag_name("a")
        for a in pages:
            if a.text == str(page +1):
                a.click()
                return collect_products(page+1,max, driver)
    elif page >= max:
        return 'done'
        
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/s?k=gaming+laptops&ref=nb_sb_noss_2")
result=collect_products(0,1,driver)

#driver.close()