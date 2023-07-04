
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup 

firefox_options = Options()
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(options=firefox_options) 
driver.get("https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj")

botoes = driver.find_elements("xpath", "//*[@id='btnDownloadUrl']")
print(botoes)
urls = [] 
for index, botao in enumerate(botoes):
    url = botao.is_displayed()
    print(f"URL de número: {index + 1} - {url}")
    urls.append(url) 
    print(url) 

html = driver.page_source 
driver.quit() 
