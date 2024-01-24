#!/usr/bin/python3
"""This module defines both Node and SinglyLinkedList class.

It is going to contain structure for both a singly linked list
and a Node class with their respective data and methods.
"""


class Node:
    """This is the node class where singly linked list will be defined.

    """

    def __init__(self, data, next_node=None):
        """This constructor initializes both a next node pointer,

        and its data.

        Args:
            data (int): this is an integer that must be stored.
            next_node (pointer): points to the next node in a linked list
		"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
    """This method retrievs the value of the data attribute.

    It serves as a getter method for the data attribute

    Returns:
        The value of the data is returned.
    """
    return (self.__data)

    @data.setter
    def data(self, value):
    """This method updates the value of the data field.

    It serves as the setter for the data attribute.

    Args:
        value (int): the value to be used in updating the data attribute

    Raises:
        TypeError: this is raised if the given value is not an integer type
    """
    if type(value) is not int:
        raise TypeError("data must be an integer")
	self.__data = value

    @property
    def next_node(self):
        """This method retrieves the address of the next_node

        Returns:
            The values of the next node is returned
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """This method updates the value of the next node

        Args:
            value (pointer):This value is used to point to a new next node

        Raises:
            TypeError: this is raised if the value is having
            neither a None of Node type
        """
        if (type(value) is not None) or (type(value) is not Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This is a SinglyLinkedList class.

    It is going to contains the structure of a node type.
    """


    # this is the header of a linked list
    head = None

    def __init__(self):
        """This instantiate a singly linked list class.

        It is going to contain a list of values in the list instance
        """
        SinglyLinkedList.head = []

    def sorted_insert(self, value):
        """This method inserts a node and sorts their value, based on
        increasing value. 1 is bigger than 0 and 0 is bigger than -1.

        Args:
        value (Node pointer): this contains the data that is to be
        stored in this linked list.
        """
        a_node = Node(value)
        if SinglyLinkedList.head == None:
            a_node.next_node = None
            SinglyLinkedList.head = a_node
