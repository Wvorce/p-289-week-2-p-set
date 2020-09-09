import math
'''
This function takes a list of values and a frequency list with corresponding 
indeces and returns a new list where each value in list1 is repeadeted n times
determined by the number at the corresponding index in the frequency list
'''
def truelistmaker(list1,freqlist):
    g = []
    for i in range(len(list1)):
        for j in range(0,freqlist[i]):
            g.append(list1[i])
    return g
'''
Original code for poissoncdf() directly below, I just condensed that ugly code
into a nice function that's easier to digest
xlist = [i for i in range(0,6)]
poisson_model = [math.exp(-1*mean_count)*(mean_count**i/math.factorial(i)) for i in range(len(xlist))]
probability = sum(poisson_model)
print(probability)

poissoncdf() (meaning poisson cumulative density function, at least I think, it's been a while since AP stats)
takes a mean, a lower bound, and an upperbound and returns the probability
that an individual observation will be within the lower and upper bounds (inclusive)
given that the phenomena in question is modeled by a posson distribution

'''
def poissoncdf(mean,lower,upper):
    return sum([math.exp(-1*mean)*(mean**i/math.factorial(i)) for i in range(lower,upper+1)])
nlist = [n for n in range(1,14)]
del nlist[1]
#print(nlist)
frequencylist = [1,2,3,6,9,11,8,8,6,2,1,1]
true_list = truelistmaker(nlist,frequencylist)
total_num_count = len(true_list)
print(f"The total count is: {total_num_count}")

'''
i)
    Total number of counts should be equal to the length of true_list
    and the sum of the frequencylist, in either case the total number
    of counts recorded it 58
'''
'''
ii)
    The mean is 7.29
'''
mean_count = sum(true_list)/total_num_count
print(f"The mean count is: {mean_count: .3f}")
'''
iii)
    The mean count rate is numerically equal to the mean count
    of 7.293 Counts, however the units are count per second, 
    so the mean is 7.293 counts per second.
'''

'''
i2?)
    The expected number of occurences at 5 counts or fewer equals
    the probability of five or fewer counts * total number of recordings
    so the expected number of occurences at 5 counts or fewer = 
    poissoncdf(mean_count,0,5)*58 which = 15.361
'''
print(f"The expected number of counts between 0 and 5 for 58 one-second counts is: {poissoncdf(mean_count,0,5)*58: .3f}")
'''
ii2?)
    This is similar to the previous question however, because of the
    greater than part we must actually consider the 1 - the compliment
    of poisson(mean_count,20,infinity) because we can't plug infinity into
    our equation. so  our equation this time will be:
    Expected number = 58*(1-poissoncdf(mean_count,0,19)) = 0.004
    (we use 19 because our function is inclusive, so including
     20 in the complement would exclude it from the calculation)
    
    This expected value of 0.004 may seem small, however it acutally
    makes a lot of sense. Firstly, if our standard deviation for the
    poisson distribution sigma =sqrt(mean) that means our closest possible value of 20
    is roughly 4.7 sigmas from the mean! Since we're taking 58 one second samples it's safe
    to compare this poisson model to what we know about normal curves via the central limit 
    theorem. If we recall the empirical rules which states that the percentage of data lying
    within 1sigma-2sigma-3sigma = 68%-95%-99.7% respectively. Comparing that to our initial point
    with a z-score of 4.7 (4.7 sigmas away) it becomes clear why our expected value is essentially
    0 despite technically capturing an infinite range of possible counts.
    
'''
print(f"The expected number of counts between 20 and infinity for 58 one-second counts is: {(1-poissoncdf(mean_count,0,19))*58: .3f}")