from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def ubah_ke_format_internasional(nomor):
    if nomor.startswith('0'):
        return '+62' + nomor[1:]
    return nomor


driver = webdriver.Firefox()
processed_numbers = []
output_file_path = '../Promosi/nomor_telephon/surabaya.txt'
file  = open(output_file_path, 'a', encoding='utf-8')
start_i = -7.466473000000001
start_j = 112.5762886
max_i = round((-1*-7.517688+start_i)// 0.01)
max_j = round((-1*112.4028987+start_j)//0.02)

print(max_i, max_j)

for i in range(0, max_i):
    for j in range (0,max_j):
        driver.get(f"https://www.google.com/maps/search/Toko/@{+start_i-i * 0.01},{start_j-j * 0.02},16z/")
        print(f"{+start_i-i * 0.01},{start_j-j * 0.02}")
        print(f"{i,j}")
        elem = driver.find_elements(By.CLASS_NAME, "UsdlK")
        if len(driver.find_elements(By.CLASS_NAME, "m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd"))>0:    
            time.sleep(10)
            for k, number in enumerate([a.text for a in elem]):
                    
                if number.startswith('('):
                    continue  # Skip numbers that start with '('
                file.write(ubah_ke_format_internasional(number))
                file.write(',')
        
        #processed_numbers.extend([a.text for a in elem])
        # Memproses nomor telepon
# processed_numbers = process_phone_numbers(processed_numbers)
# processed_numbers = list(set(processed_numbers))
# # Menyimpan hasil ke file .txt

# save_numbers_to_file(processed_numbers, output_file_path)
# print(f"Processed phone numbers have been saved to {output_file_path}")