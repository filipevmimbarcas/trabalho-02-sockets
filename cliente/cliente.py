import socket
import funcoesCliente as fc

host = '127.0.0.1'
port = 9000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, port))

while True:
    print('\t\tPrograma')
    print('[1] Incluir dados ')
    print('[2] Listar dados ')
    print('[3] Pesquisar dados ')
    print('[4] Excluir dados')
    print('[5] Finalizar')
    opcao = input('Opção >> ')

    if opcao.isdigit():
        opcao = int(opcao)
        if opcao == 1:
            dados = fc.criar(opcao)
            cliente.send(dados.encode())
        elif opcao == 2:
            cliente.send(f'{opcao}'.encode())
            dados = cliente.recv(4096).decode()
            print('Dados cadastrados:')
            print(dados)
        elif opcao == 3:
            termo_pesquisa = fc.pesquisar(opcao)
            cliente.send(termo_pesquisa.encode())
            dados = cliente.recv(4096).decode()
            print('Resultado da pesquisa:')
            print(dados)
        elif opcao == 4:
            id_exclusao = fc.excluir(opcao)
            cliente.send(id_exclusao.encode())
            dados = cliente.recv(4096).decode()
            print(dados)
        elif opcao == 5:
            print('Saindo do programa.')
            cliente.send('end'.encode())
            cliente.close()
            break
        else:
            print('Alternativa não existe.')
    else:
        print('Opção inválida!')
