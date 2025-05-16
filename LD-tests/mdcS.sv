module mdc_s(
    input ld, clk,
    input [31:0] i_a, i_b,
    output[31:0] res,
    output done);

    wire [31:0] a,b, a_i_a, b_i_b;
    wire en_a, en_b;

    assign a_i_a = a - b;
    assign b_i_b = b - a;
    // assign en_a = a >= b;
    assign en_a = a <= b;
    // assign en_b = b > a;
    assign en_b = b < a;

    // reg32 instance1 (ld, clk, en_a, i_a, a_i_a, a);
    reg32 instance1 (ld, clk, en_b, i_a, a_i_a, a);
    // reg32 instance2 (ld, clk, en_b, i_b, b_i_b, b);
    reg32 instance2 (ld, clk, en_a, i_b, b_i_b, b);

    assign res = a + b;
    assign done = !(a && b);

endmodule

module reg32(
    input ld, clk,en,
    input [31:0] x,y,
    output reg [31:0] res);

    always @(posedge clk)begin
        if(ld)
            res <= x;
        else if(en)
            res <= y;
    end



endmodule