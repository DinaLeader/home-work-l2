'''
name : dina
last name: rahbar 
---------- LIST FUNCTIONS ----------
append(+)	 Adds an element at the end of the list
clear(+)    	Removes all the elements from the list
copy(+)      Returns a copy of the list
count(+)	    Returns the number of elements with the specified value
extend(+)	Add the elements of a list (or any iterable), to the end of the current list
index(+) 	Returns the index of the first element with the specified value
insert(+)	Adds an element at the specified position
pop(+)	    Removes the element at the specified position
remove(+)	Removes the first item with the specified value
reverse(+)	Reverses the order of the list
sort(+)     	Sorts the list
'''
#append()
a = ['dina' , 'dorsa']
a.append('delsan')
print(a) #['dina', 'dorsa', 'delsan']
#yek meghdar ro be akhare list ezafe mikone.


#clear()
b = ['dina' , 'dorsa' , 'delsan']
b.clear()
print(b) #[]
#tamame ozvaye list ro pak mikone va list ro khali mikone.



#copy()
d = a.copy()
print(d) #['dina', 'dorsa', 'delsan'] 
#yek copye joda az list misaze.



#count()
e = ['dina' , 'sara' , 'dorsa' , 'dina']
print(e.count('dina')) #2
#tedade tekrare yek meghdar ro dar list hesab mikone.



#extend()
f = ['dina' , 'dorsas']
g = ['sara' , 'sarah']
f.extend(g)
print(f) #['dina', 'dorsas', 'sara', 'sarah']
#ozvaye yek iterable ro yeki yeki be akhare list ezafe mikone.
'''
append() → yek chiz ezafe mikone
extend() → chand ozv ro yeki yeki ezafe mikone
'''


#index()                         ['dina', 'dorsa', 'delsan']
print(a.index('dorsa')) #1          0        1        2
#indexe avalin bar peyda shodane yek meghdar ro dar list barmigardoone.



#insert()
h = ['dina' , 'dorsa' , 'delsan']
h.insert(1, 'sara')
print(h) #['dina', 'sara', 'dorsa', 'delsan']
#yek meghdar ro dar index-e moshakhas shode be list ezafe mikone.



#pop()
i = ['dina' , 'dorsa' , 'delsan']
i.pop(1) 
print(i) #['dina', 'delsan']


j = ['dina' , 'dorsa' , 'delsan']
k = j.pop()
print(j) #['dina', 'dorsa']
print(k) #delsan
#yek index ro az list hazf mikone va meghdare hazf shode ro bargardoone.
#pop()  → akharin index ro hazf mikone
#pop(2)  → indexe 2 ro hazf mikone



#remove()
l = ['dina' , 'dorsa' ,'sara']
l.remove('sara')
print(l) #['dina', 'dorsa']
#yek meghdar-e moshakhas ro az list hazf mikone.



#reverse()
m = ['dina' , 'dorsa' ,'delsan']
m.reverse()
print(m) #['delsan', 'dorsa', 'dina']
#tartibe ozvaye list ro baraks mikone.



#sort()
n = ['dina', 'reza' , 'dorsa' , 'ali']
n.sort()
print(n) #['ali', 'dina', 'dorsa', 'reza']
#ozvaye list ro be tartine alefba ya koochik bozorg boodan moratab mikone.

