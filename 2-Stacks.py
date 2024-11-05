class Stack:        # Stack follows LIFO (Last In First Out)
    def __init__(self):
        self.pages = []

    def push(self, item):   # Adds item to end of list
        self.pages.append(item)
        print('Page added:', item)
    
    def pop(self):  # Removes last item in list and returns item
        if not self.is_empty():
            removed = self.pages.pop()
            print('Page removed:', removed )
            return removed
        
        
    def peek(self): # Returns last item in list
        if not self.is_empty():
            return self.pages[-1]
    
    def is_empty(self):  # Boolean to check if list is empty
        return len(self.pages) == 0
    
    def size(self): # Returns # pages in list
        print('\nLength of page list:',len(self.pages))
        return len(self.pages)

    def display(self):
        if self.is_empty():
            print("No pages in list.")
        else:
            print('\nPages in list:')
            for item in self.pages:
                print(item)

browser_history = Stack()
browser_history.display()
browser_history.push({'id': '1', 'page': 'abc', 'url': 'www.abc.com'})
browser_history.push({'id': '2', 'page': 'ghj', 'url': 'www.ghj.com'})
browser_history.push({'id': '3', 'page': 'xyz', 'url': 'www.xyz.org'})
browser_history.size()
browser_history.display()
browser_history.pop()
browser_history.display()
browser_history.pop()
browser_history.display()
browser_history.pop()
browser_history.display()
