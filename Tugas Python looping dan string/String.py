#!/usr/bin/env python
# coding: utf-8

# In[1]:


nama_lengkap = input ("Masukkan Nama Anda : ")

# Menghitung jumlah huruf dari nama lengkap
jumlah_huruf = len(nama_lengkap.replace(" ", ""))

# Menghitung jumlah huruf vokal dari nama lengkap
huruf_vokal = "aiueoAIUEO"
jumlah_vokal = len([char for char in nama_lengkap if char in huruf_vokal])

# Menghitung jumlah huruf konsonan dari nama lengkap
jumlah_konsonan = jumlah_huruf - jumlah_vokal

print("Jumlah huruf dari nama lengkap Anda adalah:", jumlah_huruf)
print("Jumlah huruf vokal dari nama lengkap Anda adalah:", jumlah_vokal)
print("Jumlah huruf konsonan dari nama lengkap Anda adalah:", jumlah_konsonan)


# In[ ]:




