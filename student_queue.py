# student_queue.py
#
# Base queue implementation for the cs10 ADTs unit
#
# Our initial implementation will use a singly linked list. But, if you
# want to make a faster queue, you will need to implement the data structue
# in a different way. To do this, you will need to change the class definitions
# below.
#
# IMPORTANT: If you change the class constructions, make sure you DO NOT change the
# name of the Queue class. The testing harnesses expect your queue implementation to
# be named Queue in this file.

from typing import NoReturn


class ListElem:
    """An element of the list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """A queue made from a linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add items to the end of the Queue
        """
        new_element = ListElem(data)
        first_element = self.head
        if self.head == None:
            self.head = new_element
        else:
            current_element = first_element
            while current_element.next != None:
                next_element = current_element.next
                current_element = next_element
            current_element.next = new_element

    def popleft(self):
        """Remove first item from the Queue
        """
        if self.head != None:
            first_element = self.head
            self.head = first_element.next
            return first_element.data
        else:
            raise IndexError

    def __len__(self):
        """Checks the length of the queue
        """
        current_element = self.head
        length = 0
        while current_element != None:
            length = length + 1
            current_element = current_element.next
        return length

    def insert(self, index, data):
        """Adds an element at a partifuclar index of the queue
        """
        new_elem = ListElem(data)
        if self.head == None:
            self.append(data)
        elif index > len(self):
            self.append(data)
        elif index == 0:
            new_elem.next = self.head
            self.head = new_elem
        else:
            current_element = self.head
            for i in range(int(index)):
                next_element = current_element.next
                prev_elem = current_element
                current_element = next_element
            index_elem = current_element
            prev_elem.next = new_elem
            new_elem.next = index_elem


    def getList(self):
        ''' Outputs all data in the list on the screen
        '''
        if self.head == None:
            print('List is empty')
        else:
            current_element = self.head
            for i in range(self.__len__()):
                print(current_element.data)
                next_element = current_element.next
                current_element = next_element

    def delete(self, index):
        '''Deletes an element at a particular index
        '''
        if self.head == None:
            print('List is empty')
        elif index == 0:
            self.popleft()
        
        elif index > len(self):
            current_element = self.head
            #go to the end of the list
            while current_element.next != None:
                next_element = current_element.next
                prev_elem = current_element
                current_element = next_element
            prev_elem.next = None

        else:
            current_element = self.head
            for i in range(int(index)):
                next_element = current_element.next
                prev_elem = current_element
                current_element = next_element

            prev_elem.next = current_element.next
            current_element.next = None



#test...
q = Queue()
q.append(0)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.delete(0)
q.getList()



