import sys, os


class Node(object):
    def __init__(self, x):
        self.value = x
        self.next_node = None

    def __repr__(self):
        return '<Node:{}>'.format(self.value)


class LinkedList(object):
    def __init__(self, x):
        self.root = Node(x)

    def append(self, x):
        current = self.root
        while True:
            if current.next_node:
                current = current.next_node
            else:
                current.next_node = Node(x)
                break

    def delete(self, x):
        current = self.root
        prev = self.root
        while True:
            if current.value == x:
                if current.next_node:
                    prev.next_node = current.next_node
                del current
                print 'Node {} deleted.'.format(x)
                return
            else:
                prev = current
                if current.next_node:
                    current = current.next_node
                else:
                    break
        print 'Node {} not found!'.format(x)

    def list(self):
        print 'Listing...'
        current = self.root
        while current:
            print current
            if current.next_node:
                current = current.next_node
            else:
                break


# Q. Write a method to reverse a linked list

def reverse_linked_list(ip_ll):

    def _recurse_add(node):
        """ helper method to recurse through to last node of linked list """
        if node.next_node:
            # get the returned LL from the last node, and append the current value to it, so as to reverse the order
            ll = _recurse_add(node.next_node)
            ll.append(node.value)
            return ll
        else:
            # if reached end of linked list, create a new LL and return it
            return LinkedList(node.value)

    return _recurse_add(ip_ll.root)

# Book: 2.5
# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in
# reverse order, such that the 1'sdigit isat the head of the list. Write a function that adds the two numbers and
# returns the sum as a linked list.


# Book: 2.6
# Q. Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop.


# Book: 2.7
# Q. Implement a function to check if a linked list is a palindrome

def is_ll_palindrome():
    pass


if __name__ == '__main__':
    ll = LinkedList(0)
    for i in range(1, 10):
        ll.append(i)

    ll.list()
    ll.delete(10)
    ll.delete(3)
    ll.list()

    print '***********************************************'
    reverse_ll = reverse_linked_list(ll)
    reverse_ll.list()
