from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import requests


from selenium.webdriver.support.ui import WebDriverWait

ready = False
time.sleep(5)
while not ready:
    try:
        r = requests.get('http://172.17.0.1:4444/wd/hub/status', timeout=1)
        status = r.status_code
        if status == 200:
            ready = True
    except ConnectionResetError or ConnectionError:
        continue

driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, command_executor="http://172.17.0.1:4444/wd/hub")

driver.maximize_window()

# ADMIN CREATE
driver.get("http://172.17.0.1:9000")

driver.find_element_by_id("adminlogin").send_keys("admin")
driver.find_element_by_id("adminpass").send_keys("password")
# Uncheck install recommended apps textbox
driver.find_element_by_xpath("/html/body/div/div/main/form/fieldset[7]/p/label").click()
driver.find_element_by_class_name("primary").click()

# ENABLE LDAP
WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.action-item")))

driver.get("http://172.17.0.1:9000/settings/apps")
WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.action-item")))
driver.find_element_by_css_selector("button.action-item").click()
WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/main/div/div[1]/div/div[35]/div[5]/input")))
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[3]/main/div/div[1]/div/div[35]/div[5]/input").click()
time.sleep(3)

# CONFIGURE LDAP
driver.get("http://172.17.0.1:9000/settings/admin/ldap")
time.sleep(5)

# SERVER TAB
driver.find_element_by_id("ldap_host").send_keys("172.17.0.1")
driver.find_element_by_id("ldap_port").send_keys("389")
driver.find_element_by_id("ldap_dn").send_keys("uid=admin,cn=users,cn=accounts,dc=example,dc=test")
driver.find_element_by_id("ldap_agent_password").send_keys("Secret123")
driver.find_element_by_id("ldap_base").send_keys("dc=example,dc=test")
WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.ID, "ui-id-8")))
time.sleep(3)

# USERS TAB
driver.find_element_by_class_name("ldapWizardControls").click()
time.sleep(1)
driver.find_element_by_id("ui-id-8").click()
driver.find_element_by_id("toggleRawUserFilter").click()
driver.find_element_by_id("ldap_userlist_filter").send_keys("(|(objectclass=*))")
WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.ID, "ui-id-9")))
time.sleep(3)

# LOGIN ATTRIBUTES TAB
driver.find_element_by_id("ui-id-9").click()
driver.find_element_by_id("ui-id-9").click()
driver.find_element_by_id("toggleRawLoginFilter").click()
driver.find_element_by_id("ldap_login_filter").clear()
driver.find_element_by_id("ldap_login_filter").send_keys("(&(|(objectclass=*))(uid=%uid))")
WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.ID, "ui-id-10")))
time.sleep(3)

# GROUPS TAB
driver.find_element_by_id("ui-id-10").click()
driver.find_element_by_id("ui-id-10").click()
time.sleep(3)
driver.find_element_by_id("toggleRawGroupFilter").click()
driver.find_element_by_id("ldap_group_filter").clear()
driver.find_element_by_id("ldap_group_filter").send_keys("(|(cn=ipausers))")
WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.ID, "ui-id-12")))
time.sleep(10)

# ADVANCED TAB
# CONNECTION SETTINGS
driver.find_element_by_id("ui-id-12").click()
driver.find_element_by_id("ui-id-12").click()
time.sleep(3)
driver.find_element_by_id("ldap_configuration_active").click()
WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.ID, "ui-id-3")))
time.sleep(3)

# DIRECTORY SETTINGS
driver.find_element_by_id("ui-id-3").click()
driver.find_element_by_id("ldap_base_users").send_keys("cn=users,cn=accounts,dc=example,dc=test")
driver.find_element_by_id("ldap_base_groups").send_keys("cn=groups,cn=accounts,dc=example,dc=test")
Select(driver.find_element_by_id("ldap_group_member_assoc_attribute")).select_by_visible_text("uniqueMember")
WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.ID, "ui-id-5")))
time.sleep(3)

# SPECIAL ATTRIBUTES
driver.find_element_by_id("ui-id-5").click()
driver.find_element_by_id("ldap_email_attr").send_keys("mail")
driver.find_element_by_id("home_folder_naming_rule").send_keys("cn")
time.sleep(10)

# LOGOUT
driver.find_element_by_id("expand").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/header/div[2]/div[4]/nav/ul/li[7]/a").click()

driver.close()















