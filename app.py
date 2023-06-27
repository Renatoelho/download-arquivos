
from utils.captura_links_pagina import captura_links_arquivos_pagina
from utils.baixa_arquivos_pagina import baixa_arquivos_pagina


url_pagina = "https://transparencia.infraero.gov.br/concessao-de-uso-de-areas/"
url_pagina = "https://findthisip.com/"

if __name__ == "__main__":
    arquivos_pagina = captura_links_arquivos_pagina(url_pagina)
    if arquivos_pagina["status"]:
        for url_arquivo in arquivos_pagina["arquivos"]:
            download = baixa_arquivos_pagina(url_arquivo)
            if download["status"]:
                print("Arquivo baixado com sucesso!!!")
            else:
                print("Ocorreu algum erro ao baixar o arquivo...")
                print(download)
    else:
        print(arquivos_pagina)
