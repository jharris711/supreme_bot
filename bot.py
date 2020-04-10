from config import keys
from selenium import webdriver
from time import sleep
import requests



def orderIt(k):

    driver = webdriver.Chrome('./chromedriver')
    
    #Selenium get URL:
    driver.get(k['product_url'])
    driver.set_window_size(1120, 750)

    #Requests get URL:
    r = requests.get(k['product_url'])
    status = r.status_code


    #Check for status code: 200:
    def checkStatusCode(status=status):
        if status != 200:
            return False
        return True


    #If 200:
    if checkStatusCode():
        print(f"STATUS: {status}")
        #Start ordering process:
        order_loop = True
        while order_loop:
            status_check1 = True
            while status_check1:
                #add to cart:
                driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
                sleep(1)
                if checkStatusCode():
                    status_check1 = False
                    status_check2 = True
            while status_check2:
                #view cart:
                driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
                if checkStatusCode():
                    status_check2 = False
                    status_check3 = True
            while status_check3:
                #enter name:
                driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k['name'])
                if checkStatusCode():
                    status_check3 = False
                    status_check4 = True
            while status_check4:
                #enter email:
                driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k['email'])
                if checkStatusCode():
                    status_check4 = False
                    status_check5 = True
            while status_check5:
                #Enter tel num:
                driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k['tel'])
                if checkStatusCode():
                    status_check5 = False
                    status_check6 = True
            while status_check6:
                #Enter address:
                driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k['addy'])
                if checkStatusCode():
                    status_check6 = False
                    status_check7 = True
            while status_check7:
                #Enter ZIP Code:
                driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k['zip'])
                if checkStatusCode():
                    status_check7 = False
                    status_check8 = True
            while status_check8:
                #Enter CC Num:
                driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k['cc'])
                if checkStatusCode():
                    status_check8 = False
                    status_check9 = True
            while status_check9:
                #Enter Security Code:
                driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k['sc'])
                if checkStatusCode():
                    status_check9 = False
                    status_check10 = True
            while status_check10:
                #Enter CC Month:
                driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[11]').click()
                if checkStatusCode():
                    status_check10 = False
                    status_check11 = True
            while status_check11:
                #Enter CC Year:
                driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[4]').click()
                if checkStatusCode():
                    status_check11 = False
                    status_check12 = True
            while status_check12:
                #Click box:
                driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
                if checkStatusCode():
                    status_check12 = False
                    status_check13 = True
            while status_check13:
                #process payment:
                driver.find_element_by_xpath('//*[@id="pay"]/input').click()
                if checkStatusCode():
                    status_check13 = False
                    order_loop = False
"""
No way to bypass captcha at the moment...
Will have to be solved manually...
"""


if __name__ == '__main__':
    orderIt(keys)