## Comandos

**&** no final deixa em segundo plano exp: sleep 10 & (deixa processo rodar mas inicia prompt novo executando sleep em 2 plano)

**jobs** mostra programas que foram inciados naquele shell

**fg** processo em for ground(primeiro plano diferente de background)
ctrl + z deixa parado
ctrl + c termina(interrompe) processo
**bg** joga para background
ctrl + z para processo para voltar a rodar faça fg tirando do parado
programa que esta em background não consegue ler do terminal

**ps** verifica estado dos processos ativos em forma de lista
**kill** envia um sinal para o processo fornecendo o PID
exp kill -SIGCONT %1 (continua processo em bg com numero 1)

**man 7 signal(descreve sinais)**
por exemplo SIGINT (ação de TERM vem do keyboard ctrl + c)

kill envia por PID
killall por nome

stty -a (comandos de teclado terminal)
stty susp=^t (muda suspender de ^z para ^t)

NI = nice level(o quanto processo é nice com os outros)

nice -n 5 sleep 100 &
ps -l
coloca nivel de NI
quanto menor nivel de NI maior a prioridade

nohup deixa processo funcionando mesmo ao sair do terminal

> ou >> para redirecionar stdout
> 2> ou 2>> redirecionar stderror

fd é vetor de arquivos abertos
ls -l /proc/PID/fd
caso eu abra um arquivo em C ele vai retornar int =3 caso de certo, pq o vetor de arquivos abertos(fd) ja tem as posições 0,1,2 ocupados, respectivamente, stdin,stdout,stderr.

exp:
sleep 200 > saida & (PID = 1234)
ls -l /proc/1234/fd
retorna
lrwx------ 1 borgescaua borgescaua 64 abr 11 11:32 0 -> /dev/pts/1
l-wx------ 1 borgescaua borgescaua 64 abr 11 11:32 1 -> /home/borgescaua/Documents/SO/saida
lrwx------ 1 borgescaua borgescaua 64 abr 11 11:32 2 -> /dev/pts/1
na posição de stdout

; separa instruções
&& separa mas so funciona se anterior der certo

redirecionar para o PIPE
PIPE é um arquivo de memoria, funciona como um buffer circular vetor apontando para paginas de até 64k na memoria do kernell, usado para escrever como se fosse arquivo de forma mais eficiente, exp
sleep 200 | more &
stdout do sleep para pipe e pipe ligado em stdin do more

exp ps aux | more (dessa forma cabe na tela ligando pipe em more)

# Programando em C para syscalls
