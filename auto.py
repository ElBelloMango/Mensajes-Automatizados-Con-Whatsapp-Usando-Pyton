from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from urllib.parse import quote
import time


s = Service(EdgeChromiumDriverManager().install())
opt = Options()
opt.add_argument("user-data-dir=C:\\Users\\magoz\\AppData\\Local\\Microsoft\\Edge\\User Data 2") #Browser User Data
web = webdriver.Edge(service=s,options = opt)

def sendToPerson(nro,mensaje,driver):
    numero = nro
    message = ""
    url = "https://web.whatsapp.com/send?phone={}&text={}"
    ready = url.format(str(numero),quote(message))
    driver.get(ready)
    time.sleep(30)
    msgBox = web.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    SendButton = web.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]')
    Send(mensaje,msgBox,SendButton)
    
def Send(mensaje,msgBox,SendButton):
    msgBox.send_keys(mensaje)
    SendButton.click()

def sendToGroup(mensaje,idGrupo,driver):
    url = "https://web.whatsapp.com/accept?code={}"
    ready = url.format(str(idGrupo))
    driver.get(ready)
    time.sleep(30)
    msgBox = web.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    SendButton = web.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]')
    Send(mensaje,msgBox,SendButton)
    # driver.switchTo().alert().dismiss();

while (True):
    tiempo = time
    hora = tiempo.strftime("%H")
    minutos = tiempo.strftime("%M")
    segundos = tiempo.strftime("%S")
    if hora == "10" and minutos =="00" and segundos == "00":
        sendToGroup("¡Hora de hacer el desayuno!","FadinAo7Og5A8KgXoPQoTEF",web)
        time.sleep(2)
    elif hora == "11" and minutos =="30" and segundos == "00":
        sendToGroup("¿Hiciste el desayuno?","FadinAo7Og5A8KgXoPQoTEF",web)
        time.sleep(2)
    elif hora == "12" and minutos =="00" and segundos == "00":
        sendToGroup("¡Hora de hacer el taller de estadistica!","FadinAo7Og5A8KgXoPQoTEF",web)
        time.sleep(2)
    elif hora == "13" and minutos =="30" and segundos == "00":
        sendToGroup("¿Hiciste el taller de estadistica?","FadinAo7Og5A8KgXoPQoTEF",web)
        time.sleep(2)  
    elif hora == "14" and minutos =="00" and segundos == "00":
        sendToGroup("¡Unete al Meet!","FadinAo7Og5A8KgXoPQoTEF",web)
        time.sleep(2)
    elif hora == "15" and minutos =="30" and segundos == "00":
        sendToGroup("¿Te uniste al Meet?","FadinAo7Og5A8KgXoPQoTEF",web)
        time.sleep(2) 
    elif hora == "18" and minutos =="00" and segundos == "00":
        sendToGroup("¡Estudia para el parcial!","FadinAo7Og5A8KgXoPQoTEF",web)
        time.sleep(2)
    elif hora == "19" and minutos =="30" and segundos == "00":
        sendToGroup("¿Estudiaste para el parcial?","FadinAo7Og5A8KgXoPQoTEF",web)
        time.sleep(2) 
        web.quit()
    elif int(minutos)%10==0 and segundos == "00":
        sendToGroup("Son las "+hora+":"+minutos+" el programa funciona correctamente","GP1quFBYDqrCN3XBnuqxHF",web)
        print(hora+":"+minutos)
        time.sleep(2)
    elif int(minutos)%5==0 and segundos == "00":
        print(hora+":"+minutos)
        time.sleep(2)
    time.sleep(1)