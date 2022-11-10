def convert(var):
    try:
	    print(int(var))
    except ValueError as TypeOfError:
	    print('A string cannot be converted to an integer\n', TypeOfError)
convert('www')
a= '123'
convert(a)
print('Code keeps running after error')
