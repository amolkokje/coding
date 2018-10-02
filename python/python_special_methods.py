## args, kwargs --> https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
print '\n --- ARGS, KWARGS --- \n'

def func(arg1, arg2, arg3, arg4, arg5):
    print 'arg1={}, arg2={}, arg3={}, arg4={}, arg5={}'.format(arg1, arg2, arg3, arg4, arg5)
    
# NOTE -> name arg, *args, *kwargs is not important. Only the asterisk *, ** are imp when calling the method    
# call normally    
func('a', 'b', 'c', 'd', 'e')
# call with *args
func(*('a', 'b','c', 'd', 'e'))
# call with **kwargs --> NOTE: the key names have to match the variable names of the function
func(**{'arg1':'a', 'arg2':'b', 'arg3':'c', 'arg4':'d', 'arg5':'e'})
# call all --> NOTE: When calling all, it is required that you preserve the order
func('a', *('b','c'), **{'arg4':'d', 'arg5':'e'})



# REFERENCE: https://docs.python.org/3/reference/datamodel.html

class TestDict(dict):
    """
    __missing__() is called when a key does not exist in a dict. You can override this method by creating a child class of dict
    """
    def __missing__(self, key):
        print '-- missing: key={}'.format(key)
	
    """
    __setitem__() and __getitem__() allow to access attributes of a class instance as a dict.
    __delitem__() is used to implement deletion
    They usually point to the same dict in the model, but can reference completely separate dicts.
    """
    def __getitem__(self, key):
        print '-- __getitem__(): key={}'.format(key)        
        return super(TestDict, self).__getitem__(key)
        
    def __setitem__(self, key, item):
        print '-- __setitem__(): key={}, item={}'.format(key, item)
        super(TestDict, self).__setitem__(key, item)
		
    def __delitem__(self, key):
        print '-- __delitem__(): key={}'.format(key)
        super(TestDict, self).__delitem__(key)
        


class TestClass():
    def __init__(self, d):
        print '-- __init__(): constructor'
        self.d = d
        self._data = 'dummy'
       
    
    """
    __str__() --> used to specify the value to use when you try to convert class instance to string
    __repr__() --> used to give a representation of the class instance
    if __str__() is not defined, it defaults to using __repr__() if it is defined.
    e.g. 
    >>> import datetime
    >>> today = datetime.date.today()
    >>> str(today) --> '2017-02-02' , example of __str__()
    >>> today --> 'datetime.date(2017, 2, 2)'
    """
    def __str__(self):
	return '__str__: d:{}'.format(self.d)

    def __repr__(self):
	return '__repr__: TestClass(d={})'.format(self.d)
	
    """
    __getattribute__() is called when we try to retireve class instance attribute
    __getattr__() is called when when the attribute does not exist in the class instance
    __setattr__() is called when we set a class instance attribute
    """    
    
    def __setattr__(self, name, value):
        print '-- __setattr__(): name={}, value={}'.format(name, value)
        self.__dict__[name] = value     # self.name = value --> will cause infinite loop here
        
    def __getattribute__(self, name):
        print '-- __getattribute__(): name={}'.format(name)
        return self.__dict__[name]        
        
    def __getattr__(self, name):
        print '-- __getattr__(): name={}'.format(name)
        self.name = 'DUMMY'  # this will call __setattr__()
        return self.name
         
         
"""
PROPERTY:
The search order that Python uses for attributes goes like this:
* __getattribute__ and __setattr__
* Data descriptors, like property
* Instance variables from the object's __dict__ (when setting an attribute, the search ends here)
* Non-Data descriptors (like methods) and other class variables
* __getattr__
So, even if we have a property setter, it will call the __setattr__
"""         
         
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value        
        
        
if __name__=='__main__':
    
    print "\n --- CLASS --- \n"
    d = {'a':1, 'b':2}# this will call __setattr__()
    tc = TestClass(d)# get all attributes of class instance as a dict
    
    # __str__
    print 'str(tc)={}'.format(str(tc))
    # __repr__
    tcl = []
    for i in range(5):
	tcl.append(TestClass(i))
    print tcl
    
    print tc.__dict__    
    # __getattribute__
    print tc.d 
    # __getattr__
    print tc.x
    # __setattr__
    tc.dummy = 'dummy'
    
    print tc.data
    tc.data = 'dummy-2'
    print tc.data
    del tc.data
    
    print "\n --- DICTIONARY ---\n"
    # __missing__
    td = TestDict({'a':1, 'b':2})
    print type(td)
    # __getitem__
    print td['a']
    # __missing__
    print td['c']
    # __setitem__
    td['c'] = 3 
   
    print "\n --- CLASS PROPERTY ---\n"
    cel = Celsius()
    print cel.temperature
    cel.temperature = 45
    print cel.temperature
    
    
