
import os
import requests

def baixa_arquivo_simples(url, nome_arquivo):
    resposta = requests.get(url)
    extensao = os.path.splitext(url)[1]
    nome_arquivo_com_extensao = nome_arquivo + extensao
    with open(nome_arquivo_com_extensao, "wb") as arquivo:
        arquivo.write(resposta.content)
    print("Download concluído!")

#url_arquivo = "https://renato.tec.br/wp-content/uploads/2020/07/Foto-Renato-FULL-Tratadav4.jpg"
#nome_arquivo_local = "Foto-Renato-FULL-Tratadav4"

def baixa_arquivo_em_partes(url, nome_arquivo, tamanho_parte=8192): #Tamanho em bytes (para calcular em KBs, MBs, GBs e etc use o fator 1024)
    resposta = requests.get(url, stream=True)
    extensao = os.path.splitext(url)[1]
    nome_arquivo_com_extensao = nome_arquivo + extensao
    with open(nome_arquivo_com_extensao, "wb") as arquivo:
        for parte in resposta.iter_content(chunk_size=tamanho_parte):
            arquivo.write(parte)
    print("Download concluído!")

url_arquivo = "https://renato.tec.br/wp-content/uploads/2020/07/Foto-Renato-FULL-Tratadav4.jpg"
nome_arquivo_local = "Foto-Renato-FULL-Tratadav4"


if __name__ == "__main__":
    #baixa_arquivo_simples(url_arquivo, nome_arquivo_local)
    baixa_arquivo_em_partes(url_arquivo, nome_arquivo_local)

