#!/usr/bin/env python
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[2]:


import matplotlib.pyplot as plt
import numpy as np

get_ipython().run_line_magic('matplotlib', 'notebook')

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

# plot the histograms
plt.figure(figsize=(9,3))
plt.hist(x1, density=True, bins=20, alpha=0.5)
plt.hist(x2, density=True, bins=20, alpha=0.5)
plt.hist(x3, density=True, bins=20, alpha=0.5)
plt.hist(x4, density=True, bins=20, alpha=0.5);

plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')


# In[3]:


import matplotlib.animation as animation
import pandas as pd

# create a 2x2 grid of subplots
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2, 2, sharex=False, sharey=False)

# plot the data on the 4 subplots  
ax1.hist(x1, density=True, bins=20, alpha=0.5, color = 'skyblue')
ax1.set_title('x1\nNormal')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

ax2.hist(x2, density=True, bins=20, alpha=0.5, color = 'orange')
ax2.set_title('x2\nGamma')
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax3.hist(x3, density=True, bins=20, alpha=0.5, color = 'seagreen')
ax3.set_title('x3\nExponential')
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)

ax4.hist(x4, density=True, bins=20, alpha=0.5, color = 'indianred')
ax4.set_title('x4\nUniform')
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)

#adjust
plt.subplots_adjust(top=0.90, bottom=0.08, left=0.10, right=0.95, hspace=0.4,
                    wspace=0.30)


# In[6]:


n = 100

def update(curr):
    # check if animation is at the last frame, and if so, stop the animation a
    if curr == n: 
        a.event_source.stop()
    # clear current axis with .cla()
    bins = 20
        #plt.cla()
    plt.subplot(2,2,1)
    plt.hist(x1[:curr], density=True, bins = bins, color = 'green')
    plt.subplot(2,2,2) 
    plt.hist(x2[:curr], density=True, bins= bins, alpha=0.5, color = 'blue')
    plt.subplot(2,2,3)
    plt.hist(x3[:curr], density=True, bins= bins, alpha=0.5, color = 'red')
    plt.subplot(2,2,4)
    plt.hist(x4[:curr], density=True, bins= bins, alpha=0.5, color = 'yellow')


# In[7]:


fig = plt.figure()
#interval is in milliseconds - time between updates
a = animation.FuncAnimation(fig, update, interval=1)


# In[ ]:





# In[ ]:




