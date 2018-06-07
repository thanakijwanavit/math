#!/usr/bin/env python3
import logging
from time import time


# In[3]:


def sumarray(data):
    return sum(data)


# In[4]:


def gendice(length):
    data = [1]*length
    return data


# In[5]:


def isduplicate(A):
    d = {}
    for index, item in enumerate(A):
        if item in d:
            return 1
        else:
            d[item] = True
    return 0


# In[6]:


def checkrepeat(A):
    temp = []
    output = []
    oappend = output.append
    tappend = temp.append
    for index, item in enumerate(A):
        if item in temp:
            oappend(item)
        else:
            tappend(item)
    return output


# In[7]:


def listnumbers(list1,possible):
    output=[]
    oappend = output.append
    flat_list = [item for sublist in list1 for item in sublist]
    for i in possible:
        if i in flat_list:
            oappend(i)
    return output
            


# In[8]:


def listfaces(dice,requiredscore,index=99,match=0,list=[],bigdata=[],possible=[1,2,3,4,5,6,7,8,9]):
    listfeed=[]
    if (index==99):
        index=len(dice)-1
    for i in possible:
        dice[index]=i
        if(index ==0):
            if (sumarray(dice)==requiredscore):
                if not isduplicate(dice):
                    listfeed.append(dice[:])
        elif(index > 0):
            if(listfaces(dice,requiredscore,index=(index-1),bigdata=bigdata)['listfeed'] and not isduplicate(dice)):
                bigdata.append(listfaces(dice,requiredscore,index=(index-1),bigdata=bigdata)['listfeed'][0])
    return {'dice':dice,'bigdata':bigdata,'listfeed':listfeed,'possibilities':len(bigdata)}


# In[9]:


def listpossible(toplength,topsum,sidelength,sidesum,impossible=[]):
    possible=[x for x in [1,2,3,4,5,6,7,8,9] if x not in impossible]
    topdice= gendice(toplength)[:]
    sidedice= gendice(sidelength)[:]
    toppossible=listnumbers(listfaces(topdice,topsum,bigdata=[],possible = possible)['bigdata'],possible)
    sidepossible=listnumbers(listfaces(sidedice,sidesum,bigdata=[],possible = possible)['bigdata'],possible)
    dualpossible=checkrepeat(toppossible[:]+sidepossible[:])
    
    return {'toppossible':toppossible,'sidepossible':sidepossible,'dualpossible':dualpossible}


# In[19]:


t0 = time()
var=listpossible(2,13,2,14,impossible=[])
t1 = time()
print(var)
print ('the function took %s seconds to run' % (t1-t0))


# In[ ]:




