import math

def gen_BoothR2Adder(spice_filename, circuit_name):
	spice_file = open(spice_filename,'a')
	spice_file.write('.SUBCKT BoothR2Adder op_bus0_ op_bus1_ x y cb_in out cb_out n_vdd n_gnd')
	spice_file.write(" \n")
	spice_file.write('XU29 n8 n9 n10 out n_vdd n_gnd nand3_decode')
	spice_file.write(" Wn=nand3_BoothR2Adder_nmos Wp=nand3_BoothR2Adder_pmos \n")
	spice_file.write('XU30 op_bus1_ y n7 n9 n_vdd n_gnd nand3_decode')
	spice_file.write(" Wn=nand3_BoothR2Adder_nmos Wp=nand3_BoothR2Adder_pmos \n")
	spice_file.write('XU31 x op_bus0_ n6 n10 n_vdd n_gnd nand3_decode')
	spice_file.write(" Wn=nand3_BoothR2Adder_nmos Wp=nand3_BoothR2Adder_pmos \n")
	spice_file.write('XU32 n18 n19 cb_out n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU33 cb_in y n5 n19 n_vdd n_gnd nand3_decode')
	spice_file.write(" Wn=nand3_BoothR2Adder_nmos Wp=nand3_BoothR2Adder_pmos \n")
	spice_file.write('XU34 n22 n23 n18 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU35 n24 n25 n23 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU36 n15 n2 n_vdd n_gnd inv')
	spice_file.write(" Wn=inv_BoothR2Adder_nmos Wp=inv_BoothR2Adder_pmos \n")
	spice_file.write('XU37 n16 n17 n15 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU38 op_bus1_ n7 n21 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU39 n13 n14 n11 n_vdd n_gnd nor2_decode')
	spice_file.write(" Wn=nor2_BoothR2Adder_nmos Wp=nor2_BoothR2Adder_pmos \n")
	spice_file.write('XU40 n14 n5 n_vdd n_gnd inv')
	spice_file.write(" Wn=inv_BoothR2Adder_nmos Wp=inv_BoothR2Adder_pmos \n")
	spice_file.write('XU41 n20 n21 n14 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU42 n11 n12 n8 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU43 x n6 n7 n24 n_vdd n_gnd nand3_decode')
	spice_file.write(" Wn=nand3_BoothR2Adder_nmos Wp=nand3_BoothR2Adder_pmos \n")
	spice_file.write('XU44 op_bus0_ n7 n_vdd n_gnd inv')
	spice_file.write(" Wn=inv_BoothR2Adder_nmos Wp=inv_BoothR2Adder_pmos \n")
	spice_file.write('XU45 op_bus0_ n6 n20 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU46 op_bus1_ n6 n_vdd n_gnd inv')
	spice_file.write(" Wn=inv_BoothR2Adder_nmos Wp=inv_BoothR2Adder_pmos \n")
	spice_file.write('XU47 cb_in n3 n16 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU48 y n3 n_vdd n_gnd inv')
	spice_file.write(" Wn=inv_BoothR2Adder_nmos Wp=inv_BoothR2Adder_pmos \n")
	spice_file.write('XU49 y n4 n17 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU50 n4 n3 n22 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU51 cb_in n4 n_vdd n_gnd inv')
	spice_file.write(" Wn=inv_BoothR2Adder_nmos Wp=inv_BoothR2Adder_pmos \n")
	spice_file.write('XU52 n1 n2 n13 n_vdd n_gnd nor2_decode')
	spice_file.write(" Wn=nor2_BoothR2Adder_nmos Wp=nor2_BoothR2Adder_pmos \n")
	spice_file.write('XU53 n1 n2 n12 n_vdd n_gnd nand2_decode')
	spice_file.write(" Wn=nand2_BoothR2Adder_nmos Wp=nand2_BoothR2Adder_pmos \n")
	spice_file.write('XU54 op_bus1_ op_bus0_ n1 n25 n_vdd n_gnd nand3_decode')
	spice_file.write(" Wn=nand3_BoothR2Adder_nmos Wp=nand3_BoothR2Adder_pmos \n")
	spice_file.write('XU55 x n1 n_vdd n_gnd inv')
	spice_file.write(" Wn=inv_BoothR2Adder_nmos Wp=inv_BoothR2Adder_pmos \n")
	spice_file.write('.ENDS BoothR2Adder')
	spice_file.write(" \n")
	#Now Append the List of Transistors
	tran_names_list=[]
	tran_names_list.append("nand3_BoothR2Adder_nmos")
	tran_names_list.append("nand3_BoothR2Adder_pmos")
	tran_names_list.append("nand2_BoothR2Adder_nmos")
	tran_names_list.append("nand2_BoothR2Adder_pmos")
	tran_names_list.append("inv_BoothR2Adder_nmos")
	tran_names_list.append("inv_BoothR2Adder_pmos")
	tran_names_list.append("nor2_BoothR2Adder_nmos")
	tran_names_list.append("nor2_BoothR2Adder_pmos")
	#Now Append the List of Wires
	wire_names_list=[]
	return tran_names_list, wire_names_list

#     # Open SPICE file for appending
#     spice_file = open(spice_filename, 'a')
#     # Generate SPICE subcircuits
#     spice_file.write("******************************************************************************************\n")
#     spice_file.write("* " + circuit_name + " Half Adder for CIM\n")
#     spice_file.write("******************************************************************************************\n")
#     spice_file.write(".SUBCKT " + circuit_name + " a b c_out gnd sum vdd\n")
#     Wnvar_name = "halfadder_nmos" #using all the same Wp and Wn on all transistors in this subcircuit
#     Wpvar_name = "halfadder_pmos"

#     filestring = '''
# m2 c_out net8 gnd gnd nmos L=gate_length W=WnVarVar AS=WnVar*trans_diffusion_length AD=WnVar*trans_diffusion_length PS=WnVar+2*trans_diffusion_length PD=WnVar+2*trans_diffusion_length
# m1 net8 a net21 gnd nmos L=gate_length W=WnVar AS=WnVar*trans_diffusion_length AD=WnVar*trans_diffusion_length PS=WnVar+2*trans_diffusion_length PD=WnVar+2*trans_diffusion_length
# m0 net21 b gnd gnd nmos L=gate_length W=WnVar AS=WnVar*trans_diffusion_length AD=WnVar*trans_diffusion_length PS=WnVar+2*trans_diffusion_length PD=WnVar+2*trans_diffusion_length
# m5 c_out net8 vdd vdd pmos L=gate_length W=WpVar AS=WpVar*trans_diffusion_length AD=WpVar*trans_diffusion_length PS=WpVar+2*trans_diffusion_length PD=WpVar+2*trans_diffusion_length
# m4 net8 b vdd vdd pmos L=gate_length W=WpVar AS=WpVar*trans_diffusion_length AD=WpVar*trans_diffusion_length PS=WpVar+2*trans_diffusion_length PD=WpVar+2*trans_diffusion_length
# m3 net8 a vdd vdd pmos L=gate_length W=WpVar AS=WpVar*trans_diffusion_length AD=WpVar*trans_diffusion_length PS=WpVar+2*trans_diffusion_length PD=WpVar+2*trans_diffusion_length
# xi22 a b gnd sum vdd XOR Wn=WnVar Wp=WpVar
# .ENDS


# '''
#     filestring = filestring.replace('WnVar', Wnvar_name)
#     filestring = filestring.replace('WpVar', Wpvar_name)
#     spice_file.write(filestring)
    
#     tran_names_list = []
#     tran_names_list.append(Wnvar_name)
#     tran_names_list.append(Wpvar_name)
    
#     wire_names_list = []
#     return tran_names_list, wire_names_list