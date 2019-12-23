from selenium  import webdriver

path = "/Users/janghyeonjun/Downloads/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.naver.com")