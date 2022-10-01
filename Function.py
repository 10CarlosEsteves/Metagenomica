import os
from pysradb.sraweb import SRAweb
from pysradb.search import SraSearch

os.system("export PATH=$PATH:$HOME/.local/bin")

#Função de decisão
def decisao():
    print("#############################################################################")
    print("\nGostaria de voltar ao menu ou encerrar o programa?")
    print("[0] Voltar ao menu | [5] Encerrar programa")
    return int(input(">"))



#Função de pesquisa geral
def pesquisar():
    print("#############################################################################")
    query = str(input("Insira a sua pesquisa: "))
    print("RESULTADOS ENCONTRADOS:\n")
    instance = SraSearch(2,20,query)
    instance.search()
    df = instance.get_df()
    print(df)



#Função de retorno nulo
def default(argumento):

    if argumento=="" or argumento=="None":
        return None
    
    else:
        return argumento



#Função de Pesquisa detalhada
def detalhes_pesquisar():
    print("#############################################################################")
    print("INSTRUÇÕES: O programa fará varias perguntas para personalizar a busca. Caso")
    print("voce não queira responder uma pergunta aperte enter ou digite None, e a")
    print("pergunta será ignorada e será passada para próxima pergunta. Caso este comando")
    print("retorne um erro ou retorne nada encontrado, por favor ,verifique a ortografia")
    print("e tente novamente")
    print("#############################################################################")

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

    instance=SraSearch(2, maximo, query= pergunta, organism=organismo, platform=plataforma, source=fonte ,publication_date=data, strategy=estrategia)
    instance.search()
    df = instance.get_df()
    print(df)



#Função de consulta dos metadados
def metadados():
    print("#############################################################################")
    codigo=str(input("Por favor, digite o código SRA do NCBI para consultarmos os metadados: "))
    print("RESULTADOS ENCONTRADOS:\n")
    db = SRAweb()
    df = db.sra_metadata(codigo)
    df
    print(df)



#Função de downloads
def download():
    print("#############################################################################")
    codigo= str(input("Por favor, para começar o download, insira código SRA do NCBI: "))
    fastq = str("fasterq-dump "+codigo+" --split-files")
    print("Download ocorrendo. Isto pode demorar um pouco...")
    print("RESULTADO DO PROGRAMA:\n")
    os.system(fastq)
    print("Downloads concluidos com sucesso!")
