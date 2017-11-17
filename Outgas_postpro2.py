'''
Created on Sep 19, 2012

@author: wange
'''

import math
from pylab import show,savefig
from scipy.constants import *
import matplotlib.pyplot as plt
import matplotlib.axis as axis
import numpy as np
from pprint import pprint
from Outgas_trans import *

def density(arr,part):
    a=[0 for i in range(part)]
    tick=Length/part
    for i in range(0,part):
        #print i
        for k in range(0,len(arr)):
            ##print arr[k]
            if tick*(i)<arr[k]<tick*(i+1):
                ##print arr[k],' ',tick,' ',tick*(i+1)
                a[i]=a[i]+1
        ##print a
    a[0]=a[0]/10
    a[1]=a[1]/10
    a[2]=a[2]/5
    return a
def graphfx(tstep,tt,ip,name,num):
    name_base=name
    for k in range(1,num+1):
        lend= endstate( tstep, tt*k/num, 2*int(Lengths/High), 2,2,'endp',ip)   ##1e-5,1e-3,2,2,'endp','sq or fx'
        lend1=[lend[0][0]]
        lend2=[lend[0][1]]
    ##print kk1,kk2
        for i in range(len(lend)):
            lend1.append( lend[i][ 0])
            lend2.append( lend[i][ 1])
   ## i=np.arange(0,10,1)
    ##print lend1,lend2
        plt.subplot(311)
        plt.plot(lend1, lend2,'b.')
        plt.xlabel('Length(m)')
        plt.ylabel('Heigth(m)')
        plt.title('Particle distribution in UHV_t='+str(tt*k/num)+'s')
        plt.axis([0,Length,0,High])
        plt.subplot(312)
        plt.hist(lend1,20,color='g')
        plt.xlabel('Length(m)')
        plt.ylabel('Particle #')
   ##xticks=np.arange(0,Length+0.1,0.2)
        plt.xlim(0,Length)
        i=np.linspace(0,Length,20+1)
        ##print len(i)
        ##print len(density(lend1,20+1))
        plt.subplot(313)
        plt.plot(i,density(lend1,20+1),'bo',color='g')
        plt.xlabel('Length(m)')
        plt.ylabel('Density')
     ##   print i,density(lend1,20+1)
        current_name=name_base+str(tt*k/num)+'.png'
        ##print current_name,tt, k ,num
        savefig(current_name,format='png') 
        
       
    
    
def graphsq(tstep,tt,ip,name,num):
    name_base=name
    for k in range(1,num+1):
        lend= endstate( tstep, tt*k/num, 2*int(Lengths/High), 2,2,'endp',ip)   ##1e-5,1e-3,2,2,'endp','sq or fx'
        lend1=[lend[0][0]]
        lend2=[lend[0][1]]
    ##print kk1,kk2
        for i in range(len(lend)):
            lend1.append( lend[i][ 0])
            lend2.append( lend[i][ 1])
   ## i=np.arange(0,10,1)
    ##print lend1,lend2
        plt.subplot(211)
        plt.plot(lend1, lend2,'bo')
        plt.xlabel('Length(m)')
        plt.ylabel('Heigth(m)')
        plt.title('Particle distribution in UHV_t='+str(tt*k/num)+'s')
        plt.axis([0,Length,0,High])
        plt.subplot(212)
        plt.hist(lend1,20,color='g')
        plt.xlabel('Length(m)')
        plt.ylabel('Particle #')
   ##xticks=np.arange(0,Length+0.1,0.2)
        plt.xlim(0,Length)
        current_name=name_base+str(tt*k/num)+'.png'
        savefig(current_name,format='png') 
        
       

def main():
    ip=str(raw_input('please input boundary(fx/sq):'))
    if ip=='fx':
        graphfx(5e-6,1e-1,ip,'5e-6_fx',50)
       
    elif ip=='sq':
        graphsq(5e-6,1e-1,ip,'5e-6_sq',50)



if __name__ == '__main__':
   main()