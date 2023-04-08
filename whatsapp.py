from selenium import webdriver  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep
import pyautogui

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://web.whatsapp.com/")

info = "50"

# ============================= Main Idea ============================= 

sleep(5) # para que escanee el codigo QR de whatsapp web 


# el chat o el frupo
button = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]'))).click()


for i in range(20):

    # el buscador
    mensage = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')))
    
    # enviar el info
    mensage.send_keys(info)
    
    # precionar enter para enviar
    mensage.send_keys(Keys.ENTER)

# Espera que se mande el mensage al servidor
sleep(5)  #           importante 

