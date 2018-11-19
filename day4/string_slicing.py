Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> string = "Monty python"
>>> print (string)
Monty python
>>> string [:]
'Monty python'
>>> string [o:12]

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    string [o:12]
NameError: name 'o' is not defined
>>> string [:12]
'Monty python'
>>> string [0:12]
'Monty python'
>>> len (string)
12
>>> string[: len(len)]

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    string[: len(len)]
TypeError: object of type 'builtin_function_or_method' has no len()
>>> string [: len(string)]
'Monty python'
>>> string [-12:]
'Monty python'
>>> string [-12:-1]
'Monty pytho'
>>> string [-12:0]
''
>>> string [-12:12]
'Monty python'
>>> string [:5]
'Monty'
>>> string [6:12]
'python'
>>> string [12::]
''
>>> :-1:1
SyntaxError: invalid syntax
>>> 
>>> string [::-1]
'nohtyp ytnoM'
>>> string[12:6]
''
>>> string [12]

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    string [12]
IndexError: string index out of range
>>> string [12:]
''
>>> string [:12]
'Monty python'
>>> string [:5:-1]
'nohtyp'
>>> string [:0:-1]
'nohtyp ytno'
>>> string [4::-1]
'ytnoM'
>>> string [-8:-12]
''
>>> string [-8:-12:-1]
'ytno'
>>> string [-8:-13:-1]
'ytnoM'
>>> 
