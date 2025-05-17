# BIOS
Usando algum sistema computacional ao qual você tem acesso, vamos examinar o carregamento inicial do sistema operacional. 
Ao ligar o computador observe se há indicação de alguma combinação de teclas a serem pressionadas para ativar acesso à interface de configuração dos parâmetros de inicialização e operação desses sistema.
Se possível, ative o programa de configuração e observe os seguintes parâmetros:

- configurações do processador
- configurações de memória
- configurações dos controladores de periféricos presentes na placa-mãe
- configuração das unidades de armazenamento detectadas
- configurações de sequência de dispositivos para busca carregamento do bloco de iniciação do sistema
- configurações de senhas de acesso a esse programa!
- medições da temperatura do processador e da placa-mãe
- opções de ajuste de valores default e de salvamento das alterações realizadas (cuidado com isso!)
- ... o que mais houver para consultar ou configurar no seu sistema...


Se a memória RAM é volátil, onde está armazenado esse programa de controle? (observe que ele funciona mesmo que não exista um HD ou SSD)
Onde são salvos os parâmetros de configuração que podem ser alterados? (há uma bateria em formato de moeda na placa-mãe? Para que serve?)

é possível examinar a lista de dispositivos que o programa da BIOS do computador exibe antes do boot do sistema. Essa lista de dispositivos é mantida na forma de uma tabela com estruturas de dados padronizadas que o SO pode consultar (SMBIOS), ao invés de ter que testar cada barramento em busca dos dispositivos presentes. 

Na fase de boot, o SO vai tentar carregar controladores para os dispositivos para os quais tenha suporte. 

Uma vez conectado ao sistema, o usuário pode consultar esses dispositivos de diferentes formas:

    Num sistema Linux, por exemplo, usando a interface gráfica, é possível examinar a ferramenta de configuração e verificar quais são os dispositivos. 
    Num sistema Linux, dentro das opções de configurações do sistema é possível ver os dispositivos configurados.
    Num sistema Windows, junto às configurações do sistema (Settings) é possível ver informações sobre os dispositivos e as configurações do sistema. Dentro das "Ferramentas Administrativas" também é possível acessar o "Gerenciamento do Computador", onde há informações sobre o "Gerenciador de dispositivos". 
    Num sistema MacOS, é possível examinar "About this Mac -> System Report...".

Seja lá qual for o sistema operacional em uso, basta procurar por alguma ferramenta de configuração / informação...

Veja: processador, memória, unidades de armazenamento, interfaces de rede (com e sem fio), bluetooth, câmera de vídeo, áudio, barramentos (PCI, USB), controladores de disco (SATA, SCSI, ...), dispositivos USB, ... e o que mais houver.

