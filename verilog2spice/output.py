def gen_bus_muxp_BUS_WIDTH1_BUS_CNT2(spice_filename, circuit_name, numberofsrams):
	spice_file = open(spice_filename,'a')
	spice_file.write('.SUBCKT bus_muxp_BUS_WIDTH1_BUS_CNT2 bus_all_bus0_ bus_all_bus1_ select_bus0_ bus_out_bus0_ n_vdd n_gnd')
	spice_file.write("\n")
def gen_Transmitter(spice_filename, circuit_name, numberofsrams):
	spice_file = open(spice_filename,'a')
	spice_file.write('.SUBCKT Transmitter dirReg_Q_bus-2_ dirReg_Q_bus-1_ dirReg_Q_bus0_ levelReg_Q_bus-2_ levelReg_Q_bus-1_ levelReg_Q_bus0_ captureReg_Q_bus0_ localIn_bus0_ txOut_bus0_ n_vdd n_gnd')
	spice_file.write("\n")
	spice_file.write('XC94 1'b1 1'b1 txSelect n_vdd n_gnd nand2_decode')
	spice_file.write("Wn=45n Wp=55n \n")
	spice_file.write('.ENDS Transmitter')
	spice_file.write("\n")
	#Now Append the List of Transistors
	tran_names_list=[]
	#Now Append the List of Wires
	wire_names_list=[]
	return tran_names_list, wire_names_list