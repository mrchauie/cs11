class ListElem:
    """An element of the list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    """A list made from a linked list.
    """
    def __init__(self):
        self.head = None
    
    def __len__(self):
        """Checks the length of the queue
        """
        current_element = self.head
        length = 0
        while current_element != None:
            length = length + 1
            current_element = current_element.next
        return length

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
        """Remove first item from the List
        """
        if self.head != None:
            first_element = self.head
            self.head = first_element.next
            return first_element.data
        else:
            raise IndexError

    def popright(self):
        '''Remove the last item from the list
        '''
        if self.head == None:
            print('List is empty')
        else:
            current_element = self.head
            #go to the end of the list
            while current_element.next != None:
                next_element = current_element.next
                prev_elem = current_element
                current_element = next_element
            prev_elem.next = None

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

# create a new list
l = List()
# appends a element at the front of the list
l.append(5)
# prints out the list
l.getList()