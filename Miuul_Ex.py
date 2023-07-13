#!/usr/bin/env python
# coding: utf-8

# In[1]:


#mission_one
x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l= [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}
letters = [x, y, z, a, b, c, l, d, t, s]
for i in letters:
    print(type(i))


# In[2]:


#mission_2.1
text = "The goal is to turn data into information, and information into insight."
text = text.upper()
new_text = []
text = text.replace(',', '').replace('.', ' ')
temp = ""
for i in text:
    if i != ' ':
        temp += i
    else:
        new_text.append(temp)
        temp = ""

print(new_text)

#mission_2.2
text = text.upper()
text = text.replace(',', ' ').replace('.', ' ')
words = text.split()

print(words)


# In[3]:


#mission_3
lst = ["D", "A", "T","A","S","C","I","E","N","C","E"]
print("Step 1: " + str(len(lst)))
print("Step 2: " + str(lst[0]) + " " + str(lst[10]))
print("Step 3: " + str(lst[0:4]))
lst.remove(lst[8])
print("Step 4: " + str(lst))
lst.append('Q')
print("Step 5: " + str(lst))
lst.insert(8, 'N')
print("Step 6: " + str(lst))


# In[4]:


#mission_4
dict = {'Cristian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

print("Step 1: " + str(dict.keys()))
print("Step 2: " + str(dict.values()))
dict['Daisy'][1] = 13
print("Step 3: " + str(dict))
#dict['Ahmet'] = ["Turkey", 24]
dict.update({'Ahmet': ["Turkey", 24]})
print("Step 4: " + str(dict))
dict.pop('Antonio')
print("Step 5: " + str(dict))


# In[5]:


#mission_5
l = [2, 13, 18, 93, 22]
def func(lis):
    even = []
    odd = []
    for i in lis:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd
even_l, odd_l = func(l)
print(even_l)
print(odd_l)


# In[6]:


#mission_6
students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, student in enumerate(students, 1):
    if index < 4:
        print("Mühendislik Fakültesi " + str(index) + ". öğrenci: " + student)
    else:
        print("Tıp Fakültesi " + str(index - 3) + ". öğrenci: " + student)


# In[7]:


#mission_7
ders_kodu = ["CMP1005", "PYS1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

zipped = list(zip(ders_kodu, kredi, kontenjan))
for i in zipped:
    print(f"Kredisi {i[1]} olan {i[0]} kodlu dersin kontenjanı {i[2]} kişidir")


# In[10]:


#mission_8
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if kume1.issuperset(kume2):
    ortak_elemanlar = kume1.intersection(kume2)
    print(ortak_elemanlar)
else:
    fark = kume2.difference(kume1)
    print(fark)


# In[ ]:




