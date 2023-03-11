#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input())
a = 0
b = 1
for i in range(n):
	if i == 0:
		continue
	print(a, end=" ")
	for j in range(i):
		temp = a
		a = b
		b = temp + b
		print(a, end=" ")
	print()
	a = 0
	b = 1


# In[2]:





# In[ ]:




