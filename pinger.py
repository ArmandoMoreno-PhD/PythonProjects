# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:04:18 2020

@author: JoeMax
"""

from pythonping import ping
import numpy as np
import matplotlib.pyplot as plt
def ShowPing(IpAddress, NumberPings):
    try:
        Ip_Address = IpAddress
        Number_Pings = NumberPings
    except:
        #LoL EUW server
        Ip_Address = '104.160.141.3'
        #Local test Ip_Address = '192.168.1.130'
        Number_Pings = 1000
    
    
    response_list = ping(Ip_Address, size=60, count=Number_Pings)
    
    a = response_list._responses
    times = []
    for i in range(0,len(a),1):
        times.append(a[i].time_elapsed_ms)
        print(f'the ping #{i} is {a[i].time_elapsed_ms}ms', flush = True)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([0,Number_Pings])
    ax.set_ylim([0,300])
    ax.set_axisbelow(True)
    ax.set_ylabel('Response (ms)')
    ax.set_xlabel('ping #')
    ax.grid(which='both',linestyle ='--')
    ax.set_xticks(np.arange(0, Number_Pings, step=250),None)
    plt.plot(range(0,len(times)),times)
