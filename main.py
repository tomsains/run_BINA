# This is a sample Python script.
path_to_BINA = "/home/thomas_sainsbury/BINE/"
path_to_BCL_output = "/media/thomas_sainsbury/Samsung_T5/SeG/results/Baysian_network_inference/R_scirpts_for_assembly_paper/BCL_output/"
path_to_BCL_results_folder = "/media/thomas_sainsbury/Samsung_T5/SeG/results/Baysian_network_inference/R_scirpts_for_assembly_paper/BCL_results/BCL_BINE/"

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Run_BINA_functions import *

import multiprocessing
from functools import partial






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     condition_list = [os.path.basename(x) for x in glob.glob(path_to_BCL_output + "*WT*")]
     print(condition_list)
     for c in condition_list:
         def parallel_runs(data_list):
             pool = multiprocessing.Pool(processes=8)
             multi_BINA = partial(run_BINA_Single, path_to_BINA=path_to_BINA, data_folder=path_to_BCL_output,
                                  condition_folder=c,
                                  results_folder=path_to_BCL_results_folder)
             pool.map(multi_BINA, data_list)

         data_list = [os.path.basename(x) for x in glob.glob(path_to_BCL_output + c + "/*_spikes.dat")]
         print(data_list)
         parallel_runs(data_list)

         while checkIfProcessRunning("gibbsDPA5data") == True:
             os.wait()



#run_BINA_Single(path_to_BINA=path_to_BINA, data_folder=path_to_BCL_output, condition_folder= "WT_GR_7_dpf/",
#                   results_folder=path_to_BCL_results_folder, data_set_name="180530_WT_grav_h2b_gc6s_7dpf_f1_sa__00001_scaled_aligned_all_cells_spikes.dat")


'''
for i in range(5):


        names = ['Brown', 'Wilson', 'Bartlett', 'Rivera', 'Molloy', 'Opie']
        with multiprocessing.Pool(processes=7) as pool:
'''
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
