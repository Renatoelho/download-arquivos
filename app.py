
from utils.baixa_arquivo_em_blocos import baixa_arquivo_em_blocos


url_arquivo = "https://transparencia.infraero.gov.br/wp-content/uploads/2023/06/Relacao-de-Contratos-Vigentes-Junho-de-2023.pdf"


if __name__ == "__main__":
    teste = baixa_arquivo_em_blocos(url_arquivo)
    if teste["status"]:
        print("Arquivo baixado com sucesso!!!")
    else:
        print("Ocorreu algum erro ao baixar o arquivo...")
        print(teste)
   