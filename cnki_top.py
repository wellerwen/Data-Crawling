# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:08:08 2023

@author: Administrator
"""
import time,re,random
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome() # driver一个假人
time.sleep(3)

def get_cnki(keyword):  
    driver.get('https://www.cnki.net/')
    
    # 窗口最大化
    driver.maximize_window()
    # driver.minimize_window()
    
    # 滚动条
    js = 'window.scrollTo(0,1500)'
    driver.execute_script(js)
    js = 'window.scrollTo(0,0)'
    driver.execute_script(js)
    
    driver.find_element(By.XPATH,'//*[@id="txt_SearchText"]').send_keys(keyword)
    driver.find_element(By.CLASS_NAME,'search-btn').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,'#perPageDiv > div > span').click() # 每页显示多少条
    driver.find_element(By.XPATH,'//*[@id="perPageDiv"]/ul/li[3]').click() # 每页显示50条
    
    # 点击期刊论文
    driver.find_element(By.XPATH,'//*[@id="ModuleSearch"]/div[2]/div/div/ul/li[1]/a/span').click()
    time.sleep(2)
    #找到论文
    papers=driver.find_elements(By.XPATH,'//*[@id="gridTable"]/div/div/table/tbody/tr') 
    len(papers)
    
    if len(papers)!=0:
        for i in range(len(papers)):            
            title=papers[i].find_element(By.TAG_NAME,'a').text
            print(f'第{i}篇:\t')
            # link=papers[i].find_element(By.TAG_NAME,'a').get_attribute('href')
            source=papers[i].find_element(By.XPATH,'td[4]').text
            print(source)
            sources=['经济研究','管理世界','世界经济','中国工业经济','经济学(季刊)','财政研究']
            if source in sources:
                papers[i].find_element(By.TAG_NAME,'a').click()
                time.sleep(5)
                
                try:
                    windows=driver.window_handles
                    driver.switch_to.window(windows[1])
                    # driver.title
                    
                    driver.find_element(By.LINK_TEXT,'PDF下载').click()
                    print(f'第{i}篇:\t'+title+'\t'+'top')
                    time.sleep(random.randint(5,8))
                    driver.close()
                    driver.switch_to.window(windows[0])
                except:
                    driver.close()
                    driver.switch_to.window(windows[0])         
    else:
        pass
    return None

if __name__=="__main__":
    get_cnki('财政激励')
    
 







