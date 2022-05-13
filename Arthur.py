#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image
from IPython.display import display
import numpy as np


# In[ ]:


x = Image.open("...") #图像路径，注意I大写


# In[ ]:


display(x)


# In[ ]:


A = np.array(x)


# In[ ]:


A


# In[ ]:


B = np.full(A.shape,255)-A


# In[ ]:


B


# In[ ]:


B = B.astype(np.uint8)


# In[ ]:


display(Image.fromarray(B))

