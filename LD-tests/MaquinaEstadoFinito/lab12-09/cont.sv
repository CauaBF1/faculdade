module top(
    input clk,
    input rst, // rst
    input dir,
    output [6:0] HEX0,
    output [2:0] count
); 
    cont5 i1 (rst, dir, clk, count);
    dec7seg i2 (count, HEX0);
    // 

endmodule



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
    end

    always @(y)begin
        z = y;
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