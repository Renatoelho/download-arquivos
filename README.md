
# Baixando arquivos existentes em páginas WEB

Este projeto irá ajudá-lo a baixar arquivos existentes em páginas da web. Isso é útil quando há vários arquivos em uma única página e você precisa de todos eles. Seguindo os passos abaixo, a implantação é rápida e uma pasta chamada "Download" centraliza todos os arquivos existentes em uma determinada URL, organizando-os por domínio.


# Requisitos

+ ![Python](https://img.shields.io/badge/Python-3.8+-E3E3E3)

+ ![Git](https://img.shields.io/badge/Git-2.25.1+-E3E3E3)

+ ![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-E3E3E3)


# Implatação

### Clonando o repositório do projeto

```bash
git clone https://github.com/Renatoelho/download-arquivos.git download-arquivos
```

### Adicionando PYTHONPATH

Adicione as variáveis de ambiente o ```PYTHONPATH``` ao seu contexto de desenvolvimento. Isso pode ser feito diretamente no terminal onde você irá executar a aplicação ou no arquivo ```.bashrc``` para torná-lo permanente.


```bash
cd download-arquivos/
```

```bash
export PYTHONPATH=$PWD/utils
```

### Criando e configurando ambiente python

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -U pip setuptools wheel
```

```bash
pip install -r requiment.txt
```


### Baixando arquivos

Em app.py altere a variável 'url_pagina' pela URl que você quer baixar os arquivos e no método 'captura_links_arquivos_pagina' passe no parâmetro 'extensoes' passe uma lista das extensões que vc quer baixar.

No arquivo ```app.py```, altere a variável ```url_pagina``` para a URL da página da qual você deseja baixar os arquivos. No método ```captura_links_arquivos_pagina```, passe uma lista das extensões que você deseja baixar como parâmetro ```extensoes```.

+ Executando o código:

```bash
python3 app.py
```

> ***Aviso***: Algumas páginas da web protegem seus links utilizando recursos do JavaScript, portanto, alguns arquivos podem não ser baixados.


# Referências

Beautiful Soup Documentation, ***Beautiful Soup***. Disponível em: <https://beautiful-soup-4.readthedocs.io/en/latest/>. Acesso em: 26 de jun. 2023.

Requests: HTTP for Humans, ***Requests***. Disponível em: <https://requests.readthedocs.io/en/latest/>. Acesso em: 26 de jun. 2023.
