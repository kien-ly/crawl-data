# Import libraries and packages for the project 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
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
print('- Finish keying in email')
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
# def Crawl(driver,NamHoc, HocKy, TuanHoc):
soHang = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div/table/tbody/tr"))
# print(soHang) /html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[3]/table/tbody
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
            # print(MH)
            MaMH = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[1]"
            TC = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[4]"
            TP = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[5]"
            Thi = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[6]"
            TK = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div[" + str(bang) + "]/table/tbody/tr[" + str(hang) + "]/td[7]"
            chitiet = {'Mã MH:':driver.find_element_by_xpath(MaMH).text,
                        'Tên MH:':driver.find_element_by_xpath(Ten).text,
                        'Số TC:': driver.find_element_by_xpath(TC).text,
                        'Điểm tp:':driver.find_element_by_xpath(TP).text,
                        'THI:':driver.find_element_by_xpath(Thi).text,
                        'Tổng Kết:':driver.find_element_by_xpath(TK).text}                           
            # bangdiem[MH].append(chitiet)

            print(chitiet)

driverclose()


#                 THU = 'THỨ ' + str(cot)
#                 crawlXpath = "/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[" + str(hang) + "]/td[" + str(cot) + "]"
#                 crawl = driver.find_element_by_xpath(crawlXpath).text
#                 crawlList = crawl.split("\n")
#                 phongHoc = "/html/body/div/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[" + str(hang) + "]/td[1]"
#                 thongTinMonHoc = {'Tên môn: ': crawlList[0],
#                                   'Giờ học: ': crawlList[1],
#                                   'Tiết học: ': crawlList[2],
#                                   'Giáo viên: ': crawlList[3],
#                                   'Phòng học: ': driver.find_element_by_xpath(phongHoc).text}
#                 thoiKhoaBieu[THU].append(thongTinMonHoc)
#     return thoiKhoaBieu

# def SaveFile(thoiKhoaBieu, isVietnamese=True):
#     '''
#         HÀM LƯU DỮ LIỆU VÀO FILE JSON
#         CÓ 2 SỰ LỰA CHỌN LÀ LƯU JSON VỚI TIẾNG VIỆT VÀ LƯU JSON BÌNH THƯỜNG BỊ MÃ HÓA
#     '''
#     if isVietnamese:
#         with open('ThoiKhoaBieu.json', 'w', encoding='utf-8') as jsonFile:
#             json.dump(thoiKhoaBieu, jsonFile, indent=2, ensure_ascii=False)
#     else:
#         with open('ThoiKhoaBieu.json', 'w') as jsonFile:
#             json.dump(thoiKhoaBieu, jsonFile, indent=2)
#     return

# def OpenFile(filePath):
#     '''HÀM MỞ FILE, HIỆN CHỈ HOẠT ĐỘNG VỚI JSON ĐƯỢC MÃ HÓA KHÔNG CHẠY ĐƯỢC VỚI JSON TIẾNG VIỆT'''
#     with open(filePath) as jsonFile:
#         s = json.load(jsonFile)
#     print(s)

# def Run():
#     userName = input("Tài khoản: ")
#     passWord = input("Mật khẩu: ")
#     namHoc = input("Năm học (VD: 2020-2021): ")
#     hocKy = input("Học kỳ (VD: Học kỳ 1): ")
#     tuanHoc = input("Tuần học (VD: 8): ")
#     ThoiKhoaBieu = {}
#     options = EdgeOptions()
#     options.use_chromium = True
#     options.add_argument('headless')
#     options.add_argument('window-size=1920x1080')
#     options.add_argument("disable-gpu")
#     options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
#     driver = Edge(executable_path='.\Driver\msedgedriver.exe', options=options)
#     if (Login(driver,userName, passWord)):
#         #print(Crawl(driver,namHoc, hocKy, tuanHoc))
#         ThoiKhoaBieu = Crawl(driver,namHoc, hocKy, tuanHoc)
#     else:
#         while Login(driver,userName, passWord) == False:
#             userName = input("Tài khoản: ")
#             passWord = input("Mật khẩu: ")
#             Login(driver,userName, passWord)
#         #print(Crawl(driver,namHoc, hocKy, tuanHoc))
#         ThoiKhoaBieu = Crawl(driver, namHoc, hocKy, tuanHoc)
#     print(ThoiKhoaBieu)
#     SaveFile(ThoiKhoaBieu, isVietnamese=True)
#     #OpenFile('ThoiKhoaBieu.json')
#     driver.close()

# # Chạy chương trình
# Run()

# # Task 2: Search for the profile we want to crawl
# # Task 2.1: Locate the search bar element
# search_field = driver.find_element_by_xpath('//*[@class="search-global-typeahead__input always-show-placeholder"]')
# # Task 2.2: Input the search query to the search bar
# search_query = input('What profile do you want to scrape? ')
# search_field.send_keys(search_query)

# # Task 2.3: Search
# search_field.send_keys(Keys.RETURN)

# print('- Finish Task 2: Search for profiles')


# # Task 3: Scrape the URLs of the profiles
# # Task 3.1: Write a function to extract the URLs of one page
# def GetURL():
#     page_source = BeautifulSoup(driver.page_source)
#     profiles = page_source.find_all('a', class_ = 'app-aware-link') #('a', class_ = 'search-result__result-link ember-view')
#     all_profile_URL = []
#     for profile in profiles:
#         # profile_ID = profile.get('href')
#         # profile_URL = "https://www.linkedin.com" + profile_ID
#         profile_URL = profile.get('href')
#         if profile_URL not in all_profile_URL:
#             all_profile_URL.append(profile_URL)
#     return all_profile_URL


# # Task 3.2: Navigate through many page, and extract the profile URLs of each page
# input_page = int(input('How many pages you want to scrape: '))
# URLs_all_page = []
# for page in range(input_page):
#     URLs_one_page = GetURL()
#     sleep(2)
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #scroll to the end of the page
#     sleep(3)
#     next_button = driver.find_element_by_class_name("artdeco-pagination__button--next")
#     driver.execute_script("arguments[0].click();", next_button)
#     URLs_all_page = URLs_all_page + URLs_one_page
#     sleep(2)

# print('- Finish Task 3: Scrape the URLs')


# # Task 4: Scrape the data of 1 Linkedin profile, and write the data to a .CSV file
# with open('output.csv', 'w',  newline = '') as file_output:
#     headers = ['Name', 'Job Title', 'Location', 'URL']
#     writer = csv.DictWriter(file_output, delimiter=',', lineterminator='\n',fieldnames=headers)
#     writer.writeheader()
#     for linkedin_URL in URLs_all_page:
#         driver.get(linkedin_URL)
#         print('- Accessing profile: ', linkedin_URL)
#         sleep(3)
#         page_source = BeautifulSoup(driver.page_source, "html.parser")
#         info_div = page_source.find('div',{'class':'flex-1 mr5'})
#         try:
#             name = info_div.find('li', class_='inline t-24 t-black t-normal break-words').get_text().strip() #Remove unnecessary characters 
#             print('--- Profile name is: ', name)
#             location = info_div.find('li', class_='t-16 t-black t-normal inline-block').get_text().strip() #Remove unnecessary characters 
#             print('--- Profile location is: ', location)
#             title = info_div.find('h2', class_='mt1 t-18 t-black t-normal break-words').get_text().strip()
#             print('--- Profile title is: ', title)
#             writer.writerow({headers[0]:name, headers[1]:location, headers[2]:title, headers[3]:linkedin_URL})
#             print('\n')
#         except:
#             pass

# print('Mission Completed!')