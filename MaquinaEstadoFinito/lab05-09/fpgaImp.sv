module lab11(
    input CLOCK_50,
    input [3:0] SW,
    input [0:0] KEY0,
    output [6:0] HEX0
);
    reg [24:0] cnt; 


    always @(posedge CLOCK_50) begin
        cnt <= cnt + 1;
    end

    wire clk1hz = cnt[24];  


    fsn i1(
        .clk(clk1hz),       
        .SW(SW),            
        .KEY0(KEY0),        
        .y(),               
        .HEX0(HEX0)        
    );

endmodule

module fsn (
    input clk,            
    input [3:0] SW,       
    input KEY0,           
    output reg [2:0] y,
    output reg [6:0] HEX0
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
    
    reg [2:0] Y;  
    reg reverse;
    wire nKEY0;
    assign nKEY0 = ~KEY0;


    // Máquina de estados
    always @(posedge clk) begin
        if (nKEY0)
            y <= SW[2:0]; 
        else
            y <= Y; 
    end

    // Lógica da máquina de estados
    always @(*) begin
        reverse = SW[3]; 

        if (reverse) begin
            // Sequência reversa
            case (y)
                S0: Y = S7;   // 000 -> 111
                S1: Y = S0;   // 001 -> 000
                S2: Y = S0;   // 010 -> 001
                S3: Y = S1;   // 011 -> 010
                S4: Y = S0;   // 100 -> 011
                S5: Y = S3;   // 101 -> 100
                S6: Y = S0;   // 110 -> 101
                S7: Y = S5;   // 111 -> 101
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

    // Módulo decodificador para display de 7 segmentos
    always @(*) begin
        case (y)
            3'b000: HEX0 = 7'b1000000; // 0
            3'b001: HEX0 = 7'b1111001; // 1
            3'b010: HEX0 = 7'b0100100; // 2
            3'b011: HEX0 = 7'b0110000; // 3
            3'b100: HEX0 = 7'b0011001; // 4
            3'b101: HEX0 = 7'b0010010; // 5
            3'b110: HEX0 = 7'b0000010; // 6
            3'b111: HEX0 = 7'b1111000; // 7
            default: HEX0 = 7'b1111111; // Display desligado para valores inválidos
        endcase
    end

endmodule
