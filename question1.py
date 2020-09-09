import random as rd
import matplotlib.pyplot as plt

#rather than using random.org I used python to simulate dicerolls
def roll():
    return rd.randint(1,6)

#simulates n dicerolls, recording them in a list
def rollset(n):
    return [roll() for i in range(0,n)]

#calculates the average of some list s
def  mean(s):
    return sum(s)/len(s)

#calculates the standard deviation of some list l
def stddev(l):
    m = mean(l)
    residuals = [i-m for i in l]
    residuals_squared = [r**2 for r in residuals]
    return (sum(residuals_squared)/(len(l)-1))**0.5

#returns a list of means for "num_sets" simulated number of samples of number of rolls "num_rolls"
def meanset(num_rolls,num_sets):
    return [mean(rollset(num_rolls)) for i in range(0,num_sets)]

'''
using our functions we  can complete part a, since my function
meanset returns a new list each time it's run I will manually record
the list the console outputs for the sake of consistency
a)
    i)
I ran the code below to get the single set of 20 dicerolls 
which i copy and pasted from the console
rolls_20 = rollset(20)
print(g)
'''
rolls_20 = [4, 3, 3, 5, 4, 6, 5, 1, 1, 5, 1, 1, 6, 2, 6, 4, 1, 5, 2, 3]

'''
The code below returns a mean of 3.4 and a standard deviation of 1.847
'''
mean_rolls_20 = mean(rolls_20)
stddev_rolls_20 = stddev(rolls_20)
#print(mean_rolls_20,stddev_rolls_20)
'''
    ii)
Similar last time i will run the code once and then copy and paste
from the console for the sake of consistency

I used the following code to generate the list of means of 20 simulated
samples of 20 dicerolls
meanset_20 =meanset(20,19)
I only generated a list of 19 and added the mean we found  earlier since 
since that's what the question explicitly asked for
meanset_20.append(mean_rolls_20)
print(meanset_20)
'''
meanset_20 = [3.35, 3.0, 3.7, 3.5, 3.15, 4.15, 3.0, 3.5, 3.4, 3.45, 4.1, 2.9, 3.3, 3.05, 2.75, 3.3, 2.85, 4.1, 3.7,3.4]
mean_meanset_20 = mean(meanset_20)
stddev_meanset_20 = stddev(meanset_20)
stddev_predicted  = stddev_rolls_20/(20**0.5)
print(mean_meanset_20,stddev_meanset_20)
print(stddev_rolls_20/(20**0.5))
'''
The code above returns a mean of 3.383 ,very close to our  original mean
and  a standard deviation of 0.413 which, when we consider 3 decimal places 
is equal to our prediction for standard error in the mean of 0.413 from the  
equation sigma/sqrt(N) where  sigma is the standard deviation we found for
1 set of 20 rolls and  N is the number of  means used in out list 
'''
'''
b)
for part b I will again use code to generate a list and then record
it from the console to remain consistent, I will also use the same 
set of 20 from B
meanset_5 is the result of print(meanset(5,20))
meanset_1 is the  result of print(meanset(1,20)) (although it's functionally the same as
rollset(20))
and meanset_20 is listed , but I will restate it with meansets 1 and 5 to group everything 
'''
meanset_20 = [3.35, 3.0, 3.7, 3.5, 3.15, 4.15, 3.0, 3.5, 3.4, 3.45, 4.1, 2.9, 3.3, 3.05, 2.75, 3.3, 2.85, 4.1, 3.7,3.4]
meanset_5 = [4.4, 2.8, 3.4, 4.6, 3.8, 3.6, 4.8, 4.0, 3.2, 3.4, 4.0, 3.0, 3.4, 2.8, 4.4, 4.0, 4.0, 5.2, 3.4, 4.6]
meanset_1 = [5.0, 1.0, 1.0, 5.0, 2.0, 3.0, 2.0, 4.0, 3.0, 2.0, 1.0, 3.0, 5.0, 4.0, 2.0, 5.0, 4.0, 5.0, 6.0, 5.0]

plt.hist(meanset_20,bins=12,range =(1,6))
plt.title("Distribution of means from  20 samples of 20 dicerolls")
plt.show()
plt.title("Distribution of means from 20 samples of 5 dicerolls")
plt.hist(meanset_5,bins=12,range =(1,6))
plt.show()
plt.title("Distribution of means of 20  samples of 1 diceroll")
plt.hist(meanset_1,bins=6,range =(1,6))
plt.show()

'''
    c)
meanset_20 (mean,standard deviation) = (3.383,0.413)
meanset_5 (mean,standard  deviation) = (3.84,0.679)
meanset_1 (mean,standard deviation) = (3.4, 1.603)
Qualitatively speaking the histogram of meanset_1 is appears to b
a uniform distribution and clearly not a normal distribution. moving
on to the histogram for meanset_2 we have  something that is very 
clearly not a uniform distribution and is arguably somewhat normal.
The histogram of meanset_20 further shows this transition to a normal
shape. As out number of samples goes up or mean gets smaller and smaller
which makes sense given the formula for standard deviation is inversely
proportional to 1/sqrt(n-1). We can clearly see the central limit theorem
at work here showing that as we increase the size samples of our 
dicerolls (so that the means become useful instead of simply stating
the individual diceroll) and increase the number of samples taken
the  shape of the graph approaches a normal curve. I will include 
a graph of a large number of large size samples to demonstrate this 
further.

plt.hist(meanset(1000,1000))
plt.title("Distribution of means from  20 samples of 20 dicerolls")
plt.show()
I ran the above code to get the aforementioned graph. I've commented
it out because I don't want  it running each time I run this  program, 
it lags my  computer  a little bit.
'''
'''
    d)
Increasing the number of individual measurements reduces the standard 
deviation which essentially allows us to zoom in on the true mean of whatever
we're sampling. 
'''
