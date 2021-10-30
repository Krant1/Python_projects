from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import notifypy

s=Service('/Users/manojrai/Downloads/chromedriver')
driver=webdriver.Chrome(service=s)
url='https://www.coindesk.com/price/bitcoin/'
driver.get(url)

def bit_val():
    cur_val=driver.find_element(By.XPATH,'//*[@id="fusion-app"]/div/div[1]/div[1]/div/div[1]/div[3]/div[1]/span[2]').text
    cur_val=cur_val.replace(',','')
    return float(cur_val)

def btc():
    while True:
        prev_val=bit_val()
        time.sleep(5)
        cur_val=bit_val()
        if cur_val>prev_val:
            return f'The value rose by {cur_val-prev_val}'
        elif prev_val>cur_val:
            return f'The value fell by {prev_val-cur_val}'
        else:
            return 'The value remains the same'

while True:
    val_btc=btc() 
    notification = notifypy.Notify()    
    notification.title = "Bitcoin Price Alert"
    notification.message = val_btc
    notification.send()