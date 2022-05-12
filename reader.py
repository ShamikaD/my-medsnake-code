# from https://makersportal.com/blog/2018/2/25/python-datalogger-reading-the-serial-output-from-arduino-to-analyze-data-using-pyserial
# /Applications/anaconda3/envs/arduino <-- conda environment that I am trying to run the file in
import serial
import time
import csv
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np


# set up the serial line
ser = serial.Serial('/dev/cu.usbmodem101')
ser.readline()
# ser.flushInput()

# #set up plotting
# plot_window = 20
# y_var = np.array(np.zeros([plot_window]))

# plt.ion()
# fig, ax = plt.subplots()
# line, = ax.plot(y_var)

# # Read and record the data into "test_data.csv" as well as make a plot
# while True:
#     try:
#         ser_bytes = ser.readline()
#         try:
#             decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
#             print(decoded_bytes)
#         except:
#             continue
#         with open("test_data.csv","a") as f:
#             writer = csv.writer(f,delimiter=",")
#             writer.writerow([time.time(),decoded_bytes])
#         y_var = np.append(y_var,decoded_bytes)
#         y_var = y_var[1:plot_window+1]
#         line.set_ydata(y_var)
#         ax.relim()
#         ax.autoscale_view()
#         fig.canvas.draw()
#         fig.canvas.flush_events()
#     except:
#         print("Keyboard Interrupt")
#         break
  