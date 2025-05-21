Comum entre threads:
 - Area de memoria, vetor de arquivos abertos, segmento de codigo e dados globais

Independente
 - pilha, PC, registradores


7 transições:
- Exec -> pronto (time slice)
- exec -> bloq (esperando recurso)
- exec -> term (concluido, erro fatal(viol segme, falha recu),termino por sist ou usu )
- pront -> exec (escalonador fila de prontos)
- bloq -> pront (liberação de recursos e vai p fila de prontos)
- bloq -> term (processo é interrompido mesmo durante bloqueio)
- pront -> term (erro fatal, problema critico antes da execução ou ação usu ou sist)

