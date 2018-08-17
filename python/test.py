def deco(func):
    c = []
    print 'assigning c'
    
    def wrapper():        
        c.append(2)
        print c
        func()
    return wrapper

@deco
def testfunc():
    print 'inside testfunc()'

    
    
if __name__=='__main__':
    testfunc()
    testfunc()
    testfunc()
    ss = []
    print ss
    ss.append(2)
    print ss
    
    s2 = ss
    ss.append(2)    
    print ss, s2
    
    