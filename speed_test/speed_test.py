#! python3

# speed_test.py - fazer um teste de velocidade no site {url}
# diariamente e receber um mail caso esteja abaixo dos valores.

# Confirmar o contratualizado:
# Minimo 400Mbps / 80Mbps
# Média  475Mbps / 95Mpbs
# Máxima 500Mbps / 100Mbps

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import glob  # usar para encontrar ficheiros num dir.
import os
from dotenv import load_dotenv
import smtplib as smtp
from email.mime.text import MIMEText
import sqlite3

# Aceder ao site da NOS para fazer o teste:
# url do teste:
url = 'https://xperience.nos.pt/solution/OTT_gigaJS/'
browser = webdriver.Chrome()
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
print("Doing speed test...")
time.sleep(60)
# Criação de un dicionário para captar os dados:
dict_test = {}
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


with open(str(dict_test['id']) + '.txt', 'w') as f:
    for key, value in dict_test.items():
        f.write("%s: %s\n" % (key, value))
    f.close()
print("Closing the browser...")
browser.close()

# Enviar um mail com a informação se for abaixo do minimo 400Mbps / 80Mbps
if float(dict_test['Download']) < 400.00 or float(dict_test['Upload']) < 80.00:
    # ficheiro com a informação do teste
    txt_log = open(str(dict_test['id']) + '.txt')
    data = txt_log.read()
    # dados para o email
    load_dotenv()
    email_addr = os.getenv('email_address')
    email_passwd = os.getenv('email_password')
    email_sendr = 'diogobarrios22@gmail.com'
    email_subject = 'Teste de Velocidade a ' + str(dict_test['Data'])
    message = MIMEText(data)
    message['From'] = email_addr
    message['To'] = email_sendr
    message['Subject'] = email_subject
    print("Connecting with the server using SSL...")
    time.sleep(2)
    # Conectar ao servidor
    server = smtp.SMTP_SSL('smtp.gmail.com', 465)
    con = server.login(email_addr, email_passwd)
    print("Sending mail...")
    send_mail = server.sendmail(email_addr, email_sendr, message.as_string())
    print("Closing connection with the server...")
    time.sleep(2)
    server.quit()
else:
    None

# Remove .txt file created to send mail
remove_tmp_files = glob.glob('*.txt')
for tmp in remove_tmp_files:
    os.remove(tmp)

# Guardar os dados do dicionário numa base de dados sqlite
# connection sqlite3 database
conn = sqlite3.connect('speed_test.db')
# create cursor object
c = conn.cursor()
# create a table internet_speed:
# c.execute('''CREATE TABLE internet_speed (id integer primary key,
# data text, browser text, download real, upload real, ping real,
# jitter real)''')
# Insert new row for each test
c.execute("INSERT INTO internet_speed VALUES(?,?,?,?,?,?,?)",
[dict_test["id"], dict_test["Data"], dict_test["Browser"],
dict_test["Download"], dict_test["Upload"], dict_test["Ping"],
dict_test["Jitter"]])
# Save the changes
conn.commit()
# to see the changes
# c.execute("SELECT * FROM internet_speed")
# c.fetchall()
# Close the connection
conn.close()

# TODO: debugging:
# nao reconhece a tabela já criada no sqlite3



# TODO: Ligar ao Grafana para criar um dashboard com
# limite sup, inf, e média. (Quality Control)
