module mmc_c(
    input ld, clk,
    input [31:0] i_a, i_b,
    output [31:0] res,
    output done);

    reg [31:0] a,b;
    always @(posedge clk)begin
        if(ld)begin
            a <= i_a;
            b <= i_b;
            done <= 0 //(resetar ele para nao ter erros)
        end
        else
            if(a < b)
                a <= a + i_a;
            else if(b < a)
                b <= b + i_b;
            // melhor dq somente assinalar done <= (a == b) && res <= a
            if(a == b)begin
                done <= 1;
                res <= a;
            end

    end



endmodule