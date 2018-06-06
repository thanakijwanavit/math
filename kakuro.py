#!/usr/bin/env python3
import logging


# In[2]:


def sumarray(data):
    return sum(data)


# In[3]:


def gendice(length):
    data = [1]*length
    return data


# In[4]:


def isduplicate(A):
    d = {}
    for index, item in enumerate(A):
        if item in d:
            return 1
        else:
            d[item] = True
    return 0


# In[5]:


def checkrepeat(A):
    temp = []
    output = []
    for index, item in enumerate(A):
        if item in temp:
            output.append(item)
        else:
            temp.append(item)
    return output


# In[6]:


def listnumbers(list1,possible):
    output=[]
    flat_list = [item for sublist in list1 for item in sublist]
    for i in possible:
        if i in flat_list:
            output.append(i)
    return output
            


# In[7]:


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


# In[8]:


def listpossible(toplength,topsum,sidelength,sidesum,impossible=[]):
    possible=[x for x in [1,2,3,4,5,6,7,8,9] if x not in impossible]
    topdice= gendice(toplength)[:]
    sidedice= gendice(sidelength)[:]
    toppossible=listnumbers(listfaces(topdice,topsum,bigdata=[],possible = possible)['bigdata'],possible)
    sidepossible=listnumbers(listfaces(sidedice,sidesum,bigdata=[],possible = possible)['bigdata'],possible)
    dualpossible=checkrepeat(toppossible[:]+sidepossible[:])
    
    return {'toppossible':toppossible,'sidepossible':sidepossible,'dualpossible':dualpossible}


# In[ ]:


print(listpossible(2,8,9,45,impossible=[]))


# In[ ]:




