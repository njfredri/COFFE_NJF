/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : R-2020.09-SP5-3
// Date      : Fri Jan 24 13:40:47 2025
/////////////////////////////////////////////////////////////


module boothR2_serial_alu ( clk, x, y, ce, op, reset, out );
  input [1:0] op;
  input clk, x, y, ce, reset;
  output out;
  wire   n1, n18, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15,
         n16, n17;

  DFFX2 cb_reg_reg ( .D(n18), .CLK(clk), .QN(n1) );
  INVX2 U2 ( .IN(ce), .QN(n10) );
  NAND2X2 U3 ( .IN1(y), .IN2(n15), .QN(n11) );
  INVX2 U4 ( .IN(n14), .QN(n15) );
  NOR2X2 U5 ( .IN1(reset), .IN2(n9), .QN(n18) );
  MUX21X2 U6 ( .IN1(n16), .IN2(n17), .S(x), .Q(n14) );
  NAND2X2 U7 ( .IN1(op[0]), .IN2(op[1]), .QN(n16) );
  NAND2X2 U8 ( .IN1(n3), .IN2(y), .QN(n13) );
  XNOR2X2 U9 ( .IN1(op[0]), .IN2(op[1]), .Q(n3) );
  INVX2 U10 ( .IN(op[1]), .QN(n8) );
  NAND2X4 U11 ( .IN1(n7), .IN2(n8), .QN(n17) );
  INVX2 U12 ( .IN(op[0]), .QN(n7) );
  AO21X1 U13 ( .IN1(n2), .IN2(n3), .IN3(n4), .Q(out) );
  MUX21X1 U14 ( .IN1(n5), .IN2(n6), .S(n7), .Q(n4) );
  ISOLANDX1 U15 ( .D(y), .ISO(n8), .Q(n6) );
  ISOLANDX1 U16 ( .D(x), .ISO(op[1]), .Q(n5) );
  XNOR3X1 U17 ( .IN1(y), .IN2(x), .IN3(n1), .Q(n2) );
  OA22X1 U18 ( .IN1(n10), .IN2(n11), .IN3(n1), .IN4(n12), .Q(n9) );
  AND3X1 U19 ( .IN1(ce), .IN2(n13), .IN3(n14), .Q(n12) );
endmodule


module alu_serial_unit ( clk, x, y, ce_alu, opConfig, opLoad, reset, out );
  input [2:0] opConfig;
  input clk, x, y, ce_alu, opLoad, reset;
  output out;
  wire   n12, n13, n14, n15, n16, n17, n18, n19, n20;
  wire   [1:0] op_reg;

  boothR2_serial_alu boothR2_ALU ( .clk(clk), .x(x), .y(y), .ce(ce_alu), .op(
        op_reg), .reset(reset), .out(out) );
  DFFX1 \op_reg_reg[1]  ( .D(n13), .CLK(clk), .Q(op_reg[1]) );
  DFFX1 \op_reg_reg[0]  ( .D(n12), .CLK(clk), .Q(op_reg[0]) );
  ISOLANDX1 U14 ( .D(n14), .ISO(reset), .Q(n13) );
  MUX21X1 U15 ( .IN1(op_reg[1]), .IN2(n15), .S(opLoad), .Q(n14) );
  MUX21X1 U16 ( .IN1(opConfig[1]), .IN2(n16), .S(opConfig[2]), .Q(n15) );
  NOR2X0 U17 ( .IN1(x), .IN2(n17), .QN(n16) );
  ISOLANDX1 U18 ( .D(n18), .ISO(reset), .Q(n12) );
  MUX21X1 U19 ( .IN1(op_reg[0]), .IN2(n19), .S(opLoad), .Q(n18) );
  MUX21X1 U20 ( .IN1(opConfig[0]), .IN2(n20), .S(opConfig[2]), .Q(n19) );
  NAND2X0 U21 ( .IN1(x), .IN2(n17), .QN(n20) );
  INVX0 U22 ( .IN(y), .QN(n17) );
endmodule

