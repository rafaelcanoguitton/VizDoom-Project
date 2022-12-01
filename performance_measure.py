# # Importing the essential libraries
# import psutil
# import GPUtil
# # Testing the psutil library for both CPU and RAM performance details
# print(psutil.cpu_percent())
# print(psutil.virtual_memory().percent)
# # Testing the GPUtil library for both GPU performance details
# GPUtil.showUtilization()
# Importing the numpy and visualization library
# import numpy as np
# import matplotlib.pyplot as plt
# # Plotting the axis
# plt.axis([0, 10, 0, 1])
# # Creating a random scatter plot
# for i in range(10):
#     y = np.random.random()
#     plt.scatter(i, y)
#     plt.pause(0.05)
# plt.show()
# Importing the required libraries
# import psutil
# import GPUtil
# import numpy as np
# import matplotlib.pyplot as plt
# # Creating an almost infinite for loop to monitor the details continuously
# for i in range(100000000):
#     # Obtaining all the essential details
#     cpu_usage = psutil.cpu_percent()
#     mem_usage = psutil.virtual_memory().percent
#     print(cpu_usage)
#     print(mem_usage)
#     # Creating the scatter plot
#     plt.scatter(i, cpu_usage, color = "red")
#     plt.scatter(i, mem_usage, color = "blue")
#     plt.legend(["CPU", "Memory"], loc ="lower right")
#     plt.pause(0.05)
#     # Obtaining the GPU details
#     GPUtil.showUtilization()
#     print(GPUtil.getGPUs()[0].load)
# # Plotting the information
# plt.show()
import psutil
import torch
for _ in range(1):
    print(f'Uso de CPU de este proceso: {psutil.Process().cpu_percent(interval=1)}')
    print(f'Uso de CPU total de la PC:{psutil.cpu_percent()}')
    print(f'Uso de memoria de este proceso: {psutil.Process().memory_percent()}')
    print(f'Uso de memoria total de la PC: {psutil.virtual_memory().percent}')
    print("\n")

print("torch.cuda.memory_localizada: %fGB"%(torch.cuda.memory_allocated(0)/1024/1024/1024))
print("torch.cuda.memory_reservada: %fGB"%(torch.cuda.memory_reserved(0)/1024/1024/1024))
print("torch.cuda.max_memory_reservada: %fGB"%(torch.cuda.max_memory_reserved(0)/1024/1024/1024))

