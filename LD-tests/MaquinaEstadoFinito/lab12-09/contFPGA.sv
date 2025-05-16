module top(
    input CLOCK_50,
    input [1:0] KEY, // rst
    input [1:0] SW, //direction
    output [6:0] HEX0,
    output [2:0] count,
    output [3:0] LEDR
);
    reg [25:0] cnt;
    wire nKEY;

    always @(posedge CLOCK_50) begin
        cnt <= cnt + 1;
    end

    wire clk1hz = cnt[25];  

    assign nKEY = ~KEY[0];
    cont5 i1 (nKEY, SW[1], clk1hz, count);
    dec7seg i2 (count, HEX0);
	

    always @(posedge clk1hz)begin
	LEDR[0] <= ~LEDR[0];
    end
endmodule

/*
reg [25:0] cnt;

always @(posedge CLOCK_50)
    if(cnt < (25_000_000 -1))
        cnt <= cnt + 1;
    else
        cnt <= 0;
        clk1hz <= ~clk1hz
*/



module cont5 (
    input rst,
    input sw,
    input clk,
    output [2:0] z
);

    parameter A = 3'b000, B = 3'b001, C = 3'b010, D = 3'b011, E = 3'b100,
    F = 3'b101;


    reg [2:0] y, Y;

    always @(*) begin
        case(y)
            A: Y <= sw ? F : B;
            B: Y <= sw ? A : C;
            C: Y <= sw ? B : D;
            D: Y <= sw ? C : E;
            E: Y <= sw ? D : F;
            F: Y <= sw ? E : A; 
            default: Y <= 3'bxx;
            
        endcase
    end

    always @(posedge clk)begin
        if(!rst)
            y <= A;
        else
            y <= Y;
        z <= y;
    end


endmodule


module dec7seg(
    input [2:0] hex,
    output reg [6:0] seg
);
    always @(*) begin
        case (hex)
            3'b000: seg = 7'b1000000; // 0
            3'b001: seg = 7'b1111001; // 1
            3'b010: seg = 7'b0100100; // 2
            3'b011: seg = 7'b0110000; // 3
            3'b100: seg = 7'b0011001; // 4
            3'b101: seg = 7'b0010010; // 5
            3'b110: seg = 7'b0000010; // 6
            3'b111: seg = 7'b1111000; // 7
            default: seg = 7'b1111111; // Display desligado para valores inválidos
        endcase
    
    end
endmodule
