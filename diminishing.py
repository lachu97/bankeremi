#import bank as bk
n=24
p=float(30000)
emi=float(300)
i=0.06
mi=float(i/12)
l=[p]
for term in range(0,n):
    t_i=float(mi*l[-1])     #Interest
    t_p=float(emi-t_i)      #amp ount towards principal
    p=p-t_p
    l.append(p)
    print("Int={0},Pto={1},bl={2}".format(t_i,t_p,l[-1]))