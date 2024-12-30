
order_id = 101002387
order_price = 347.86
order_description = "iPhone"
order_qty = 2

var_str = "Welcome to www.3aayaam.in"

'''
multi-line comment
whatever i put in between opening and closing 3 quotes, will be considered as 
comments.
'''
#-----------------------------------------------------------------------------
# print Function
#-----------------------------------------------------------------------------
# print("Welcome")
# print(var_str)
# print('order id is : ', order_id)
# print(order_id, order_description)
# print("order id : ", order_id, " price : ", order_price)
# print("order_id : {0}  price : {1}".format(order_id, order_price))
# print("order_id : {id}  price : {amt}".format(id=12345,amt=23.45))
# print("order_id : {id}  price : {amt}".format(id=order_id,amt=order_price))

#-----------------------------------------------------------------------------
# Conditional statement - if
#-----------------------------------------------------------------------------
# order_price = 500.00
# order_qty = 17

# if (order_price > 10000.00 and order_qty > 20):
#     print("something fishy... you are spending ${0} for {1} items!!!".format(order_price, order_qty))
# elif (order_price > 7500.00 and order_qty > 15):
#     print("are you sure you want to spend ${0} for {1} items".format(order_price, order_qty))
# elif (order_price >= 5000.00 and order_qty > 10):
#     print("you are spending ${0} for {1} items".format(order_price, order_qty))
# else:
#     print("all good... you have spent ${0} on {1} items".format(order_price, order_qty))

# if (order_price > 10000.00 or order_qty > 20):
#     print("something fishy... you are spending ${0} for {1} items!!!".format(order_price, order_qty))
# elif (order_price > 7500.00 or order_qty > 15):
#     print("are you sure you want to spend ${0} for {1} items".format(order_price, order_qty))
# elif (order_price >= 5000.00 or order_qty > 10):
#     print("you are spending ${0} for {1} items".format(order_price, order_qty))
# else:
#     print("all good... you have spent ${0} on {1} items".format(order_price, order_qty))

#-----------------------------------------------------------------------------
# Conditional loop - for
#-----------------------------------------------------------------------------
# var_list = [10,'a',20,'b',30,'c']
# var_set = {10,'a',20,'b',30,'c'}
# var_dict = {'order_id': 101002387, 'order_price' : 347.86, 'order_description' : "iPhone", 'order_qty' : 2}

# for x in var_list:
#     print('current value is : ', x)
#     if (x == 'b'):
#         break

# for x in var_set:
#     print('current value is : ', x)

# for x in var_dict:
#     print('current value is : ', x, var_dict[x])

#-----------------------------------------------------------------------------
# Conditional loop - while
#-----------------------------------------------------------------------------

# order_price = 200.00
# i = 0

# while (order_price > 100.00):
#     print('your order value is : ', order_price)
#
#     i = i + 1
#     if (i == 70):
#         print("i is :", i)
#         break
#
#     if order_price == 160:
#         break
    # order_price = order_price - 20

#-----------------------------------------------------------------------------
# Functions / Methods - Definition and RETURN
#-----------------------------------------------------------------------------
# order_id = 101002387
# order_price = 347.86
# order_discount = 20
# order_description = "iPhone"
# order_qty = 2
#
# def calc_final_price():
#     order_price = 2347.86
#     order_discount = 20
#     order_price = order_price - (order_price*order_discount/100)
#     if order_price > 1000.00:
#         final_price = order_price * 0.95
#     else:
#         final_price = order_price
    # print('Final price of your order : ', final_price)
    # print(final_price)
    # return final_price, order_price, "values returned"

# calc_final_price()
# calc_final_price()
# calc_final_price()
# calc_final_price()
# price = calc_final_price()
# price, order_amount, desc = calc_final_price()
# print(price, order_amount, desc)
# print(type(price), type(order_amount))
# print(type(price))
# print(price)

#-----------------------------------------------------------------------------
# Functions Scope - LGB Rule & Global keyword
#-----------------------------------------------------------------------------
# x = 30
# print(x)

# def scope_func_1():
#     x = 2
#     print(x)
#
# def scope_func_2():
#     print(x)
#
# def scope_func_3():
#     global x
#     x = 100
#     print(x)

# x = 40
# print(x)
# # scope_func_1()
# # scope_func_2()
# scope_func_3()
# print(x)

#-----------------------------------------------------------------------------
# Functions Arguments
#-----------------------------------------------------------------------------
# def calc_final_price(amount, discount, final_discount):
#     disc_price = amount - (amount*discount/100)
#     print("memory address of amount (inside func): ", id(amount))
#     print("memory address of discount (inside func): ", id(discount))
#     print("memory address of final_discount (inside func): ", id(final_discount))
#     if (disc_price > 7500):
#        total_price = disc_price * (1 - final_discount/100)
#     else:
#         total_price = disc_price
#     return total_price
#
# amount = 10000
# discount = 15
# final_discount = 10
# print("memory address of amount : ", id(amount))
# print("memory address of discount : ", id(discount))
# print("memory address of final_discount : ", id(final_discount))
# final_price = calc_final_price(amount,discount,final_discount)
# print(final_price)

#-----------------------------------------------------------------------------
# Functions Arguments - Number, String, List, Set, Dictionary, Tuple
#-----------------------------------------------------------------------------

# def mod_int_str(var_is):
#     var_is = 2000.00
#     print(var_is)

# def mod_list(var_list):
    # var_list[0]='three_aayaam'
    # var_list[2][1] = 'Data Engg'
    # var_list[2][0] = 'Machine Learning'
    # var_list[3]['program1'] = 'Java'
    # var_list[3]['program2'] = 'PostgreSQL'
    # # var_list = ['a', 'b', 'c']
    # print(var_list)

def mod_set(var_set):
    pass

def mod_dict(var_dict):
    pass

def mod_tuple(var_tuple):
    pass

# var_is = '3aayaam'
# print(var_is)
# mod_int_str(var_is)
# print(var_is)

# var_list = ['3aayaam', 2000.00, ['data engg', 'machine learning'], {'program1':'python', 'program2':'sql'}]
# print(var_list)
# mod_list(var_list)
# print(var_list)

#-----------------------------------------------------------------------------
# Functions Arguments - Positional & Keyword
#-----------------------------------------------------------------------------
# def process_order(order_id, order_price, order_qty, order_desc):
#     print("order id: ", order_id)
#     order_price = order_price / 11
#     print("order price: ", order_price)
#     order_qty = order_qty * 20
#     print("order qty: ", order_qty)
#     print("description: ", order_desc)
#
# id = 12345
# price = 500.75
# qty = 24
# desc = "stationary items"
# process_order(id, price, qty, desc)
# process_order(order_id=12345,order_qty=20, order_desc='kwarg',order_price=200.76)
# process_order(order_id=id,order_qty=qty, order_desc=desc,order_price=price)
# process_order(order_id=id,order_qty=qty, order_desc=desc,order_price=price)

#-----------------------------------------------------------------------------
# Functions Arguments - *args & **kwargs
#-----------------------------------------------------------------------------
def process_customer(*args):
    print(args)
    for i in args:
        print(i)
    return args[3]

def process_order(**kwargs):
    print(kwargs)
    print(kwargs['order_price'])

def variable_input(*args, **kwargs):
    print(args)
    print(kwargs)


# a = 1
# b = 2
# c = 'nice video'
# order_id = 12345
# process_customer(a,b,c, order_id)
# order_id = process_customer(a,b,c, order_id)
# print(order_id)
# process_order(a=1,b=2,order_qty=25, order_price=1500)
# variable_input(a,b,c,order_id,a=1,b=100,c=1000,order_qty=25, order_price=1500, order_id=102408,
#                cust_name="3aayaam", cust_id=102408, cust_addr1='BLR')








