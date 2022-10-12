# Protótipo Pytheas número 3

(12/10/2022): Atualmente estamos fazendo uso de 3 API's, pysradb, SRA Toolkit e o EnaBrowserTools. O problema de acesso as ferramentas do SRA e do ENA foram parcialmente resolvidas. Para o funcionamento correto dos dois programas é necessário que o usuário execute o pytheas.py dentro do diretório pois para utilizar tanto o Ena Browser quanto o SRA Tools, o pytheas.py acessa os dois por meio de caminhos, acessando seus respcetivos diretórios até achar seus executáveis. As seguintes modificações foram feitas em relação a sua versão anterior: Adição de interfaces gráficas simples em que dá ao usuário a oportunidade de usar o NCBI ou o ENA para sua consulta e download, esta função foi adcionado tanto para pesquisa quanto para pesquisa detalhada e download de fastq. Foram adcionados também 3 novas funções a ENA_pesquisar, ENA_detalhado_pesquisar e ENA_download, as duas primeiras fazem uso do pysradb e são versões específicas para pesquisa no ENA, a terceira e última é uma função que faz downloads no formato fastq.gz direto do ENA usando ENABrowserTools, esta função faz o download e retorna como resultado um diretório contendo o arquivo fastq na extenção .gz, isso pode dificultar a vida do usuário que apenas gostaria de ver seu arquivo completo. Por padrão programei para colocar o diretório na pasta pessoal do usuário ou "~/". 

Possíveis futuras modificações e anotações paras proximas versões:

1 - Pelo Efetch podemos criar novas funções para fazer download de nucleotídeos,
    sequencias de DNA ou RNA e de proteínas e de genes. Embora nosso foco momen-
    taneo seja FASTQ e SRA, podemos expandir para mais e mais fornecendo uma am-
    pla gama de variedades ao usúario.
    
2 - Ler mais a respeito do EnaBrowsertools, podemos garantir novas funções para
    o usuário, bem como ler mais a respeito do SRAtoolkits para adcionar funções
    extras na nossa ferramenta.
    
3 - Tentar tornar o código principal mais limpo, talvez por meio de módulos.
