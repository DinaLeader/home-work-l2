'''
name : dina
lasr name : rahbar 
---------- DICTIONARY METHODS ----------
clear(+)  	Removes all the elements from the dictionary
copy(+)  	Returns a copy of the dictionary
fromkeys(+)	Returns a dictionary with the specified keys and value
get(+)   	Returns the value of the specified key
items(+)	    Returns a list containing a tuple for each key value pair
keys(+)	     Returns a list containing the dictionary's keys
pop(+)	      Removes the element with the specified key
popitem(+)   	Removes the last inserted key-value pair
setdefault(+)	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update(+)	   Updates the dictionary with the specified key-value pairs
values(+)	  Returns a list of all the values in the dictionary

'''
me = {'name' : 'dina' , 
      'last name' : 'rahbar' , 
      'city' : 'tehran' ,
      'grade' : '8' ,
      'age' : '14' }

#clear()
me.clear()
print(me) #{}
#tamame key va value haye dictionary ro pak mikone.



#copy()
my_copy = me.copy()
#yek copye joda az dictionary misaze.



#fromkeywords()
new_me = me.fromkeys('abcd') 

you = ['name' , 'last name' , 'city' , 'grade' , 'age']
new_you = dict.fromkeys(you, "unknown")
print(new_you) #{'name': 'unknown', 'last name': 'unknown', 'city': 'unknown', 'grade': 'unknown', 'age': 'unknown'} 
#az yek list az keyha yek dictionary jadid misaze va valuee moshtarak barashoon mizar.



#get()
me.get('name') #'dina'
#ya mitoonim injori benevisim :: 
n = me['name'] #'dina'
print(n) #dina
#value yek key ro az dictionary barmigardoone.


#items() 
me.items() # dict_items([('name', 'dina'), ('last name', 'rahbar'), ('city', 'tehran'), ('grade', '8'), ('age', '14')])
#tamame key va value ha ro be sorate joft bar migardoone.



#keys()
me.keys() #dict_keys(['name', 'last name', 'city', 'grade', 'age'])
#tamame key haye dictionary ro barmigardoone.



#pop()
x = me.pop('city')
print(x) #tehran
print(me) #{'name': 'dina', 'last name': 'rahbar', 'grade': '8', 'age': '14'}
#yek key ro ba valuesh az dictionary hazf mikone va mitoone value ro bargardoone.



#popitem()
g = me.popitem()
print(g) #('age', '14') ---> tuple
print(me) #{'name': 'dina', 'last name': 'rahbar', 'grade': '8'} 
#akharin key va value ro az dictionary hazf mikone va mitoone be sorate tuple bargardoone.



#setdefault()
a = me.setdefault('hobby' , 'listening to music')
print(a) #listening to music
print(me) #{'name': 'dina', 'last name': 'rahbar', 'grade': '8', 'hobby': 'listening to music'} 
#age key vojood dashte bashe valuesh ro barmigardoone, agar nabashe key ro ezafe mikone.



#update()
me.update({ 'age' : '15' , 'twins name' : 'dorsa' })
print(me) #{'name': 'dina', 'last name': 'rahbar', 'grade': '8', 'hobby': 'listening to music', 'age': '15', 'twins name': 'dorsa'}
#key/value haye jadid ro ezafe mikone ya value key haye mojood ro taghir mide.




#values()
print(me.values()) #dict_values(['dina', 'rahbar', '8', 'listening to music', '15', 'dorsa'])
#tamame value haye dictionary ro bargardoon mikone.



