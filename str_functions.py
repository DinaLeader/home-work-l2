'''
name : dina
last name : rahbar 
---------- STR FUNCTIONS ----------
-capitalize(+)	 Converts the first character to upper case
-casefold(+)	     Converts string into lower case
-center(+)	     Returns a centered string
-count(+)	     Returns the number of times a specified value occurs in a string
-encode(+)	     Returns an encoded version of the string
-endswith(+)      Returns true if the string ends with the specified value
-expandtabs(+)    Sets the tab size of the string
-find(+)	         Searches the string for a specified value and returns the position of where it was found
-format(+)	     Formats specified values in a string
-format_map(+)	 Formats specified values from a dictionary in a string
-index(+)	     Searches the string for a specified value and returns the position of where it was found
-isalnum(+)	     Returns True if all characters in the string are alphanumeric
-isalpha(+)	     Returns True if all characters in the string are in the alphabet
-isascii(+)	     Returns True if all characters in the string are ascii characters
-isdecimal(+)   	 Returns True if all characters in the string are decimals
-isdigit(+)	     Returns True if all characters in the string are digits
-isidentifier(+)	 Returns True if the string is an identifier
-islower(+)	     Returns True if all characters in the string are lower case
-isnumeric(+)	 Returns True if all characters in the string are numeric
-isprintable(+)	 Returns True if all characters in the string are printable
-isspace(+)	     Returns True if all characters in the string are whitespaces
-istitle(+)	     Returns True if the string follows the rules of a title
-isupper(+)	     Returns True if all characters in the string are upper case
-join(+)	         Converts the elements of an iterable into a string
-ljust(+)	     Returns a left justified version of the string
-lower(+)	     Converts a string into lower case
-lstrip(+)	     Returns a left trim version of the string
-maketrans(+)	 Returns a translation table to be used in translations
-partition(+)	 Returns a tuple where the string is parted into three parts
-replace(+)	     Returns a string where a specified value is replaced with a specified value
-rfind(+)	     Searches the string for a specified value and returns the last position of where it was found
-rindex(+)	     Searches the string for a specified value and returns the last position of where it was found
-rjust(+)	     Returns a right justified version of the string
-rpartition(+)	 Returns a tuple where the string is parted into three parts
-rsplit(+)	     Splits the string at the specified separator, and returns a list
-rstrip(+)	     Returns a right trim version of the string
-split(+)	     Splits the string at the specified separator, and returns a list
-splitlines(+) 	 Splits the string at line breaks and returns a list
-startswith(+)	 Returns true if the string starts with the specified value
-strip(+)	     Returns a trimmed version of the string
-swapcase(+)	     Swaps cases, lower case becomes upper case and vice versa
-title(+)	     Converts the first character of each word to upper case
-translate(+)	 Returns a translated string
-upper(+)	     Converts a string into upper case
-zfill(+)	     Fills the string with a specified number of 0 values at the beginning
'''


#capitalize()
a = 'dina'
print(a.capitalize()) #Dina
#hroofe avale har  kalame ro bozorg mikone


#casefold()
b = 'DINa'
print(b.casefold()) #dina
#hame hroof ro bozorg mikone


#center()
c= 'dina'
print(c.center(20)) #        dina        
print(c.center(20 , '-')) #--------dina--------
#behesh ye meghdari ro midim va dar marcaz oon matnemoon ro mizare


#count ()
d = 'dina'
print(d.count('i')) #1 
#tedade hroofe mored nazaro mige
#age masalan dota a dashte bashim avalishomige


#encode()
e = 'dina'
print(e.encode()) #b'dina'
#str <-- .encode() --> bytes
#b avale khoroje --> byte shode
#baraye zakhire ya enteghale dade ha estefade mishavad 


#endswith()
f = 'dina'
print(f.endswith('a')) #True
#taeed mikoneke akhare jomle ya kalamamon ba harf ya alamate morede nazar tamoomshode


#expandtabs()
g = 'dina\tdarsa'
print(g.expandtabs(1)) #dina darsa
#\t = space (tab)
#mitoonim tedade sapce haro moshakhas konim


#find()
h = 'dina'               #d i n a
print(h.find('n')) #2     0 1 2 3
#harchi bekhay indexesho mide
#age do ta n dashte bashim avalisho mide

#format()
i = 'dina {}'
print(i.format(b)) #dina DINa
#Raveshe Herfeii tar :
print(f'{e} {b} ') #dina DINa 
print(f'my name is {e} ') #my name is dina
#value ro dakhele matn jaygozarimikonr --> natije = str


#format_map()
j = { 'name' : 'dina' , 'age' : 14 }
print('my name is {name} and im {age}.' .format_map(j)) #my name is dina and im 14.
#meghdar haye yek ditionary ra bar asase esmeshon dar {} gharar mode


#index()
k = 'dina'          #      d i n a
print(k.index('a')) #3     0 1 2 3   
#hroofe morede nazareto migi va indexsho migiri
#agar az ye hroof 2 ta dashte bashi avalisho mige 


#isalnum()
l = 'dina14'
print(l.isalnum()) #True
'im dina'.isalnum() #False --> space dare
#agar str faghad shamele hroof va adad bashe True mide
#agar space dashte bashe False mide


#isalpha()
m = 'Dina'
print(m.isalpha()) #True
'im happy'.isalpha() #False --> space dare
'im 14'.isalpha() #False -- space va adad dare
#agar hroofe alefba bashe True mode
#agar space ya adad dashte bashe False mide


#isascii()
'hello world !'.isascii() #True
'hello 123'.isascii() #True
'سلام'.isascii() #False
#agar str ha ASCII bashan True mide vagarna False

'''
ASCII chie?
ghablan computer ha nemitonestan mafhome A ya B ro mostaghiman befahman pas
oomadan yek standard sakhtan --> baraye har character adade moshakhas gharar bedim 
masalan ::: 
A = 65
B = 66
C = 67
------------
a = 97
b = 98
------------
0 = 48
1 = 49

in adad ha tebghe jadvale ASCII ghabalan moshakhas shodan va ma khodemon entekhabeshon nemi konim 

ASCII shamele :::
   1. En(capital) --> A , B
   2. En(small) --> a , b
   3. numbers --> 1 , 2 , 3
   4. alamt ha --> @ # & * $ %
   5. space --> \n
   
PAS --> zaban haye farsi , chini , arabi ... ro support nemikone
baraye hamin vaghti farsi neveshtim False dad . 
'''

#isdecimal()
n = 'nono'
print(n.isdecimal()) #false
'145'.isdecimal() #True
'-127'.isdecimal() #False
'47.9'.isdecimal() #False
#mige aya hame character haye reshte ragham hastand ya na


#isdigit()
o = 'dina'
print(o.isdigit()) #false
'DINA'.isdigit() #False
'12674'.isdigit() #True
#check mikone ke aya in reshte faghad shamele adad ast? True/False


#isidentifier()
'dina'.isidentifier() #True
'class 1'.isidentifier() #False
#false
#aya in reshte baraye esme zarf monasebe ? True/False


#islower()
'dina'.islower() #True
'Dina'.islower() #False
'dina1'.islower() #True
#mige aya hame hroofe reshte kochik hastan ya ne True/False
#az adad ham mitonim estefade konim


#isnumeric()
'123'.isnumeric() #True
'dina1'.isnumeric() #False
'dina'.isnumeric() #False
#aya reshte faghat az character adadi tashkil shode? True/False

'''
isdecimal() --> mahdood tar
isdigit() --> kami bishtar
isnumeric() --> gostarde tarin

decimal < digit < numeric
'''

#isprintable()
'dina'.isprintable() #True
'123'.isprintable() #True
'dina\ndorsa'.isprintable() #False
'dina\tdorsa'.isprintable() #False
#aya hame character haye in rashte ghable namayesh hastan? #T/F



#isspace()
'   '.isspace() #True
'hello'.isspace() #False
#ayain reshte faghat az space sakhte shode? T/F


#istitile()
p = 'Dina Rahbar'
print(p.istitle()) #True
'dina rahbar'.istitle() #False
#aya hroofe avale har kalame bozorg ast? T/F



#isupper()
'DINA'.isupper() #True
'Dina'.isupper() #False
#aya kole reshte ba hrofe bozorg neveshte shode? T/F


#join
q = [ 'dina', 'sara', 'dorsa' ]
' '.join(q) #'dina sara dorsa'
#chizi ke mihkaym ro dar list ezafe mikone
#faght mitoone str haro be ham bechasboone
# agar dar listemoon adad ya int dashte bashim join eror mide PAS :
r = [ 'dina' , 'dorsa' , 14 ]
'-'.join(map(str , r)) #'dina-dorsa-14'

'''
MAP CHIE?
map yak tabe ro roye tak tak ajzaye list ejramikone.
pas ba map aval hame ro str mikonim va baeed join .
'''

#ljust()
s = 'dina'
print(s.ljust(10)) #dina    
print(s.ljust(10 , '-')) #dina------
#str ro az chap negah midare va az rast behesh space/character ezafe mikone ta be toole moshakhas shode berese

#rjust()
t = 'dina'
print(t.rjust(10)) #      dina
print(t.rjust(10 , '-')) #------dina
#strro az rast negah midare va az chap behesh space/character  ezafe mikone ta be toole moshakhas shode berese


#lower()
u = 'DINA'
print(u.lower()) #dina
#hame hroof haro koochik mikone


#lstrip()
v= '  dina'
print(v.lstrip()) #dina
'#dina'.lstrip('#') #'dina'
#hroofe ezafie chap ra pak mikone , mitoonim moshakhas konim kodom horof pak beshe .


#rstrip()
w = 'dina  '
print(w.rstrip()) #dina
'dina@#'.rstrip('@#') #'dina'
#hroofe ezafe rast ra pak mikone , mitoonim moshakhas konim kodom horof pak beshe.


#strip()
x= ' dina rahbar '
print(x.strip()) #dina rahbar
'@dina rahbar#'.strip('@' '#') #'dina rahbar'
#hroofe ezafie har do taraf ra pak mikone , mitoonim moshakhas konim kodom horof pak beshe .


#maketrans()     translate()
#in dota mamolanba ham estefade mishan 
z = 'dina'
z2 = str.maketrans('in' , '14') # i --> 1   n --> 4
print(z.translate(z2)) #d14a
#maketrans() ---> jadvale tabdil misaze 
#translate() ---> oon jadval ra ro str ejra mikone
#az translate mitoonim joda ham estefade konim::
    
a1 = {97: 49, 98: 50}
print("ab".translate(a1)) #12 
#Raveshe dovoom ::
c1 = 'dina'
c2 = { ord('i'): '1' ,  ord('n'): '2' }
print(c1.translate(c2)) #d12a
#baraye inke az translate() be sorate joda estefade konim bayad dict besazim
'''
ord yek character ro migira va code unicode(ASCII) ro mide
ord('a') → 97
chr(97)  → 'a'
'''

#partition()
a1 = 'dina-sara-dorsa'
print(a1.partition('-')) # ('dina', '-', 'sara-dorsa') --> 3 ghesmat: ghable avalin hyphen , hyphen, baede hyphen
#str ro be 3 ghesmat taghsim mikone
#avalin joda konande


#replace()
b1 = 'dina is happy'
print(b1.replace('happy' , 'sad')) #dina is sad
#yek ghesmat az reshte ro ba chizi jaygozin mikone


#rfind()
b2 = 'maryam'
print(b2.rfind('m')) #5
#harchi bekhay indexesho mide
#age do ta n dashte bashim akharisho mide
#agar chizi peyda nashe --> -1


#rindex()
f1 = 'maryam'
print(f1.rfind('m')) #5
#hroofe morede nazareto migi va indexsho migiri
#agar az ye hroof 2 ta dashte bashi akharisho mige 


#rpartition()
d1 = 'dina-sara-dorsa'
print(d1.rpartition('-')) #('dina-sara', '-', 'dorsa') --> 3 ghesmat: ghable akharin hyphen , hyphen, baede hyphen
#str ro be 3 ghesmat taghsim mikone
#akharin joda konande


#rsplit()
r1 = 'dina-sara-dorsa'
print(r1.rsplit('-')) #['dina', 'sara', 'dorsa']
'dina-sara-dorsa'.rsplit('-' , 1) #['dina-sara', 'dorsa']
#str ro az vhap ba joda konande moshakhas shode az rast be chand ghesmat taghsim mikonad


#spilt(0
h1 = 'dina-sara-dorsa'
print(h1.split('-')) #['dina', 'sara', 'dorsa']
'dina-sara-dorsa'.split('-' , 1) #['dina', 'sara-dorsa']
#str ro az vhap ba joda konande moshakhas az chap shode be chand ghesmat taghsim mikonad


#splitlines()
j1 = 'dina\ndelsan\ndorsa'
print(j1.splitlines()) #['dina', 'delsan', 'dorsa']
#str ro bar asase khat haye jadid joda mikone va be sorate list barmigardoone
#\n --> khate jadid


#startswith()
m1 = 'dina'
print(a1.startswith('d')) #True
'sara'.startswith('d') #False
#aya avlin hrfe str ba chizemoshakhas shode shroe mishavad?


#swapcase()
f1 = 'Dina'
print(f1.swapcase()) #dINA
#horoofe bozorg ro kochik va horoofe kochik ro bozorg mikone


#title()
k1 = 'in the name of god'
print(k1.title()) #In The Name Of God
#horoofe avale har kalame ro bozorg mikone


#upper()
m1 = 'dina'
print(m1.upper()) #DINA
#horoofe avale har kalame ro bozorg mikone


#zfill
y1 = '25'
print(y1.zfill(5)) #00025
#az samte chap 0 ezafe mikone ta str be toole moshakhas shode berese














