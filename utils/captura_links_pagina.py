
#pip install requests beautifulsoup4


import requests
from bs4 import BeautifulSoup

# URL da página que você deseja extrair os links
url = "http://www.example.com"

# Faz a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Cria um objeto BeautifulSoup para analisar o conteúdo HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Encontra todos os elementos <a> (links) na página
    links = soup.find_all("a")
    
    # Itera sobre os links encontrados e exibe suas URLs
    for link in links:
        print(link.get("href"))
else:
    print("Falha ao acessar a página:", response.status_code)



import requests
from bs4 import BeautifulSoup

# URL da página que você deseja extrair os links
url = "http://www.example.com"

# Faz a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Cria um objeto BeautifulSoup para analisar o conteúdo HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Encontra todos os elementos <a> (links) na página
    links_a = soup.find_all("a")
    
    # Itera sobre os links encontrados e exibe suas URLs
    for link in links_a:
        print(link.get("href"))
    
    # Encontra todos os elementos <link> na página
    links_link = soup.find_all("link")
    
    # Itera sobre os links encontrados e exibe suas URLs
    for link in links_link:
        print(link.get("href"))
    
    # Encontra todos os elementos <script> na página
    links_script = soup.find_all("script")
    
    # Itera sobre os links encontrados e exibe suas URLs
    for link in links_script:
        print(link.get("src"))
    
    # Encontra todos os elementos <img> na página
    links_img = soup.find_all("img")
    
    # Itera sobre os links encontrados e exibe suas URLs
    for link in links_img:
        print(link.get("src"))
        
    # Adicione outros elementos HTML, se necessário
    
else:
    print("Falha ao acessar a página:", response.status_code)


import requests
from bs4 import BeautifulSoup

# URL da página que você deseja extrair os links
url = "http://www.example.com"

# Faz a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Cria um objeto BeautifulSoup para analisar o conteúdo HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Encontra todos os elementos <a> (links) na página
    links = soup.find_all("a")
    
    # Itera sobre os links encontrados
    for link in links:
        href = link.get("href")
        # Verifica se o link se refere a um arquivo de imagem
        if href.endswith((".jpg", ".jpeg", ".png", ".gif")):
            print(href)
else:
    print("Falha ao acessar a página:", response.status_code)
