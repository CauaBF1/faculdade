module ES(clk, rst, w, z);
	input clk, rst, w;
    output z;
  
    wire y1,y2,nw,ny1,g,h,Y1,Y2;
 
    // Pegrando proximo estado e colocando no estado atual
    FFD Y1F(clk,rst,Y1,y1);
    FFD Y2F(clk,rst,Y2,y2);
    

    // Portas logicas tiradas do mapa de karnout
    not(nw,w);
    not(ny1,y1);
    
    and(Y1, w, w);
    and(g,nw,y1);
    and(h,w,y2,ny1);
    or(Y2,h,g);
    and(z,y2,y1);
    
endmodule

module FFD(input clk,res,d ,output reg q,nq);
  
  always @(posedge clk, posedge res)
    
    if(res)
      q <= 0;
  	else q <= d;

  assign nq = ~q;  
endmodule