""" linked_list.py

Student: Marcus Steiner
Mail: marcus.steiner.3581@student.uu.se
Reviewed by: Anna Seiderer
Date reviewed: 9/10 - 2024
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):           #
        f = self.first
        index = 0
        while f:
            index += 1
            f = f.succ
        return(index)

    def mean(self):               
        pass

    def remove_last(self):       # 
        if self.first is None:
            raise ValueError("ERROR")
        elif self.first.succ is None:
            removed = self.first.data
            self.first = None
            return removed
        else:
            f = self.first
            while f.succ.succ:
                f = f.succ
            f_removed = f.succ.data
            f.succ = None
        return f_removed
        

    def remove(self, x):         # 
        if self.first is None:
            return False
        else:
            f = self.first
            while f.succ and x >= f.data:
                if x == f.data:
                    f.data = f.succ.data
                    f.succ = f.succ.succ
                    return True
                f = f.succ
            
            if x == f.data:
                f = None
                return True
        return False


    def to_list(self):            #
        
        def _to_list(f):
            if f is None:
                return []
            elif f.succ is None:
                return [f.data]
            else:
                return [f.data] + _to_list(f.succ)
        
        return _to_list(self.first)

    def remove_all(self, x):      #
        
        def _remove_all(f):
            if x == f.data:
                if f.succ is None:
                    self.remove_last()
                    return 1
                f.data = f.succ.data
                f.succ = f.succ.succ
                return _remove_all(f) + 1
            elif f.succ is None:    #Om listan alltid är sorterad behöver man inte koden under
                return 0            #Då kan man returnera 0 direkt
            else:                   #Alt en fel kod
                return _remove_all(f.succ)
        
        return _remove_all(self.first)
    
    def __str__(self):            #
        return f"({', '.join(str(f) for f in self)})"

    # def copy(self):             #
    #     result = LinkedList()
    #     for x in self:          #theta(n)
    #         result.insert(x)    #theta(n)
    #     return result           #total of theta(n^2)
    ''' Complexity for this implementation: 

    '''

    def copy(self):               # Should be more efficient
        old = self.first
        new_lst = LinkedList()
        if old is None:
            return new_lst
        else:
            new_lst.first = self.Node(old.data, None)
            new_value = new_lst.first
            while old.succ:
                old = old.succ
                new_value.succ = self.Node(old.data, None)
                new_value = new_value.succ
            return new_lst
    ''' Complexity for this implementation:

    '''

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    # for x in [3, 1, 2, 6, 1]:
        # lst.insert(x)
    # lst.print()
    
    #lst.remove_last()
    
    #lst.remove(1)
    
    #lst.to_list()
    
    #print(lst.remove_all(9))
    
    # new_lst = lst.copy()
    # new_lst.print()
    
    # print(str(lst))
    
    # Test code:


if __name__ == '__main__':
    main()
