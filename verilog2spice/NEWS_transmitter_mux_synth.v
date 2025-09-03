/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Expert(TM) in wire load mode
// Version   : R-2020.09-SP5-3
// Date      : Mon Jun  9 15:25:22 2025
/////////////////////////////////////////////////////////////


module bus_muxp_BUS_WIDTH1_BUS_CNT2 ( bus_all, select, bus_out );
  input [1:0] bus_all;
  input [0:0] select;
  output [0:0] bus_out;

  tri   [1:0] bus_all;
  tri   \select[0] ;
  tri   \bus_out[0] ;

  mux \mux_arr_msb.m  ( .channels(bus_all), .select(select[0]), .out(
        bus_out[0]) );
endmodule


module Transmitter ( dirReg_Q, levelReg_Q, captureReg_Q, localIn, txOut );
  input [-2:0] dirReg_Q;
  input [-2:0] levelReg_Q;
  input [0:0] captureReg_Q;
  input [0:0] localIn;
  output [0:0] txOut;

  tri   \captureReg_Q[0] ;
  tri   \localIn[0] ;
  tri   \txOut[0] ;
  tri   txSelect;

  bus_muxp_BUS_WIDTH1_BUS_CNT2 transmitMux ( .bus_all({captureReg_Q[0], 
        localIn[0]}), .select(txSelect), .bus_out(txOut[0]) );
  NAND2X1 C94 ( .IN1(1'b1), .IN2(1'b1), .QN(txSelect) );
endmodule
