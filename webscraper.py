# import modules
import csv
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
try:     
    import pandas as pd
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

#
all_orgs = []

# for loop for i in list from df
# set profile = i
data_provided = pd.read_csv('sample.csv')
website = data_provided['guidestar_url'].values

for i in website:
    profile = i
    driver.get(str(profile))
    try:
        name = driver.find_element_by_class_name('profile-org-name')
        year = driver.find_element_by_xpath('/html/body/div[3]/div[10]/div/div[2]/section[1]/p[2]')
        principle_officer = driver.find_element_by_xpath('/html/body/div[3]/div[10]/div/div[2]/section[2]/p[2]')

        sector_area = driver.find_element_by_xpath("/html/body/div[3]/div[10]/div/div[3]/section[4]/p[2]/span[2]")
        subject_area = driver.find_element_by_xpath("/html/body/div[@id='mainPageContent']/div[@class='extended-banner bb-gold'][2]/div[@id='summary']/div[@class='col-lg-2'][2]/section[@class='report-section'][2]")

        target_audience = driver.find_element_by_xpath("/html/body/div[@id='mainPageContent']/div[@class='extended-banner bb-gold'][2]/div[@id='summary']/div[@class='col-lg-2'][2]/section[@class='report-section'][3]")
        org_type = 'non_profit'

        mission = driver.find_element_by_xpath("/html/body/div[@id='mainPageContent']/div[@class='extended-banner bb-gold'][2]/div[@id='summary']/div[@class='col-lg-6']/section[@class='report-section border-top-0 border-bottom-0 pt-0']/p[@id='mission-statement']")

        website = driver.find_element_by_xpath("/html/body/div[3]/div[7]/div[2]/div/span[3]/a")


        services= driver.find_element_by_xpath("/html/body/div[@id='mainPageContent']/div[@id='mission']/div[@class='row']/section[@id='programsAndAreasServed']/div[@class='profile-row']/div[@class='profile-col-6'][1]")
        keywords = driver.find_element_by_xpath("/html/body/div[@id='mainPageContent']/div[@id='mission']/div[@class='row']/section[@id='programsAndAreasServed']/div[@class='profile-row']/div[@class='profile-col-6'][1]")

        page_info = {'name': name.text, 'year': year.text, 'principle_officer': principle_officer.tex,
        'mission': mission.tex, 'subject_area':subject_area.text, 'sector_area':sector_area.text, 'website':website.text, 'org_type':org_type, 'services':services.text, 'keywords': keywords.text, 'target_audience':target_audience.text}
    except:
        print("Error in webpage", i , "continuing...")
df = pd.DataFrame(all_orgs)
compression_opts = dict(method='zip', archive_name='database.csv')  

df.to_csv('database.zip', index=False, compression=compression_opts)
