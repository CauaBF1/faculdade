// Top Level Module
module top_level (
    input wire clk,      // Clock direto do DigitalJS
    input wire reset,      // Botão de reset
    input wire dir,        // Chave de direção (0 = UP, 1 = DOWN)
    output wire [6:0] segs, // Saída para o display de 7 segmentos
    output wire [3:0] count // Saída da contagem
);

    wire [2:0] contador;    // Saída de 3 bits do contador (contagem de 0 a 5)
    wire [3:0] contador_ext; // Saída estendida para 4 bits (necessário para o decodificador)

    // Módulo contador Moore
    contador_moore contador_inst (
      .clk(clk), 
        .reset(reset), 
        .dir(dir), 
        .count(contador) // Saída de 3 bits
    );

    // Expandir os 3 bits do contador para 4 bits (adicionando um bit extra 0)
    assign contador_ext = {1'b0, contador}; // Adiciona 0 ao bit mais significativo

    // Módulo decodificador de 7 segmentos
    dec7seg decodificador_inst (
        .hex(contador_ext), 
        .segs(segs)
    );

    // Atribuição da saída do contador (facultativo, pode ser útil para debug ou outros fins)
    assign count = contador_ext;

endmodule

// Módulo Contador Moore
module contador_moore(
  input wire clk,       // Clock direto do DigitalJS
    input wire reset,       // Botão de reset
    input wire dir,         // Chave de direção (0 = UP, 1 = DOWN)
    output reg [2:0] count  // Saída da contagem (3 bits para contar de 0 a 5)
    
);

    // Estados da máquina de estados
    typedef enum reg [2:0] {
        S0 = 3'b000,
        S1 = 3'b001,
        S2 = 3'b010,
        S3 = 3'b011,
        S4 = 3'b100,
        S5 = 3'b101
     } state_t;


    // Estado atual e próximo estado
    reg [2:0] current_state, next_state;

    // Máquina de estados
  always @(posedge clk or posedge reset) begin
        if (reset) begin
            current_state <= S0;
        end else begin
            current_state <= next_state;
        end
    end

    // Lógica de transição de estados
    always @(*) begin
        case (current_state)
            S0: next_state = dir ? S5 : S1;
            S1: next_state = dir ? S0 : S2;
            S2: next_state = dir ? S1 : S3;
            S3: next_state = dir ? S2 : S4;
            S4: next_state = dir ? S3 : S5;
            S5: next_state = dir ? S4 : S0;
            default: next_state = S0;
        endcase
    end

    // Lógica de saída
    always @(current_state) begin
        count = current_state;
    end

endmodule

// Módulo Decodificador de 7 Segmentos
module dec7seg (
    input  [3:0] hex,
    output reg [6:0] segs
);

    always @(hex) begin
        case (hex)         // gfedcba
            4'b0000 : segs = 7'b0111111; // 0
            4'b0001 : segs = 7'b0000110; // 1
            4'b0010 : segs = 7'b1011011; // 2
            4'b0011 : segs = 7'b1001111; // 3
            4'b0100 : segs = 7'b1100110; // 4
            4'b0101 : segs = 7'b1101101; // 5
            4'b0110 : segs = 7'b1111101; // 6
            4'b0111 : segs = 7'b0000111; // 7
            4'b1000 : segs = 7'b1111111; // 8
            4'b1001 : segs = 7'b1101111; // 9
            4'b1010 : segs = 7'b1110111; // A
            4'b1011 : segs = 7'b1111100; // b
            4'b1100 : segs = 7'b0111001; // C
            4'b1101 : segs = 7'b1011110; // d
            4'b1110 : segs = 7'b1111001; // E
            4'b1111 : segs = 7'b1110001; // F
        endcase
    end

endmodule
