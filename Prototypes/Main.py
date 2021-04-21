import os
import multiprocessing

processes = ('GUI.py', 'GetData.py')

def run_processes(process):
    os.system('python {}'.format(process))



if __name__ == '__main__':
    Manager = multiprocessing.Manager()
    return_data = Manager.dict()
    pool = multiprocessing.Pool(processes=3)
    pool.map(run_processes, processes)
    print(return_data)


"""
    ProcessD = multiprocessing.Process(target=GetData.Serial_get())
    ProcessG = multiprocessing.Process(target=GUI.update_Data())
    ProcessD.start()
    print(return_data)
    ProcessG.start()"""