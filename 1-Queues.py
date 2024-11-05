class Queues:       # Queue follows FIFO (First In First Out)
    def __init__(self):
        self.orders = []

    def enqueue(self, item): # Add item to queue
        self.orders.append(item)
        print('Order added:', item)

    def dequeue(self): # Removes first item from list, returns item
        if not self.is_empty():
            removed = self.orders.pop(0)
            print('Order completed:', removed )
            return removed

    def is_empty(self):  # Boolean to check if list is empty
        return len(self.orders) == 0
    
    def size(self): # Returns # orders in list
        print('\nLength of orders list:',len(self.orders))
        return len(self.orders)
    
    def display(self):
        if self.is_empty():
            print("No orders in list.")
        else:
            print('\nOrders in list:')
            for item in self.orders:
                print(item)

restaurant_orders = Queues()
restaurant_orders.display()
restaurant_orders.enqueue({'id': '1', 'dishes': ['menu item 1', 'menu item 3'], 'table#': 4, 'total': '$20.00'})
restaurant_orders.enqueue({'id': '2', 'dishes': ['menu item 2'], 'table#': 2, 'total': '$10.00'})
restaurant_orders.enqueue({'id': '3', 'dishes': ['menu item 4', 'menu item 5'], 'table#': 1, 'total': '$30.00'})
restaurant_orders.size()
restaurant_orders.display()
restaurant_orders.dequeue()
restaurant_orders.dequeue()
restaurant_orders.display()
restaurant_orders.dequeue()
restaurant_orders.display()
