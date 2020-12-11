import glob
import os
import multiprocessing

import psutil


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def run_BINA_Single(data_set_name, path_to_BINA, condition_folder, results_folder, data_folder, n_iter = 80000,
             initial_assemblies = 400, trim = 10, burn_in = 60000, seed = 1, recorded_assemblies = 200, min_neuron =15, min_act = 3, continue_run =0, verbose = 1):
    os.chdir(path_to_BINA)
    print(os.getcwd())
    print(data_folder + condition_folder + "/" + data_set_name)
    prefix = data_set_name.replace('_scaled_aligned_all_cells_spikes.dat','')
    print(prefix)
    os.system("./bin/gibbsDPA5data " + "--file=" + data_folder + condition_folder + "/" + data_set_name + " --folder=" + prefix +
              " --niter=" + str(n_iter)+ " --assemblies=" + str(initial_assemblies) + " --assemblies " + str(initial_assemblies) + " --trim " + str(trim) + " --burn_in " + str(burn_in) +
                 " --seed " + str(seed) + " --min_neur " + str(min_neuron) + " --min_act " + str(min_act) +
                 " --recorded_assemblies " + str(recorded_assemblies))
    #os.system("mkdir " + results_folder + condition_folder +"/"+ prefix)
    os.system("mv " + prefix + "/ " + results_folder + condition_folder + "/" + prefix)



