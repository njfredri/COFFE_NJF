/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : R-2020.09-SP5-3
// Date      : Tue Jun  3 13:48:38 2025
/////////////////////////////////////////////////////////////


module boothR2_serial_alu ( clk, x, y, ce, op, reset, out );
  input [1:0] op;
  input clk, x, y, ce, reset;
  output out;
  wire   n35, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47, n48,
         n49, n50, n51, n52, n53, n54, n55, n56, n57, n58, n59, n60, n61, n62,
         n63, n64, n65, n66, n67, n68, n69, n70, n71;

  DFFX1 cb_reg_reg ( .D(n35), .CLK(clk), .Q(n71), .QN(n36) );
  NAND2X0 U37 ( .IN1(n37), .IN2(n38), .QN(out) );
  NAND2X0 U38 ( .IN1(n39), .IN2(n40), .QN(n38) );
  NAND2X0 U39 ( .IN1(n41), .IN2(n42), .QN(n40) );
  NAND2X0 U40 ( .IN1(n43), .IN2(n71), .QN(n42) );
  INVX0 U41 ( .IN(n44), .QN(n43) );
  NAND2X0 U42 ( .IN1(n44), .IN2(n36), .QN(n41) );
  NAND2X0 U43 ( .IN1(n45), .IN2(n46), .QN(n44) );
  NAND2X0 U44 ( .IN1(y), .IN2(n47), .QN(n46) );
  NAND2X0 U45 ( .IN1(x), .IN2(n48), .QN(n45) );
  INVX0 U46 ( .IN(y), .QN(n48) );
  NOR2X0 U47 ( .IN1(n49), .IN2(n50), .QN(n37) );
  NOR2X0 U48 ( .IN1(n51), .IN2(n52), .QN(n50) );
  NAND2X0 U49 ( .IN1(x), .IN2(n53), .QN(n52) );
  NOR2X0 U50 ( .IN1(op[0]), .IN2(n54), .QN(n49) );
  NAND2X0 U51 ( .IN1(y), .IN2(op[1]), .QN(n54) );
  NOR2X0 U52 ( .IN1(reset), .IN2(n55), .QN(n35) );
  NOR2X0 U53 ( .IN1(n56), .IN2(n57), .QN(n55) );
  NOR2X0 U54 ( .IN1(n58), .IN2(n36), .QN(n57) );
  NOR2X0 U55 ( .IN1(n59), .IN2(n60), .QN(n58) );
  NAND2X0 U56 ( .IN1(ce), .IN2(n61), .QN(n60) );
  NAND2X0 U57 ( .IN1(n39), .IN2(y), .QN(n61) );
  INVX0 U58 ( .IN(n62), .QN(n39) );
  NAND2X0 U59 ( .IN1(n63), .IN2(n64), .QN(n62) );
  NAND2X0 U60 ( .IN1(op[1]), .IN2(n51), .QN(n64) );
  NAND2X0 U61 ( .IN1(op[0]), .IN2(n53), .QN(n63) );
  NOR2X0 U62 ( .IN1(n65), .IN2(n66), .QN(n56) );
  NAND2X0 U63 ( .IN1(y), .IN2(n59), .QN(n66) );
  NAND2X0 U64 ( .IN1(n67), .IN2(n68), .QN(n59) );
  NAND2X0 U65 ( .IN1(n69), .IN2(n53), .QN(n68) );
  INVX0 U66 ( .IN(op[1]), .QN(n53) );
  NOR2X0 U67 ( .IN1(op[0]), .IN2(n47), .QN(n69) );
  INVX0 U68 ( .IN(x), .QN(n47) );
  NAND2X0 U69 ( .IN1(n70), .IN2(op[1]), .QN(n67) );
  NOR2X0 U70 ( .IN1(x), .IN2(n51), .QN(n70) );
  INVX0 U71 ( .IN(op[0]), .QN(n51) );
  INVX0 U72 ( .IN(ce), .QN(n65) );
endmodule



module alu_serial_unit ( clk, x, y, ce_alu, opConfig, opLoad, reset, out );
  input [2:0] opConfig;
  input clk, x, y, ce_alu, opLoad, reset;
  output out;
  wire   n21, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32, n33, n34,
         n35, n36, n37, n38, n39, n40, n41, n42, n43;
  wire   [1:0] op_reg;

  boothR2_serial_alu boothR2_ALU ( .clk(clk), .x(x), .y(y), .ce(ce_alu), .op(
        op_reg), .reset(reset), .out(out) );
  DFFX1 \op_reg_reg[1]  ( .D(n22), .CLK(clk), .Q(op_reg[1]), .QN(n43) );
  DFFX1 \op_reg_reg[0]  ( .D(n21), .CLK(clk), .Q(op_reg[0]), .QN(n42) );
  NOR2X0 U25 ( .IN1(reset), .IN2(n23), .QN(n22) );
  NAND2X0 U26 ( .IN1(n24), .IN2(n25), .QN(n23) );
  NAND2X0 U27 ( .IN1(n26), .IN2(n43), .QN(n25) );
  NAND2X0 U28 ( .IN1(opLoad), .IN2(n27), .QN(n24) );
  NAND2X0 U29 ( .IN1(n28), .IN2(n29), .QN(n27) );
  NAND2X0 U30 ( .IN1(n30), .IN2(n31), .QN(n29) );
  INVX0 U31 ( .IN(opConfig[1]), .QN(n30) );
  NAND2X0 U32 ( .IN1(opConfig[2]), .IN2(n32), .QN(n28) );
  NAND2X0 U33 ( .IN1(y), .IN2(n33), .QN(n32) );
  NOR2X0 U34 ( .IN1(reset), .IN2(n34), .QN(n21) );
  NAND2X0 U35 ( .IN1(n35), .IN2(n36), .QN(n34) );
  NAND2X0 U36 ( .IN1(n26), .IN2(n42), .QN(n36) );
  INVX0 U37 ( .IN(opLoad), .QN(n26) );
  NAND2X0 U38 ( .IN1(n37), .IN2(opLoad), .QN(n35) );
  NAND2X0 U39 ( .IN1(n38), .IN2(n39), .QN(n37) );
  NAND2X0 U40 ( .IN1(n40), .IN2(n31), .QN(n39) );
  INVX0 U41 ( .IN(opConfig[2]), .QN(n31) );
  INVX0 U42 ( .IN(opConfig[0]), .QN(n40) );
  NAND2X0 U43 ( .IN1(n41), .IN2(opConfig[2]), .QN(n38) );
  NOR2X0 U44 ( .IN1(y), .IN2(n33), .QN(n41) );
  INVX0 U45 ( .IN(x), .QN(n33) );
endmodule
