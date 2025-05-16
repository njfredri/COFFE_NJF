/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : R-2020.09-SP5-3
// Date      : Wed Mar 12 12:38:39 2025
/////////////////////////////////////////////////////////////


module opmux_behav ( clk, rf_portA, rf_portB, net_stream, confSig, confLoad, 
        opnX, opnY );
  input [15:0] rf_portA;
  input [15:0] rf_portB;
  input [0:0] net_stream;
  input [2:0] confSig;
  output [15:0] opnX;
  output [15:0] opnY;
  input clk, confLoad;
  wire   n90, n91, n92, n116, n117, n118, n119, n120, n121, n122, n123, n124,
         n125, n126, n127, n128, n129, n130, n131, n132, n133, n134, n135,
         n136, n137, n138, n139, n140, n141, n142, n143, n144, n145, n146,
         n147, n148, n149, n150, n151, n152, n153, n154, n155, n156, n157,
         n158, n159, n160, n161, n162, n163, n164, n165, n166, n167, n168,
         n169, n170, n171, n172, n173, n174, n175, n176, n177, n178, n179,
         n180, n181, n182, n183, n184, n185, n186, n187, n188, n189, n190,
         n191, n192, n193, n194, n195, n196, n197, n198, n199, n200, n201,
         n202, n203, n204, n205, n206;

  DFFX1 \conf_reg_reg[2]  ( .D(n92), .CLK(clk), .Q(n205), .QN(n117) );
  DFFX1 \conf_reg_reg[1]  ( .D(n91), .CLK(clk), .Q(n206), .QN(n116) );
  DFFX1 \conf_reg_reg[0]  ( .D(n90), .CLK(clk), .Q(n204), .QN(n118) );
  NAND2X1 U124 ( .IN1(n196), .IN2(n205), .QN(n183) );
  NAND2X2 U125 ( .IN1(n179), .IN2(n180), .QN(n120) );
  INVX0 U126 ( .IN(n119), .QN(opnY[9]) );
  NAND2X0 U127 ( .IN1(rf_portB[9]), .IN2(n120), .QN(n119) );
  INVX0 U128 ( .IN(n121), .QN(opnY[8]) );
  NAND2X0 U129 ( .IN1(rf_portB[8]), .IN2(n120), .QN(n121) );
  NAND2X0 U130 ( .IN1(n122), .IN2(n123), .QN(opnY[7]) );
  NAND2X0 U131 ( .IN1(rf_portA[15]), .IN2(n124), .QN(n123) );
  NAND2X0 U132 ( .IN1(rf_portB[7]), .IN2(n120), .QN(n122) );
  NAND2X0 U133 ( .IN1(n125), .IN2(n126), .QN(opnY[6]) );
  NAND2X0 U134 ( .IN1(rf_portA[14]), .IN2(n124), .QN(n126) );
  NAND2X0 U135 ( .IN1(rf_portB[6]), .IN2(n120), .QN(n125) );
  NAND2X0 U136 ( .IN1(n127), .IN2(n128), .QN(opnY[5]) );
  NAND2X0 U137 ( .IN1(rf_portA[13]), .IN2(n124), .QN(n128) );
  NAND2X0 U138 ( .IN1(rf_portB[5]), .IN2(n120), .QN(n127) );
  NAND2X0 U139 ( .IN1(n129), .IN2(n130), .QN(opnY[4]) );
  NAND2X0 U140 ( .IN1(rf_portA[12]), .IN2(n124), .QN(n130) );
  NAND2X0 U141 ( .IN1(rf_portB[4]), .IN2(n120), .QN(n129) );
  NAND2X0 U142 ( .IN1(n131), .IN2(n132), .QN(opnY[3]) );
  NAND2X0 U143 ( .IN1(rf_portA[7]), .IN2(n133), .QN(n132) );
  NOR2X0 U144 ( .IN1(n134), .IN2(n135), .QN(n131) );
  INVX0 U145 ( .IN(n136), .QN(n135) );
  NAND2X0 U146 ( .IN1(rf_portB[3]), .IN2(n120), .QN(n136) );
  NOR2X0 U147 ( .IN1(n137), .IN2(n138), .QN(n134) );
  NAND2X0 U148 ( .IN1(n139), .IN2(n140), .QN(opnY[2]) );
  NAND2X0 U149 ( .IN1(rf_portA[6]), .IN2(n133), .QN(n140) );
  NOR2X0 U150 ( .IN1(n141), .IN2(n142), .QN(n139) );
  INVX0 U151 ( .IN(n143), .QN(n142) );
  NAND2X0 U152 ( .IN1(rf_portB[2]), .IN2(n120), .QN(n143) );
  NOR2X0 U153 ( .IN1(n137), .IN2(n144), .QN(n141) );
  INVX0 U154 ( .IN(n145), .QN(opnY[1]) );
  NOR2X0 U155 ( .IN1(n146), .IN2(n147), .QN(n145) );
  NAND2X0 U156 ( .IN1(n148), .IN2(n149), .QN(n147) );
  NAND2X0 U157 ( .IN1(rf_portB[1]), .IN2(n120), .QN(n149) );
  NAND2X0 U158 ( .IN1(rf_portA[5]), .IN2(n133), .QN(n148) );
  INVX0 U159 ( .IN(n150), .QN(n133) );
  NAND2X0 U160 ( .IN1(n151), .IN2(n152), .QN(n146) );
  NAND2X0 U161 ( .IN1(rf_portA[3]), .IN2(n153), .QN(n152) );
  NAND2X0 U162 ( .IN1(rf_portA[9]), .IN2(n124), .QN(n151) );
  INVX0 U163 ( .IN(n137), .QN(n124) );
  INVX0 U164 ( .IN(n154), .QN(opnY[15]) );
  NAND2X0 U165 ( .IN1(rf_portB[15]), .IN2(n120), .QN(n154) );
  INVX0 U166 ( .IN(n155), .QN(opnY[14]) );
  NAND2X0 U167 ( .IN1(rf_portB[14]), .IN2(n120), .QN(n155) );
  INVX0 U168 ( .IN(n156), .QN(opnY[13]) );
  NAND2X0 U169 ( .IN1(rf_portB[13]), .IN2(n120), .QN(n156) );
  INVX0 U170 ( .IN(n157), .QN(opnY[12]) );
  NAND2X0 U171 ( .IN1(rf_portB[12]), .IN2(n120), .QN(n157) );
  INVX0 U172 ( .IN(n158), .QN(opnY[11]) );
  NAND2X0 U173 ( .IN1(rf_portB[11]), .IN2(n120), .QN(n158) );
  INVX0 U174 ( .IN(n159), .QN(opnY[10]) );
  NAND2X0 U175 ( .IN1(rf_portB[10]), .IN2(n120), .QN(n159) );
  NAND2X0 U176 ( .IN1(n160), .IN2(n161), .QN(opnY[0]) );
  NOR2X0 U177 ( .IN1(n162), .IN2(n163), .QN(n161) );
  NAND2X0 U178 ( .IN1(n164), .IN2(n165), .QN(n163) );
  NAND2X0 U179 ( .IN1(n166), .IN2(n167), .QN(n165) );
  NOR2X0 U180 ( .IN1(n168), .IN2(n169), .QN(n167) );
  NOR2X0 U181 ( .IN1(rf_portA[1]), .IN2(n204), .QN(n169) );
  NOR2X0 U182 ( .IN1(net_stream[0]), .IN2(n118), .QN(n168) );
  NOR2X0 U183 ( .IN1(n206), .IN2(n117), .QN(n166) );
  NAND2X0 U184 ( .IN1(rf_portA[2]), .IN2(n153), .QN(n164) );
  INVX0 U185 ( .IN(n170), .QN(n153) );
  NAND2X0 U186 ( .IN1(n171), .IN2(n204), .QN(n170) );
  NOR2X0 U187 ( .IN1(n205), .IN2(n116), .QN(n171) );
  NOR2X0 U188 ( .IN1(n137), .IN2(n172), .QN(n162) );
  NAND2X0 U189 ( .IN1(n173), .IN2(n204), .QN(n137) );
  NOR2X0 U190 ( .IN1(n205), .IN2(n206), .QN(n173) );
  NOR2X0 U191 ( .IN1(n174), .IN2(n175), .QN(n160) );
  NOR2X0 U192 ( .IN1(n150), .IN2(n176), .QN(n175) );
  NAND2X0 U193 ( .IN1(n177), .IN2(n206), .QN(n150) );
  NOR2X0 U194 ( .IN1(n204), .IN2(n205), .QN(n177) );
  INVX0 U195 ( .IN(n178), .QN(n174) );
  NAND2X0 U196 ( .IN1(rf_portB[0]), .IN2(n120), .QN(n178) );
  NAND2X0 U197 ( .IN1(n181), .IN2(n117), .QN(n180) );
  NOR2X0 U198 ( .IN1(n204), .IN2(n206), .QN(n181) );
  NAND2X0 U199 ( .IN1(n205), .IN2(n206), .QN(n179) );
  INVX0 U200 ( .IN(n182), .QN(opnX[9]) );
  NAND2X0 U201 ( .IN1(n183), .IN2(rf_portA[9]), .QN(n182) );
  NOR2X0 U202 ( .IN1(n184), .IN2(n172), .QN(opnX[8]) );
  INVX0 U203 ( .IN(rf_portA[8]), .QN(n172) );
  INVX0 U204 ( .IN(n185), .QN(opnX[7]) );
  NAND2X0 U205 ( .IN1(n183), .IN2(rf_portA[7]), .QN(n185) );
  INVX0 U206 ( .IN(n186), .QN(opnX[6]) );
  NAND2X0 U207 ( .IN1(n183), .IN2(rf_portA[6]), .QN(n186) );
  INVX0 U208 ( .IN(n187), .QN(opnX[5]) );
  NAND2X0 U209 ( .IN1(n183), .IN2(rf_portA[5]), .QN(n187) );
  NOR2X0 U210 ( .IN1(n184), .IN2(n176), .QN(opnX[4]) );
  INVX0 U211 ( .IN(rf_portA[4]), .QN(n176) );
  INVX0 U212 ( .IN(n188), .QN(opnX[3]) );
  NAND2X0 U213 ( .IN1(n183), .IN2(rf_portA[3]), .QN(n188) );
  INVX0 U214 ( .IN(n189), .QN(opnX[2]) );
  NAND2X0 U215 ( .IN1(n183), .IN2(rf_portA[2]), .QN(n189) );
  INVX0 U216 ( .IN(n190), .QN(opnX[1]) );
  NAND2X0 U217 ( .IN1(n183), .IN2(rf_portA[1]), .QN(n190) );
  INVX0 U218 ( .IN(n191), .QN(opnX[15]) );
  NAND2X0 U219 ( .IN1(n183), .IN2(rf_portA[15]), .QN(n191) );
  INVX0 U220 ( .IN(n192), .QN(opnX[14]) );
  NAND2X0 U221 ( .IN1(n183), .IN2(rf_portA[14]), .QN(n192) );
  INVX0 U222 ( .IN(n193), .QN(opnX[13]) );
  NAND2X0 U223 ( .IN1(n183), .IN2(rf_portA[13]), .QN(n193) );
  INVX0 U224 ( .IN(n194), .QN(opnX[12]) );
  NAND2X0 U225 ( .IN1(n183), .IN2(rf_portA[12]), .QN(n194) );
  NOR2X0 U226 ( .IN1(n184), .IN2(n138), .QN(opnX[11]) );
  INVX0 U227 ( .IN(rf_portA[11]), .QN(n138) );
  NOR2X0 U228 ( .IN1(n184), .IN2(n144), .QN(opnX[10]) );
  INVX0 U229 ( .IN(rf_portA[10]), .QN(n144) );
  INVX0 U230 ( .IN(n183), .QN(n184) );
  INVX0 U231 ( .IN(n195), .QN(opnX[0]) );
  NAND2X0 U232 ( .IN1(rf_portA[0]), .IN2(n183), .QN(n195) );
  NOR2X0 U233 ( .IN1(n204), .IN2(n116), .QN(n196) );
  NAND2X0 U234 ( .IN1(n197), .IN2(n198), .QN(n92) );
  NAND2X0 U235 ( .IN1(n205), .IN2(n199), .QN(n198) );
  NAND2X0 U236 ( .IN1(confSig[2]), .IN2(confLoad), .QN(n197) );
  NAND2X0 U237 ( .IN1(n200), .IN2(n201), .QN(n91) );
  NAND2X0 U238 ( .IN1(n206), .IN2(n199), .QN(n201) );
  NAND2X0 U239 ( .IN1(confSig[1]), .IN2(confLoad), .QN(n200) );
  NAND2X0 U240 ( .IN1(n202), .IN2(n203), .QN(n90) );
  NAND2X0 U241 ( .IN1(n204), .IN2(n199), .QN(n203) );
  INVX0 U242 ( .IN(confLoad), .QN(n199) );
  NAND2X0 U243 ( .IN1(confSig[0]), .IN2(confLoad), .QN(n202) );
endmodule
