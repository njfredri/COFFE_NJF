*** BASIC SUBCIRCUITS
.INCLUDE "../spice_models/ptm_22nm_bulk_hp.l"
.LIB BASIC_SUBCIRCUITS
.param gate_length=22n
.param trans_diffusion_length=52.0n
******************************************************************************************
* Interconnect wire
******************************************************************************************
.SUBCKT wire n_in n_out Rw=1 Cw=1
CWIRE_1 n_in gnd Cw
RWIRE_1 n_in n_out Rw
CWIRE_2 n_out gnd Cw
.ENDS


******************************************************************************************
* Pass-transistor
******************************************************************************************
.SUBCKT ptran n_in n_out n_gate n_gnd Wn=45n 
MNPASS n_in n_gate n_out n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
.ENDS


******************************************************************************************
* PMOS Pass-transistor
******************************************************************************************
.SUBCKT ptranp n_in n_out n_gate n_vdd Wn=45n 
MPPASS n_in n_gate n_out n_vdd pmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
.ENDS


******************************************************************************************
* Transmission gate
******************************************************************************************
.SUBCKT tgate n_in n_out n_gate_nmos n_gate_pmos n_vdd n_gnd Wn=45n Wp=45n
MNTGATE n_in n_gate_nmos n_out n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPTGATE n_in n_gate_pmos n_out n_vdd pmos L=gate_length W=Wp AS=Wp*trans_diffusion_length AD=Wp*trans_diffusion_length PS=Wp+2*trans_diffusion_length PD=Wp+2*trans_diffusion_length
.ENDS


******************************************************************************************
* Transmission gate
******************************************************************************************
.SUBCKT tgate_lp n_in n_out n_gate_nmos n_gate_pmos n_vdd n_gnd Wn=45n Wp=45n
MNTGATE n_in n_gate_nmos n_out n_gnd nmos_lp L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPTGATE n_in n_gate_pmos n_out n_vdd pmos_lp L=gate_length W=Wp AS=Wp*trans_diffusion_length AD=Wp*trans_diffusion_length PS=Wp+2*trans_diffusion_length PD=Wp+2*trans_diffusion_length
.ENDS


******************************************************************************************
* Level-restorer PMOS
******************************************************************************************
.SUBCKT rest n_pull n_gate n_vdd n_gnd Wp=45n
MPREST n_pull n_gate n_vdd n_vdd pmos L=gate_length*rest_length_factor W=Wp AS=Wp*trans_diffusion_length AD=Wp*trans_diffusion_length PS=Wp+2*trans_diffusion_length PD=Wp+2*trans_diffusion_length
.ENDS


******************************************************************************************
* Inverter
******************************************************************************************
.SUBCKT inv n_in n_out n_vdd n_gnd Wn=45n Wp=45n
MNDOWN n_out n_in n_gnd n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP n_out n_in n_vdd n_vdd pmos L=gate_length W=Wp AS=Wp*trans_diffusion_length AD=Wp*trans_diffusion_length PS=Wp+2*trans_diffusion_length PD=Wp+2*trans_diffusion_length
.ENDS


******************************************************************************************
* Low Power Inverter
******************************************************************************************
.SUBCKT inv_lp n_in n_out n_vdd n_gnd Wn=45n Wp=45n
MNDOWN n_out n_in n_gnd n_gnd nmos_lp L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP n_out n_in n_vdd n_vdd pmos_lp L=gate_length W=Wp AS=Wp*trans_diffusion_length AD=Wp*trans_diffusion_length PS=Wp+2*trans_diffusion_length PD=Wp+2*trans_diffusion_length
.ENDS


******************************************************************************************
* nand2
******************************************************************************************
.SUBCKT nand2 n_in n_out n_vdd n_gnd Wn=45n Wp=45n
MNDOWN2 n_out n_vdd n_z n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MNDOWN1 n_z n_in n_gnd n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP1 n_out n_vdd n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP2 n_out n_in n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
.ENDS


******************************************************************************************
* nand2 decoder
******************************************************************************************
.SUBCKT nand2_decode n_in1 n_in2 n_out n_vdd n_gnd Wn=45n Wp=45n
MNDOWN2 n_out n_in1 n_z n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MNDOWN1 n_z n_in2 n_gnd n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP1 n_out n_in1 n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP2 n_out n_in2 n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
.ENDS


******************************************************************************************
* nor2 decoder
******************************************************************************************
.SUBCKT nor2_decode n_in1 n_in2 n_out n_vdd n_gnd Wn=45n Wp=45n
MNDOWN2 n_out n_in1 n_gnd n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MNDOWN1 n_out n_in2 n_gnd n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP1 n_out n_in1 n_z n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP2 n_z n_in2 n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
.ENDS


******************************************************************************************
* nand2
******************************************************************************************
.SUBCKT nand2_lp n_in n_out n_vdd n_gnd Wn=45n Wp=45n
MNDOWN2 n_out n_vdd n_z n_gnd nmos_lp L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MNDOWN1 n_z n_in n_gnd n_gnd nmos_lp L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP1 n_out n_vdd n_vdd n_vdd pmos_lp L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP2 n_out n_in n_vdd n_vdd pmos_lp L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
.ENDS


******************************************************************************************
* nand3
******************************************************************************************
.SUBCKT nand3 n_in n_out n_vdd n_gnd Wn=45n Wp=45n
MNDOWN2 n_out n_vdd n_z n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MNDOWN1 n_z n_vdd n_z2 n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MNDOWN0 n_z2 n_in n_gnd n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP0 n_out n_vdd n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP1 n_out n_vdd n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP2 n_out n_in n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
.ENDS


******************************************************************************************
* nand3 decoder
******************************************************************************************
.SUBCKT nand3_decode n_in1 n_in2 n_in3 n_out n_vdd n_gnd Wn=45n Wp=45n
MNDOWN3 n_out n_in1 n_z n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MNDOWN2 n_z n_in2 n_y n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MNDOWN1 n_y n_in3 n_gnd n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP1 n_out n_in1 n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP2 n_out n_in2 n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP3 n_out n_in3 n_vdd n_vdd pmos L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
.ENDS


******************************************************************************************
* nand3
******************************************************************************************
.SUBCKT nand3_lp n_in n_out n_vdd n_gnd Wn=45n Wp=45n
MNDOWN2 n_out n_vdd n_z n_gnd nmos_lp L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MNDOWN1 n_z n_vdd n_z2 n_gnd nmos_lp L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MNDOWN0 n_z2 n_in n_gnd n_gnd nmos_lp L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP0 n_out n_vdd n_vdd n_vdd pmos_lp L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP1 n_out n_vdd n_vdd n_vdd pmos_lp L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPUP2 n_out n_in n_vdd n_vdd pmos_lp L=gate_length W=Wp AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
.ENDS


******************************************************************************************
* Transmission gate
******************************************************************************************
.SUBCKT RAM_tgate n_in n_out n_gate_nmos n_gate_pmos n_vdd n_gnd Wn=200n Wp=250n
MNTGATE n_in n_gate_nmos n_out n_gnd nmos L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPTGATE n_in n_gate_pmos n_out n_vdd pmos L=gate_length W=Wp AS=Wp*trans_diffusion_length AD=Wp*trans_diffusion_length PS=Wp+2*trans_diffusion_length PD=Wp+2*trans_diffusion_length
.ENDS


******************************************************************************************
* Transmission gate
******************************************************************************************
.SUBCKT RAM_tgate_lp n_in n_out n_gate_nmos n_gate_pmos n_vdd n_gnd Wn=200n Wp=250n
MNTGATE n_in n_gate_nmos n_out n_gnd nmos_lp L=gate_length W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length
MPTGATE n_in n_gate_pmos n_out n_vdd pmos_lp L=gate_length W=Wp AS=Wp*trans_diffusion_length AD=Wp*trans_diffusion_length PS=Wp+2*trans_diffusion_length PD=Wp+2*trans_diffusion_length
.ENDS

**** dff ****
.SUBCKT dff clk d q qn vdd vss

* First stage: Generate a delayed version of the clock (clk_delayed)
Xinv1 clk clk_n vdd vss inv    * Inverter to delay the clock

* Second stage: Master latch (controlled by clk)
* Use NAND gates to create the master latch behavior (latches on the high clock)
Xnand1 clk d net1 vdd vss nand2_decode   * NAND gate for input D with clk
Xnand2 clk net1 n1 vdd vss nand2_decode  * NAND gate for feedback to the master latch
Xnor1 net1 n1 q vdd vss nor2_decode     * NOR gate for output Q
Xnor2 n1 net1 qn vdd vss nor2_decode    * NOR gate for output Qn

* Third stage: Slave latch (controlled by the inverted clock)
Xnand3 clk_n d net2 vdd vss nand2_decode   * NAND gate for input D with inverted clk
Xnand4 clk_n net2 n2 vdd vss nand2_decode  * NAND gate for feedback to the slave latch
Xnor3 net2 n2 q vdd vss nor2_decode       * NOR gate for output Q
Xnor4 n2 net2 qn vdd vss nor2_decode      * NOR gate for output Qn

.ends



**** dff_no_q ****
.SUBCKT dff_no_q clk d qn vdd vss

* First stage: Generate a delayed version of the clock (clk_delayed)
Xinv1 clk clk_n vdd vss inv    * Inverter to delay the clock

* Second stage: Master latch (controlled by clk)
Xnand1 clk d net1 vdd vss nand2_decode
Xnand2 clk net1 n1 vdd vss nand2_decode
* Removed Xnor1 which drives q
Xnor2 n1 net1 qn vdd vss nor2_decode    * NOR gate for output Qn

* Third stage: Slave latch (controlled by the inverted clock)
Xnand3 clk_n d net2 vdd vss nand2_decode
Xnand4 clk_n net2 n2 vdd vss nand2_decode
* Removed Xnor3 which drives q
Xnor4 n2 net2 qn vdd vss nor2_decode

.ends



**** boothR2_serial_alu ****
.SUBCKT boothR2_serial_alu op_bus0_ op_bus1_ clk x y ce reset out n_vdd n_gnd

Xdff1 clk n36 0 n71 n_vdd n_gnd dff

Xnand1 n37 n38 out n_vdd n_gnd nand2_decode

Xnand2 n39 n40 n38 n_vdd n_gnd nand2_decode

Xnor1 n41 n42 n40 n_vdd n_gnd nor2_decode

Xnor2 n71 n43 n42 n_vdd n_gnd nor2_decode

Xinv1 n44 n41 n_vdd n_gnd inv

Xnand3 n43 n71 n44 n_vdd n_gnd nand2_decode

Xinv2 n45 n43 n_vdd n_gnd inv

Xnand4 n46 n47 n45 n_vdd n_gnd nand2_decode

Xnand5 y n48 n47 n_vdd n_gnd nand2_decode

Xnand6 x n49 n46 n_vdd n_gnd nand2_decode

Xinv3 y n49 n_vdd n_gnd inv

Xnor3 n50 n51 n37 n_vdd n_gnd nor2_decode

Xnor4 n52 n53 n51 n_vdd n_gnd nor2_decode

Xnand7 x n54 n53 n_vdd n_gnd nand2_decode

Xnor5 op_bus0_ n55 n50 n_vdd n_gnd nor2_decode

Xnand8 op_bus1_ y n55 n_vdd n_gnd nand2_decode

Xnor6 reset n56 n36 n_vdd n_gnd nor2_decode

Xnor7 n57 n58 n56 n_vdd n_gnd nor2_decode

Xnor8 n71 n59 n58 n_vdd n_gnd nor2_decode

Xnor9 n60 n61 n59 n_vdd n_gnd nor2_decode

Xnand9 ce n62 n61 n_vdd n_gnd nand2_decode

Xnand10 n39 y n62 n_vdd n_gnd nand2_decode

Xnor10 n63 n64 n39 n_vdd n_gnd nor2_decode

Xnor11 op_bus1_ n52 n64 n_vdd n_gnd nor2_decode

Xnor12 op_bus0_ n54 n63 n_vdd n_gnd nor2_decode

Xnor13 n65 n66 n57 n_vdd n_gnd nor2_decode

Xnand11 y n60 n66 n_vdd n_gnd nand2_decode

Xnand12 n67 n68 n60 n_vdd n_gnd nand2_decode

Xnand13 n69 n54 n68 n_vdd n_gnd nand2_decode

Xinv4 op_bus1_ n54 n_vdd n_gnd inv

Xnor14 op_bus0_ n48 n69 n_vdd n_gnd nor2_decode

Xinv5 x n48 n_vdd n_gnd inv

Xnand14 n70 op_bus1_ n67 n_vdd n_gnd nand2_decode

Xnor15 x n52 n70 n_vdd n_gnd nor2_decode

Xinv6 op_bus0_ n52 n_vdd n_gnd inv

Xinv7 ce n65 n_vdd n_gnd inv



.ends

.ENDL BASIC_SUBCIRCUITS