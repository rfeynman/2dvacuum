'''
Created on Sep 14, 2012

@author: wange
This code generate a end particles state list
the multipar() statement:
multipar(tstep,tt,Num,b) where tstep is step time, tt is total time duration,Num is initial particle number and b is location
the function return a listoflist of end particles state [[time,x position, y postion,vx,vy,exsit],...[]]
'''

import math
import random
from scipy.stats import maxwell
from pylab import show
from scipy.constants import *
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from Outgas_initial import *

##k=[0, 0.02, 0, -60.097725927514141, 52.630120103224506,1 ] ##[1]:time, [2]:x,[3]:y,[4]vx,[5]vy
def sqmove(tstep,tt,single,r):    ## move(*,x),x=1 return process,x=0 return end state
    n=int(tt/tstep) ##tt:total time
    ss=[]
 
    for i in range(n):
        single[ 0]=single[ 0]+tstep*i
        single[ 1]=single[ 1]+tstep*single[ 3]
        single[ 2]=single[ 2]+tstep*single[ 4]
        ##print single[0:5]
        if single[ 1]< 0:   ## if particle out of edge, than change the speed sign
            single[ 3]=-single[ 3]
        else: single[ 3]=single[ 3]
        if single[ 2]< 0 or single[ 2]>High:
            single[ 4]=-single[ 4]
        else: single[ 4]=single[ 4]
        if single[ 1]>Length:
            single[ 5]= 0
        isingle=[single[ 0],single[ 1],single[ 2],single[ 3],single[ 4],single[ 5 ]]## generation one particles state in process
        ss.append(isingle)  ## ss : generate a list including all the state in process
    if r==0:
        return single ## single: one paarticle end state
    else:
        return ss
   
def fxmove(tstep,tt,single,r):    ## move(*,x),x=1 return process,x=0 return end state
    n=int(tt/tstep) ##tt:total time
    ss=[]
 
    for i in range(1,n):
        single[ 0]=single[ 0]+tstep*i
        single[ 1]=single[ 1]+tstep*single[ 3]
        single[ 2]=single[ 2]+tstep*single[ 4]
        ##print single[0:5]
        if single[ 1]< 0:   ## if particle out of edge, than change the speed sign
            single[ 3]=-single[ 3]
        elif single[ 2]>Highs and Lengths+single[ 3]*tstep>=single[ 1]>=Lengths:
            single[ 3]=-single[ 3]
        else: single[ 3]=single[ 3]
       
        if single[ 2]< 0 or single[ 2]>High:
            single[ 4]=-single[ 4]
        elif single[ 1]>Lengths and Highs+single[ 4]*tstep>=single[ 2]>=Highs:
            single[ 4]=-single[ 4]
        else: single[ 4]=single[ 4]
       
        if single[ 1]>Length:
            single[ 5]= 0
        isingle=[single[ 0],single[ 1],single[ 2],single[ 3],single[ 4],single[ 5 ]]## generation one particles state in process
        ss.append(isingle)  ## ss : generate a list including all the state in process
    if r==0:
        return single ## single: one paarticle end state
    else:
        return ss

def multipar_oneb(tstep,tt,Num,b,bd): ## from one boundary particles' end state
    rp=Random_particles(Num,b)
    if bd=='sq' :
        for i in range(int(Num)):
            rp[i]=sqmove(tstep,tt,rp[i], 0)
    elif bd=='fx' :
        for i in range(int(Num)):
            rp[i]=fxmove(tstep,tt,rp[i], 0)
    return rp

def multipar(tstep,tt,Num_ub,Num_l,Num_t,bd): ## from all boundary particles' end state
    if bd=='sq' :
        mpl=multipar_oneb(tstep,tt,Num_l, 'left',' sq')
        mpl.extend(multipar_oneb(tstep,tt,Num_ub, 'up',' sq'))
        mpl.extend(multipar_oneb(tstep,tt,Num_ub, 'bottem','sq' ))
    elif bd=='fx' :
         mpl=multipar_oneb(tstep,tt,Num_ub, 'left','fx' )
         ##mpl.extend(multipar_oneb(tstep,tt,Num_ub, 'up',' fx'))
         mpl.extend(multipar_oneb(tstep,tt,Num_t, 'bottem','fx' ))
         mpl.extend(multipar_oneb(tstep,tt,Num_t, 'up_l', 'fx'))
         mpl.extend(multipar_oneb(tstep,tt,Num_ub, 'up_h', 'fx'))
         mpl.extend(multipar_oneb(tstep,tt,Num_ub, 'left_r', 'fx'))
    return mpl
  

def endstate(tstep,tt,Num_ub,Num_l,Num_t,s,bd): ## from all boundary particles' end state in static in the active range
    N=int(tt/tstep)
    ends=[]
    for i in range(N/10):
        ends.extend(multipar(tstep,( 10*i+ 1)*tstep,Num_ub,Num_l,Num_t,bd))
    ends=filter(lambda(ends):ends[ 5]== 1,ends)
    ends=filter(lambda(ends):ends[1]<=Lengths or ends[2]<=Highs,ends)
    endp=[]
    for i in range(len(ends)):
        endp.extend( [ends[i][ 1: 3]])
   
    if s=='ends': ## return end full list
        return ends
    elif s=='endp' :## return end partile position
        f=open( 'endp.txt','w' )
        f.write(str(endp))
        f.close()
        return endp


def main():
    ##print len(endstate( 1e-5, 5e-3, 2, 2,'endp'))
    pprint(endstate( 1e-5, 5e-3, 2, 2,1,'endp' ,'fx'))
    print Lengths, High
    ##pprint(endstate( 5e-6, 1e-3, 2*int(Lengths/High), 2,1,' endp','fx '))
    ##pprint(multipar_oneb(1e-5, 5e-3, 2, 'up'))
    ##pprint(multipar(1e-5, 5e-3, 2, 2))
   

    '''
    rp=Random_particles(1000,'up')
    print move(1e-5,5e-3,k,0), ' ', rp[1]
  
    kk=move(1e-5,5e-3,k,1)
    kk1=[ kk[0][1]]
    kk2=[ kk[0][5]]
    print kk1,kk2
    for i in range(500):
        kk1.append( kk[i][ 1])
        kk2.append( kk[i][ 2])
   ## i=np.arange(0,10,1)
    print kk1,kk2
    plt.plot(kk1, kk2)
    show()
   '''

 
 
if __name__=='__main__':
    main()
