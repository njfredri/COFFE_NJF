import math

def generate_alu_half_adder(spice_filename, circuit_name, nandtype):
    # Open SPICE file for appending
    spice_file = open(spice_filename, 'a')
    # Generate SPICE subcircuits
    spice_file.write("******************************************************************************************\n")
    spice_file.write("* " + circuit_name + " Half Adder for CIM\n")
    spice_file.write("******************************************************************************************\n")
    spice_file.write(".SUBCKT " + circuit_name + " a b c_out gnd sum vdd\n")
    Wnvar_name = "halfadder_nmos" #using all the same Wp and Wn on all transistors in this subcircuit
    Wpvar_name = "halfadder_pmos"

    filestring = '''
m2 c_out net8 gnd gnd nmos L=gate_length W=WnVarVar AS=WnVar*trans_diffusion_length AD=WnVar*trans_diffusion_length PS=WnVar+2*trans_diffusion_length PD=WnVar+2*trans_diffusion_length
m1 net8 a net21 gnd nmos L=gate_length W=WnVar AS=WnVar*trans_diffusion_length AD=WnVar*trans_diffusion_length PS=WnVar+2*trans_diffusion_length PD=WnVar+2*trans_diffusion_length
m0 net21 b gnd gnd nmos L=gate_length W=WnVar AS=WnVar*trans_diffusion_length AD=WnVar*trans_diffusion_length PS=WnVar+2*trans_diffusion_length PD=WnVar+2*trans_diffusion_length
m5 c_out net8 vdd vdd pmos L=gate_length W=WpVar AS=WpVar*trans_diffusion_length AD=WpVar*trans_diffusion_length PS=WpVar+2*trans_diffusion_length PD=WpVar+2*trans_diffusion_length
m4 net8 b vdd vdd pmos L=gate_length W=WpVar AS=WpVar*trans_diffusion_length AD=WpVar*trans_diffusion_length PS=WpVar+2*trans_diffusion_length PD=WpVar+2*trans_diffusion_length
m3 net8 a vdd vdd pmos L=gate_length W=WpVar AS=WpVar*trans_diffusion_length AD=WpVar*trans_diffusion_length PS=WpVar+2*trans_diffusion_length PD=WpVar+2*trans_diffusion_length
xi22 a b gnd sum vdd XOR Wn=WnVar Wp=WpVar
.ENDS


'''
    filestring = filestring.replace('WnVar', Wnvar_name)
    filestring = filestring.replace('WpVar', Wpvar_name)
    spice_file.write(filestring)
    
    tran_names_list = []
    tran_names_list.append(Wnvar_name)
    tran_names_list.append(Wpvar_name)
    
    wire_names_list = []
    return tran_names_list, wire_names_list