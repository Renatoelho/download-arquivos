
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def _remove_extensoes_indesejadas(
        lista_arquivos: list,
        extensoes: list
    ) -> list:
    return list(
        filter(
            lambda item:
            any(str(item)
                .endswith(extensao)
                for extensao
                in extensoes
            ),
            lista_arquivos
        )
    )


def _reestrutura_url_arquivos(url_pagina: str, url_arquivos: list):
    estrutura_url_pagina = urlparse(url_pagina)

    def _atualiza_url_arquivo(url_arquivos, valida_url_arquivo):
        return list(map(valida_url_arquivo, url_arquivos))
    
    def _valida_url_arquivo(url_arquivo):
        estrutura_url_arquivo = urlparse(url_arquivo)
        if len(str(estrutura_url_arquivo.netloc)) == 0:
            return str(estrutura_url_pagina.scheme) + "://" + str(estrutura_url_pagina.netloc) + str(estrutura_url_arquivo.path)
        else:
            return url_arquivo

    return _atualiza_url_arquivo(url_arquivos, _valida_url_arquivo)

   
def captura_links_arquivos_pagina(
        url: str,
        tipo_arquivo:list=[".csv", ".txt", ".xls", ".xlsx", ".pdf"]
    ) -> dict:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            tags_para_pesquisar = (
                {
                    "a": "href",
                    "link": "href",
                    "script": "src",
                    "img": "src"
                }
            )
            links_encontrados = []
            for tag, elemento in tags_para_pesquisar.items():
                links_temp = soup.find_all(tag)
                for link in links_temp:
                    links_encontrados.append(link.get(elemento))
            links_encontrados = _remove_extensoes_indesejadas(list(set(links_encontrados)), tipo_arquivo)
            links_encontrados = _reestrutura_url_arquivos(url, links_encontrados)
            assert len(links_encontrados) > 0, "Não tem arquivos p/ download."
        return {"status": True, "arquivos": links_encontrados}
    except Exception as erro:
        return {"status": False, "mensagem": str(erro)}


if __name__ == "__main__":
    url = "https://findthisip.com/"
    url = "https://transparencia.infraero.gov.br/concessao-de-uso-de-areas/"
    print(captura_links_arquivos_pagina(url))
