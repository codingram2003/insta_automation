
from bs4 import BeautifulSoup as bs
import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
print("enter username")
username = "follyfool99"
 
print("enter password")
password = "Jaishriram@12345"
 
print("enter the url")
url = "https://www.instagram.com/"


def path():  
    global chrome
    print("enter the chrome path")
    exe_path = r"C:\Users\shrir\Downloads\chromedriver_win32\chromedriver.exe"
 
    # starts a new chrome session
    chrome = webdriver.Chrome() 



def url_name(url):  
    # the web page opens up
    chrome.get(url) 
    
    # webdriver will wait for 4 sec before throwing a  
    # NoSuchElement exception so that the element 
    # is detected and not skipped.
    time.sleep(4) 

def login(username, your_password):
	

	# finds the username box
	usern = chrome.find_element(By.NAME,"username") 

	# sends the entered username
	usern.send_keys(username) 

	# finds the password box
	passw = chrome.find_element(By.NAME, "password") 

	# sends the entered password
	passw.send_keys(your_password)	 
	passw.send_keys(Keys.RETURN)
	time.sleep(10)
	notn = chrome.find_element(By.CLASS_NAME, "x1i10hfl")# dont save info button
	notn.click()# click don't save button
	time.sleep(10)
	no = chrome.find_element(By.CLASS_NAME, "_a9_1")# dont save info button
	no.click()# click don't save button
	time.sleep(5)
def first_picture():
	pictures = chrome.find_elements(By.CLASS_NAME,'_aagw')
	for picture in pictures:
		picture.click()
		print("Clicked")
		picture.click()
		print("Clicked")
		time.sleep(1000)
		#like_pic()
		#time.sleep(3)



def like_pic():
	time.sleep(2)
	like = chrome.find_element(By.CLASS_NAME,'xyb1xck')
	soup = bs(like.get_attribute('innerHTML'),'html.parser')
	if(soup.find('svg')['aria-label'] == 'Like'):
		like.click()
	time.sleep(10000)

def next_picture():
	time.sleep(2)
	try:
		nex = chrome.find_element_by_class_name("coreSpriteRightPaginationArrow")
		time.sleep(1)
		return nex
	except selenium.common.exceptions.NoSuchElementException:
		return 0

def continue_liking():
	while(True):
		next_el = next_picture()

		# if next button is there then
		if next_el != False:

			# click the next button
			next_el.click()
			time.sleep(2)

			# like the picture
			like_pic()
			time.sleep(2)
		else:
			print("not found")
			break

path()
time.sleep(1)

url_name(url)

login(username, password)

first_picture()
#like_pic()

#continue_liking()
#chrome.close()
