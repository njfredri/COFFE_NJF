def inverter_generate(filename, use_finfet):
	""" Generates the SPICE subcircuit for an inverter. Appends it to file 'filename'. """

	# Open the file for appending
	spice_file = open(filename, 'a')  

	if not use_finfet :
		spice_file.write("******************************************************************************************\n")
		spice_file.write("* Inverter\n")
		spice_file.write("******************************************************************************************\n")
		spice_file.write(".SUBCKT inv n_in n_out n_vdd n_gnd Wn=45n Wp=45n\n")
		spice_file.write("MNDOWN n_out n_in n_gnd n_gnd nmos L=gate_length W=Wn ")
		spice_file.write("As=Wn*trans_diffusion_length Ad=Wn*trans_diffusion_length Ps=Wn+2*trans_diffusion_length Pd=Wn+2*trans_diffusion_length\n")
		spice_file.write("MPUP n_out n_in n_vdd n_vdd pmos L=gate_length W=Wp ")
		spice_file.write("As=Wp*trans_diffusion_length Ad=Wp*trans_diffusion_length Ps=Wp+2*trans_diffusion_length Pd=Wp+2*trans_diffusion_length\n")
		spice_file.write(".ENDS\n\n\n")
	else :
		spice_file.write("******************************************************************************************\n")
		spice_file.write("* Inverter\n")
		spice_file.write("******************************************************************************************\n")
		spice_file.write(".SUBCKT inv n_in n_out n_vdd n_gnd Wn=1 Wp=1\n")
		spice_file.write("MNDOWN n_out n_in n_gnd n_gnd nmos L=gate_length nfin=Wn ")
		spice_file.write("As=Wn*trans_diffusion_length*min_tran_width Ad=Wn*trans_diffusion_length*min_tran_width Ps=Wn+2*trans_diffusion_length*min_tran_width Pd=Wn+2*trans_diffusion_length*min_tran_width\n")
		spice_file.write("MPUP n_out n_in n_vdd n_vdd pmos L=gate_length nfin=Wp ")
		spice_file.write("As=Wp*trans_diffusion_length*min_tran_width Ad=Wp*trans_diffusion_length*min_tran_width Ps=Wp+2*trans_diffusion_length*min_tran_width Pd=Wp+2*trans_diffusion_length*min_tran_width\n")
		spice_file.write(".ENDS\n\n\n")

	spice_file.close()
	
	
def rest_generate(filename, use_finfet):
	""" Generates the SPICE subcircuit for a level-restorer. Appends it to file 'filename'. """

	# Open the file for appending
	spice_file = open(filename, 'a')  

	if not use_finfet :
		spice_file.write("******************************************************************************************\n")
		spice_file.write("* Level-restorer PMOS\n")
		spice_file.write("******************************************************************************************\n")
		spice_file.write(".SUBCKT rest n_pull n_gate n_vdd n_gnd Wp=45n\n")
		spice_file.write("MPREST n_pull n_gate n_vdd n_vdd pmos L=gate_length W=Wp ")
		spice_file.write("As=Wp*trans_diffusion_length Ad=Wp*trans_diffusion_length Ps=Wp+2*trans_diffusion_length Pd=Wp+2*trans_diffusion_length\n")
		spice_file.write(".ENDS\n\n\n")
	else :
		spice_file.write("******************************************************************************************\n")
		spice_file.write("* Level-restorer PMOS\n")
		spice_file.write("******************************************************************************************\n")
		spice_file.write(".SUBCKT rest n_pull n_gate n_vdd n_gnd Wp=1 \n")
		spice_file.write("MPREST n_pull n_gate n_vdd n_vdd pmos L=gate_length*rest_length_factor nfin=Wp ")
		spice_file.write("As=Wp*trans_diffusion_length*min_tran_width Ad=Wp*trans_diffusion_length*min_tran_width Ps=Wp+2*trans_diffusion_length*min_tran_width Pd=Wp+2*trans_diffusion_length*min_tran_width\n")
		spice_file.write(".ENDS\n\n\n")   
		
	spice_file.close()
	
	
def wire_generate(filename):
	""" Generates the SPICE subcircuit for a wire. Appends it to file 'filename'. """

	# Open the file for appending
	spice_file = open(filename, 'a')  
	spice_file.write("******************************************************************************************\n")
	spice_file.write("* Interconnect wire\n")
	spice_file.write("******************************************************************************************\n")
	spice_file.write(".SUBCKT wire n_in n_out Rw=1 Cw=1\n")
	spice_file.write("CWIRE_1 n_in gnd Cw\n")
	spice_file.write("RWIRE_1 n_in n_out Rw\n")
	spice_file.write("CWIRE_2 n_out gnd Cw\n")
	spice_file.write(".ENDS\n\n\n")   
	spice_file.close()
	
	
def ptran_generate(filename, use_finfet):
	""" Generates the SPICE subcircuit for a pass-transistor. Appends it to file 'filename'. """

	# Open the file for appending
	spice_file = open(filename, 'a')  

	if not use_finfet :
		spice_file.write("******************************************************************************************\n")
		spice_file.write("* Pass-transistor\n")
		spice_file.write("******************************************************************************************\n")
		spice_file.write(".SUBCKT ptran n_in n_out n_gate n_gnd Wn=45n\n")
		spice_file.write("MNPASS n_in n_gate n_out n_gnd nmos L=gate_length W=Wn ")
		spice_file.write("As=Wn*trans_diffusion_length Ad=Wn*trans_diffusion_length Ps=Wn+2*trans_diffusion_length Pd=Wn+2*trans_diffusion_length\n")
		spice_file.write(".ENDS\n\n\n")   
	else :
		spice_file.write("******************************************************************************************\n")
		spice_file.write("* Pass-transistor\n")
		spice_file.write("******************************************************************************************\n")
		spice_file.write(".SUBCKT ptran n_in n_out n_gate n_gnd Wn=1\n")
		spice_file.write("MNPASS n_in n_gate n_out n_gnd nmos L=gate_length nfin=Wn ")
		spice_file.write("As=Wn*trans_diffusion_length*min_tran_width Ad=Wn*trans_diffusion_length*min_tran_width Ps=Wn+2*trans_diffusion_length*min_tran_width Pd=Wn+2*trans_diffusion_length*min_tran_width \n")
		spice_file.write(".ENDS\n\n\n")   

	spice_file.close()
	
	
def tgate_generate(filename, use_finfet):
	""" Generates the SPICE subcircuit for a transmission gate. Appends it to file 'filename'. """

	# Open the file for appending
	spice_file = open(filename, 'a')  

	if not use_finfet :
		spice_file.write("******************************************************************************************\n")
		spice_file.write("* Transmission gate\n")
		spice_file.write("******************************************************************************************\n")
		spice_file.write(".SUBCKT tgate n_in n_out n_gate_nmos n_gate_pmos n_vdd n_gnd Wn=45n Wp=45n\n")
		spice_file.write("MNTGATE n_in n_gate_nmos n_out n_gnd nmos L=gate_length W=Wn ")
		spice_file.write("As=Wn*trans_diffusion_length Ad=Wn*trans_diffusion_length Ps=Wn+2*trans_diffusion_length Pd=Wn+2*trans_diffusion_length\n")
		spice_file.write("MPTGATE n_in n_gate_pmos n_out n_vdd pmos L=gate_length W=Wp ")
		spice_file.write("As=Wp*trans_diffusion_length Ad=Wp*trans_diffusion_length Ps=Wp+2*trans_diffusion_length Pd=Wp+2*trans_diffusion_length\n")
		spice_file.write(".ENDS\n\n\n")   
	else :
		spice_file.write("******************************************************************************************\n")
		spice_file.write("* Transmission gate\n")
		spice_file.write("******************************************************************************************\n")
		spice_file.write(".SUBCKT tgate n_in n_out n_gate_nmos n_gate_pmos n_vdd n_gnd Wn=1 Wp=1\n")
		spice_file.write("MNTGATE n_in n_gate_nmos n_out n_gnd nmos L=gate_length nfin=Wn ")
		spice_file.write("As=Wn*trans_diffusion_length*min_tran_width Ad=Wn*trans_diffusion_length*min_tran_width Ps=Wn+2*trans_diffusion_length*min_tran_width Pd=Wn+2*trans_diffusion_length*min_tran_width\n")
		spice_file.write("MPTGATE n_in n_gate_pmos n_out n_vdd pmos L=gate_length nfin=Wp ")
		spice_file.write("As=Wp*trans_diffusion_length*min_tran_width Ad=Wp*trans_diffusion_length*min_tran_width Ps=Wp+2*trans_diffusion_length*min_tran_width Pd=Wp+2*trans_diffusion_length*min_tran_width\n")
		spice_file.write(".ENDS\n\n\n")

	spice_file.close()