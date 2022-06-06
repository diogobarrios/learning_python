#! python3

# speed_test.py - fazer um teste de velocidade no site {url}
# diariamente e receber um mail.

# Confirmar o contratualizado:
# Minimo 400Mbps / 80Mbps
# Média  475Mbps / 95Mpbs
# Máxima 500Mbps / 100Mbps

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# TODO: Marcar diariamente o teste:

# Aceder ao site a fazer o teste:

# url do teste:
url = 'https://xperience.nos.pt/solution/OTT_gigaJS/'
browser = webdriver.Chrome()
# browser.maximize_window()
browser.get(url)
time.sleep(20)

# Aceitar os termos e condições
button = browser.find_element(By.ID, 'startButton')
button.click()
time.sleep(5)
chk = browser.find_element(By.TAG_NAME, 'label')
chk.click()
time.sleep(5)
button = browser.find_element(By.ID, 'startButton')
button.click()
# Tirar os dados de download/upload do teste:
print("Doing test speed...")
time.sleep(60)
# Criação de un dicionário para captar os dados:
dict_test = {'id': (browser.find_element(
                By.ID, 'testid')).get_attribute('innerHTML'),
             'Data': (browser.find_element(
                 By.ID, 'data')).get_attribute('innerHTML'),
             'Browser': (browser.find_element(
                 By.ID, 'browser')).get_attribute('innerHTML'),
             'Download': (browser.find_element(
                 By.ID, 'dl')).get_attribute('innerHTML'),
             'Upload': (browser.find_element(
                 By.ID, 'ul')).get_attribute('innerHTML'),
             'Ping': (browser.find_element(
                 By.ID, 'ping')).get_attribute('innerHTML'),
             'Jitter': (browser.find_element(
                 By.ID, 'jitter')).get_attribute('innerHTML')
             }

print("The values are...")
for item in dict_test:
    print("%s: %s" % (item, dict_test[item]))

print("Closing...")
browser.close()
# TODO: Enviar um mail.

# TODO: Criar uma tabela onde o dicionário vai adicionando os dados
# TODO: Ligar ao Grafana para criar um dashboard com
# limite sup, inf, e média. (Quality Control)
