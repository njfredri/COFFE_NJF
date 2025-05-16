.lib "../spice_models/ptm_22nm_bulk_hp.l" 22NM_BULK_HP .endl

.lib "basic_subcircuits.l" BASIC_SUBCIRCUITS .endl

.lib "minlib.sp" ADDITIONAL_LIB .endl

*

*  temp.sp : SPICE netlist translated from the VERILOG netlist : opmux_behav_subset_synth.v

*            on the 2025-04-09 12:58:25.730781

*

*********************************************************************************************

*.GLOBAL n_vdd n_gnd

.SUBCKT opmux_behav rf_portA_bus0_ rf_portA_bus1_ rf_portA_bus2_ rf_portA_bus3_ rf_portA_bus4_ rf_portA_bus5_ rf_portA_bus6_ rf_portA_bus7_ rf_portA_bus8_ rf_portA_bus9_ rf_portA_bus10_ rf_portA_bus11_ rf_portA_bus12_ rf_portA_bus13_ rf_portA_bus14_ rf_portA_bus15_ rf_portB_bus0_ rf_portB_bus1_ rf_portB_bus2_ rf_portB_bus3_ rf_portB_bus4_ rf_portB_bus5_ rf_portB_bus6_ rf_portB_bus7_ rf_portB_bus8_ rf_portB_bus9_ rf_portB_bus10_ rf_portB_bus11_ rf_portB_bus12_ rf_portB_bus13_ rf_portB_bus14_ rf_portB_bus15_ net_stream_bus0_ confSig_bus0_ confSig_bus1_ confSig_bus2_ opnX_bus0_ opnX_bus1_ opnX_bus2_ opnX_bus3_ opnX_bus4_ opnX_bus5_ opnX_bus6_ opnX_bus7_ opnX_bus8_ opnX_bus9_ opnX_bus10_ opnX_bus11_ opnX_bus12_ opnX_bus13_ opnX_bus14_ opnX_bus15_ opnY_bus0_ opnY_bus1_ opnY_bus2_ opnY_bus3_ opnY_bus4_ opnY_bus5_ opnY_bus6_ opnY_bus7_ opnY_bus8_ opnY_bus9_ opnY_bus10_ opnY_bus11_ opnY_bus12_ opnY_bus13_ opnY_bus14_ opnY_bus15_ clk confLoad n_vdd n_gnd

X\conf_reg_reg2 clk n92 n205 n117 n_vdd n_gnd dff

X\conf_reg_reg1 clk n91 n206 n116 n_vdd n_gnd dff

X\conf_reg_reg0 clk n90 n204 n118 n_vdd n_gnd dff

XU124 n196 n205 n183 n_vdd n_gnd nand2_decode

XU125 n179 n180 n120 n_vdd n_gnd nand2_decode

XU126 n119 opnY_bus9_ n_vdd n_gnd inv

XU127 rf_portB_bus9_ n120 n119 n_vdd n_gnd nand2_decode

XU128 n121 opnY_bus8_ n_vdd n_gnd inv

XU129 rf_portB_bus8_ n120 n121 n_vdd n_gnd nand2_decode

XU130 n122 n123 opnY_bus7_ n_vdd n_gnd nand2_decode

XU131 rf_portA_bus15_ n124 n123 n_vdd n_gnd nand2_decode

XU132 rf_portB_bus7_ n120 n122 n_vdd n_gnd nand2_decode

XU133 n125 n126 opnY_bus6_ n_vdd n_gnd nand2_decode

XU134 rf_portA_bus14_ n124 n126 n_vdd n_gnd nand2_decode

XU135 rf_portB_bus6_ n120 n125 n_vdd n_gnd nand2_decode

XU136 n127 n128 opnY_bus5_ n_vdd n_gnd nand2_decode

XU137 rf_portA_bus13_ n124 n128 n_vdd n_gnd nand2_decode

XU138 rf_portB_bus5_ n120 n127 n_vdd n_gnd nand2_decode

XU139 n129 n130 opnY_bus4_ n_vdd n_gnd nand2_decode

XU140 rf_portA_bus12_ n124 n130 n_vdd n_gnd nand2_decode

XU141 rf_portB_bus4_ n120 n129 n_vdd n_gnd nand2_decode

XU142 n131 n132 opnY_bus3_ n_vdd n_gnd nand2_decode

XU143 rf_portA_bus7_ n133 n132 n_vdd n_gnd nand2_decode

XU144 n134 n135 n131 n_vdd n_gnd nor2_decode

XU145 n136 n135 n_vdd n_gnd inv

XU146 rf_portB_bus3_ n120 n136 n_vdd n_gnd nand2_decode

XU147 n137 n138 n134 n_vdd n_gnd nor2_decode

XU148 n139 n140 opnY_bus2_ n_vdd n_gnd nand2_decode

XU149 rf_portA_bus6_ n133 n140 n_vdd n_gnd nand2_decode

XU150 n141 n142 n139 n_vdd n_gnd nor2_decode

XU151 n143 n142 n_vdd n_gnd inv

XU152 rf_portB_bus2_ n120 n143 n_vdd n_gnd nand2_decode

XU153 n137 n144 n141 n_vdd n_gnd nor2_decode

XU154 n145 opnY_bus1_ n_vdd n_gnd inv

XU155 n146 n147 n145 n_vdd n_gnd nor2_decode

XU156 n148 n149 n147 n_vdd n_gnd nand2_decode

XU157 rf_portB_bus1_ n120 n149 n_vdd n_gnd nand2_decode

XU158 rf_portA_bus5_ n133 n148 n_vdd n_gnd nand2_decode

XU159 n150 n133 n_vdd n_gnd inv

XU160 n151 n152 n146 n_vdd n_gnd nand2_decode

XU161 rf_portA_bus3_ n153 n152 n_vdd n_gnd nand2_decode

XU162 rf_portA_bus9_ n124 n151 n_vdd n_gnd nand2_decode

XU163 n137 n124 n_vdd n_gnd inv

XU164 n154 opnY_bus15_ n_vdd n_gnd inv

XU165 rf_portB_bus15_ n120 n154 n_vdd n_gnd nand2_decode

XU166 n155 opnY_bus14_ n_vdd n_gnd inv

XU167 rf_portB_bus14_ n120 n155 n_vdd n_gnd nand2_decode

XU168 n156 opnY_bus13_ n_vdd n_gnd inv

XU169 rf_portB_bus13_ n120 n156 n_vdd n_gnd nand2_decode

XU170 n157 opnY_bus12_ n_vdd n_gnd inv

XU171 rf_portB_bus12_ n120 n157 n_vdd n_gnd nand2_decode

XU172 n158 opnY_bus11_ n_vdd n_gnd inv

XU173 rf_portB_bus11_ n120 n158 n_vdd n_gnd nand2_decode

XU174 n159 opnY_bus10_ n_vdd n_gnd inv

XU175 rf_portB_bus10_ n120 n159 n_vdd n_gnd nand2_decode

XU176 n160 n161 opnY_bus0_ n_vdd n_gnd nand2_decode

XU177 n162 n163 n161 n_vdd n_gnd nor2_decode

XU178 n164 n165 n163 n_vdd n_gnd nand2_decode

XU179 n166 n167 n165 n_vdd n_gnd nand2_decode

XU180 n168 n169 n167 n_vdd n_gnd nor2_decode

XU181 rf_portA_bus1_ n204 n169 n_vdd n_gnd nor2_decode

XU182 net_stream_bus0_ n118 n168 n_vdd n_gnd nor2_decode

XU183 n206 n117 n166 n_vdd n_gnd nor2_decode

XU184 rf_portA_bus2_ n153 n164 n_vdd n_gnd nand2_decode

XU185 n170 n153 n_vdd n_gnd inv

XU186 n171 n204 n170 n_vdd n_gnd nand2_decode

XU187 n205 n116 n171 n_vdd n_gnd nor2_decode

XU188 n137 n172 n162 n_vdd n_gnd nor2_decode

XU189 n173 n204 n137 n_vdd n_gnd nand2_decode

XU190 n205 n206 n173 n_vdd n_gnd nor2_decode

XU191 n174 n175 n160 n_vdd n_gnd nor2_decode

XU192 n150 n176 n175 n_vdd n_gnd nor2_decode

XU193 n177 n206 n150 n_vdd n_gnd nand2_decode

XU194 n204 n205 n177 n_vdd n_gnd nor2_decode

XU195 n178 n174 n_vdd n_gnd inv

XU196 rf_portB_bus0_ n120 n178 n_vdd n_gnd nand2_decode

XU197 n181 n117 n180 n_vdd n_gnd nand2_decode

XU198 n204 n206 n181 n_vdd n_gnd nor2_decode

XU199 n205 n206 n179 n_vdd n_gnd nand2_decode

XU200 n182 opnX_bus9_ n_vdd n_gnd inv

XU201 n183 rf_portA_bus9_ n182 n_vdd n_gnd nand2_decode

XU202 n184 n172 opnX_bus8_ n_vdd n_gnd nor2_decode

XU203 rf_portA_bus8_ n172 n_vdd n_gnd inv

XU204 n185 opnX_bus7_ n_vdd n_gnd inv

XU205 n183 rf_portA_bus7_ n185 n_vdd n_gnd nand2_decode

XU206 n186 opnX_bus6_ n_vdd n_gnd inv

XU207 n183 rf_portA_bus6_ n186 n_vdd n_gnd nand2_decode

XU208 n187 opnX_bus5_ n_vdd n_gnd inv

XU209 n183 rf_portA_bus5_ n187 n_vdd n_gnd nand2_decode

XU210 n184 n176 opnX_bus4_ n_vdd n_gnd nor2_decode

XU211 rf_portA_bus4_ n176 n_vdd n_gnd inv

XU212 n188 opnX_bus3_ n_vdd n_gnd inv

XU213 n183 rf_portA_bus3_ n188 n_vdd n_gnd nand2_decode

XU214 n189 opnX_bus2_ n_vdd n_gnd inv

XU215 n183 rf_portA_bus2_ n189 n_vdd n_gnd nand2_decode

XU216 n190 opnX_bus1_ n_vdd n_gnd inv

XU217 n183 rf_portA_bus1_ n190 n_vdd n_gnd nand2_decode

XU218 n191 opnX_bus15_ n_vdd n_gnd inv

XU219 n183 rf_portA_bus15_ n191 n_vdd n_gnd nand2_decode

XU220 n192 opnX_bus14_ n_vdd n_gnd inv

XU221 n183 rf_portA_bus14_ n192 n_vdd n_gnd nand2_decode

XU222 n193 opnX_bus13_ n_vdd n_gnd inv

XU223 n183 rf_portA_bus13_ n193 n_vdd n_gnd nand2_decode

XU224 n194 opnX_bus12_ n_vdd n_gnd inv

XU225 n183 rf_portA_bus12_ n194 n_vdd n_gnd nand2_decode

XU226 n184 n138 opnX_bus11_ n_vdd n_gnd nor2_decode

XU227 rf_portA_bus11_ n138 n_vdd n_gnd inv

XU228 n184 n144 opnX_bus10_ n_vdd n_gnd nor2_decode

XU229 rf_portA_bus10_ n144 n_vdd n_gnd inv

XU230 n183 n184 n_vdd n_gnd inv

XU231 n195 opnX_bus0_ n_vdd n_gnd inv

XU232 rf_portA_bus0_ n183 n195 n_vdd n_gnd nand2_decode

XU233 n204 n116 n196 n_vdd n_gnd nor2_decode

XU234 n197 n198 n92 n_vdd n_gnd nand2_decode

XU235 n205 n199 n198 n_vdd n_gnd nand2_decode

XU236 confSig_bus2_ confLoad n197 n_vdd n_gnd nand2_decode

XU237 n200 n201 n91 n_vdd n_gnd nand2_decode

XU238 n206 n199 n201 n_vdd n_gnd nand2_decode

XU239 confSig_bus1_ confLoad n200 n_vdd n_gnd nand2_decode

XU240 n202 n203 n90 n_vdd n_gnd nand2_decode

XU241 n204 n199 n203 n_vdd n_gnd nand2_decode

XU242 confLoad n199 n_vdd n_gnd inv

XU243 confSig_bus0_ confLoad n202 n_vdd n_gnd nand2_decode

.ENDS opmux_behav