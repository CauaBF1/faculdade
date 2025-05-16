module fsm_with_7seg (
    input clk,            // Clock de 1Hz
    input reset,          // Reset
  	input [2:0] SW,       // SW[2:0] para estado inicial e SW[3] para sequência reversa
    input KEY0,           // Botão para carregar o estado inicial
    input KEY1,
  	output reg [2:0] y,   // Estado atual (y)
    output [6:0] hex_out  // Display de 7 segmentos para mostrar o estado atual
);

    // Definir os estados
    parameter S0 = 3'b000,
              S1 = 3'b001,
              S2 = 3'b010,
              S3 = 3'b011,
              S4 = 3'b100,
              S5 = 3'b101,
              S6 = 3'b110,
              S7 = 3'b111;

    // Registrador de próximo estado
    reg [2:0] Y;  // Próximo estado (Y)
    reg reverse;  // Flag para controlar a sequência reversa

    // Lógica de transição de estados
    always @(posedge clk or posedge reset) begin
        if (reset)
            y <= S0; // Reset para o estado inicial 000
        else if (KEY0)
            y <= SW[2:0]; // Carregar estado inicial de SW[2:0]
        else
            y <= Y; // Atualizar o estado atual
    end

    // Lógica combinacional para determinar o próximo estado
    always @(*) begin
        reverse = KEY1; // Ativar sequência reversa se SW[3] estiver acionado

        if (reverse) begin
            // Sequência reversa
            case (y)
                S0: Y = S7;   // 000 -> 111
                S1: Y = S0;   // 001 -> 000
                S2: Y = S1;   // 010 -> 001
                S3: Y = S2;   // 011 -> 010
                S4: Y = S3;   // 100 -> 011
                S5: Y = S4;   // 101 -> 100
                S6: Y = S5;   // 110 -> 101
                S7: Y = S6;   // 111 -> 110
                default: Y = S0;
            endcase
        end else begin
            // Sequência normal
            case (y)
                S0: Y = S1;   // 000 -> 001
                S1: Y = S3;   // 001 -> 011
                S2: Y = S0;   // 010 -> 000
                S3: Y = S5;   // 011 -> 101
                S4: Y = S0;   // 100 -> 000
                S5: Y = S7;   // 101 -> 111
                S6: Y = S0;   // 110 -> 000
                S7: Y = S0;   // 111 -> 000
                default: Y = S0;
            endcase
        end
    end

    // Lógica para o display de 7 segmentos
    always @(*) begin
        case (y)
            3'b000: hex_out = 7'b1000000; // 0
            3'b001: hex_out = 7'b1111001; // 1
            3'b010: hex_out = 7'b0100100; // 2
            3'b011: hex_out = 7'b0110000; // 3
            3'b100: hex_out = 7'b0011001; // 4
            3'b101: hex_out = 7'b0010010; // 5
            3'b110: hex_out = 7'b0000010; // 6
            3'b111: hex_out = 7'b1111000; // 7
            default: hex_out = 7'b1111111; // Display desligado para valores inválidos
        endcase
    end

endmodule

