from multiprocessing import Process, Manager

MULTIPROCESSING_ENABLE = True
MULTIPROCESSING_BATCH_SIZE = 6

def calculatecost_process(area, delay, area_opt_weight, delay_opt_weight, cost_function, shared_cost_list, index:int):
    cost = cost_function(area, delay, area_opt_weight, delay_opt_weight)
    shared_cost_list[index] = (cost, index)
    return

def calculatecost_parallel(eval_delay_list, area_list, cost_function, area_opt_weight, delay_opt_weight):
    # Calculate cost for each combo (area-delay product)
    # Results list holds a tuple, (cost, combo_index, area, delay)
    print("Parallel calculating cost for each transistor sizing combinations...")
    print("")
    final_cost_list = []
    eval_len = len(eval_delay_list)
    with Manager() as manager:
        shared_cost_list = manager.list([0] * eval_len)
        #Create and run all processes for calculating cost
        for batch_start in range(eval_len, MULTIPROCESSING_BATCH_SIZE):
            # area = area_list[i]
            # delay = eval_delay_list[i]
            # cost = cost_function(area, delay, area_opt_weight, delay_opt_weight)
            # cost_list.append((cost, i))
            processes = []
            batch_end = min(batch_start+MULTIPROCESSING_BATCH_SIZE, eval_len)
            for i in range(batch_start, batch_end):
                p = Process(target=calculatecost_parallel, args=(area_list[i], eval_delay_list[i], area_opt_weight, delay_opt_weight, cost_function, shared_cost_list, i))
                processes.append(p)
                p.start()
            for p in processes:
                p.join()
        final_cost_list = list(shared_cost_list)
    return final_cost_list

def sb_mux_update_delay(sb_mux, spice_interface, parameter_dict, shared_delay_dict):
    print("  Updating delay for " + sb_mux.name)
    spice_meas = spice_interface.run(sb_mux.top_spice_path, parameter_dict)
    if spice_meas["meas_total_tfall"][0] == "failed" or spice_meas["meas_total_trise"][0] == "failed" :
        valid_delay = False
        tfall = 1
        trise = 1
    else :  
        tfall = float(spice_meas["meas_total_tfall"][0])
        trise = float(spice_meas["meas_total_trise"][0])
    if tfall < 0 or trise < 0 :
        valid_delay = False
    # sb_mux.tfall = tfall
    # sb_mux.trise = trise
    # sb_mux.delay = max(tfall, trise)
    delay = max(tfall, trise)
    # crit_path_delay += sb_mux.delay*sb_mux.delay_weight
    # fpga.delay_dict[sb_mux.name] = sb_mux.delay
    # sb_mux.power = float(spice_meas["meas_avg_power"][0])
    power = float(spice_meas["meas_avg_power"][0])
    name = sb_mux.name
    shared_delay_dict[name] = (trise, tfall, delay, sb_mux.delay_weight, power)
    
def generic_update_delay(circ, spice_interface, parameter_dict, shared_delay_dict):
    print("  Updating delay for " + circ.name)
    spice_meas = spice_interface.run(circ.top_spice_path, parameter_dict)
    if spice_meas["meas_total_tfall"][0] == "failed" or spice_meas["meas_total_trise"][0] == "failed" :
        valid_delay = False
        tfall = 1
        trise = 1
    else :  
        tfall = float(spice_meas["meas_total_tfall"][0])
        trise = float(spice_meas["meas_total_trise"][0])
    if tfall < 0 or trise < 0 :
        valid_delay = False
    delay = max(tfall, trise)
    power = float(spice_meas["meas_avg_power"][0])
    return {circ.name : (trise, tfall, delay, circ.delay_weight, power)}