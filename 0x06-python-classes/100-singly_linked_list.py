#!/usr/bin/python3
"""
A python implementation of singly linked list
returns {}
"""


class Node:
    """ The Node class"""
    def __init__(self, data, next_node=None):
        """ Initializing the data and next_node pointer"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Getter for the data value"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data node"""
        if type(self.__data) != int:
            raise TypeError('data must be an integer')
        self.data = value

    @property
    def next_node(self):
        """ Getter for the linked list node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next node"""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList():
    """ Singly linked list class object"""
    def __init__(self):
        """Initializing the head attribute"""
        self.__head = None
    def sorted_insert(self, value):
        """Method to allow sorted insertion"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while value >= current.data:
            prev = current
            if current.next_node:
                current = current.next_node
            else:
                current.next_node = new_node
                return
        prev.next_node = new_node
        new_node.next_node = current

    def __str__(self):
        """ String representation of the linked list"""
        string = ""
        current = self.__head
        while current:
            string += str(current.data) + "\n"
            current = current.next_node
        return string[:-1]
