module mmc_s( //estrutural
    input ld, clk,
    input [31:0] i_a, i_b,
    output [31:0] res, //resultado
    output done); //pronto

    wire [31:0] a, b, a_i_a, b_i_b;
    wire en_a, en_b;
    // acumula o menor
    assign a_i_a = a + i_a;
    assign b_i_b = b + i_b;
    assign en_a = a < b;
    assign en_b = b < a;

    reg32 ra(ld, clk, en_a, i_a, a_i_a, a);
    reg32 rb(ld, clk, en_b, i_b, b_i_b, b);
    // ao final, os dois serao iguais
    assign res = a;
    assign done = (a == b);
endmodule

module reg32( //apenas instanciar
    input ld, clk, en,
    input [31:0] data_l, data_i,
    output reg [31:0] data_o);
    
    always @(posedge clk)
    if (ld) 
        data_o = data_l;
    else if (en) 
        data_o = data_i;
endmodule