""" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =  
                                                            
                                                            🤵 Author : Mohammed Rayaan Pasha
                                                            📅 Last Date of update: 16-03-2025
                                                            🍂 Toughts: it simulates RR_Interval: which is the time it takes for one heart beat to take a beat.
                                                                         - firstly Normal distribution is F** awesome, we can use it to simulate like any situation, man that fun.
                                                                         - so im assuming avg time it takes for heart to take a beat is 60, with sd of say 5. then im picking iter number 
                                                                           simulations on it, and then displaying this thingy..

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ="""
# 🏗️ Libraries
import numpy as np
import matplotlib.pyplot as plt

# Params ❄️
mean = 60
standard_dev = 5
iters = 10000000

# normal distribution random simulation 📊
r_r_intervals = np.random.normal(mean,standard_dev,iters)

# at what time is did heartbeat i, beat? 🫀
accumulated_time = np.cumsum(r_r_intervals) / 1000


# graph plotting: 📈
plt.plot(accumulated_time[:100],r_r_intervals[:100])
plt.xlabel("Time")
plt.ylabel("heart-beat time")
plt.show()
