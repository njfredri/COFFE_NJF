#verilog netlist
#     module addder_8bit ( A, B, Cin, Sum, Cout );
#   input [7:0] A;
#   input [7:0] B;
#   output [7:0] Sum;
#   input Cin;
#   output Cout;
#   wire   n76, n77, n78, n79, n80, n81, n82, n83, n84, n85, n86, n87, n88, n89,
#          n90;

#   XOR2X1 U73 ( .IN1(n76), .IN2(A[7]), .Q(Sum[7]) );
#   XOR2X1 U74 ( .IN1(n77), .IN2(A[6]), .Q(Sum[6]) );
#   XOR2X1 U75 ( .IN1(n78), .IN2(A[5]), .Q(Sum[5]) );
#   XOR2X1 U76 ( .IN1(n79), .IN2(A[4]), .Q(Sum[4]) );
#   XOR2X1 U77 ( .IN1(n80), .IN2(A[3]), .Q(Sum[3]) );
#   XOR2X1 U78 ( .IN1(n81), .IN2(A[2]), .Q(Sum[2]) );
#   XOR2X1 U79 ( .IN1(n82), .IN2(A[1]), .Q(Sum[1]) );
#   XOR2X1 U80 ( .IN1(A[0]), .IN2(n83), .Q(Sum[0]) );
#   AO22X1 U81 ( .IN1(B[7]), .IN2(n84), .IN3(A[7]), .IN4(n76), .Q(Cout) );
#   XOR2X1 U82 ( .IN1(n84), .IN2(B[7]), .Q(n76) );
#   AO22X1 U83 ( .IN1(B[6]), .IN2(n85), .IN3(A[6]), .IN4(n77), .Q(n84) );
#   XOR2X1 U84 ( .IN1(n85), .IN2(B[6]), .Q(n77) );
#   AO22X1 U85 ( .IN1(B[5]), .IN2(n86), .IN3(A[5]), .IN4(n78), .Q(n85) );
#   XOR2X1 U86 ( .IN1(n86), .IN2(B[5]), .Q(n78) );
#   AO22X1 U87 ( .IN1(B[4]), .IN2(n87), .IN3(A[4]), .IN4(n79), .Q(n86) );
#   XOR2X1 U88 ( .IN1(n87), .IN2(B[4]), .Q(n79) );
#   AO22X1 U89 ( .IN1(B[3]), .IN2(n88), .IN3(A[3]), .IN4(n80), .Q(n87) );
#   XOR2X1 U90 ( .IN1(n88), .IN2(B[3]), .Q(n80) );
#   AO22X1 U91 ( .IN1(B[2]), .IN2(n89), .IN3(A[2]), .IN4(n81), .Q(n88) );
#   XOR2X1 U92 ( .IN1(n89), .IN2(B[2]), .Q(n81) );
#   AO22X1 U93 ( .IN1(B[1]), .IN2(n90), .IN3(A[1]), .IN4(n82), .Q(n89) );
#   XOR2X1 U94 ( .IN1(n90), .IN2(B[1]), .Q(n82) );
#   AO22X1 U95 ( .IN1(B[0]), .IN2(Cin), .IN3(A[0]), .IN4(n83), .Q(n90) );
#   XOR2X1 U96 ( .IN1(B[0]), .IN2(Cin), .Q(n83) );
# endmodule