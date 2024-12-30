#------------------------------------------------------------------
# Run a single thread
#------------------------------------------------------------------
import threading, time
# from threading import Thread

# def func(t):
#     print('you are in func with thread {}'.format(t))
#     time.sleep(120)

# t = threading.Thread(target=func,args=('thread1',))

# t.start()
# t.join()

#------------------------------------------------------------------
# Run multiple threads
#------------------------------------------------------------------
# def func(t):
#     print('----------------------------------------')
#     print('you are in func with thread {}'.format(t))
#     time.sleep(120)
#
# no_of_threads_to_run = 5
#
# threads = list()
#
# for i in range(1,(no_of_threads_to_run+1)):
#     t = threading.Thread(target=func,args=(i,))
#     threads.append(t)
#     t.start()
#     print("Current Thread: ", t)
#
# for thread in threads:
#     thread.join()


#------------------------------------------------------------------
# Read multiple files using multiple threads parallely
#------------------------------------------------------------------
import threading, time
from memory_profiler import profile

@profile
def read_files(filename):
    # pass
    with open(filename, 'r') as ip_file:
        lines = ip_file.readlines()
        count = 0
        for record in lines:
            # print(record)
            count = count+1
            # if (count == 3):
            #     time.sleep(60)
            #     count = 0


if __name__ == "__main__":
    no_of_files = 1
    threads = list()

    for i in range(1,(no_of_files+1)):
        filename = 'sample_files/python_orders_file_' + str(i) + '.csv'
        print("Currently executing... thread {}".format(i))
        print("----------------------------------")
        t = threading.Thread(target=read_files,args=(filename,))
        threads.append(t)
        t = t.start()

    for thread in threads:
        thread.join()

#-------------------------------------------
# Hands On Exercise some more processing
#-------------------------------------------






