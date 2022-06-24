#! python3

# speed_test.py - fazer um teste de velocidade no site {url}
# diariamente e receber um mail.

# Confirmar o contratualizado:
# Minimo 400Mbps / 80Mbps
# Média  475Mbps / 95Mpbs
# Máxima 500Mbps / 100Mbps

import time
import speed_test_func as stf

# Access to url, do the test, store the data
dict_test = stf.test_access_store(input('(nos/meo/vodafone): '))

# Rest for a while.
time.sleep(30)

# create a tmp .txt file with the data
tmp_file = stf.wr_tmp_files(dict_test['id'])

# send mail with the basis of the file
stf.send_mail('diogobarrios22@gmail.com', 400.00, 80.00)

# remove the file from os
stf.rm_tmp_files('*.txt')

# insert the values from collect data into database
stf.insert_values(dict_test["id"], dict_test["Data"], dict_test["Browser"],
                  dict_test["Download"], dict_test["Upload"], dict_test["Ping"],
                  dict_test["Jitter"])
