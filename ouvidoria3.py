from metodos import *

conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria')

opcao = 10

# Menu
while opcao != 9:
    opcao = menu()


    # Inserir reclamação
    if opcao == 1:
        insereReclamacao(conexao)


    # Listar reclamações
    elif opcao == 2:
        listaReclamacoes(conexao)


    # Pesquisar reclamação pelo código
    elif opcao == 3:
        listaReclamacoes(conexao)
        pesquisaReclamacao(conexao)


    # Opção 4: Remover reclamação pelo código
    elif opcao == 4:
        listaReclamacoes(conexao)
        removeReclamacao(conexao)


    # Inserir elogio ou sugestão
    elif opcao == 5:
        insereElogioSugestao(conexao)


    # Listar elogios ou sugestões
    elif opcao == 6:
        listaElogioSugestao(conexao)


    # Pesquisar elogio ou sugestão pelo código
    elif opcao == 7:
        listaElogioSugestao(conexao)
        pesquisaElogioSugestao(conexao)


    # Remover elogio ou sugestão pelo código
    elif opcao == 8:
        listaElogioSugestao(conexao)
        removeElogioSugestao(conexao)


    elif opcao != 9:
        print('Opção inválida!')

encerrarBancoDados(conexao)

print()
print('Agradecemos por utilizar o nosso portal de Ouvidoria!')
print('Até a próxima!')













