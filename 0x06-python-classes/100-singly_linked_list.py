#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = node
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        """Setter for the data node"""
        self.data = value
        if type(self.__data) != int:
            raise TypeError('data must be an integer')
    @property
    def next_node(self):
        """ Getter for the linked list node"""
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        """Setter for the next node"""
        self.__next_node = value
        if self.__next_node != Node or self.__next_node != None:
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList(Node):
    def __init__(self):
        Node.__init__(self, data, next_node=None)
    __head = None
    node = Node()
    def sorted_insert(self, value):
        node.data(value)
        if self.__head == None:
            Node.data(value)
            self.__head = next_node()
