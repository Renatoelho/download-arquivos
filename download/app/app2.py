from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Configurando as opções do Firefox para executar em modo headless
firefox_options = Options()
firefox_options.add_argument('-headless')

# Configurando o caminho para o GeckoDriver
webdriver_path = "/usr/local/bin/geckodriver"

# Criando uma instância do driver do Firefox
driver = webdriver.Firefox(executable_path=webdriver_path, options=firefox_options)

# Exemplo de uso: navegando para uma página e obtendo seu título
driver.get('https://www.exemplo.com')
print(driver.title)

# Realize outras ações ou operações de scraping aqui

# Fechando o navegador controlado pelo Selenium
driver.quit()
