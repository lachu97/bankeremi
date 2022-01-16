import math
import argparse as arg
def calcexp(a,b):
    return math.pow(a,b)
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def sub(a,b):
    return a-b
def interest(p,i,n):
    i=i/100
    return divide(multiply(p,i),sub(1,calcexp(1+i,-n)))
parser = arg.ArgumentParser()
parser.add_argument("-p",help="= Principal Amount in Rs",type=float,required=True)
parser.add_argument("-i",help="= Rate of Interest in %  for per year",type=float,required=True)
parser.add_argument("-y",help="= Number of Years",type=int,required=True)
fields= parser.parse_args()
p = fields.p
i = fields.i
year = fields.y
n=int(year)*12
r=float(i)/12

emi=interest(int(p),r,n)
amount=emi*n - float(p)

print("Principal= "+str(p))
print("Monthly EMI in Rs for {0} months".format(n))
print(math.ceil(emi))
print("Total Amount Paid as Interest for the Whole amount in Rs= ")
print(math.ceil(emi*n))
print("Amount paid extra as Interest in Rs")
print(math.ceil(amount))

