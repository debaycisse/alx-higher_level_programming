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
        if isinstance(value, int) is False:
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
        if (value is not None) and (isinstance(value, Node) is False):
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
        SinglyLinkedList.head = None

    def __iter__(self):
        """This is a default iteration method for every instance of the class.

        It fetches each data in this list, esepcially when the print
        function tries to print an object of this class.

        Returns:
            Each data, stored in this list is returned
        """
        self.__current_node = SinglyLinkedList.head
        return (self.__current_node)

    def __next__(self):
        """This is an iterator method that return each data field in the list.
        """
        if self.__current_node is not None:
            while self.__current_node is not None:
                yield self.__current_node.data
                self.__current_node = self.__current_node.next_node
        else:
            yield None

    def sorted_insert(self, value):
        """This method inserts a node and sorts their value, based on
        increasing value. 1 is bigger than 0 and 0 is bigger than -1.

        Args:
        value (Node pointer): this contains the data that is to be
        stored in this linked list.
        """
        new_node = Node(value)
        current_node = SinglyLinkedList.head
        prev_node = None
        counter = 0
        if current_node is None:
            new_node.next_node = None
            SinglyLinkedList.head = new_node
        elif current_node is not None:
            while current_node is not None:
                if value > current_node.data:
                    counter += 1
                    prev_node = current_node
                    current_node = current_node.next_node
                    if current_node is None:
                        prev_node.next_node = new_node
                        new_node.next_node = None
                        break
                elif value < current_node.data and counter == 0:
                    new_node.next_node = SinglyLinkedList.head
                    SinglyLinkedList.head = new_node
                    break
                elif value < current_node.data and counter > 0:
                    new_node.next_node = current_node
                    prev_node.next_node = new_node
                    break
                break
