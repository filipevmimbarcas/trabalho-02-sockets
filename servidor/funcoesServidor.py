import os

nome_arquivo = 'arquivo.txt'

def gerar_id():
    if not os.path.exists(nome_arquivo):
        print(f'O arquivo {nome_arquivo} não existe, criando arquivo...\n')
        return 1
    else:
        print(f'O arquivo {nome_arquivo} já existe')
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
        return len(linhas) + 1

def criar(nome, fabricante, modelo):
    with open(nome_arquivo, 'a', encoding='utf8') as arquivo:
        id = gerar_id()
        arquivo.write(f'{id};{nome};{fabricante};{modelo}\n')
        print('Ativo registrado com sucesso')
        linha = {'id': id, 'nome': nome, 'fabricante': fabricante, 'modelo': modelo}
        print(linha)

def listar() -> str:
    if not os.path.exists(nome_arquivo):
        return 'Nenhum dado encontrado.'
    with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
        dados = arquivo.read()
    return dados

def pesquisar(termo: str) -> str:
    if not os.path.exists(nome_arquivo):
        return 'Nenhum dado encontrado.'
    with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
        linhas = arquivo.readlines()
    resultados = [linha for linha in linhas if termo in linha]
    return ''.join(resultados) if resultados else 'Nenhum dado correspondente encontrado.'

def excluir(id_registro: str) -> str:
    if not os.path.exists(nome_arquivo):
        return 'Nenhum dado encontrado.'
    with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
        linhas = arquivo.readlines()
    novas_linhas = [linha for linha in linhas if not linha.startswith(id_registro + ';')]
    if len(novas_linhas) == len(linhas):
        return 'Nenhum registro encontrado com o ID fornecido.'
    with open(nome_arquivo, 'w', encoding='utf8') as arquivo:
        arquivo.writelines(novas_linhas)
    return 'Registro excluído com sucesso.'
