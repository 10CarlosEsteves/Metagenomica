#! /usr/bin/python3
import os
from pysradb.sraweb import SRAweb
from pysradb.search import SraSearch
from pysradb.search import EnaSearch


os.system("export PATH=$PATH:$HOME/.local/bin")
os.system("export PATH=$PATH:$PWD/sratoolkit.3.0.0-ubuntu64/bin")


#Função de decisão
def decisao():
    print("_____________________________________________________________________________")
    print("\nGostaria de voltar ao menu ou encerrar o programa?")
    print("[0] Voltar ao menu | [5] Encerrar programa")
    return int(input(">"))



#Função de pesquisa geral no SRA/NCBI
def SRApesquisar():
    print("_____________________________________________________________________________")
    query = str(input("Insira a sua pesquisa: "))
    print("RESULTADOS ENCONTRADOS:\n")
    instance = SraSearch(2,20,query)
    instance.search()
    df = instance.get_df()
    print(df)

def ENApesquisar():
    print("_____________________________________________________________________________")
    query = str(input("Insira a sua pesquisa: "))
    print("RESULTADOS ENCONTRADOS:\n")
    instance = EnaSearch(2, 20, query)
    instance.search()
    df = instance.get_df()
    print(df)

#Função de retorno nulo
def default(argumento):
    if argumento=="" or argumento=="None":
        return None

    else:
        return argumento



#Função de Pesquisa detalhada no SRA/NCBI
def SRAdetalhado_pesquisar():
    print("_____________________________________________________________________________")
    print("INSTRUÇÕES: O programa fará varias perguntas para personalizar a busca. Caso")
    print("voce não queira responder uma pergunta aperte enter ou digite None, e a")
    print("pergunta será ignorada e será passada para próxima pergunta. Caso este comando")
    print("retorne um erro ou retorne nada encontrado, por favor ,verifique a ortografia")
    print("e tente novamente")
    print("_____________________________________________________________________________")

    maximo=str(input("Digite o máximo de resultados a ser retornado: "))

    pergunta=str(input("Digite a sua pesquisa: "))
    maximo=default(maximo)

    organismo=str(input("Digite o organismo de preferencia: "))
    maximo=default(maximo)

    plataforma=str(input("Digite a plataforma usada no sequenciamento(illumina, ion torrent, oxford nanopore): "))
    maximo=default(maximo)

    fonte=str(input("Digite a biblioteca fonte(genomic, metagenomic, transcriptomic) :"))
    maximo=default(maximo)

    data = str(input("Digite uma data específica(dd-mm-yyyy): "))
    maximo=default(maximo)

    estrategia = str(input("Digite a estratégia(wgs, amplicon, rna seq): "))
    maximo=default(maximo)

    print("RESULTADOS ENCONTRADOS:\n")

    try:
        instance=SraSearch(2, maximo, query= pergunta, organism=organismo, platform=plataforma, source=fonte ,publication_date=data, strategy=estrategia)
        instance.search()
        df = instance.get_df()
        print(df)

    except:
        print("_____________________________________________________________________________")
        print("ERRO SINTÁTICO DETECTADO, POR FAVOR, TENTE NOVAMENTE")


#Função de pesquisa detalhada no banco de dados do ENA
def ENAdetalhado_pesquisar():
    print("_____________________________________________________________________________")
    print("INSTRUÇÕES: O programa fará varias perguntas para personalizar a busca. Caso")
    print("voce não queira responder uma pergunta aperte enter ou digite None, e a")
    print("pergunta será ignorada e será passada para próxima pergunta. Caso este comando")
    print("retorne um erro ou retorne nada encontrado, por favor ,verifique a ortografia")
    print("e tente novamente")
    print("_____________________________________________________________________________")

    maximo=str(input("Digite o máximo de resultados a ser retornado: "))

    pergunta=str(input("Digite a sua pesquisa: "))
    maximo=default(maximo)

    organismo=str(input("Digite o organismo de preferencia: "))
    maximo=default(maximo)

    plataforma=str(input("Digite a plataforma usada no sequenciamento(illumina, ion torrent, oxford nanopore): "))
    maximo=default(maximo)

    fonte=str(input("Digite a biblioteca fonte(genomic, metagenomic, transcriptomic) :"))
    maximo=default(maximo)

    data = str(input("Digite uma data específica(dd-mm-yyyy): "))
    maximo=default(maximo)

    estrategia = str(input("Digite a estratégia(wgs, amplicon, rna seq): "))
    maximo=default(maximo)

    print("RESULTADOS ENCONTRADOS:\n")
    try:
        instance=EnaSearch(2, maximo, query= pergunta, organism=organismo, platform=plataforma, source=fonte ,publication_date=data, strategy=estrategia)
        instance.search()
        df = instance.get_df()
        print(df)

    except:
        print("_____________________________________________________________________________")
        print("ERRO SINTÁTICO DETECTADO, POR FAVOR, TENTE NOVAMENTE")


#Função de consulta dos metadados
def metadados():
    print("_____________________________________________________________________________")
    codigo=str(input("Por favor, digite o código SRA do NCBI para consultarmos os metadados: "))
    print("RESULTADOS ENCONTRADOS:\n")
    db = SRAweb()
    df = db.sra_metadata(codigo)
    df
    print(df)



#Função de downloads do NCBI
def SRA_download():
    print("_____________________________________________________________________________")
    codigo= str(input("Por favor, para começar o download, insira código SRA do NCBI: "))
    fastq = str("./sratoolkit.3.0.0-ubuntu64/bin/fasterq-dump --split-files "+codigo)
    print("Download ocorrendo. Isto pode demorar um pouco...")
    print("RESULTADO DO PROGRAMA:\n")
    os.system(fastq)

def ENA_download():
    print("_____________________________________________________________________________")
    codigo= str(input("Por favor, para começar o download, insira código SRA do ENA: "))
    fastq = str("./enaBrowserTools-1.1.0/python3/enaDataGet -f fastq "+codigo+" -d ~")
    print("Download ocorrendo. Isto pode demorar um pouco...")
    print("RESULTADO DO PROGRAMA:\n")
    os.system(fastq)
