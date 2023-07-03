
import os
import re
from pathlib import Path
from urllib.parse import urlparse

import requests

from cabecalho_requisicoes import cabecalho


def baixa_arquivos_pagina(url: str, tamanho_bloco: int = 1024*1024) -> dict:
    """
    Tamanho do bloco em bytes.
    Neste exemplo aqui estamos baixando
    por default em blocos de 1MB (1024*1024)
    """
    try:
        resposta = requests.get(url, stream=True, headers=cabecalho())

        nome_arquivo_com_extensao = (
            re.sub(r"\s+", "-", str(os.path.basename(url)).lower())
        )

        local_novo_arquivos = (
            str(Path(os.path.abspath(__file__)).parent.parent)
        )

        dominio_pagina = str(urlparse(url).netloc)

        caminho_completo = (
            f"{local_novo_arquivos}/downloads/"
            f"{dominio_pagina}/"
            f"{nome_arquivo_com_extensao}"
        )

        os.makedirs(Path(caminho_completo).parent, exist_ok=True)

        with open(caminho_completo, "wb") as arquivo:
            for bloco in resposta.iter_content(chunk_size=tamanho_bloco):
                arquivo.write(bloco)

        return {"status": True}

    except Exception as erro:
        return {"status": False, "mensagem": str(erro)}


url_arquivo = "https://www.google.com/robots.txt"


if __name__ == "__main__":
    print(baixa_arquivos_pagina(url_arquivo))
