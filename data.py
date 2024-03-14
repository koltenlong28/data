import matplotlib.pyplot as plt

dataFile = open('ViolentCrimes.txt')

crimesList = dataFile.readlines()

print(crimesList)

for i in range(len(crimesList)):
    crimesList[i]= int(crimesList[i])

plt.xlabel("years")
plt.ylabel("violent crimes")
plt.ion
plt.isinteractive
plt.subplots(1,2)
plt.plot(range(1999,2019),crimesList,'r.--',markersize=5)
plt.axis([1999,2020,0,2500000])
plt.show()
