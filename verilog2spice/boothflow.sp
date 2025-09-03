.lib "../spice_models/ptm_22nm_bulk_hp.l" 22NM_BULK_HP .endl

.lib "basic_subcircuits.l" BASIC_SUBCIRCUITS .endl

.lib "minlib.sp" ADDITIONAL_LIB .endl

*

*  temp.sp : SPICE netlist translated from the VERILOG netlist : boothR2_serial_alu_synth.v

*            on the 2025-06-16 13:30:38.906205

*

*********************************************************************************************

*.GLOBAL n_vdd n_gnd

.SUBCKT boothR2_serial_alu_flow op_bus0_ op_bus1_ clk x y ce reset out n_vdd n_gnd

Xcb_reg_reg clk n35 n71 n36 n_vdd n_gnd dff

XU37 n37 n38 out n_vdd n_gnd nand2_decode

XU38 n39 n40 n38 n_vdd n_gnd nand2_decode

XU39 n41 n42 n40 n_vdd n_gnd nand2_decode

XU40 n43 n71 n42 n_vdd n_gnd nand2_decode

XU41 n44 n43 n_vdd n_gnd inv

XU42 n44 n36 n41 n_vdd n_gnd nand2_decode

XU43 n45 n46 n44 n_vdd n_gnd nand2_decode

XU44 y n47 n46 n_vdd n_gnd nand2_decode

XU45 x n48 n45 n_vdd n_gnd nand2_decode

XU46 y n48 n_vdd n_gnd inv

XU47 n49 n50 n37 n_vdd n_gnd nor2_decode

XU48 n51 n52 n50 n_vdd n_gnd nor2_decode

XU49 x n53 n52 n_vdd n_gnd nand2_decode

XU50 op_bus0_ n54 n49 n_vdd n_gnd nor2_decode

XU51 y op_bus1_ n54 n_vdd n_gnd nand2_decode

XU52 reset n55 n35 n_vdd n_gnd nor2_decode

XU53 n56 n57 n55 n_vdd n_gnd nor2_decode

XU54 n58 n36 n57 n_vdd n_gnd nor2_decode

XU55 n59 n60 n58 n_vdd n_gnd nor2_decode

XU56 ce n61 n60 n_vdd n_gnd nand2_decode

XU57 n39 y n61 n_vdd n_gnd nand2_decode

XU58 n62 n39 n_vdd n_gnd inv

XU59 n63 n64 n62 n_vdd n_gnd nand2_decode

XU60 op_bus1_ n51 n64 n_vdd n_gnd nand2_decode

XU61 op_bus0_ n53 n63 n_vdd n_gnd nand2_decode

XU62 n65 n66 n56 n_vdd n_gnd nor2_decode

XU63 y n59 n66 n_vdd n_gnd nand2_decode

XU64 n67 n68 n59 n_vdd n_gnd nand2_decode

XU65 n69 n53 n68 n_vdd n_gnd nand2_decode

XU66 op_bus1_ n53 n_vdd n_gnd inv

XU67 op_bus0_ n47 n69 n_vdd n_gnd nor2_decode

XU68 x n47 n_vdd n_gnd inv

XU69 n70 op_bus1_ n67 n_vdd n_gnd nand2_decode

XU70 x n51 n70 n_vdd n_gnd nor2_decode

XU71 op_bus0_ n51 n_vdd n_gnd inv

XU72 ce n65 n_vdd n_gnd inv

.ENDS boothR2_serial_alu_flow