
import os
import re
from pathlib import Path
from datetime import datetime

import requests


def baixa_arquivo_em_blocos(url: str, tamanho_bloco: int = 1024*1024) -> dict: 
    """
    Tamanho do bloco em bytes.
    Neste exemplo aqui estamos baixando
    por default em blocos de 1MB (1024*1024)
    """
    try:
        resposta = requests.get(url, stream=True)
        nome_arquivo_com_extensao = (
            re.sub(r"\s+", "-", str(os.path.basename(url)).lower())
        )
        local_novo_arquivos = (
            str(Path(os.path.abspath(__file__)).parent.parent)
        )
        caminho_completo = (
            f"{local_novo_arquivos}/downloads/"
            f"{datetime.now().strftime('%Y%m%d%H%M%S')}/"
            f"{nome_arquivo_com_extensao}"
        )
        os.makedirs(Path(caminho_completo).parent, exist_ok=True)
        with open(caminho_completo, "wb") as arquivo:
            for bloco in resposta.iter_content(chunk_size=tamanho_bloco):
                arquivo.write(bloco)
        return {"status": True}
    except Exception as erro:
        return {"status": False, "mensagem": erro} 

url_arquivo = "https://www.google.com/robots.txt"


if __name__ == "__main__":
    print(baixa_arquivo_em_blocos(url_arquivo))
