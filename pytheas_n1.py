import os
import Function

comando = int(0)

while comando!=5:
    os.system("clear")
    print("#############################################################################")
    print("#                                                                           #")
    print("#                        LEITOR DE ARQUIVOS NCBI SRA                        #")
    print("#                                                                           #")
    print("#############################################################################")
    print("#                                                                           #")
    print("#                          [1] Pesquisa Geral                               #")
    print("#                          [2] Pesquisa Detalhada                           #")
    print("#                          [3] Lista de Metadados                           #")
    print("#                          [4] Download de arquivos                         #")
    print("#                          [5] Sair                                         #")
    print("#                                                                           #")
    print("#############################################################################")

    comando = int(input("Digite o número referente a sua escolha\n> "))


    if comando==1:
        Function.pesquisar()
        comando = Function.decisao()


    elif comando == 2:
        Function.detalhes_pesquisar()
        comando = Function.decisao()


    elif comando == 3:
        Function.metadados()
        comando = Function.decisao()


    elif comando == 4:
        Function.download()
        comando = Function.decisao()


    elif comando == 5:
        print("#############################################################################")
        print("Encerrado!")
