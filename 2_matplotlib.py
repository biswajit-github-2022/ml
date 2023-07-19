import numpy as np
import matplotlib.pyplot as plt
# x = np.random.normal(170, 10, 250)

# print(x)
# plt.hist(x)
# plt.show() 


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm
# #
# # Draw random samples from normal distribution
# # with a predefined mean and standard deviation
# #
# x = np.random.normal(loc=5, scale = 2, size=1000)
# #
# # Plot probability distribution function
# #
# x_sorted = np.sort(x)
# plt.figure(figsize=(7, 5))
# plt.plot(x_sorted, norm.pdf(x_sorted, loc=5, scale=2))
# plt.title("Normal distribution", fontsize=16)





# Creating x axis with range and y axis with Sine
# Function for Plotting Sine Graph
x = np.arange(0, 5*np.pi, 0.1)
y = np.sin(x)

# Plotting Sine Graph
plt.plot(x, y, color='green')
plt.show()




# Creating x axis with range and y axis with Sine
# Function for Plotting Cosine Graph
x = np.arange(0, 5*np.pi, 0.1)
y = np.cos(x)
 
# Plotting coine Graph
plt.plot(x, y, color='green')
plt.show()



# Creating x axis with range and y axis with Sine
# Function for Plotting Cosine Graph
x = np.arange(0, 5*np.pi, 0.1)
y = np.tan(x)
 
# Plotting coine Graph
plt.plot(x, y, color='green')
plt.show()