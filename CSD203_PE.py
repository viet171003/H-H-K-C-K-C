# this is PE test for CSD203. Do not delete this line
# your code here
class Book:
    def __init__(self,code,name,author,price):
        self.code = code
        self.name = name
        self.author = author
        self.price = price

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def append(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            self.len += 1
            return
        temp = self.head
        while temp is not None:
            temp = temp.next
        temp.next = NewNode
        self.len = 1

    def search_book_by_name(self,value):
        temp = self.head
        while temp is not None:
            if temp.data.name == value:
                print(temp.data.code,temp.data.name,temp.data.author,temp.data.price)
                break
            temp = temp.next

    def update_book_by_code(self,value):
        temp = self.head
        while temp is not None:
            if temp.data.code == value:
                temp.data.name = input('Enter new name: ')
                temp.data.author = input('Enter new author: ')
                temp.data.price = input('Enter new price: ')
                return Book(temp.data.code,temp.data.name,temp.data.author,temp.data.price)
            temp = temp.next

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data.code,temp.data.name,temp.data.author,temp.data.price)
            temp = temp.next

def EnterBook():
    code = input('Enter book code: ')
    name = input('Enter book name: ')
    author = input('Enter author book: ')
    price = input('Enter book price: ')
    return Book(code,name,author,price)

def menu():
    print('----------------------------')
    print('1 - Add book')
    print('2 - Search book by name')
    print('3 - Update book from code')
    print('4 - Delete book')
    print('5 - Display all book')
    print('6 - Exit')
    print('------------------------------')

def main():
    ll = LinkedList()
    while True:
        menu()
        choose = int(input('Enter your number from menu: '))
        if choose == 1:
            print('Add book')
            book = EnterBook()
            ll.append(book)
            print('Done')
        elif choose == 2:
            print('Search book by name')
            name = input('Enter book name: ')
            ll.search_book_by_name(name)
        elif choose == 3:
            print('Update code base on code')
            code = input('Enter book code: ')
            ll.update_book_by_code(code)
        elif choose == 4:
            print('Delete book via code')
        elif choose == 5:
            print('Display all book')
            ll.display()
        elif choose == 6:
            exit()
        else:
            print('Please enter again')
main()
