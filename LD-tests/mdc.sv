module mdc_b( //comportamental
    input ld, clk,
    input [31:0] i_a, i_b,
    output [31:0] res, //resultado
    output done); //pronto

    reg [31:0] a, b;

    always @(posedge clk)
        if (ld) begin // carrega
            a <= i_a; // valores
            b <= i_b; // iniciais
        end
        else // subtrai o menor do maior
            if (b <= a)
                a <= a - b;
            else
                b <= b - a;
    // ao final, um deles sera zero
    assign res = a + b;
    assign done = !(a && b);
endmodule