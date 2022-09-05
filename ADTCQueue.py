class CQElem:
    """An element of the CQueue.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class CQueue:
    """A circular queue made from a linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, e):
        '''enqueue(self, E e): void - Insert an element E into the back of the queue
        '''
        # check to see if the CQ is empty
        if self.isEmpty() == True:
            self.head = e
            self.tail = e
            self.tail.next = self.head
        else:
            self.tail.next = e
            self.tail = e
            self.tail.next = self.head

    def viewCQ(self):
        loc = self.head
        do = True
        while do:
            print(loc.data)
            loc = loc.next
            if loc == self.head:
                do = False

    def dequeue(self):
        '''dequeue(self): E - removes the first element of the queue, returns the element
        '''
        if self.head == None:
            return None
        elif self.head == self.tail:
            data = self.head.next
            self.head = None
            self.tail = None
            return data.data
        else:
            data = self.head
            self.head = self.head.next
            self.tail.next = self.head
            return data.data

    def isEmpty(self):
        '''isEmpty(self): bool - checks if the queue is empty, returns a boolean (true/false)
        '''
        if self.head == None:
            return True
        else:
            return False

q = CQueue()
q.enqueue(CQElem('mon'))
q.enqueue(CQElem('tues'))
q.enqueue(CQElem('wed'))
q.enqueue(CQElem('thurs'))
q.enqueue(CQElem('friday'))
q.enqueue(CQElem('sat'))
q.enqueue(CQElem('sun'))
print(q.dequeue())
print('alksdfjklsad')
q.viewCQ()











#     def __len__(self):
#         """Checks the length of the queue
#         """
#         current_element = self.head
#         length = 0
#         while current_element != None:
#             length = length + 1
#             current_element = current_element.next
#         return length

#     def getList(self):
#         ''' Outputs all data in the list on the screen
#         '''
#         if self.head == None:
#             print('List is empty')
#         else:
#             current_element = self.head
#             for i in range(self.__len__()):
#                 print(current_element.data)
#                 next_element = current_element.next
#                 current_element = next_element

#     def append(self, data):
#         """Add items to the end of the Queue
#         """
#         new_element = ListElem(data)
#         first_element = self.head
#         if self.head == None:
#             self.head = new_element
#         else:
#             current_element = first_element
#             while current_element.next != None:
#                 next_element = current_element.next
#                 current_element = next_element
#             current_element.next = new_element

#     def popleft(self):
#         """Remove first item from the List
#         """
#         if self.head != None:
#             first_element = self.head
#             self.head = first_element.next
#             return first_element.data
#         else:
#             raise IndexError

#     def popright(self):
#         '''Remove the last item from the list
#         '''
#         if self.head == None:
#             print('List is empty')
#         else:
#             current_element = self.head
#             #go to the end of the list
#             while current_element.next != None:
#                 next_element = current_element.next
#                 prev_elem = current_element
#                 current_element = next_element
#             prev_elem.next = None

#     def insert(self, index, data):
#         """Adds an element at a partifuclar index of the queue
#         """
#         new_elem = ListElem(data)
#         if self.head == None:
#             self.append(data)
#         elif index > len(self):
#             self.append(data)
#         elif index == 0:
#             new_elem.next = self.head
#             self.head = new_elem
#         else:
#             current_element = self.head
#             for i in range(int(index)):
#                 next_element = current_element.next
#                 prev_elem = current_element
#                 current_element = next_element
#             index_elem = current_element
#             prev_elem.next = new_elem
#             new_elem.next = index_elem

#     def delete(self, index):
#         '''Deletes an element at a particular index
#         '''
#         if self.head == None:
#             print('List is empty')
#         elif index == 0:
#             self.popleft()
        
#         elif index > len(self):
#             current_element = self.head
#             #go to the end of the list
#             while current_element.next != None:
#                 next_element = current_element.next
#                 prev_elem = current_element
#                 current_element = next_element
#             prev_elem.next = None

#         else:
#             current_element = self.head
#             for i in range(int(index)):
#                 next_element = current_element.next
#                 prev_elem = current_element
#                 current_element = next_element

#             prev_elem.next = current_element.next
#             current_element.next = None

# # create a new list
# l = List()
# # appends a element at the front of the list
# l.append(5)
# # prints out the list
# l.getList()