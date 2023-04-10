# Projeto Ouvidoria-Fase 3

### ALUNOS:

- Kleiton Ferreira
- João Vitor
- Flávia Amorim
- José Sandro 
- Sabrina Marques
- Jonathan Gois

### DESCRIÇÃO BÁSICA DOS ARQUIVOS

Essa fase do projeto é composta por três arquivos em Python que funcionam em conjunto: ouvidoria3, metodos, operacoesbd.

 **ouvidoria3:** se trata de um código, em Python, que executa um menu de opções para um portal de ouvidoria. Ele funciona como um arquivo main que importa todas as funções contidas no arquivo externo chamado "metodos".

**metodos:** diz respeito a um conjunto de funções necessárias para executar o programa de ouvidoria de uma universidade (poderia ser para qualquer tipo de empresa, pessoa física ou jurídica, como um hospital, uma loja de brinquedos, etc. O tipo de estabelecimento dependeria do cliente, mas nesse caso, escolhemos ficticiamente, uma universidade) que permite aos usuários inserir e visualizar reclamações, elogios e sugestões. Esse programa importa outro conjunto de funções para efetuar operações no banco de dados através do arquivo “operacoesbd”.
 
**operacoesbd:** conjunto de funções Python que permitem a conexão dos dois códigos dos arquivos “ouvidoria3” e “metodos” a um banco de dados MySQL para realizar os comandos de inserir, listar, pesquisar e excluir manifestações no banco de dados.


### PREPARAÇÃO BÁSICA DO PROGRAMA

**1)** No MySQL Wokbench, criar  um schema chamado **‘ouvidoria’** com as seguintes tabelas:

create table reclamacoes (

codigo int auto_increment,

reclamacao varchar (1000),

primary key (codigo)

);

create table elogios_sugestoes (

codigo int auto_increment,

elogio_sugestao varchar (1000),

primary key (codigo)

);

**2)** Com o aquivo ‘ouvidoria3.py’ aberto no pycharm, trocar a senha do MySQL Workbench pela senha do MySQL em uso, na hora de executar o código, para estabelecer a conexão entre o Pycharm e o MySQL.

**3)** Com o arquivo ‘operacoesbd’ aberto no Pycharm, passar o cursor do mouse sobre “mysql.connector” na primeira linha, onde está sublinhado na cor vermelha, e clicar em  “Install package mysql”. Como na imagem abaixo.

![Imagem1](https://user-images.githubusercontent.com/127905306/231015356-09ad1c2a-b2fe-4e76-a29b-b3622eeecc61.png)

**4)** Após o término da instalação mencionada anteriormente, aponte o cursor do mouse, novamente, em “mysql.connector” na primeira linha que ainda está com sublinha vermelha e dê um clique. Em seguida, aparecerá um ícone de lâmpada vermelha na linha dois, clique na lâmpada e e selecione a segunda opção para instalar o pacote do conector python para mysql. Imagem a seguir.

![Imagem2](https://user-images.githubusercontent.com/127905306/231015996-30988d21-f96f-4007-83ba-48b40d79c3ff.png)

Ao fim da segunda instalação, o programa estará preparado para ser executado.

**Observação:** os procedimentos de instalação acima só devem ser feitos caso os pacotes ainda não estejam instalados. Se estiverem instalados, não aparecerá a sublinha vermelha em “mysql.connector.

**Observação 2:** utilizamos o código “try except” para evitar erros ao digitar floats, strings e qualquer outra digitação que não seja um número inteiro nas opções de input.

