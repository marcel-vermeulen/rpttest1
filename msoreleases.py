## firefox dependency: sudo apt-get install firefox-geckodriver
## pip3 install selenium
## run webdriver as headless

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

url_source = "https://docs.microsoft.com/en-us/windows-server/get-started/windows-server-release-info#windows-server-current-versions-by-servicing-option"
print(url_source)

browser.get(url_source)
div_target = browser.find_element_by_id("windows-server-current-versions-by-servicing-option")
print(str(div_target.text))
#div_lsstage = browser.find_element_by_id("lsstatus")
#print(str(div_lsstage.text))

table_data = []
table_header = []

table = browser.find_element_by_tag_name('table')

head = table.find_element_by_tag_name('thead')
head_line = head.find_element_by_tag_name("tr")
table_header = [header.text for header in head_line.find_elements_by_tag_name('th')]
table_data.append(table_header)

print(table_data)

body = table.find_element_by_tag_name('tbody')
body_rows = body.find_elements_by_tag_name('tr')
for row in body_rows:
    data = row.find_elements_by_tag_name('td')
    table_row = []
    for info in data:
        info_text = info.text #.encode('utf8')
        table_row.append(info_text)
    table_data.append(table_row)

print(table_data)