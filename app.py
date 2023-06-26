
from utils.captura_links_pagina import captura_links_arquivos_pagina
from utils.baixa_arquivo_em_blocos import baixa_arquivo_em_blocos


#url_arquivo = "https://transparencia.infraero.gov.br/wp-content/uploads/2023/06/Relacao-de-Contratos-Vigentes-Junho-de-2023.pdf"
url_pagina = "https://transparencia.infraero.gov.br/concessao-de-uso-de-areas/"

if __name__ == "__main__":
    arquivos_pagina = captura_links_arquivos_pagina(url_pagina)
    for url_arquivo in arquivos_pagina["arquivos"]:
        teste = baixa_arquivo_em_blocos(url_arquivo)
        if teste["status"]:
            print("Arquivo baixado com sucesso!!!")
        else:
            print("Ocorreu algum erro ao baixar o arquivo...")
            print(teste)



from urllib.parse import urlsplit

url = "https://www.example.com/path/page.html?query=123"

parsed_url = urlsplit(url)
base_url = parsed_url.scheme + "://" + parsed_url.netloc

print(base_url)


from urllib.parse import urljoin

base_url = "https://www.example.com/path/"
relative_url = "../page.html"

absolute_url = urljoin(base_url, relative_url)
print(absolute_url)


from urllib.parse import urlparse

def is_url_relativa(url):
    parsed_url = urlparse(url)
    return not bool(parsed_url.scheme)

# Exemplos de URLs
url_absoluta = "https://www.example.com/path/page.html"
url_relativa = "/path/page.html"

print(is_url_relativa(url_absoluta))  # False
print(is_url_relativa(url_relativa))  # True
