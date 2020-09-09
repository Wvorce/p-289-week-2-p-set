import matplotlib.pyplot as plt
import math
import scipy.stats as st

'''
This function should return the probability of point occuring  
given  a mean using the poisson distribution
'''
def poissonpdf(mean,point):
    return math.exp(-1*mean)*(mean**point/math.factorial(point))
'''
11 and 59 are from mean +/- 4*roundedup(sqrt(mean))
I  added  1 to 59 because range is not inclusive to the 
upper bound
'''
average = 35
xlist = [n for n in range(11,60)]
poisson_dist = [poissonpdf(average,g) for g in xlist]
'''
I just used the norm.pdf function because we're studying 
the poisson distribution mainly, not the normal distribution
'''
normal_dist = [st.norm.pdf(x,average,average**0.5) for x in xlist]


fig, ax = plt.subplots()
plt.bar(xlist,poisson_dist)
ax.plot(xlist,normal_dist, 'r-')
plt.title("Gaussian Curve over Poisson Distribution with mean = 35 and Standard Deviation = \u221a(35)")
plt.show()
'''
Honestly these two distributions look quite similar. The only difference 
really is the few areas where the poisson distribution slightly over-estimates.
I think  the largest difference outside of that would be that a normal curve is
a continuous function. A poisson distribution can't be continuous simply
because of the presence of a factorial in the equation for normpdf. 
'''