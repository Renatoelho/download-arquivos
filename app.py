
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
