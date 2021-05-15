astr = 'like a saury!'
try:
	istr = int(astr)
except:
	istr = 0.1
print('First', istr)

astr = '123'
try:
	istr = int(astr)
except:
	istr = -1
print('Second',istr)