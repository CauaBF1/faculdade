// module countUpDown(
//     input [n-1:0] R,
//     input L, clk, en, up_down,
//     output reg [n-1: 0] res);

//     parameter n = 8;

//     always @(posedge clk)begin
//         if(L)
//             res <= R;
//         else if (en)
//             res <= res + (up_down ? 1 : -1);
//     end


// endmodule


// module divideMult2(
//     input [n-1 : 0] R,
//     input L, clk, en, div_mult,
//     output reg [n-1: 0] res
// );

//     parameter n = 8;

//     always @(posedge clk) begin

//         if (L)
//             res <= R;  // Carrega o valor de R em res se L for 1
//         else if (en)
//             res <= div_mult ? (res >> 1) : (res << 1); 
        
//     end

// endmodule



module contUpDown(
    input [n-1:0] R,
    input E, L, up_down, clk,
    output reg [n-1:0] Q
);
parameter n = 8;

always @(posedge clk) begin
    if (L)
        Q <= R;
    
    else if (E)
        Q <= Q + (up_down ? 1 : -1);
end



endmodule