module fsm (
    input clk,           // Clock
    input reset,         // Reset
    output reg [2:0] y   // Estado atual (y)
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
    reg [2:0] Y; // Próximo estado (Y)

    // Lógica de transição de estados
    always @(posedge clk or posedge reset) begin
        if (reset)
            y <= S0; // Reset para o estado inicial 000
        else
            y <= Y;  // Atualiza o estado atual para o próximo estado
    end

    // Lógica combinacional para determinar o próximo estado
    always @(*) begin
        case (y)
            S0: Y = S1;   // 000 -> 001
            S1: Y = S3;   // 001 -> 011
            S2: Y = S0;   // 010 -> 000
            S3: Y = S5;   // 011 -> 101
            S4: Y = S0;   // 100 -> 000
            S5: Y = S7;   // 101 -> 111
            S6: Y = S0;   // 110 -> 000
            S7: Y = S0;   // 111 -> 000
            default: Y = S0; // Estado padrão
        endcase
    end

endmodule

