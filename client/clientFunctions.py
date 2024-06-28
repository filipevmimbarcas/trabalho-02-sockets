def Create(num) -> str:
    name = input('Nome: ')
    vendor = input('Fabricante: ')
    model = input('Modelo: ')
    option = str(num)
    data = f'{name},{vendor},{model},{option}'
    return data

def Search(num) -> str:
    search_term = input('Termo de pesquisa: ')
    option = str(num)
    data = f'{search_term},{option}'
    return data

def Delete(num) -> str:
    delete_id = input('ID do registro a ser excluído: ')
    option = str(num)
    data = f'{delete_id},{option}'
    return data
