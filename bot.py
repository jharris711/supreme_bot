from config import keys
from selenium import webdriver
from time import sleep
import urllib.request


def orderIt(k):

    driver = webdriver.Chrome('./chromedriver')
    

    driver.get(k['product_url'])
    driver.set_window_size(1120, 750)

    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    sleep(.5)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k['name'])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k['email'])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k['tel'])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k['addy'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k['zip'])
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k['cc'])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k['sc'])
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[11]').click()
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[4]').click()
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    #process payment:
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()
    



if __name__ == '__main__':
    orderIt(keys)