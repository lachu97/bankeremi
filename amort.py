#import bank as bk
import argparse as arg
import math as m
def calculate_amount(*args):
    for c in args:
        print(c.p,c.y,c.i,c.e)
        f,integer=m.modf(c.y)
        n=int(integer*12+m.ceil(f*12)) 
        p=float(c.p)
        emi=float(c.e)
        i=float(c.i/100)
    mi=float(i/12)
    l=[p]
    for term in range(0,n):
        if l[-1] > 0 :
            t_i=float(mi*l[-1])     #Interest
            t_p=float(emi-t_i)      # amount towards principal
            p=p-t_p                 
            l.append(p)
            print("No.{0} Interest={1:.2f},PtP={2:.2f},bal={3:.2f},EMI={4:.2f}".format(term+1,t_i,t_p,l[-1],emi))
        else:
            break
parser = arg.ArgumentParser()
parser.add_argument("-p",help="= Principal Amount in Rs",type=float,required=True)
parser.add_argument("-i",help="= Rate of Interest in %  for per year",type=float,required=True)
parser.add_argument("-y",help="= Number of Years in whole number",type=float,required=True)
parser.add_argument("-e",help="= Monthly EMI",type=float,required=True)
fields= parser.parse_args()
calculate_amount(fields)