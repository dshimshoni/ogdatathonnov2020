# import modules
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
try:     
    import pandas
except ImportError:
    print("No module named 'pandas' found")
try:
    from selenium import webdriver
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except ImportError:
    print("No module named 'selenium' found")
try:
    import bs4 as bs
except ImportError:
    print("No module named 'bs4' (beautifulsoup4) found")

#set up path enviroment
path='/Users/keerthanamanivasakan/documents/github/ogdatathonnov2020/chromedriver'
driver = webdriver.Chrome(path)
profile = 'https://www.guidestar.org/profile/11-1633549'
driver.get(profile)

page_info = []

name = driver.find_element_by_class_name('profile-org-name')

each = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'report-section')))
element = driver.find_elements_by_class_name('report-section')

for i in element:
    if i.find_element_by_class_name('report-section-header') == 'Ruling year':
        value = i.find_element_by_class_name('report-section-text')
        year = value.get_attribute('p') 
    elif i.find_element_by_class_name('report-section-header') == 'President' or element.find_element_by_class_class_name('report-section-header') == 'Principle Officer':
        value = i.find_element_by_class_name('report-section-text')
        principle_officer = value.get_attribute('p')
    elif i.find_element_by_class_name('report-section-header') == 'SIC Code':
        value = i.find_element_by_class_name('report-section-text mb-2')
        sector_area = value.get_attribute('p')
    elif i.find_element_by_class_name('report-section-header') == 'Subject area':
        subject_area = i.find_element_by_class_name('report-section-text mb-2')
    elif i.find_element_by_class_name('report-section-header') == 'Population served':
        target_audience = i.find_element_by_class_name('report-section-text mb-2')
    org_type = 'non_profit'

mission = driver.find_element_by_id("mission")
element = driver.find_element_by_class_name('hide-print-url')
website = element.get_attribute('href') # check to see if this get's fucked up

num_employees= driver.find_element_by_id("mission")
services= driver.find_element_by_id("mission")
description= driver.find_element_by_id("mission")
reach= driver.find_element_by_id("mission")
org_size= driver.find_element_by_id("mission")
size_of_audience= driver.find_element_by_id("mission")

element = driver.find_element_by_id('keywords')
values = element.find_element_by_id('keyword')
keywords = values.get_attribute('p')

page_info.append({'name': name, 'year': year, 'principle_officer': principle_officer,
'mission': mission, 'subject_area':subject_area, 'sector_area':sector_area, 'website':website, 
'num_employees':num_employees, 'org_type':org_type, 'services':services, 'keywords': keywords, 
'description':description, 'target_audience':target_audience,
'reach':reach, 'org_size':org_size, 'size_of_audience':size_of_audience})

print(page_info)

