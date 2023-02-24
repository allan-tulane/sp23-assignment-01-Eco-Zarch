"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(n):
    if n <= 1:
        return n
    else:
        ra, rb = foo(n-1), foo(n-2)
        return ra + rb



def longest_run(mylist, key):
    runs = []
    for i in range(len(mylist)):
        n = 0
        while mylist[i+n] == key:
                n += 1
        runs += n
    return max(runs)

def longest_run(mylist, key):
    maxlength = 0
    currlength = 0
    prev = None
    for item in mylist:
        if (item == key) and (prev != key):
            currlength = 1
        if (item == prev):
            currlength+=1
            if currlength > maxlength:
                maxlength = currlength
        prev = item

    return maxlength




class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    return helper_longest_run_recursive(mylist, key).longest_size


def helper_longest_run_recursive(mylist, key):
    if mylist.count(key) == 0:
        return Result(0,0,0, False)
    if mylist.count(key) == len(mylist):
        return Result(len(mylist),len(mylist),len(mylist),mylist[0]==key)

    left = helper_longest_run_recursive(mylist[:(len(mylist)//2)],key)
    right = helper_longest_run_recursive(mylist[(len(mylist)//2):],key)
    middle = left.right_size + right.left_size

    if ((middle) > right.longest_size) and ((middle) > left.longest_size):
        return Result(0,0,middle,True)
    return left if left.longest_size > right.longest_size else right

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run_recursive([2,12,12,8,12,0,12,0,12,1], 12) == 2
    assert longest_run_recursive([2,12,0,0,12,0,12,0,12,1], 0) == 2

print(test_longest_run())
