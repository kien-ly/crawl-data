# Import libraries and packages for the project 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
print('- Finish importing packages')

# Task 0: Import from text.txt
credential = open('text.txt')
line = credential.readlines()
url = line[0]
username = line[1]
password = line[2]
print('- Finish importing')

# Task 1.1: Open Chrome and Access web login site
driver = webdriver.Chrome(executable_path="./chromedriver")
sleep(2)
# url = 'https://www.linkedin.com/login'
driver.get(url)
print('- Finish initializing a driver')
sleep(2)

# Task 1.2: Key in login credentials
email_field = driver.find_element_by_id('username')
email_field.send_keys(username)
print('- Finish keying in user')
sleep(2)

password_field = driver.find_element_by_id('password')
# password_field = driver.find_element_by_name('session_password')
password_field.send_keys(password)
print('- Finish keying in password')
sleep(2)

# # Task 1.2: Click the Login button
# signin_field = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
# signin_field.click()
# sleep(3)

print('- Finish Task 1: Login ')
diem_field = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[4]/div/div/div[1]/div/div[3]/a/div')
diem_field.click()
print('** click ')
sleep(4)


# Task: Scrape the data, and write the data to a .CSV file
with open('output.csv', 'w',  newline = '') as file_output:
    headers = ['Mã MH', 'Tên MH', 'Số TC', 'Điểm tp','THI','Tổng Kết']
    writer = csv.DictWriter(file_output, delimiter=',', lineterminator='\n',fieldnames=headers)
    writer.writeheader()

    soHang = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div/table/tbody/tr"))
    # print(soHang) 
    soBang = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div/table/tbody"))
    # print(soBang)
    bangdiem = {'Mã MH': [],  'Tên MH':[],'Số TC': [], 'Điểm tp': [], 'THI': [], 'Tổng Kết': []}
    for bang in range(3, soBang*3+1,3):
        soHang = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr"))
        for hang in range(1, soHang + 1):
            if hang <= soHang-2:
                # print(soHang)
                Ten = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[2]"
                MH =driver.find_element_by_xpath(Ten).text
                MaMH = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[1]"
                TC = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[4]"
                TP = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[5]"
                Thi = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[6]"
                TK = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[7]"
                ma = driver.find_element_by_xpath(MaMH).text
                name= driver.find_element_by_xpath(Ten).text
                tc = driver.find_element_by_xpath(TC).text
                tp = driver.find_element_by_xpath(TP).text
                thi = driver.find_element_by_xpath(Thi).text
                tk = driver.find_element_by_xpath(TK).text                           
                # bangdiem[MH].append(chitiet)
                chitiet = [name, ma, tc, tk]
                print(chitiet)
                writer.writerow({headers[0]:ma, headers[1]:name, headers[2]:tc, headers[3]:tp, headers[4]:thi, headers[5]:tk})
    print('Mission Completed!')
