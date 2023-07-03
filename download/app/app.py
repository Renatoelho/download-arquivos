
from utils.captura_links_pagina import captura_links_arquivos_pagina
from utils.baixa_arquivos_pagina import baixa_arquivos_pagina


url_pagina = "https://www.gov.br/ans/pt-br/acesso-a-informacao/perfil-do-setor/dados-abertos-1/dados-abertos"

if __name__ == "__main__":
    arquivos_pagina = (
        captura_links_arquivos_pagina(url_pagina, extensoes=[".pdf"])
    )

    if arquivos_pagina["status"]:
        for index, url_arquivo in enumerate(arquivos_pagina["arquivos"]):
            download = baixa_arquivos_pagina(url_arquivo)

            if download["status"]:
                print(f"{index + 1}º Arquivo baixado com sucesso!!!")
            else:
                print(f"{index + 1}º Arquivo não foi baixado...")
                print(download)
    else:
        print(arquivos_pagina)
