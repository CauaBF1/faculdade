////////////////////////////Comportamental/////////////////////////////////////////////
module grupo06(input w, clk, rst, output z);

  reg [1:0] y, Y;
  parameter [1:0] A = 2'b00, B = 2'b01, C = 2'b10, D = 2'b11;

  always @(posedge clk, negedge rst)begin
    if (!rst)	
      y <= A;
	else	
      y <= Y;
  end
		
  always @(w,y) begin
      case (y)
        A: Y <= w ? B : A;
        B: Y <= w ? B : C;
        C: Y <= w ? D : A;
        D: Y <= w ? B : C;
        default: Y <= 2'bxx;
      endcase
  end
  
assign z = (y == D);
endmodule


/////////////////////////////////Estrutural////////////////////////////////////////////////

module grupo06Estrutual(input w, clk, rst, output z);

  wire [1:0] y;
  wire [1:0] Y;

  
  fsm_logic fsm(.y(y), .w(w), .Y(Y));

  
  d_flipflop ff0(.d(Y[0]), .clk(clk), .rst(rst), .q(y[0]));
  d_flipflop ff1(.d(Y[1]), .clk(clk), .rst(rst), .q(y[1]));

  
  assign z = (y == 2'b11);

endmodule

// circuito logico CC
module fsm_logic(input [1:0] y, input w, output reg [1:0] Y);
  parameter [1:0] A = 2'b00, B = 2'b01, C = 2'b10, D = 2'b11;

  always @(*) begin
    case (y)
      A: Y = w ? B : A;
      B: Y = w ? B : C;
      C: Y = w ? D : A;
      D: Y = w ? B : C;
      default: Y = 2'bxx;
    endcase
  end
endmodule

// Flip Flop
module d_flipflop(input d, clk, rst, output reg q);
  always @(posedge clk or negedge rst) begin
    if (!rst)
      q <= 0;
    else
      q <= d;
  end
endmodule
// Prof luciano deixou (;
  

