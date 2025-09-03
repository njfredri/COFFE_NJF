.lib "../spice_models/ptm_22nm_bulk_hp.l" 22NM_BULK_HP .endl

.lib "basic_subcircuits.l" BASIC_SUBCIRCUITS .endl

.lib "minlib.sp" ADDITIONAL_LIB .endl


*

*  temp.sp : SPICE netlist translated from the VERILOG netlist : NEWS_transmitter_mux_synth.v

*            on the 2025-06-16 14:20:29.449336

*

***********************************************************************************************

*.GLOBAL n_vdd n_gnd

.SUBCKT bus_muxp_BUS_WIDTH1_BUS_CNT2 bus_all_bus0_ bus_all_bus1_ select_bus0_ bus_out_bus0_ n_vdd n_gnd

.ENDS
*.GLOBAL n_vdd n_gnd

.SUBCKT Transmitter dirReg_Q_bus-2_ dirReg_Q_bus-1_ dirReg_Q_bus0_ levelReg_Q_bus-2_ levelReg_Q_bus-1_ levelReg_Q_bus0_ captureReg_Q_bus0_ localIn_bus0_ txOut_bus0_ n_vdd n_gnd

XC94 1'b1 1'b1 txSelect n_vdd n_gnd nand2_decode

.ENDS Transmitter