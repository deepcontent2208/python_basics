"""
1. Print full name and random email id. Input – first and last name.
2. Get customer details from a lookup table (customer id, name, address, location, privilege flag).
   Input - customer id.
3. Add new customers to the lookup table and print the output. Input – customer id, name, address, location,
   privilege flag.
"""


import random

cust_table = [
    {'cust_id': 100, 'fname': 'Aarti', 'lname': 'Dey', 'address': 'BKC', 'location': 'Mumbai', 'priv_flag': 'Y'},
    {'cust_id': 200, 'fname': 'John', 'lname': 'Wick', 'address': 'Manhattan', 'location': 'NY', 'priv_flag': 'Y'},
    {'cust_id': 300, 'fname': 'Sam', 'lname': 'Altman', 'address': '9th Street','location': 'Chicago', 'priv_flag': 'N'},
    {'cust_id': 400, 'fname': 'Jai', 'lname': 'Shankar', 'address': 'Arjun Road', 'location': 'New Delhi','priv_flag': 'Y'},
    {'cust_id': 500, 'fname': 'Anuradha', 'lname': 'TK', 'address': 'Adyar', 'location': 'Chennai','priv_flag': 'N'}
]

def add_customer(fn, ln, addr, loc, flag):
    global cust_table
    id = random.randint(100,10000)
    new_cust = {'cust_id':id, 'fname':fn, 'lname': ln, 'address': addr, 'location': loc,'priv_flag': flag}
    cust_table.append(new_cust)

    print('Following are all customer ids:')
    for i in cust_table:
        print('Id: ',i['cust_id'], ' ', 'Name: ', i['fname'].capitalize(), ' ', i['lname'].capitalize())

    return id

def get_cust_details(cust_id):
    global cust_table

    cust_id = int(cust_id)
    count = 0

    for i in cust_table:
        if (i['cust_id'] == cust_id):
            print('-----------------------------------')
            print('Following are the customer details:')
            print('-----------------------------------')
            print('Id:            ', cust_id)
            print('Name:          ', i['fname'] + ' ' + i['lname'])
            print('Location:      ', i['location'])
            print('Priv Customer? ', i['priv_flag'])
            count = count + 1

    if (count == 0):
        print('No customer found with customer id {}!!'.format(cust_id))

    if __name__ == '__main__':
        pass
    else:
        print(__name__)
        print('cust_operations has been called from another module')



def generate_full_name_email(fn,ln):
    fn=str(fn)
    ln=str(ln)
    full_name = fn.capitalize() + ' ' + ln.capitalize()

    random_no = random.randint(100,500)
    email_id = fn.lower() + '.' + ln.lower() + '.' + str(random_no) + '@3aayaam.in'

    print('Full Name: ', full_name)
    print('Email Id : ', email_id)


if __name__ == '__main__':
    generate_full_name_email('Shankar','mahadevan')
    print(cust_table)
    cust_id = add_customer('Dr. APJ','Abdul Kalam', 'Rameswaram', 'TN', 'Y')
    get_cust_details(cust_id)
