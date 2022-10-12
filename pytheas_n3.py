#! /usr/bin/python3
import os
import Function

comando = int(0)

while comando!=5:

    print("_____________________________________________________________________________")
    print("|                                                                           |")
    print("|                          LEITOR DE ARQUIVOS SRA                           |")
    print("|___________________________________________________________________________|")
    print("|                                                                           |")
    print("|                          [1] Pesquisa Geral                               |")
    print("|                          [2] Pesquisa Detalhada                           |")
    print("|                          [3] Lista de Metadados                           |")
    print("|                          [4] Download de arquivos                         |")
    print("|                          [5] Sair                                         |")
    print("|___________________________________________________________________________|")

    comando = int(input("Digite o número referente a sua escolha\n> "))

    #Caso digito for para pesquisa geral
    if comando==1:
        print("_____________________________________________________________________________")
        print("|                                                                           |")
        print("|                      TERMINAL DE PESQUISAS GERAIS                         |")
        print("|___________________________________________________________________________|")
        print("|                                                                           |")
        print("|                       [1] Pesquisa Geral No NCBI                          |")
        print("|                       [2] Pesquisa Geral No ENA                           |")
        print("|                       [3] Sair da Aba atual                               |")
        print("|___________________________________________________________________________|")
        comando = int(input("Digite o número referente a sua escolha\n> "))

        #Pesquisa no NCBI
        if comando==1:
            Function.SRApesquisar()
            comando = Function.decisao()

        #Pesquisa no ENA
        elif comando==2:
            Function.ENApesquisar()
            comando = Function.decisao()

        #Sair da aba atual
        elif comando==3:
            print("Feito!")




    #Caso digito for para pesquisa detalhada
    elif comando == 2:
        print("_____________________________________________________________________________")
        print("|                                                                           |")
        print("|                     TERMINAL DE PESQUISAS DETALHADAS                      |")
        print("|___________________________________________________________________________|")
        print("|                                                                           |")
        print("|                     [1] Pesquisa Detalhada No NCBI                        |")
        print("|                     [2] Pesquisa Detalhada No ENA                         |")
        print("|                     [3] Sair da Aba atual                                 |")
        print("|___________________________________________________________________________|")
        comando = int(input("Digite o número referente a sua escolha\n> "))
        
        #Pesquisa detalhada no NCBI
        if comando==1:
            Function.SRAdetalhado_pesquisar()
            comando=Function.decisao()

        #Pesquisa detalhada no ENA
        elif comando==2:
            Function.ENAdetalhado_pesquisar()
            comando=Function.decisao()

        #Sair da aba atual
        elif comando==3:
            print("Feito!")



    #Caso digito for para consulta de metadados, somente para NCBI
    elif comando == 3:
        Function.metadados()
        comando = Function.decisao()




    #Caso digito for para download 
    elif comando == 4:
        print("_____________________________________________________________________________")
        print("|                                                                           |")
        print("|                      TERMINAL DE DOWNLOAD DE DADOS                        |")
        print("|___________________________________________________________________________|")
        print("|                                                                           |")
        print("|                      [1] Download de Dados do NCBI                        |")
        print("|                      [2] Download de Dados do ENA                         |")
        print("|                      [3] Sair da Aba atual                                |")
        print("|___________________________________________________________________________|")
        comando = int(input("Digite o número referente a sua escolha\n> "))
       
       #Download no NCBI
        if comando==1:
            Function.SRA_download()
            comando = Function.decisao()

        #Download no ENA
        elif comando==2:
            Function.ENA_download()
            comando = Function.decisao()

        #Sair da aba atual
        elif comando==3:
            print("Feito!")



    #Encerramento do programa
    elif comando == 5:
        print("_____________________________________________________________________________")
        print("Encerrado!")
