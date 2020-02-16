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
        prev = None
        while True:
            if current.value == x:
                if prev:  # not the first node
                    if current.next_node:
                        prev.next_node = current.next_node
                    del current
                else:  # for the first node, prev=None
                    self.root = current.next_node
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

# METHOD-1: recursion (here) --> New LL
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


# METHOD-2: put all elements in stack as you go till last node, and then start popping out --> Same LL
def reverse_ll_stack(ip_ll):
    stack = list()
    current = ip_ll.root
    while current:
        stack.append(current.value)
        if current.next_node:
            current = current.next_node
        else:
            break

    current = ip_ll.root
    while stack:
        current.value = stack.pop(-1)
        if current.next_node:
            current = current.next_node
        else:
            break


# Book: 2.5
# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in
# reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and
# returns the sum as a linked list.


# Book: 2.6
# Q. Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop.


# Book: 2.7
# Q. Implement a function to check if a linked list is a palindrome

# METHOD-1: using recursion
def is_palindrome_recursion(ll):
    node_list = list()

    def _recurse(node):
        node_list.append(node.value)

        if node.next_node:
            i, isp = _recurse(node.next_node)
            if isp:
                return (i + 1), node.value == node_list[i]
            else:
                return None, False
        else:
            return 1, node.value == node_list[0]

    return _recurse(ll.root)[1]


# METHOD-2: using stack
def is_palindrome_stack(ll):
    stack = list()

    current = ll.root
    while current:
        stack.append(current.value)
        if current.next_node:
            current = current.next_node
        else:
            break

    current = ll.root
    while stack:
        if current.value == stack.pop(-1):
            if current.next_node:
                current = current.next_node
        else:
            return False
    return True


"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    ll = LinkedList(0)
    for i in range(1, 10):
        ll.append(i)

    ll.list()
    ll.delete(0)
    ll.delete(3)
    ll.list()

    print '***********************************************'

    print '*** Reverse LL in Place ***'
    ll.list()
    reverse_ll_stack(ll)
    ll.list()

    print '*** Reverse LL using new LL ***'
    reverse_ll = reverse_linked_list(ll)
    reverse_ll.list()

    print '***********************************************'


    def _get_palindome_ll():
        ll = LinkedList(0)
        for i in range(1, 5):
            ll.append(i)
        for i in range(5)[::-1]:
            ll.append(i)
        return ll


    print '*** Is-Palindrome using recursion *** '
    ll = _get_palindome_ll()
    ll.list()
    print is_palindrome_recursion(ll)
    ll.append(10)
    print is_palindrome_recursion(ll)

    print '*** Is-Palindrome using stack *** '
    ll2 = _get_palindome_ll()
    ll2.list()
    print is_palindrome_stack(ll2)
    ll2.append(10)
    print is_palindrome_stack(ll2)
