Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print(type(2))
<class 'int'>
type("a")
<class 'str'>
type(2.4)
<class 'float'>
a=5j

type(a)
<class 'complex'>
List=["minu",121,9.0,4j]
type(List)
<class 'list'>
Tuple=("minu",121,9.0,4j)
type(tuple)
<class 'type'>
set={"apple","banana","orange"}
type(set)
<class 'set'>
Dict={"name":"minal","rollno":121}
type(Dict)
<class 'dict'>
n=None
type(n)
<class 'NoneType'>
a=4
b=5
print(a+b)
9
a-b
-1
a*b
20
a/b
0.8
a**b
1024
a%b
4
a//b
0
print("assignment")
assignment
a==b
False
>>> a+=b
>>> a
9
>>> b-=a
>>> b
-4
>>> a=5
>>> b=4
>>> a*b
20
>>> a
5
>>> a*=b
>>> a
20
>>> a/=b
>>> a
5.0
>>> a=6
>>> b=5
>>> a//=b
>>> a
1
>>> a**=b
>>> a
1
>>> print("comparison")
comparison
>>> a=14
>>> b=45
>>> c=a>b
>>> c
False
>>> a<b
True
>>> a>=b
False
>>> a<=b
True
>>> a==b
False
>>> print("logical")
logical
>>> a=16
>>> b=47
>>> a>10 and b>13
True
a<2 or b>10
True
not(a=23)
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
not(a==23)
True
range(5)
range(0, 5)
a=56
b=90
a&b
24
x="hello world"
y="world"
x in y
False
y in x
True
x not in y
True
y is x
False
x is y
False
x=10
y=10

x is y
True
x is not y
False
a|b
122
List=["Minu",12,67,9.0]
List.append("minal")
List
['Minu', 12, 67, 9.0, 'minal']
['Minu', 12, 67, 9.0, 'minal']
['Minu', 12, 67, 9.0, 'minal']
KeyboardInterrupt
List[2]
67
Tuple=("shweta",67,5.0)
Tuple
('shweta', 67, 5.0)
Tuple[1]
67
set={"apple","banana","orange"}
set
{'orange', 'banana', 'apple'}
Dict={"name":"minal","rollno":45}
Dict
{'name': 'minal', 'rollno': 45}
Dict["rollno"]
45
List=["Minu",12,67,9.0]
 List.insert(1,45)
 
SyntaxError: unexpected indent
List.insert(1,45)
List
['Minu', 45, 12, 67, 9.0]
List.remove(12)
List
['Minu', 45, 67, 9.0]
['Minu', 45, 67, 9.0]
['Minu', 45, 67, 9.0]
List.pop()
9.0
List.pop(2)
67
List.extend([88,90])
List
['Minu', 45, 88, 90]
