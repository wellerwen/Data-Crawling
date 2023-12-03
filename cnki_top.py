# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:08:08 2023

@author: Administrator
"""

import time,random,math
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome() 
time.sleep(3)

def download_paper():
    # 滚动条，加载内容
    js = 'window.scrollTo(0,3000)'
    driver.execute_script(js)
    time.sleep(1)
    js = 'window.scrollTo(0,0)'
    driver.execute_script(js)  
    
    #找到论文
    papers=driver.find_elements(By.XPATH,'//*[@id="gridTable"]/div/div/table/tbody/tr') 
    if len(papers)!=0:
        for i in range(len(papers)):            
            title=papers[i].find_element(By.TAG_NAME,'a').text
            # link=papers[i].find_element(By.TAG_NAME,'a').get_attribute('href')
            source=papers[i].find_element(By.XPATH,'td[4]').text
            sources=['中国社会科学','经济研究','管理世界','世界经济','中国工业经济','经济学(季刊)','金融研究','经济学动态','数量经济技术经济研究','统计研究'] #可以继续添加
            if source in sources:
                papers[i].find_element(By.TAG_NAME,'a').click()
                time.sleep(5)
                
                try:
                    windows=driver.window_handles
                    driver.switch_to.window(windows[1])
                    # driver.title
                    
                    driver.find_element(By.LINK_TEXT,'PDF下载').click()
                    print(source+':\t'+title+'\t'+'downloding')
                    time.sleep(random.randint(5,8))
                    driver.close()
                    driver.switch_to.window(windows[0])
                except:
                    driver.close()
                    driver.switch_to.window(windows[0])         
    else:
        pass
    return None

def get_papers(keyword):
    driver.get('https://www.cnki.net/')
    driver.maximize_window()
        
    driver.find_element(By.XPATH,'//*[@id="txt_SearchText"]').send_keys(keyword)
    driver.find_element(By.CLASS_NAME,'search-btn').click()
    time.sleep(3)    
    # 点击期刊论文
    driver.find_element(By.XPATH,'//*[@id="ModuleSearch"]/div[2]/div/div/ul/li[1]/a/span').click()
    time.sleep(2)     
    # 每页显示50条
    driver.find_element(By.CSS_SELECTOR,'#perPageDiv > div > span').click()  
    button50=driver.find_element(By.XPATH,'//*[@id="perPageDiv"]/ul/li[3]')
    button50.click() 
    
    totalpapers=driver.find_element(By.XPATH,'//*[@id="countPageDiv"]/span[1]/em').text
    clicknum=math.ceil(int(totalpapers)/50)
    if clicknum==1:
        download_paper()
    elif clicknum>1:
        download_paper()
        for i in range(clicknum-1):
            driver.find_element(By.ID,'Page_next_top').click() #跳转到下一页
            time.sleep(2)
            download_paper() 
            if i==9:
                break # 当爬取了10页后，就跳出循环，不再爬取
    else:
        print('存在错误')
    driver.close        
    return None

if __name__=="__main__":
    get_papers('财政激励') #输入你的关键词，比如'财政激励'
    
    #当数据爬取完毕后，网页自动会关闭，在此之前，请勿关闭浏览器。
    
 







