__author__ = 'Abdullah AlOfi'

"""
Future Improvement:
* Count for multiple modes in the same list
* Ask user for list input
"""

nos = [3, 4, 2, 7, 6, 9, 1, 1, 9, 0 , -100, -1, -100]
nos.sort()
print('The list sorted is ' + str(nos))
print('The list has {0} members'.format(len(nos)))
# tot = 0
# for i in range(0,len(nos)):
#    tot += nos[i]
def averagefinder(l):
    tot = sum(l)
    avg = (tot / len(l))
    return(avg)


def modefinder (l):
    rep = -1
    maxrep = 0
    md = None
    for j in range(0,len(nos)-1):
        for h in range(0,len(nos)-1):
            if nos[j] == nos[h]:
                rep += 1

        if rep > maxrep:
            md = l[j]
            maxrep = rep
        elif maxrep == 0:
            md = None
        rep = -1
    return(md)



def medianfinder(l):
    if len(l) % 2 == 0:
        med = (l[(len(l) // 2) -1] + l[((len(l) // 2))])//2
    else:
        med = l[(len(l) // 2)]
    return med


print('Median is {0}'.format(medianfinder(nos)))
print('The Average is {0}'.format(averagefinder(nos)))
print ('mode is {0}'.format(modefinder(nos)))