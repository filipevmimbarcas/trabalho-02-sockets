def criar(num) -> str:
    nome = input('Nome: ')
    fabricante = input('Fabricante: ')
    modelo = input('Modelo: ')
    opcao = str(num)
    dados = f'{nome},{fabricante},{modelo},{opcao}'
    return dados

def pesquisar(num) -> str:
    termo_pesquisa = input('Termo de pesquisa: ')
    opcao = str(num)
    dados = f'{termo_pesquisa},{opcao}'
    return dados

def excluir(num) -> str:
    id_exclusao = input('ID do registro a ser excluído: ')
    opcao = str(num)
    dados = f'{id_exclusao},{opcao}'
    return dados