from flask import *
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/prenota")
def result():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    CHROME_DRIVER = r"chromedriver.exe"
    service = Service(executable_path=CHROME_DRIVER)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url="https://www.booking.com/city/ru/moscow.it.html")
    time.sleep(1)
    cookies=driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
    cookies.click()
    driver2 = webdriver.Chrome(service=service, options=chrome_options)
    driver2.get(url="https://www.google.com/flights?rlz=1C1CHBF_itIT956IT956&sxsrf=AJOqlzWbSwcV52M1Uy2J1mQyFA6DxymMBg%3A1677103678767&source=flun&uitype=cuA_&hl=it&gl=it&curr=EUR&tfs=CAEQARoeEgoyMDIzLTAzLTEwMgJUS2oMCAISCC9tLzBjNjZtGh4SCjIwMjMtMDMtMTQyAlRLcgwIAhIIL20vMGM2Nm16aENqUklZa1JKYjJ3eVkwOUZXR05CUTFORVFrRkNSeTB0TFMwdExTMHRMUzEzWldGcE5VRkJRVUZCUjFBeWEybzBUalprTmtGQkVnRXpHZ3NJMUt3QkVBSWFBMFZWVWpnRGNJaTNBUT09&ved=2ahUKEwjD1JiIkqr9AhUkolwKHY-bDgwQlhd6BAgUEA4")
    time.sleep(1)
    cookies2 = driver2.find_element(by=By.XPATH, value= '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/form[1]/div/div/button/span')
    cookies2.click()
    time.sleep(2)
    andata = driver2.find_element(by= By.XPATH, value= '//*[@id="i15"]/div[4]/div/div/div[1]/div/div/input')
    time.sleep(1)
    andata.click()
    time.sleep(1)
    ritorno = driver2.find_element(by=By.XPATH, value='//*[@id="i15"]/div[6]/div[2]/div[2]/div[1]/div/input')
    time.sleep(1)
    ritorno.send_keys("Mosca")
    time.sleep(1)
    mosca = driver2.find_element(by=By.XPATH, value='//*[@id="c50"]/div[2]')
    mosca.click()
    time.sleep(1)
    cerca = driver2.find_element(by=By.XPATH, value='//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button/span[2]')
    cerca.click()
    return "Grazie di aver utilizzato il nostro servizio!"





if __name__ == "__main__":
    app.run(debug=True)