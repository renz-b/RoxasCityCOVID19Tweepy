from selenium import webdriver
import time
import os
PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=PATH, options=options) 

# automates the search parameters that I need 
# find a way to extract data maybe an api
def automation_script():
    driver.get("https://public.tableau.com/views/COVID-19CasesandDeathsinthePhilippines_15866705872710/Home?:language=en&:display_count=y&:origin=viz_share_link")
    time.sleep(10)
    # Province dropbox
    link = driver.find_element_by_xpath("""//*[@id="tableau_base_widget_LegacyCategoricalQuickFilter_0"]/div/div[3]/span/div[1]""")
    link.click()
    time.sleep(1)
    # Clicks All checkbox
    link = driver.find_element_by_xpath("""//*[@id="FI_federated.1a7aw9i1th8dp91bs6jbh1f985fz,none:Calculation_2996441926413623304:nk9923946406123244083_7517927501805016533_(All)"]/div[2]/input""")
    link.click()
    time.sleep(1)
    # Clicks Capiz checkbox
    link = driver.find_element_by_xpath("""//*[@id="FI_federated.1a7aw9i1th8dp91bs6jbh1f985fz,none:Calculation_2996441926413623304:nk9923946406123244083_7517927501805016533_26"]/div[2]/input""")
    link.click()
    time.sleep(1)
    # Clicks Apply button
    link = driver.find_element_by_xpath("""//*[@id="tableau_base_widget_LegacyCategoricalQuickFilter_0_menu"]/div[3]/button[2]/span[2]""")
    link.click()
    time.sleep(10)
    # Click outside to collapse dropbox
    link = driver.find_element_by_xpath("""/html/body/div[5]""")
    link.click()
    # Facilities dropbox
    link = driver.find_element_by_xpath("""//*[@id="tableau_base_widget_LegacyCategoricalQuickFilter_1"]/div/div[3]/span/div[1]""")
    link.click()
    time.sleep(1)
    # Clicks all checkbox
    link = driver.find_element_by_xpath("""//*[@id="FI_federated.1n6cst61r3e2md12o72n00fhtgw8 (copy),none:city_mun:nk9923946406123244083_5809079969173967208_(All)"]/div[2]/input""")
    link.click()
    time.sleep(1)
    # Clicks Roxas City checkbox
    link = driver.find_element_by_xpath("""//*[@id="FI_federated.1n6cst61r3e2md12o72n00fhtgw8 (copy),none:city_mun:nk9923946406123244083_5809079969173967208_399"]/div[2]/input""")
    link.click()
    time.sleep(1)
    # Clicks Apply button
    link = driver.find_element_by_xpath("""//*[@id="tableau_base_widget_LegacyCategoricalQuickFilter_1_menu"]/div[2]/button[2]/span[2]""")
    link.click()
    time.sleep(10)
    # Click outside to collapse dropbox
    link = driver.find_element_by_xpath("""/html/body/div[5]""")
    link.click()
     # Clicks Laboratory dropbox
    link = driver.find_element_by_xpath("""//*[@id="tableau_base_widget_LegacyCategoricalQuickFilter_4"]/div/div[3]/span/div[1]""")
    link.click()
    time.sleep(1)
    # Clicks All checkbox
    link = driver.find_element_by_xpath("""//*[@id="FI_federated.0jj2drt07e2rvp0zope591re6hui,none:facility_name:nk9923946406123244083_8775405739952795266_(All)"]/div[2]/input""")
    link.click()
    time.sleep(1)
    # Clicks Roxas Lab checkbox
    link = driver.find_element_by_xpath("""//*[@id="FI_federated.0jj2drt07e2rvp0zope591re6hui,none:facility_name:nk9923946406123244083_8775405739952795266_130"]/div[2]/input""")
    link.click()
    time.sleep(10)
    # Clicks Apply button
    link = driver.find_element_by_xpath("""//*[@id="tableau_base_widget_LegacyCategoricalQuickFilter_4_menu"]/div[3]/button[2]/span[2]""")
    link.click()
    time.sleep(10)
    # Click outside to collapse dropbox
    link = driver.find_element_by_xpath("""/html/body""")
    link.click()

#screenshots the needed data and moves to file/date dir
def scrnshot(): 
    driver.find_element_by_xpath(
            """//*[@id="view9923946406123244083_10433653274507920528"]/div[1]/div[2]/canvas[2]""").screenshot(
                'date_cases_capiz.png')
    driver.find_element_by_xpath(
            """//*[@id="view9923946406123244083_12793915411520878484"]/div[1]/div[2]/canvas[2]""").screenshot(
                'total_cases.png')
    driver.find_element_by_xpath(
            """//*[@id="view9923946406123244083_14235547432543860772"]/div[1]/div[2]/canvas[2]""").screenshot(
                'active_cases.png')
    driver.find_element_by_xpath(
            """//*[@id="view9923946406123244083_7419800422794211819"]/div[1]/div[2]/canvas[2]""").screenshot(
                'recovered.png')
    driver.find_element_by_xpath(
            """//*[@id="view9923946406123244083_1174943117186403758"]/div[1]/div[2]/canvas[2]""").screenshot(
                'died.png')
    driver.find_element_by_xpath(
            """//*[@id="view9923946406123244083_8775405739952795266"]/div[1]/div[2]/canvas[2]""").screenshot(
                'date_roxas_lab.png')           
    driver.find_element_by_xpath(
            """//*[@id="view9923946406123244083_11293018607611585061"]/div[1]/div[2]/canvas[2]""").screenshot(
                'samples_tested.png')
    driver.find_element_by_xpath(
            """//*[@id="view9923946406123244083_6625130945190664444"]/div[1]/div[2]/canvas[2]""").screenshot(
                'individuals_tested.png')
    driver.find_element_by_xpath(
            """//*[@id="view9923946406123244083_9211313482570117425"]/div[1]/div[2]/canvas[2]""").screenshot(
                'bed_occupancy.png')
    driver.find_element_by_xpath(
            """//*[@id="view9923946406123244083_13934144258911594285"]/div[1]/div[2]/canvas[2]""").screenshot(
                'date_facilities.png')
    driver.close()

def main():
    pass

if __name__ == '__main__':
    main()
