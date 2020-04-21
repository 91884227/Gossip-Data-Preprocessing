#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import pandas as pd
import numpy as np
import re
from itertools import compress
from tqdm import tqdm
import sys


# In[2]:


def str_contain_keyword(str_):
    conditions = ["[新聞]", "Re:", "[公告]", "Fw:"]
    #global CONDITIONS
    #conditions = CONDITIONS
    buf = any([str_.startswith(i)  for i in conditions])
    return(buf)


# In[3]:


def str_adjust(str_):
    buf = str_
    try:
        m = re.match(r'(\[.*\] ?)(.*)', str_)
        buf = m.group(2)
#         if(len(buf) < 5):
#             print("to short: %s\n" % str_)
    except:
        pass
        #print("error happend: %s\n" % str_)
        #print("error happend")
    return(buf)


# In[4]:


if __name__ == '__main__':

    #FIALNAME = "Gossip_title_30000_to_39040.csv"
    FIALNAME =  sys.argv[1]
    MIN_LENGTH = 10
    CONDITIONS = ["[新聞]",  "Re:",  "[公告]",  "Fw:"]

    print("read %s in " % FIALNAME)
    df = pd.read_csv(FIALNAME, encoding="utf-8")
    #df = pd.read_csv(FIALNAME, encoding="gb2312")
    title = df.title.to_numpy()

    print("delete title starting with %s" %  CONDITIONS)
    bool_want = [not str_contain_keyword(i) for i in tqdm(title)]
    title_A = list(compress(title, bool_want))

    print("adjust title e.g. %s " %  "[問卦] 國王的女兒說我性侵她該怎麼辦？ -> 國王的女兒說我性侵她該怎麼辦？")
    title_B = [str_adjust(i) for i in tqdm(title_A)]

    print("delete title that len(title) < %d" % MIN_LENGTH)
    title_length = [len(i) for i in title_B]
    bool_want = np.array(title_length) > 10
    title_C = list(compress(title_B, bool_want))

    # save
    name = "%s_adjust.npy" % FIALNAME[:-4]

    try:
        np.save(name, title_C)
        print("preprocessing successfully")
        print("save as %s" % name)
    except:
        print("preprocessing failed")


# In[ ]:





# In[ ]:




