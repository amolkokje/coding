## Q: Given 2 lists, find starting index where second list is a subset of first list, else return -1
# EXAMPLE -1 
# Input Format:
# 3 // length of first list
# 1
# 2
# 3
# 2 // length of second list
# 2
# 3
# // output -> 1
# ------------------------------------
# EXAMPLE -2
# Input Format
# 3 // length of first list
# 1
# 2
# 3
# 2 // length of second list
# 3
# 2
# // output -> -1

def contains_list_index(main, sub):
    m = len(main)    
    s = len(sub)
    
    if m == s and main == sub:
        return 0
    
    for i in range(m-s+1):
        if main[i:i+s] == sub:
            return i
          
    return -1    
        


if __name__ == '__main__':
    
    list1_count = int(raw_input('Enter num of elements for list1:'))
    list1 = [None]*list1_count
    for i in range(list1_count):
        list1[i] = raw_input()
        
    list2_count = int(raw_input('Enter num of elements for list2:'))
    list2 = [None]*list2_count
    for i in range(list2_count):
        list2[i] = raw_input()   
           
    print '{} is contained in {}. Index={}'.format(list2, list1, contains_list_index(list1, list2))
           
           
    