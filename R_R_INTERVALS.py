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
import logging

# 🎯 Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Params ❄️
mean = 60
standard_dev = 5
iters = 10000000

logging.info(f"Starting RR_Interval Simulation with {iters} iterations.")
logging.info(f"Mean: {mean}, Standard Deviation: {standard_dev}")

# normal distribution random simulation 📊
r_r_intervals = np.random.normal(mean, standard_dev, iters)

# Basic stats logging
logging.info(f"Generated RR Intervals: Mean={np.mean(r_r_intervals):.2f}, StdDev={np.std(r_r_intervals):.2f}")

# at what time did heartbeat i, beat? 🫀
accumulated_time = np.cumsum(r_r_intervals) / 1000

# graph plotting: 📈
plt.plot(accumulated_time[:100], r_r_intervals[:100])
plt.xlabel("Time")
plt.ylabel("Heart-beat time")
plt.show()

logging.info("Simulation completed successfully.")
