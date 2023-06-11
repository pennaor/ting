# TING (Trybe is not Google)

Aplicação que simula um algoritmo de indexação de documentos similar ao do Google capaz de identificar ocorrências de termos em arquivos TXT.
Foi desenvolvida como projeto de aprendizado no curso de desenvolvimento web da [Trybe](www.betrybe.com).

<details>
<summary><strong>Ferramentas utilizadas</strong></summary>

- [Python](https://www.python.org)
- [Pytest](https://docs.pytest.org/en/7.3.x)

</details>

<details>
<summary><strong>Habilidades trabalhadas</strong></summary>

- Manipular Pilhas;

- Manipular Deque;

- Manipular Nó e Listas Ligadas;

- Manipular Listas Duplamente Ligadas.

</details>

<details>
<summary><strong>Módulos</strong></summary>

A aplicação conta com dois <strong>módulos</strong> e seus respectivos `componentes`:

- <strong>ting_file_management</strong>: gerencia e anexa arquivos de texto (formato TXT):
  - `Queue`: estrutura de dados FIFO(First In First Out) utilizada para armazenar e manipular os arquivos que serão lidos.
  - `txt_importer`: função que importa notícias a partir de um caminho para um arquivo TXT. Retorna uma lista contendo as linhas do arquivo ou None em caso de erro.
  - `process`: função que transforma o conteúdo da lista gerada pela função txt_importer em um dicionário que será armazenado dentro da `Queue`.
    - `is_file_unique`: função que assegura que arquivos com o mesmo nome e caminho não devem ser readicionados a `Queue`.
    - `remove`: função que remove o primeiro arquivo processado da `Queue`.
    - `file_metadata`: função que imprime as informações superficiais de um arquivo processado.
  - `PriorityQueue`: Utiliza `Queue` para armazenar arquivos pequenos com prioridade. Arquivos com menos de 5 linhas são armazenados de forma prioritária na fila. Classe implementada pela [Trybe](www.betrybe.com).

- <strong>ting_word_searches</strong>: operador de funções de busca sobre os arquivos anexados:
  - `exists_word`: Busca numeração das linhas em que a palavra ocorre nos arquivos processados
  - `search_by_word`: Busca numeração && conteúdo das linhas em que a palavra ocorre nos arquivos processados

</details>

<details>
<summary><strong>Instalação</strong></summary>

1. Clone o repositório e entre na pasta do repositório que você acabou de clonar

```bash
git clone git@github.com:pennaor/ting.git
cd ./ting
```

2. Crie o ambiente virtual para o projeto

```bash
python3 -m venv .venv && source .venv/bin/activate
```

3. Instale as dependências

```bash
python3 -m pip install -r dev-requirements.txt
```

</details>

<details>
<summary><strong>Utilização</strong></summary>

  1. Abra um terminal Python importando as funções do arquivo main.py

```bash
python3 -i main.py
```

  2. Execute as funções `exists_word` ou `search_by_word`.
  - Ambas esperam receber uma palavra como primeiro argumento, seguido pelos caminhos dos arquivos a serem analisados
  - Arquivos de texto prontos podem ser encontrados no diretório `./statics/`

```bash
  exists_word("acima", "statics/arquivo_teste.txt", "statics/nome_pedro.txt")

#   SAÍDA:

#   1. INFORMAÇÕES DO ARQUIVO PROCESSADO:
#     {'nome_do_arquivo': 'statics/arquivo_teste.txt', 'qtd_linhas': 3, 'linhas_do_arquivo': ['Acima de tudo,', 'é fundamental ressaltar que a adoção de políticas
#       descentralizadoras nos obriga', 'à análise do levantamento das variáveis envolvidas.']}
#     -- RESULTADO DA BUSCA:
#     {'palavra': 'acima', 'arquivo': 'statics/arquivo_teste.txt', 'ocorrencias': [{'linha': 1}]}

#   2. INFORMAÇÕES DO ARQUIVO PROCESSADO:
#     {'nome_do_arquivo': 'statics/nome_pedro.txt', 'qtd_linhas': 3, 'linhas_do_arquivo': ['Aqui contem um texto que fala sobre um menino pobre chamado Pedro.',
#      'Ele era um menino feliz e cativante.', 'Pedro tinha uma amiga chamada Carol.']}
#     -- RESULTADO DA BUSCA:
#     {'palavra': 'acima', 'arquivo': 'statics/nome_pedro.txt', 'ocorrencias': 'Sem ocorrência'}

```

```bash
  search_by_word("acima", "statics/nome_pedro.txt", "statics/arquivo_teste.txt")

#   1. INFORMAÇÕES DO ARQUIVO PROCESSADO:
#   {'nome_do_arquivo': 'statics/nome_pedro.txt', 'qtd_linhas': 3, 'linhas_do_arquivo': ['Aqui contem um texto que fala sobre um menino pobre chamado Pedro.',
#     'Ele era um menino feliz e cativante.', 'Pedro tinha uma amiga chamada Carol.']}
#   -- RESULTADO DA BUSCA:
#   {'palavra': 'acima', 'arquivo': 'statics/nome_pedro.txt', 'ocorrencias': 'Sem ocorrência'}

#   2. INFORMAÇÕES DO ARQUIVO PROCESSADO:
#   {'nome_do_arquivo': 'statics/arquivo_teste.txt', 'qtd_linhas': 3, 'linhas_do_arquivo': ['Acima de tudo,', 'é fundamental ressaltar que a adoção de políticas
#    descentralizadoras nos obriga', 'à análise do levantamento das variáveis envolvidas.']}
#   -- RESULTADO DA BUSCA:
#   {'palavra': 'acima', 'arquivo': 'statics/arquivo_teste.txt', 'ocorrencias': [{'conteudo': 'Acima de tudo,', 'linha': 1}]}

```

</details>

<details>
<summary><strong>Teste da classe PriorityQueue</strong></summary>

`PriorityQueue` utiliza `Queue` do pacote <strong>ting_file_management</strong> para armazenar arquivos pequenos com prioridade. Arquivos com menos de 5 linhas são armazenados de forma prioritária na fila. Classe implementada pela [Trybe](www.betrybe.com).

O teste verifica se:
  - Quando um arquivo prioritário (_com menos de 5 linhas_) é adicionado à fila de prioridades, este arquivo ficará "após" todos os arquivos prioritários já inseridos, mas ficará "antes" de todos os arquivos não-prioritários já inseridos.
  - Quando um arquivo não-prioritário (_com 5 linhas ou mais_) é adicionado à fila de prioridades, este arquivo ficará "após" todos os arquivos já inseridos.

Exemplo:
```bash
# Tamanhos dos arquivos, em ordem de inserção na fila: 
[9, 4, 2, 5, 7, 11, 3]

# Tamanhos dos arquivos, em ordem de remoção da fila:
[4, 2, 3, 9, 5, 7, 11]
```

Para executar o teste, digite em um terminal:
```bash
python3 -m pytest
```
⚠️ O ambiente virtual deve estar ativado!

</details>