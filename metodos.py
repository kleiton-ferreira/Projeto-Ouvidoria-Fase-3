from operacoesbd import *

def menu():
    print()
    print('UNIVERSIDADE zZz')
    print('PORTAL DE OUVIDORIA')
    print()
    print('OPÇÕES:')
    print('1) Inserir reclamação (até mil caracteres)')
    print('2) Listar as reclamações')
    print('3) Pesquisar reclamação pelo código')
    print('4) Remover uma reclamação pelo código')
    print('5) Inserir elogio ou sugestão (até mil carecteres)')
    print('6) Listar elogios ou sugestões')
    print('7) Pesquisar um elogio ou sugestão pelo código')
    print('8) Remover elogio ou sugestão pelo código')
    print('9) Sair')
    print()
    opcao = input('Digite a sua opção: ')


    try:
        opcao = int(opcao)
    except ValueError:
        pass
    return opcao


# Opção 1: Inserir reclamação
def insereReclamacao(conexao):

    reclamacao = input('Digite a nova reclamação: ')
    print()

    consultaInserirNovaReclamacao = 'insert into reclamacoes(reclamacao) values(%s)'
    dados = (reclamacao,)

    insertNoBancoDados(conexao, consultaInserirNovaReclamacao, dados)

    print('Reclamação inserida com sucesso!')


#Opçao 2: Listar reclamações
def listaReclamacoes(conexao):

    consultaListagem = ('select * from reclamacoes')
    listaReclamacoes = listarBancoDados(conexao, consultaListagem)

    if len(listaReclamacoes) == 0:
        print('Não há reclamações disponíveis')
    else:
        print()
        print('Lista de reclamações')
        print()
        for reclamacao in listaReclamacoes:
            print('Código:', reclamacao[0], '/', 'Reclamação:', reclamacao[1])


#Opção 3: Pesquisar reclamação pelo código
def pesquisaReclamacao(conexao):

    consultaListagem = ('select * from reclamacoes')
    listaReclamacoes = listarBancoDados(conexao, consultaListagem)

    if len(listaReclamacoes) == 0:
        return

    else:
        print()
        print('Pesquisa de reclamação por código')

        try:
            codigo = int(input('Digite o código da reclamação: '))
            print()
            consultaListagem = ('select * from reclamacoes where codigo = ' + str(codigo))
            listaReclamacaoPesquisada = listarBancoDados(conexao, consultaListagem)

            if len(listaReclamacaoPesquisada) == 0:
                print('Código inválido!')

            else:
                print('Resultado da pesquisa')
                for reclamacao in listaReclamacaoPesquisada:
                    print('Código da reclamção pesquisada:', reclamacao[0], '/', 'Reclamação pesquisada:', reclamacao[1])

        except ValueError:
            print()
            print('Código inválido!')


#Opção 4: Remover reclamação pelo código
def removeReclamacao(conexao):

    consultaListagem = ('select * from reclamacoes')
    listaReclamacoes = listarBancoDados(conexao, consultaListagem)

    if len(listaReclamacoes) == 0:
        return

    else:
        print()
        try:
            codigo = int(input('Digite o código da reclamação a ser removida: '))
            print()

            consultaListagem = ('select * from reclamacoes where codigo = ' + str(codigo))
            listaReclamacaoRemovida = listarBancoDados(conexao, consultaListagem)
            consultaRemoverReclamacao = 'delete from reclamacoes where codigo = %s'
            dados = (codigo,)

            if len(listaReclamacaoRemovida) == 0:
                print('Código inválido!')

            else:
                excluirBancoDados(conexao, consultaRemoverReclamacao, dados)
                for reclamacao in listaReclamacaoRemovida:
                    print('Reclamação removida com sucesso!')
                    print('Código da reclamação removida:', reclamacao[0], '/', 'Reclamação removida:', reclamacao[1])

        except ValueError:
            print()
            print('Código inválido!')


#Opção 5: Inserir elogio ou sugestão
def insereElogioSugestao(conexao):

    elogioSugestao = input('Digite o novo elogio ou sugestão: ')
    print()
    consultaInserirNovoElogioSugestao = 'insert into elogios_sugestoes(elogio_sugestao) values(%s)'
    dados = (elogioSugestao,)

    insertNoBancoDados(conexao, consultaInserirNovoElogioSugestao, dados)
    print('Elogio ou sugestão inserido(a) com sucesso!')


#Opção 6: Listar elogios ou sugestões
def listaElogioSugestao(conexao):

    consultaListagem = ('select * from elogios_sugestoes')
    listaElogioSugestao = listarBancoDados(conexao, consultaListagem)

    if len(listaElogioSugestao) == 0:
        print('Não há elogios ou sugestões disponíveis')
    else:
        print()
        print('Lista de elogios ou sugestões')
        print()
        for elogioSugestao in listaElogioSugestao:
            print('Código:', elogioSugestao[0], '/', 'Elogio ou sugestão:', elogioSugestao[1])


#Opção 7: Pesquisar elogio ou sugestão pelo código
def pesquisaElogioSugestao(conexao):

    consultaListagem = ('select * from elogios_sugestoes')
    listaElogioSugestao = listarBancoDados(conexao, consultaListagem)

    if len(listaElogioSugestao) == 0:
        return

    else:
        print()
        try:
            codigo = int(input('Digite o código do elogio ou sugestão: '))
            print()
            consultaListagem = ('select * from elogios_sugestoes where codigo = ' + str(codigo))
            listaElogioSugestaoPesquisada = listarBancoDados(conexao, consultaListagem)

            if len(listaElogioSugestaoPesquisada) == 0:
                print('Código inválido!')
            else:
                print()
                print('Resultado da pesquisa')
                for elogioSugestao in listaElogioSugestaoPesquisada:
                    print('Código do elogio ou sugestão pesquisado(a):', elogioSugestao[0], '/',
                          'Elogio ou Sugestão pesquisado(a):', elogioSugestao[1])

        except ValueError:
            print()
            print('Código inválido!')


#Opção 8: Remover elogio ou sugestão pelo código
def removeElogioSugestao(conexao):

    consultaListagem = ('select * from elogios_sugestoes')
    listaElogioSugestao = listarBancoDados(conexao, consultaListagem)

    if len(listaElogioSugestao) == 0:
        return

    else:
        print()
        try:
            codigo = int(input('Digite o código do elogio ou sugestão a ser removido(a): '))
            print()
            consultaListagem = ('select * from elogios_sugestoes where codigo = ' + str(codigo))
            listaElogioSugestaoRemovido = listarBancoDados(conexao, consultaListagem)

            if len(listaElogioSugestaoRemovido) == 0:
                print('Código inválido!')
            else:
                consultaRemoverElogioSugestao = 'delete from elogios_sugestoes where codigo = %s'
                dados = (codigo,)

                excluirBancoDados(conexao, consultaRemoverElogioSugestao, dados)
                print('Elogio ou sugestão removido(a) com sucesso!')
                for elogioSugestao in listaElogioSugestaoRemovido:
                    print('Código do elogio ou seguestão removido(a):', elogioSugestao[0], '/',
                          'Elogio ou Sugestão removido(a):', elogioSugestao[1])
        except ValueError:
            print()
            print('Código inválido!')

