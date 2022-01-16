import math as m
g=3.5
f,i=m.modf(g)
print(i,f)
print(f*12)
print(m.ceil(f*12))
print(i*12)
print("Total Months={0:.2f}".format(int(i*12+m.ceil(f*12))))
