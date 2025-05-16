// Top Level Module
module top_level (
    input wire CLOCK_50,    // Clock de 50 MHz
    input wire [3:0] SW,       // Botão de reset (ativo alto, mas será negado)
    input wire [3:0] KEY,         // Botão de direção (ativo alto, mas será negado)
    output wire [6:0] HEX0, // Saída para o display de 7 segmentos (negado)
    output wire [3:0] count, // Saída da contagem (negado)
	 output reg [3:0] LEDR
);

    wire [2:0] contador;    // Saída de 3 bits do contador (contagem de 0 a 5)
    wire [3:0] contador_ext; // Saída estendida para 4 bits (necessário para o decodificador)
    wire clk_1Hz;            // Clock de 1 Hz gerado pelo divisor de frequência

    // Divisor de Frequência para gerar 1 Hz a partir de 50 MHz
    divisor_frequencia divisor_inst (
        .clk_50MHz(CLOCK_50), 
        .reset(KEY[0]), // Negar o sinal de reset
        .clk_1Hz(clk_1Hz)  // Clock de 1 Hz gerado
    );
	 
    // Módulo contador Moore
    contador_moore contador_inst (
        .CLOCK(clk_1Hz), 
        .reset(KEY[0]),  // Negar o sinal de reset
        .dir(SW[3]),      // Negar o sinal de direção
        .count(contador) // Saída de 3 bits
    );

    // Expandir os 3 bits do contador para 4 bits (adicionando um bit extra 0)
    assign contador_ext = {1'b0, contador}; // Adiciona 0 ao bit mais significativo

    // Módulo decodificador de 7 segmentos
    wire [6:0] segs;
    dec7seg decodificador_inst (
        .hex(contador_ext), 
        .segs(segs)
    );

    // Negar as saídas dos displays
    assign HEX0 = segs;   // Inverter os sinais de saída do display de 7 segmentos
    assign count = contador_ext;  // Inverter a contagem
	 
	 always @(posedge clk_1Hz) begin
		LEDR[0] <= ~LEDR[0]; // Alterna o estado do LED na borda de subida
	 end

endmodule

// Módulo Divisor de Frequência
module divisor_frequencia (
    input wire clk_50MHz,  // Clock de 50 MHz
    input wire reset,      // Botão de reset
    output reg clk_1Hz     // Clock de 1 Hz
);

    parameter DIVISOR = 50000000; // Divisor para gerar 1 Hz a partir de 50 MHz
    reg [25:0] counter_50MHz = 0; // Contador de 26 bits (suficiente para contar até 50 milhões)

    // Divisor de frequência
    always @(posedge clk_50MHz or posedge reset) begin
        if (reset) begin
            counter_50MHz <= 0;
            clk_1Hz <= 0;
        end else if (counter_50MHz == (DIVISOR - 1)) begin
            counter_50MHz <= 0;
            clk_1Hz <= ~clk_1Hz;
        end else begin
            counter_50MHz <= counter_50MHz + 1;
        end
    end

endmodule

// Módulo Contador Moore
module contador_moore(
    input wire CLOCK,       // Clock de 1 Hz
    input wire reset,       // Botão de reset
    input wire dir,         // Botão de direção
    output reg [2:0] count  // Saída da contagem (3 bits para contar de 0 a 5)
);

    // Estados da máquina de estados
    reg [2:0] current_state, next_state;

    // Definição dos estados
    localparam S0 = 3'b000;
    localparam S1 = 3'b001;
    localparam S2 = 3'b010;
    localparam S3 = 3'b011;
    localparam S4 = 3'b100;
    localparam S5 = 3'b101;

    // Máquina de estados
    always @(posedge CLOCK or posedge reset) begin
        if (reset) begin
            current_state <= S0; // Reset
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
            4'b0000 : segs = 7'b1000000; // 0
            4'b0001 : segs = 7'b1111001; // 1
            4'b0010 : segs = 7'b0100100; // 2
            4'b0011 : segs = 7'b0110000; // 3
            4'b0100 : segs = 7'b0011001; // 4
            4'b0101 : segs = 7'b0010010; // 5
            4'b0110 : segs = 7'b0000010; // 6
            4'b0111 : segs = 7'b1111000; // 7
            4'b1000 : segs = 7'b0000000; // 8
            4'b1001 : segs = 7'b0010000; // 9
            4'b1010 : segs = 7'b0001000; // A
            4'b1011 : segs = 7'b0000011; // b
            4'b1100 : segs = 7'b1000110; // C
            4'b1101 : segs = 7'b0100001; // d
            4'b1110 : segs = 7'b0000110; // E
            4'b1111 : segs = 7'b0001110; // F
        endcase
    end

endmodule
