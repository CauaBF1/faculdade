## Prova 4 LD

## Resolução P2 antiga
## Questão 1
---
### Complete com o codigo necessário para calcular overflow

```verilog
module alu(input [3:0] a,b,
            input op,
            output [3:0] y,
            output ov);

wire [31:0] nb, bb;
assign nb = ~b;
assign bb = op ? nb : b;
assign y = a + bb + op;
assign ov = (a[3] && b[3] && ~y[3]) || (~a[3] && ~b[3] && y[3]);
endmodule
```
nb: Esta variável representa o complemento de 2 do operando b. No contexto de subtração em binário, subtrair um número é equivalente a adicionar o seu complemento de 2. O complemento de 2 de um número é obtido invertendo todos os bits (complemento de 1) e, em seguida, adicionando 1 ao resultado. No código Verilog, nb é calculado como o complemento bit a bit de b (~b).

bb: Esta variável é usada para escolher entre b e nb dependendo do valor de op (sinal de operação). Se op for 0 (indicando uma operação de soma), bb será igual a b. Se op for 1 (indicando uma operação de subtração), bb será igual a nb.


### Usando full adder
```verilog
module alu(
    input [3:0] a, b,
    input op,
    output [3:0] y,
    output ov
);
    wire [3:0] nb, bb;
    wire c1, c2, c3, c4;
    
    // Complemento de 2 para b
    assign nb = ~b;
    
    // Escolhe b ou nb com base em op
    assign bb = op ? nb : b;
    
    // Instancia 4 full_adders
    full_adder fa0(op, a[0], bb[0], y[0], c1);
    full_adder fa1(c1, a[1], bb[1], y[1], c2);
    full_adder fa2(c2, a[2], bb[2], y[2], c3);
    full_adder fa3(c3, a[3], bb[3], y[3], c4);
    
    // Calcula overflow
    assign ov = (a[3] & bb[3] & ~y[3]) | (~a[3] & ~bb[3] & y[3]);

endmodule


module full_adder(
    input Cin, X, Y,
    output S, Cout);
    
    assign S = X ^ Y ^ Cin;
    assign Cout = (X & Y) | (Cin & X) | (Cin & Y);
endmodule

```
## Questão 2
---
### Usando verilog estrutural complete o codigo abaixo para gerar um crossbar 2x2
```verilog

module cross2x2(x1,x2,s,y1,y2);
    mux2to1 instance1 (s, x1,x2,y1);
    mux2to1 instance2 (s,x2,x1,y2);
endmodule


module mux2to1 (s,w0,w1,f);
    input s,w0,w1;
    output f;

    assign f = s ? w1 : w0;
endmodule

```
