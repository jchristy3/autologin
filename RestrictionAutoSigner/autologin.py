import time
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
import re
import sys

# program to automate restriction signing so that I can sign in like 5 seconds

driver = webdriver.Chrome('chromedriver.exe')  # Optional argument,
driver.get('https://cacprdapp.citadel.edu')
user_box = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lgnvwDefault_UserName')
user_box.send_keys(sys.argv[1])
time.sleep(1)
pass_box = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lgnvwDefault_Password')
pass_box.send_keys(sys.argv[2])
time.sleep(1)
log_box = driver.find_element_by_id('ctl00_ContentPlaceHolder1_lgnvwDefault_btnLogin')
log_box.click()
time.sleep(5)
# discipline = driver.find_element_by_xpath('//*[@id="ctl00_navigationControl_lgnvwDefault_Menu1"]/ul/li[2]')
# hover = ActionChains(driver).move_to_element(discipline)
# hover.perform()
print(driver.current_url)
url = driver.current_url
rand = re.match('^https://cacprdapp.citadel.edu/\(S\([\w]*\)\)', url)
url = rand.group(0)
print(url)
url = url + '/SignInOut.aspx?id=siores'
driver.get(url)
sign = driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctl00$btnSI_Submit')
sign.click()
time.sleep(5)    # Let the user actually see something!
driver.close()

#<input type="submit" name="ctl00$ContentPlaceHolder1$ctl00$btnSI_Submit" value="Submit" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ContentPlaceHolder1$ctl00$btnSI_Submit&quot;, &quot;&quot;, true, &quot;SignInCadet&quot;, &quot;&quot;, false, false))" id="ctl00_ContentPlaceHolder1_ctl00_btnSI_Submit"
#style="color: #FFF; background: #0064a7; padding: 5px 20px; border: 1px solid #0064a7; border-radius: 4px; text-decoration: none;">
