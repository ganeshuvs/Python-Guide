
# coding: utf-8

# In[7]:


def myfibo(n):
    a,b = 0,1
    fibolist = list()
    
    while True:
        fibolist.append(a)
        a,b = b,a+b
        if a>n:
            break
    
    print('__name__ is:',__name__)
    return fibolist


# In[8]:


myfibo(100)

