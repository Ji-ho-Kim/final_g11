from urllib.error import HTTPError
from selenium import webdriver
from openpyxl import Workbook, load_workbook
import datetime

now = datetime.datetime.now()
date = now.strftime('%Y.%m.%d')

seoul_file_path = 'C:/Users/atom2/'
seoul_file_name = 'seoul.txt'

chrome_driver_path = 'C:/Users/atom2/chromedriver.exe'

excel_file_path = 'C:/Users/atom2/'
excel_file_name = excel_file_path + date + '.xlsx'
excel_sheet_title = 'confirm'
excel_row = 2

def make_excel():
    work_book = Workbook()
    sheet1 = work_book.active
    sheet1.title = excel_sheet_title

    sheet1.cell(row=1, column=1).value = '위치 구'
    sheet1.cell(row=1, column=2).value = '식당이름'
    sheet1.cell(row=1, column=3).value = '평점'
    
    work_book.save(filename = excel_file_name)
    work_book.close()


def make_request():
    seoul_file = open(seoul_file_path+seoul_file_name, 'r', encoding='UTF-8')
    for seoul_code in seoul_file.readlines():
        
        url = 'https://www.mangoplate.com/search/' + seoul_code
        driver = webdriver.Chrome(chrome_driver_path)
        driver.get(url)
        crawling(driver, seoul_code)

            
        

    seoul_file.close()

def crawling(driver,seoul_code):
    titles = driver.find_elements_by_css_selector('body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li:nth-child(2) > div:nth-child(2) > figure > figcaption > div > a > h2')
    
    points = driver.find_elements_by_class_name("point search_point ")
    for i in range(0,10):
        crawling_results = []
        crawling_results.append(seoul_code)
        crawling_results.append(titles[i+1].text)
        #crawling_results.append(points[0].text)

        global excel_row
        insert_data_to_excel(crawling_results)
        excel_row += 1

    driver.close()
    insert_data_to_excel(crawling_results)

def insert_data_to_excel(crawling_results):
    excel_file = load_workbook(excel_file_name)
    sheet1 = excel_file[excel_sheet_title]

    excel_column = 1;
    for data in crawling_results:
        sheet1.cell(row=excel_row, column=excel_column).value = data
        excel_column+=1

    excel_file.save(excel_file_name)
    excel_file.close()
    
make_excel()
make_request()

