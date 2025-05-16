module vm (
    input D, N, clk, rst,
    output z
);

    reg [5:1] y, Y;         // 0            // 10       // 5            // 15           // 20
    parameter [5:1] s1 = 5'b00000, s2 = 5'b01010, s3 = 5'b00101, s4 = 5'b01111, s5 = 5'b10100;
    
    always @(D, N, y) begin
        case(y)
            s1: Y = N ? s3 : s1;

            s3: Y = N ? s2 : D ? s4 : s3;

            s2: Y = N ? s4 : D ? s5 : s2;

            s4: Y = s1;

            s5: Y = s3; 

            default: Y = 5'bxxxxx;  
        endcase
    end

    always @(posedge clk or negedge rst)begin
        if(!rst)
            y <= s1;
        else 
            y <= Y;

    end

    assign z = (y == s4);

endmodule
