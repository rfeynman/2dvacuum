
'''
Created on Sep 12, 2012

@author: wange

This code generate a initial particles list
the Random_particles statement:
Random_particles( number, b) where number is initial particle number and b is location
the function return a list[time,x position, y postion,vx,vy,exsit]
'''
import math
import random
from scipy.stats import maxwell
from pylab import show
from scipy.constants import *
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
 
u=1/(6.022*(10**23)) ## C12 mass
m=1.00794*2*u  ## H2 mass
kb=1.38*(10**(-23)) ## boltzmann constant
pi=math.pi## pi
T=293 ##temperature
High=0.01
Length=1.0
Highs=High/10
Lengths=Length/10

def Max_bolt(v):  ## Maxwell b distribution
    return 4*pi*(m/(2*pi*kb*T))**( 3/ 2)*(v** 2)*np.exp(-m*(v** 2)/( 2*kb*T))



def Random_max(length): ## random maxwell distribution
    a=(m/(kb*T))**0.5
    scales=1/(a)
    return maxwell.rvs(scale=scales,size=length)

##def Randomlist( Num,mi ,ma):
##  Rlist=[]
##  for i in range(Num):
  ##      Rlist.append(random.uniform(mi ,ma))
  ##  return Rlist
 

def Random_particles(Num,b):  ## Num : particles number, b is the edge for'left','top','bottem'
    Vx=Random_max(Num+1)*( 2**(- 0.5)) ## velocity x direction
    Vy=Random_max(Num+1)*( 2**(- 0.5)) ## velocity y direction
 
    if b=='up':
        Ptsi=[ 0,random.uniform( 0,Length),High,Vx[ 1],-Vy[ 1], 1]
        Pts=[Ptsi]
        for i in range(Num- 1):
            Pts.append([ 0,random.uniform( 0,Length),High,random.choice([- 1 , 1 ])*Vx[random.randint(0,Num)],-Vy[random.randint( 0 ,Num)], 1 ])
    elif b=='up_h':
        Ptsi=[ 0,random.uniform( 0,Lengths),High,Vx[ 1],-Vy[ 1], 1]
        Pts=[Ptsi]
        for i in range(Num- 1):
            Pts.append([ 0,random.uniform( 0,Lengths),High,random.choice([- 1 , 1 ])*Vx[random.randint(0,Num)],-Vy[random.randint( 0 ,Num)], 1 ])
    elif b=='up_l':
        Ptsi=[ 0,random.uniform( Lengths,Length),High,Vx[ 1],-Vy[ 1], 1]
        Pts=[Ptsi]
        for i in range(Num- 1):
            Pts.append([ 0,random.uniform( Lengths,Length),High,random.choice([- 1 ,1 ])*Vx[random.randint(0 ,Num)],-Vy[random.randint( 0,Num)], 1])
    elif b=='left':
        Ptsi=[ 0, 0,random.uniform( 0,High),Vx[ 1],Vy[ 1], 1]
        Pts=[Ptsi]
        for i in range(Num- 1):
            Pts.append([ 0, 0,random.uniform( 0,High),Vx[random.randint( 0 ,Num)],random.choice([-1,1 ])*Vy[random.randint( 0,Num)], 1])
    elif b=='left_r':
        Ptsi=[ 0, Lengths,random.uniform( Highs,High),Vx[ 1],Vy[ 1], 1]
        Pts=[Ptsi]
        for i in range(Num- 1):
            Pts.append([ 0, Lengths,random.uniform( Highs,High),-Vx[random.randint(0 ,Num)],random.choice([-1,1])*Vy[random.randint( 0,Num)], 1 ])
    elif b=='bottem':
        Ptsi=[ 0,random.uniform( 0,Length), 0,Vx[ 1],Vy[ 1], 1]
        Pts=[Ptsi]
        for i in range(Num- 1):
            Pts.append([ 0,random.uniform( 0,Length), 0,random.choice([- 1 , 1 ])*Vx[random.randint(0,Num)],Vy[random.randint( 0 ,Num)], 1 ])
    return Pts   #return a list of list pts[[time,x position,y position,x speed,y speed,1],...],every particles is a list,where 1 is exsit and 0 is disappear
 
     
     
 
##def Boundary(left,right,up,bottom):
 ##   if left==1:
     

 
def main():
    ##pprint(Random_particles( 5, 'left_r'))## generate maxwell distribution particles ar the edge
    pprint(Random_max(10))
    ##x=np.arange(0,500,1)
    ##plt.plot(x, 0.0117*Max_bolt(x))
    ##plt.hist(Random_max(10000),20,normed=1)
    ## plt.hist(Random_max(50,10000),10,color='r')
    ##show()
    print Lengths, High
 
 
if __name__=='__main__':
    main()

    
