from dataclasses import dataclass

@dataclass
class Produto:
    nome: str
    preco: float
    quantidade: int = 1

    @property
    def subtotal(self):
        if self.preco < 0:
            raise ValueError("Preço não pode ser negativo")
        if self.quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")
        return self.preco * self.quantidade


def aplicar_desconto(valor, cupom):
    if valor < 0:
        raise ValueError("Valor inválido")

    if cupom == "ALUNO10":
        return valor * 0.90

    if cupom == "ES2":
        return valor * 0.80

    return valor

