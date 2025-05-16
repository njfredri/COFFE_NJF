#/bin/bash
rm *.ic0
rm *.st0
rm *.tr0
rm *.tr0.lis
rm *.csv
rm *.pa0
# python3 new_v2s.py -i opmux_behav_subset_synth.v -l saed90nm.cdl -p P12 -n N12 -m ../spice_models/ptm_22nm_bulk_hp.l -o opmux.sp
# echo Please go and change the libraries mentioned in opmux.sp.
# read
# echo Please go and set Wn and Wp to 45n in minlib.sp
# read
python3 generateTBInput.py -i opmux_times.txt -m ../spice_models/ptm_22nm_bulk_hp.l -d opmux_behav -c opmux.sp
python3 generateTestbench.py -i testbench.json -o testbench.sp
hspice testbench.sp > hspice_raw_output.txt
python3 process_output.py -i hspice_raw_output.txt -o hspice_processed_output.txt
#cleanup temp files
rm temp_translation.json
rm temp.json