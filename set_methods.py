'''
name : dina
last name : rahbar
---------- SET METHODS ----------
add(+)	 	
clear(+)	 	
copy(+)	 	
difference(+)	
difference_update(+)		
discard(+)	 	
intersection(+)	
intersection_update(+)   
isdisjoint(+)	 	
issubset(+) 
issuperset(+)
pop(+)	 
remove(+)	
symmetric_difference(+)		
symmetric_difference_update(+)		
union(+)	
update(+)		


set : 
    1. not ordered
    2. not duplicates
    3. mutable
    4. indexed
'''

#add()
a = {'dina' , 'dorsa'}
a.add('delsan')
print(a) #{'dorsa', 'delsan', 'dina'}
#yek ozv jadid be set ezafe mikone.



#clear
b = {'dorsa', 'delsan', 'dina'}
b.clear()
print(b) #set()



#copy()
c = {'dorsa', 'delsan', 'dina'}
d = c.copy()
print(d) #{'dina', 'dorsa', 'delsan'}
#yek copye joda az set misaze.



#difference_update()
e = {'dorsa', 'delsan', 'dina'}
f = {'dina', 'delsan', 'ali'}
g = e.difference(f)
print(g) #{'dorsa'}
# ozvayi ke faghat dar sete aval hastan ro bargardoone.




#difference_update()
h = {'dorsa', 'delsan', 'dina'}
i = {'dina', 'delsan', 'ali'}
h.difference_update(i)
print(h) #{'dorsa'}
# ozvayi ke dar sete dovom hastan ro az sete aval hazf mikone.



#discard()
j = {'dorsa', 'delsan', 'dina'}
j.discard('delsan')
print(j) #{'dina', 'dorsa'}
# yek ozv-e moshakhas ro az set hazf mikone.



#intersection()
k = {'dorsa', 'delsan', 'dina'}
l = {'dina', 'delsan', 'ali'}
m = k.intersection(l)
print(m) #{'dina', 'delsan'}
# ozvaye moshtarak-e do set ro bargardoone.



#intersection_update()
n = {'dorsa', 'delsan', 'dina'}
o = {'dina', 'delsan', 'ali'}
n.intersection_update(o)
print(n) #{'dina', 'delsan'} 
# faghat ozvaye moshtarak ro dar sete aval negah midare.



#isdisjoint()
p = {'dorsa', 'delsan', 'dina'}
q = {'ali', 'reza', 'sara'}
print(p.isdisjoint(q)) #True



#issubset()
r = {'dina', 'delsan'}
s = {'dorsa', 'delsan', 'dina', 'ali'}
print(r.issubset(s)) #True

r1 = {'dina', 'reza'}
s1 = {'dorsa', 'delsan', 'dina', 'ali'}
print(r1.issubset(s1)) #False
# check mikone ke aya tamame ozvaye set-e aval dar sete dovom vojood daran ya na.



#issuperset()
t = {'dorsa', 'delsan', 'dina', 'ali'}
u = {'dina', 'delsan'}
print(t.issuperset(u)) #True

t1 = {'dorsa', 'delsan', 'dina'}
u1 = {'dina', 'ali'}
print(t1.issuperset(u1)) #False
# check mikone ke aya tamame ozvaye sete dovom dar sete aval vojood daran ya na.



#pop()
v = {'dorsa', 'delsan', 'dina'}
w = v.pop()
print(v) #{'dorsa', 'delsan'}
print(w) #dina
# yek ozv ro az set hazf mikone va hamoon ozv ro bargardoone.



#remove()
x = {'dorsa', 'delsan', 'dina'}
x.remove('delsan')
print(x) # {'dina', 'dorsa'}
# yek ozv-e moshakhas ro az set hazf mikone.



#symmetric_difference()
a2 = {'dorsa', 'delsan', 'dina'}
b2 = {'dina', 'delsan', 'ali'}
c2 = a2.symmetric_difference(b2)
print(c2) #{'dorsa', 'ali'} 
# ozvayi ke faghat dar yeki az do set hastan ro bargardoone.



#symmetric_difference_update() 
d2 = {'dorsa', 'delsan', 'dina'}
e2 = {'dina', 'delsan', 'ali'}
d2.symmetric_difference_update(e2)
print(d2) #{'dorsa', 'ali'}
## ozvaye moshtarak ro hazf mikone va ozvaye gheyrmoshtarak ro negah midare.



#union() 
f2 = {'dorsa', 'delsan', 'dina'}
g2 = {'dina', 'delsan', 'ali'}
h2 = f2.union(g2)
print(h2) #{'dorsa', 'delsan', 'dina', 'ali'}
# ozvaye har do set ro ba ham tarkib mikone va tekrari ha ro hazf mikone.




#update()
i2 = {'dorsa', 'delsan', 'dina'}
j2 = {'dina', 'delsan', 'ali'}
i2.update(j2)
print(i2) #{'dorsa', 'delsan', 'dina', 'ali'} 
# ozvaye sete dovom ro be sete aval ezafe mikone va tekrari ha ro nadide migire.
''' union()  → set jadid misaze
update() → khode set aval ro taghir mide '''
