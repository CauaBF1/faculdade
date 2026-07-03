class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, titulo, responsavel=None):
        tarefa = {
            "titulo": titulo,
            "responsavel": responsavel,
            "status": "todo"
        }
        self.tarefas.append(tarefa)
        return tarefa

    def iniciar(self, titulo):
        for tarefa in self.tarefas:
            if tarefa["titulo"] == titulo:
                tarefa["status"] = "in_progress"
                return tarefa
        raise ValueError("Tarefa não encontrada")

    def finalizar(self, titulo):
        for tarefa in self.tarefas:
            if tarefa["titulo"] == titulo:
                tarefa["status"] = "done"
                return tarefa
        raise ValueError("Tarefa não encontrada")

    def contar(self):
        return len(self.tarefas)

    def contar_por_status(self, status):
        return len([t for t in self.tarefas if t["status"] == status])

    def limpar(self):
        self.tarefas.clear()

