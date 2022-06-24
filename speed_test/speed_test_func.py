#! python3

# speed_test_func.py - fazer um teste de velocidade no site {url}
# diariamente e receber um mail.

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


def test_access_store(isp):
    """Accessing to internet service provider (isp)
       Save the data in a dictionary"""

    if isp.lower() == 'nos':

        url = 'https://xperience.nos.pt/solution/OTT_gigaJS/'
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(30)

        start_simulated = browser.find_element(By.ID, 'startButton')
        start_simulated.click()
        time.sleep(5)

        check_button = browser.find_element(By.TAG_NAME, 'label')
        check_button.click()
        time.sleep(5)

        start_button = browser.find_element(By.ID, 'startButton')
        start_button.click()
        print("Starting speed test...")
        time.sleep(80)
        init_dict = {'id': 'testid', 'Data': 'data', 'Browser': 'browser',
                     'Download': 'dl', 'Upload': 'ul', 'Ping': 'ping',
                     'Jitter': 'jitter'}

        dict_finale = {}
        for k, v in init_dict.items():
            find_on_page = browser.find_element(By.ID, v).get_attribute('innerHTML')
            dict_finale[k] = find_on_page
        print("Storing the data speed test...")

    else:
        None  # it will have another isp here!

    print("Closing the browser...")
    return dict_finale
    browser.close()


def wr_tmp_files(string):
    """Create a .txt file to attach to a mail"""

    print("Creating .txt tmp files...")
    with open(str(string) + '.txt', 'w') as tmp_file:
        for key, value in dict_test.items():
            tmp_file.write("%s: %s\n" % (key, value))
        tmp_file.close()
    return tmp_file


def send_mail(email_sender, min_download, min_upload):
    """Sending a mail with the information
        if the data is below the metrics of Download/Upload"""

    if float(dict_test['Download']) < min_download or float(dict_test['Upload']) < min_upload:

        print("Abrir o ficheiro .txt com os dados para enviar mail...")
        txt_log = open(str(dict_test['id']) + '.txt')
        data = txt_log.read()
        load_dotenv()
        email_addr = os.getenv('email_address')
        email_passwd = os.getenv('email_password')
        email_subject = 'Teste de Velocidade a ' + str(dict_test['Data'])
        message = MIMEText(data)
        message['From'] = email_addr
        message['To'] = email_sender
        message['Subject'] = email_subject
        print("Connecting with the server using SSL...")
        time.sleep(2)

        print("Conectando ao servidor")
        server = smtp.SMTP_SSL('smtp.gmail.com', 465)
        con = server.login(email_addr, email_passwd)

        print("Sending mail...")
        send_mail = server.sendmail(email_addr, email_sender, message.as_string())
        print("Closing connection with the server...")
        time.sleep(2)
        server.quit()
    else:
        None


def rm_tmp_files(type_of_file):
    """Remove tmp .txt file created to send mail"""

    remove_tmp_files = glob.glob(type_of_file)
    print("Cleaning tmp files...")
    for tmp in remove_tmp_files:
        os.remove(tmp)


def insert_values(id, data, browser, download, upload, ping, jitter):
    """Updating speed_test database with the new data"""

    try:
        conn = sqlite3.connect('speed_test.db')
        c = conn.cursor()
        print('Connected to SQLite')

        sqlite_insert_param = """INSERT INTO internet_speed
                            (id, data, browser, download, upload, ping, jitter)
                            VALUES (?, ?, ?, ?, ?, ?, ?);"""

        test_speed_data = (id, data, browser, download, upload, ping, jitter)
        c.execute(sqlite_insert_param, test_speed_data)
        conn.commit()
        print(f'Data from speed test done at {data} inserted successfully!')

        conn.close()

    except sqlite3.Error as error:
        print("Failed to insert data from speed test into internet_speed table", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")
