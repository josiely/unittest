#date:2018/1/4
from selenium import webdriver
from selenium.webdriver import Remote

# 启动浏览器驱动
def browser():
    host = '127.0.0.1:4444'
    dc = {'browserName':'firefox'}
    driver = Remote(command_executor='http://'+ host + '/wd/hub',
                  desired_capabilities=dc)
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get('https://www.baidu.com')
    dr.quit()