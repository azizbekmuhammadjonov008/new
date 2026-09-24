# Bu vazifa javobi 1-masala.py faylida bo’lishi shart.  
# Ikki lug‘atni birlashtiruvchi funksiya yozing. Agar bir xil kalit bo‘lsa,qiymatlarining yig’indisi olinsin.
# Input: 
# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"b": 4, "d": 5}

# Output: {"a": 1, "b": 6, "c": 3, "d": 5}

import os
os.system('cls')


def func1(dic1,dic2):
    new = {}
    for i in d1:
        new[i] = d1[i]
    for i in d2:
        if i in new:
            new[i] = new[i] + d2[i]
        else:
            new[i] = d2[i]
    return new
            
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "d": 5}

natija = func1(d1,d2)
        
print('Natija:',natija)
