module tb_grupoA5();

    reg Clock;
    reg reset;
    reg w;
    wire z_comportamental;
    wire z_estrututal;

  
    grupo06 a1 (
        .clk(Clock),
        .rst(reset),
        .w(w),
        .z(z_comportamental)
    );

    
  	grupo06Estrutual a2 (
        .clk(Clock),
        .rst(reset),
        .w(w),
        .z(z_estrututal)
    );

  always #50 Clock = ~Clock;

  initial begin

    Clock = 0;
    reset = 0;
    w = 0;

    #10 reset = 1;

    #10 @(posedge Clock) w = 1; 
    #10 display_check(1);
    
    #10 @(posedge Clock)  w = 0; 
    #10 display_check(2);
    
    #10 @(posedge Clock)  w = 1; 
    #10 display_check(3);
    
    #10 @(posedge Clock)  w = 0; 
    #10 display_check(4);
    
    #10 @(posedge Clock)  w = 1; 
    #10 display_check(5);
    
    #10 @(posedge Clock)  w = 1; 
    #10 display_check(6);
    
    #10 @(posedge Clock)  w = 0; 
    #10 display_check(7);
    
    #10 @(posedge Clock)  w = 1; 
    #10 display_check(8);
    
    #10 @(posedge Clock)  w = 0; 
    #10 display_check(9);
    
    #10 @(posedge Clock)  w = 0; 
    #10 display_check(10);
    
    #10 @(posedge Clock)  w = 0; 
    #10 display_check(11);
    
    #10 @(posedge Clock)  w = 1; 
    #10 display_check(12);

    
    #20 $finish;
  end

  //exibir o resultado de cada teste
  task display_check(input integer cycle);
    begin
      if (z_comportamental === z_estrututal)
        $display("Teste %0d: w = %b, z_comportamental = %b, z_estrututal = %b -- OK", cycle, w, z_comportamental, z_estrututal);
      else
        $display("Teste %0d: w = %b, z_comportamental = %b, z_estrututal = %b -- ERRO", cycle, w, z_comportamental, z_estrututal);
    end
  endtask

endmodule


