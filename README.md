
# EM DESENVOLVIMENTO...

# Baixando arquivos existentes em páginas WEB

Este projeto irá ajudá-lo a baixar arquivos existentes em páginas da web. Isso é útil quando há vários arquivos em uma única página e você precisa de todos eles. Seguindo os passos abaixo, a implantação é rápida e uma pasta chamada ```Download``` centraliza todos os arquivos existentes em uma determinada URL, organizando-os por domínio.


# Requisitos

+ ![Docker](https://img.shields.io/badge/Docker-23.0.3-E3E3E3)

+ ![Docker-compose](https://img.shields.io/badge/Docker--compose-1.25.0-E3E3E3)

+ ![Git](https://img.shields.io/badge/Git-2.25.1%2B-E3E3E3)

+ ![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-E3E3E3)


# Implantação

### Clonando o repositório do projeto

```bash
git clone https://github.com/Renatoelho/download-arquivos.git download-arquivos
```

### Build Docker-compose

- UP

```bash
docker-compose -f docker-compose.yaml --compatibility up -d --build
```

- DOWN

```bash
docker-compose -f docker-compose.yaml --compatibility down
```


# Referências

Beautiful Soup Documentation, ***Beautiful Soup***. Disponível em: [\<https://beautiful-soup-4.readthedocs.io/en/latest/\>](https://beautiful-soup-4.readthedocs.io/en/latest/). Acesso em: 26 de jun. 2023.

Requests: HTTP for Humans, ***Requests***. Disponível em: [\<https://requests.readthedocs.io/en/latest/\>](https://requests.readthedocs.io/en/latest/). Acesso em: 26 de jun. 2023.

The Selenium Browser Automation Project, ***Selenium***. Disponível em: [\<https://www.selenium.dev/documentation/\>](https://www.selenium.dev/documentation/). Acesso em: 04 de jul. 2023.
