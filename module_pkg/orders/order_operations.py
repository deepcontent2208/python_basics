"""
1. Get order details (id, invoice amount, total items, item description)
2. Add orders and calculate total price of the order. Input – multiple order
   items and their price.
"""
class order:
    def get_order_details(self,order_id):
        self.id = order_id

        count = 0
        for i in order_table:
            if (i[0] == order_id):
                print('Order Id: ', i[0])
                print('Invoice Amt: ', i[1])
                print('Quantity: ', i[2])
                print('Description: ', i[3])
                count = count + 1

        if (count == 0):
            print("No orders found with order id {}!!".format(order_id))

    def add_orders(self):
        pass

order_table = (
    [1101, 235.67, 3, 'headphones'],
    [2202, 1000, 1, 'iPhone'],
    [3303, 15000, 4, 'MacBook Pro'],
    [4404, 23.65, 1, 'microphone'],
    [5505, 100, 3, 'utensils'],
    [6606, 250, 100, 'Ballpens'],
)

# order = order()
# order.get_order_details(1101)