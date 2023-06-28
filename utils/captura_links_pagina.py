
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from cabecalho_requisicoes import cabecalho


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


def _reestrutura_urls_relativas(url_pagina: str, url_arquivos: list):
    estrutura_url_pagina = urlparse(url_pagina)

    def _atualiza_urls_arquivos(url_arquivos, adiciona_protocolo_dominio):
        return list(map(adiciona_protocolo_dominio, url_arquivos))

    def _adiciona_protocolo_dominio(url_arquivo):
        estrutura_url_arquivo = urlparse(url_arquivo)
        if len(str(estrutura_url_arquivo.netloc)) == 0:
            return (
                str(estrutura_url_pagina.scheme) +
                "://" +
                str(estrutura_url_pagina.netloc) +
                str(estrutura_url_arquivo.path)
            )
        else:
            return url_arquivo

    return _atualiza_urls_arquivos(
        url_arquivos,
        _adiciona_protocolo_dominio
    )


def captura_links_arquivos_pagina(
        url: str,
        extensoes: list = [".csv", ".txt", ".xls", ".xlsx"]
) -> dict:
    """
    Para escolher outras extensões ou reduzir a
    quantidade é necessário enviar uma nova lista
    para o parâmetro 'extensoes'.

    Exemplo de redução de extensões:
        [".csv", ".txt"]

    Exemplo de novas extensões:
        [".waw", ".mp3", ".mp4"]

    """
    try:
        response = requests.get(url, headers=cabecalho())

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

            links_pagina = []

            for tag, elemento in tags_para_pesquisar.items():
                links_temp = soup.find_all(tag)
                for link in links_temp:
                    links_pagina.append(link.get(elemento))

            links_arquivos = (
                _remove_extensoes_indesejadas(
                    list(set(links_pagina)),
                    extensoes
                )
            )

            links_arquivos = (
                _reestrutura_urls_relativas(url, links_arquivos)
            )

            assert len(links_arquivos) > 0, "Não tem arquivo(s) p/ baixar."

        return {"status": True, "arquivos": links_arquivos}

    except Exception as erro:
        return {"status": False, "mensagem": str(erro)}


if __name__ == "__main__":
    url = "https://..../"

    print(captura_links_arquivos_pagina(url))
