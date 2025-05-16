* HSPICE Testbench for boothR2_serial_alu
.include "boothR2.sp"


* Power Supply 
VDD VDD 0 0.8V
VSS VSS 0 0V

* Instantiate the DUT
X1 op_bus0_ op_bus1_ clk x y ce reset out VDD VSS boothR2_serial_alu
* Input stimuli for clk using Piecewise Linear Voltage (PWL)
V1 clk 0 PWL(0ns 0V 
+ 4.9ns 0V 5ns 0.8VV 
+ 9.9ns 0.8VV 10ns 0V 
+ 14.9ns 0V 15ns 0.8VV 
+ 19.9ns 0.8VV 20ns 0V 
+ 24.9ns 0V 25ns 0.8VV 
+ 29.9ns 0.8VV 30ns 0V 
+ 34.9ns 0V 35ns 0.8VV 
+ 39.9ns 0.8VV 40ns 0V 
+ 44.9ns 0V 45ns 0.8VV 
+ 49.9ns 0.8VV 50ns 0V 
+ 54.9ns 0V 55ns 0.8VV 
+ 59.9ns 0.8VV 60ns 0V 
+ 64.9ns 0V 65ns 0.8VV 
+ 69.9ns 0.8VV 70ns 0V 
+ 74.9ns 0V 75ns 0.8VV 
+ 79.9ns 0.8VV 80ns 0V 
+ 84.9ns 0V 85ns 0.8VV 
+ 89.9ns 0.8VV 90ns 0V 
+ 94.9ns 0V 95ns 0.8VV 
+ 99.9ns 0.8VV 100ns 0V 
+ 104.9ns 0V 105ns 0.8VV 
+ 109.9ns 0.8VV 110ns 0V 
+ 114.9ns 0V 115ns 0.8VV 
+ 119.9ns 0.8VV 120ns 0V 
+ 124.9ns 0V 125ns 0.8VV 
+ 129.9ns 0.8VV 130ns 0V 
+ 134.9ns 0V 135ns 0.8VV 
+ 139.9ns 0.8VV 140ns 0V 
+ 144.9ns 0V 145ns 0.8VV 
+ 149.9ns 0.8VV 150ns 0V 
+ 154.9ns 0V 155ns 0.8VV 
+ 159.9ns 0.8VV 160ns 0V 
+ 164.9ns 0V 165ns 0.8VV 
+ 169.9ns 0.8VV 170ns 0V 
+ 174.9ns 0V 175ns 0.8VV 
+ 179.9ns 0.8VV 180ns 0V 
+ 184.9ns 0V 185ns 0.8VV 
+ 189.9ns 0.8VV 190ns 0V 
+ 194.9ns 0V 195ns 0.8VV 
+ 199.9ns 0.8VV 200ns 0V 
+ 204.9ns 0V 205ns 0.8VV 
+ 209.9ns 0.8VV 210ns 0V 
+ 214.9ns 0V 215ns 0.8VV 
+ 219.9ns 0.8VV 220ns 0V 
+ 224.9ns 0V 225ns 0.8VV 
+ 229.9ns 0.8VV 230ns 0V 
+ 234.9ns 0V 235ns 0.8VV 
+ 239.9ns 0.8VV 240ns 0V 
+ 244.9ns 0V 245ns 0.8VV 
+ 249.9ns 0.8VV 250ns 0V 
+ 254.9ns 0V 255ns 0.8VV 
+ 259.9ns 0.8VV 260ns 0V 
+ 264.9ns 0V 265ns 0.8VV 
+ 269.9ns 0.8VV 270ns 0V 
+ 274.9ns 0V 275ns 0.8VV 
+ 279.9ns 0.8VV 280ns 0V 
+ 284.9ns 0V 285ns 0.8VV 
+ 289.9ns 0.8VV 290ns 0V 
+ 294.9ns 0V 295ns 0.8VV 
+ 299.9ns 0.8VV 300ns 0V 
+ 304.9ns 0V 305ns 0.8VV 
+ 309.9ns 0.8VV 310ns 0V 
+ 314.9ns 0V 315ns 0.8VV 
+ 319.9ns 0.8VV 320ns 0V 
+ 324.9ns 0V 325ns 0.8VV 
+ 329.9ns 0.8VV 330ns 0V )
* Input stimuli for x using Piecewise Linear Voltage (PWL)
V2 x 0 PWL(0ns 0V 
+ 5ns 0V 
+ 10ns 0V 
+ 15ns 0V 
+ 20ns 0V 
+ 25ns 0V 
+ 30ns 0V 
+ 35ns 0V 
+ 40ns 0V 
+ 45ns 0V 
+ 49.9ns 0V 50ns 0.8VV 
+ 55ns 0.8VV 
+ 60ns 0.8VV 
+ 65ns 0.8VV 
+ 70ns 0.8VV 
+ 75ns 0.8VV 
+ 80ns 0.8VV 
+ 85ns 0.8VV 
+ 89.9ns 0.8VV 90ns 0V 
+ 95ns 0V 
+ 100ns 0V 
+ 105ns 0V 
+ 110ns 0V 
+ 115ns 0V 
+ 120ns 0V 
+ 125ns 0V 
+ 129.9ns 0V 130ns 0.8VV 
+ 135ns 0.8VV 
+ 140ns 0.8VV 
+ 145ns 0.8VV 
+ 150ns 0.8VV 
+ 155ns 0.8VV 
+ 160ns 0.8VV 
+ 165ns 0.8VV 
+ 169.9ns 0.8VV 170ns 0V 
+ 175ns 0V 
+ 180ns 0V 
+ 185ns 0V 
+ 190ns 0V 
+ 195ns 0V 
+ 200ns 0V 
+ 205ns 0V 
+ 209.9ns 0V 210ns 0.8VV 
+ 215ns 0.8VV 
+ 220ns 0.8VV 
+ 225ns 0.8VV 
+ 230ns 0.8VV 
+ 235ns 0.8VV 
+ 240ns 0.8VV 
+ 245ns 0.8VV 
+ 249.9ns 0.8VV 250ns 0V 
+ 255ns 0V 
+ 260ns 0V 
+ 265ns 0V 
+ 270ns 0V 
+ 275ns 0V 
+ 280ns 0V 
+ 285ns 0V 
+ 289.9ns 0V 290ns 0.8VV 
+ 295ns 0.8VV 
+ 300ns 0.8VV 
+ 305ns 0.8VV 
+ 310ns 0.8VV 
+ 315ns 0.8VV 
+ 320ns 0.8VV 
+ 325ns 0.8VV 
+ 330ns 0.8VV )
* Input stimuli for y using Piecewise Linear Voltage (PWL)
V3 y 0 PWL(0ns 0V 
+ 5ns 0V 
+ 10ns 0V 
+ 15ns 0V 
+ 20ns 0V 
+ 25ns 0V 
+ 29.9ns 0V 30ns 0.8VV 
+ 35ns 0.8VV 
+ 40ns 0.8VV 
+ 45ns 0.8VV 
+ 49.9ns 0.8VV 50ns 0V 
+ 55ns 0V 
+ 60ns 0V 
+ 65ns 0V 
+ 69.9ns 0V 70ns 0.8VV 
+ 75ns 0.8VV 
+ 80ns 0.8VV 
+ 85ns 0.8VV 
+ 89.9ns 0.8VV 90ns 0V 
+ 95ns 0V 
+ 100ns 0V 
+ 105ns 0V 
+ 109.9ns 0V 110ns 0.8VV 
+ 115ns 0.8VV 
+ 120ns 0.8VV 
+ 125ns 0.8VV 
+ 129.9ns 0.8VV 130ns 0V 
+ 135ns 0V 
+ 140ns 0V 
+ 145ns 0V 
+ 149.9ns 0V 150ns 0.8VV 
+ 155ns 0.8VV 
+ 160ns 0.8VV 
+ 165ns 0.8VV 
+ 169.9ns 0.8VV 170ns 0V 
+ 175ns 0V 
+ 180ns 0V 
+ 185ns 0V 
+ 189.9ns 0V 190ns 0.8VV 
+ 195ns 0.8VV 
+ 200ns 0.8VV 
+ 205ns 0.8VV 
+ 209.9ns 0.8VV 210ns 0V 
+ 215ns 0V 
+ 220ns 0V 
+ 225ns 0V 
+ 229.9ns 0V 230ns 0.8VV 
+ 235ns 0.8VV 
+ 240ns 0.8VV 
+ 245ns 0.8VV 
+ 249.9ns 0.8VV 250ns 0V 
+ 255ns 0V 
+ 260ns 0V 
+ 265ns 0V 
+ 269.9ns 0V 270ns 0.8VV 
+ 275ns 0.8VV 
+ 280ns 0.8VV 
+ 285ns 0.8VV 
+ 289.9ns 0.8VV 290ns 0V 
+ 295ns 0V 
+ 300ns 0V 
+ 305ns 0V 
+ 309.9ns 0V 310ns 0.8VV 
+ 315ns 0.8VV 
+ 320ns 0.8VV 
+ 325ns 0.8VV 
+ 330ns 0.8VV )
* Input stimuli for ce using Piecewise Linear Voltage (PWL)
V4 ce 0 PWL(0ns 0V 
+ 5ns 0V 
+ 10ns 0V 
+ 15ns 0V 
+ 19.9ns 0V 20ns 0.8VV 
+ 25ns 0.8VV 
+ 29.9ns 0.8VV 30ns 0V 
+ 35ns 0V 
+ 39.9ns 0V 40ns 0.8VV 
+ 45ns 0.8VV 
+ 49.9ns 0.8VV 50ns 0V 
+ 55ns 0V 
+ 59.9ns 0V 60ns 0.8VV 
+ 65ns 0.8VV 
+ 69.9ns 0.8VV 70ns 0V 
+ 75ns 0V 
+ 79.9ns 0V 80ns 0.8VV 
+ 85ns 0.8VV 
+ 90ns 0.8VV 
+ 95ns 0.8VV 
+ 99.9ns 0.8VV 100ns 0V 
+ 105ns 0V 
+ 110ns 0V 
+ 115ns 0V 
+ 119.9ns 0V 120ns 0.8VV 
+ 125ns 0.8VV 
+ 129.9ns 0.8VV 130ns 0V 
+ 135ns 0V 
+ 139.9ns 0V 140ns 0.8VV 
+ 145ns 0.8VV 
+ 149.9ns 0.8VV 150ns 0V 
+ 155ns 0V 
+ 159.9ns 0V 160ns 0.8VV 
+ 165ns 0.8VV 
+ 170ns 0.8VV 
+ 175ns 0.8VV 
+ 179.9ns 0.8VV 180ns 0V 
+ 185ns 0V 
+ 190ns 0V 
+ 195ns 0V 
+ 199.9ns 0V 200ns 0.8VV 
+ 205ns 0.8VV 
+ 209.9ns 0.8VV 210ns 0V 
+ 215ns 0V 
+ 219.9ns 0V 220ns 0.8VV 
+ 225ns 0.8VV 
+ 229.9ns 0.8VV 230ns 0V 
+ 235ns 0V 
+ 239.9ns 0V 240ns 0.8VV 
+ 245ns 0.8VV 
+ 250ns 0.8VV 
+ 255ns 0.8VV 
+ 259.9ns 0.8VV 260ns 0V 
+ 265ns 0V 
+ 270ns 0V 
+ 275ns 0V 
+ 279.9ns 0V 280ns 0.8VV 
+ 285ns 0.8VV 
+ 289.9ns 0.8VV 290ns 0V 
+ 295ns 0V 
+ 299.9ns 0V 300ns 0.8VV 
+ 305ns 0.8VV 
+ 309.9ns 0.8VV 310ns 0V 
+ 315ns 0V 
+ 319.9ns 0V 320ns 0.8VV 
+ 325ns 0.8VV 
+ 330ns 0.8VV )
* Input stimuli for op_bus0_ using Piecewise Linear Voltage (PWL)
V5 op_bus0_ 0 PWL(0ns 0V 
+ 5ns 0V 
+ 10ns 0V 
+ 15ns 0V 
+ 20ns 0V 
+ 25ns 0V 
+ 30ns 0V 
+ 35ns 0V 
+ 40ns 0V 
+ 45ns 0V 
+ 50ns 0V 
+ 55ns 0V 
+ 60ns 0V 
+ 65ns 0V 
+ 70ns 0V 
+ 75ns 0V 
+ 80ns 0V 
+ 85ns 0V 
+ 90ns 0V 
+ 95ns 0V 
+ 100ns 0V 
+ 105ns 0V 
+ 110ns 0V 
+ 115ns 0V 
+ 120ns 0V 
+ 125ns 0V 
+ 130ns 0V 
+ 135ns 0V 
+ 140ns 0V 
+ 145ns 0V 
+ 150ns 0V 
+ 155ns 0V 
+ 160ns 0V 
+ 165ns 0V 
+ 169.9ns 0V 170ns 0.8VV 
+ 175ns 0.8VV 
+ 180ns 0.8VV 
+ 185ns 0.8VV 
+ 190ns 0.8VV 
+ 195ns 0.8VV 
+ 200ns 0.8VV 
+ 205ns 0.8VV 
+ 210ns 0.8VV 
+ 215ns 0.8VV 
+ 220ns 0.8VV 
+ 225ns 0.8VV 
+ 230ns 0.8VV 
+ 235ns 0.8VV 
+ 240ns 0.8VV 
+ 245ns 0.8VV 
+ 250ns 0.8VV 
+ 255ns 0.8VV 
+ 260ns 0.8VV 
+ 265ns 0.8VV 
+ 270ns 0.8VV 
+ 275ns 0.8VV 
+ 280ns 0.8VV 
+ 285ns 0.8VV 
+ 290ns 0.8VV 
+ 295ns 0.8VV 
+ 300ns 0.8VV 
+ 305ns 0.8VV 
+ 310ns 0.8VV 
+ 315ns 0.8VV 
+ 320ns 0.8VV 
+ 325ns 0.8VV 
+ 330ns 0.8VV )
* Input stimuli for op_bus1_ using Piecewise Linear Voltage (PWL)
V6 op_bus1_ 0 PWL(0ns 0V 
+ 5ns 0V 
+ 10ns 0V 
+ 15ns 0V 
+ 20ns 0V 
+ 25ns 0V 
+ 30ns 0V 
+ 35ns 0V 
+ 40ns 0V 
+ 45ns 0V 
+ 50ns 0V 
+ 55ns 0V 
+ 60ns 0V 
+ 65ns 0V 
+ 70ns 0V 
+ 75ns 0V 
+ 80ns 0V 
+ 85ns 0V 
+ 89.9ns 0V 90ns 0.8VV 
+ 95ns 0.8VV 
+ 100ns 0.8VV 
+ 105ns 0.8VV 
+ 110ns 0.8VV 
+ 115ns 0.8VV 
+ 120ns 0.8VV 
+ 125ns 0.8VV 
+ 130ns 0.8VV 
+ 135ns 0.8VV 
+ 140ns 0.8VV 
+ 145ns 0.8VV 
+ 150ns 0.8VV 
+ 155ns 0.8VV 
+ 160ns 0.8VV 
+ 165ns 0.8VV 
+ 169.9ns 0.8VV 170ns 0V 
+ 175ns 0V 
+ 180ns 0V 
+ 185ns 0V 
+ 190ns 0V 
+ 195ns 0V 
+ 200ns 0V 
+ 205ns 0V 
+ 210ns 0V 
+ 215ns 0V 
+ 220ns 0V 
+ 225ns 0V 
+ 230ns 0V 
+ 235ns 0V 
+ 240ns 0V 
+ 245ns 0V 
+ 249.9ns 0V 250ns 0.8VV 
+ 255ns 0.8VV 
+ 260ns 0.8VV 
+ 265ns 0.8VV 
+ 270ns 0.8VV 
+ 275ns 0.8VV 
+ 280ns 0.8VV 
+ 285ns 0.8VV 
+ 290ns 0.8VV 
+ 295ns 0.8VV 
+ 300ns 0.8VV 
+ 305ns 0.8VV 
+ 310ns 0.8VV 
+ 315ns 0.8VV 
+ 320ns 0.8VV 
+ 325ns 0.8VV 
+ 330ns 0.8VV )
* Input stimuli for reset using Piecewise Linear Voltage (PWL)
V7 reset 0 PWL(0ns 0.8VV 
+ 5ns 0.8VV 
+ 9.9ns 0.8VV 10ns 0V 
+ 15ns 0V 
+ 20ns 0V 
+ 25ns 0V 
+ 30ns 0V 
+ 35ns 0V 
+ 40ns 0V 
+ 45ns 0V 
+ 50ns 0V 
+ 55ns 0V 
+ 60ns 0V 
+ 65ns 0V 
+ 70ns 0V 
+ 75ns 0V 
+ 80ns 0V 
+ 85ns 0V 
+ 90ns 0V 
+ 95ns 0V 
+ 100ns 0V 
+ 105ns 0V 
+ 110ns 0V 
+ 115ns 0V 
+ 120ns 0V 
+ 125ns 0V 
+ 130ns 0V 
+ 135ns 0V 
+ 140ns 0V 
+ 145ns 0V 
+ 150ns 0V 
+ 155ns 0V 
+ 160ns 0V 
+ 165ns 0V 
+ 170ns 0V 
+ 175ns 0V 
+ 180ns 0V 
+ 185ns 0V 
+ 190ns 0V 
+ 195ns 0V 
+ 200ns 0V 
+ 205ns 0V 
+ 210ns 0V 
+ 215ns 0V 
+ 220ns 0V 
+ 225ns 0V 
+ 230ns 0V 
+ 235ns 0V 
+ 240ns 0V 
+ 245ns 0V 
+ 250ns 0V 
+ 255ns 0V 
+ 260ns 0V 
+ 265ns 0V 
+ 270ns 0V 
+ 275ns 0V 
+ 280ns 0V 
+ 285ns 0V 
+ 290ns 0V 
+ 295ns 0V 
+ 300ns 0V 
+ 305ns 0V 
+ 310ns 0V 
+ 315ns 0V 
+ 320ns 0V 
+ 325ns 0V 
+ 330ns 0V )

.tran 1ns 335.0ns 0 1ns
.probe V(op_bus0_) V(op_bus1_) V(clk) V(x) V(y) V(ce) V(reset) V(out) V(n_vdd) V(n_gnd) 
.print TRAN V(op_bus0_) V(op_bus1_) V(clk) V(x) V(y) V(ce) V(reset) V(out) V(n_vdd) V(n_gnd) 
.option post=2 probe
.end