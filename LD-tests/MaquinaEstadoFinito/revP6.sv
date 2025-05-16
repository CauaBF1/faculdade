module g6 (
    input w,
    input clk,
    input rst,
    output z
);

reg [1:0] y, Y;

parameter A = 2'b00, B = 2'b01, C = 2'b10, D = 2'b11;


always @(posedge clk, negedge rst) begin
    if(!rst)
        y <= A;
    else
        y <= Y;
end


always @(*)begin

    case(y)
        A: Y <= w ? B : A;
        B: Y <= w ? B : C;
        C: Y <= w ? D : A;
        D: Y <= w ? B : C;
        default: Y <= 2'bxx;
    endcase
end

assign z = (y == D);



endmodule