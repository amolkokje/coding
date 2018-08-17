# REFERENCE: https://docs.python.org/3/reference/datamodel.html

class TestDict(dict):
    """
    __missing__() is called when a key does not exist in a dict. You can override this method by creating a child class of dict
    """
    def __missing__(self, key):
        print '-- missing: key={}'.format(key)


class TestClass():
    def __init__(self, d):
        print '-- __init__(): constructor'
        self.d = d
      
    """
    __setitem__() and __getitem__() allow to access attributes of a class instance as a dict.
    __delitem__() is used to implement deletion
    They usually point to the same dict in the model, but can reference completely separate dicts.
    """
    def __getitem__(self, key):
        print '-- __getitem__(): key={}'.format(key)        
        return self.d[key]  # this will call the __getattribute__()
        
    def __setitem__(self, key, item):
        print '-- __setitem__(): key={}, item={}'.format(key, item)
        self.d[key] = item  # this will call the __setattr__()
        
    def __delitem__(self, key):
        print '-- __delitem__(): key={}'.format(key)
        del self.d[key]
        
        
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
        
        
        
if __name__=='__main__':
    d = {'a':1, 'b':2}
    tc = TestClass(d) # this will call __setattr__() 
    
    # __setitem__
    tc['x'] = 2
    # __getitem__
    print "tc['x']={}".format(tc['x'])
    # __delitem__
    del tc['x']
    
    # get all attributes of class instance as a dict
    print tc.__dict__
    
    # __getattribute__
    print tc.d 
    # __getattr__
    print tc.x
    
    # __missing__
    td = TestDict({'a':1, 'b':2})
    print type(td)
    print td['a']
    print td['c']
   
    
    
    
    
