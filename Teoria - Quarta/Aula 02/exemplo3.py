Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def addup(first, last):
	if first > last:
		sum =-1
	else:
		sum=0
		for i in range(first, last+1):
			sum=sum+i
	return sum

>>> print(addup(1,10))
55
>>> print(addup(first=1,last=10))
55
>>> print(addup(last=10,first=1))
55
>>> 
