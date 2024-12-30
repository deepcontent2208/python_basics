"""
Classes, methods and functions:
--------
Classes
--------
1. three_aayaam
2. customers
3. customers2
4. customers3
5. onboard_cust
6. hike_generator
--------
methods
--------
1. find_technology (in three_aayaam)
2. calc_discount (in customers)
3. cust_details (in customers)
4. get_cust_details (in customers2)
5. generate_profile (in onboard_cust)
6. calc_hike (in hike_generator)
-----------
Functions:
-----------
1. calc_yrs_of_exp
"""
#-------------------------------------------------------------------------
# Class definition, object creation
#-------------------------------------------------------------------------
# class three_aayaam:
#     name = "3aayaam_training"
#     def find_technology(self):
#         pass
#
# student1 = three_aayaam()
# student2 = three_aayaam()
# var_str = "technology"
#
# print(student1.name)
# student1.find_technology()
# print(type(student1))
#
# print(student2.name)
# student2.find_technology()
# print(type(student2))
#
# print(type(var_str))

#-------------------------------------------------------------------------
# "self" keyword
#-------------------------------------------------------------------------

# class customers:
#     def __init__(self):
#         pass
#
#     def calc_discount(self,amt):
#         print('amt: ',amt)
#         print(type(self))
#         print(id(self))
#
#     def cust_details(self, cust_id):
#         print('cust_id: ', cust_id)
#         print(type(self))
#         print(id(self))
#
# cust_1 = customers()
# cust_2 = customers()
# cust_id = 1100
#
# print(id(cust_id))
# print('cust_1')
# print(type(cust_1))
# print(id(cust_1))
# cust_1.calc_discount(100)
# cust_1.cust_details(12345)
# print('cust_2')
# print(type(cust_2))
# print(id(cust_2))
# cust_2.calc_discount(200)
# cust_2.cust_details(2208)

#-------------------------------------------------------------------------
# Class variable and Instance variable
#-------------------------------------------------------------------------
# class customers2:
#     org = 'BLR'
#     location = 'India'
#
#     def get_cust_details(self, id):
#         self.cust_id = id
#         # org = 'method'
#         # print(self.cust_id)
#         print(org)
#         # print(customers.org, "-", customers.location)
#         customers.org = 'Railways'
#         customers.location = 'NFR'
#         # print(customers.org, "-", customers.location)
#
# org = 'program'
# print(org)
# cust1 = customers2()
# cust1.get_cust_details(12345)
# print(org)
#
# cust2 = customers2()
# cust2.get_cust_details(102208)

#-------------------------------------------------------------------------
# __init__ method (dunder init dunder)
#-------------------------------------------------------------------------
# class customers3:
#     def __init__(self, fn, ln, loc):
#         print(self)
#         self.first_name = fn
#         self.last_name = ln
#         self.location = loc
#         # print(org)
#
# cust = customers3('cust','cust','cust')
# print(cust)
# org = 'freedom fighters'
# cust1=customers3('netaji','bose', 'India')
# print('name: ', cust1.first_name, ' ', cust1.last_name)
# print('location :', cust1.location)
#
# cust2=customers3('nelson','mandela', 'SA')
# print('name: ', cust2.first_name, ' ', cust2.last_name)
# print('location :', cust2.location)
# print(org)

#------------------------------------------------------------------------------------
# Hands On
#------------------------------------------------------------------------------------
# Create a class for the following:
# 1. Use first name, last name, date of birth (yyyy-mm-dd) to print full name & age.
#    Generate random customer id and email id.
# 2. Use current salary to calculate hike based on percentage. Use date of
#    joining to calculate the years of experience.
#    a. If years of experience is more than 20 then 3% hike.
#    b. If years of experience is 10-20 then 4% hike.
#    c. If years of experience is less than 10 then 5% hike.
#    d. Or random hike.
# Take input from user to print the above information.
#------------------------------------------------------------------------------------
# Hands On 1
#------------------------------------------------------------------------------------
# from datetime import date, datetime
import random
#
# class onboard_cust:
#     def __init__(self,fn,ln,dob):
#         self.first_name = fn
#         self.last_name = ln
#         self.dob = dob
#         print('Full Name: ', self.first_name + ' '+ self.last_name)
#
#         today = datetime.today()
#         today_date = datetime.date(today)
#         dob = datetime.strptime(self.dob, '%Y-%m-%d')
#         dob = datetime.date(dob)
#         age = today_date - dob
#         print('Age (in yrs): ', int(age.days/365))
#
#     def generate_profile(self, fn,ln):
#         cust_id = random.randint(100000,300000)
#         self.fn = fn
#         self.ln = ln
#         email_id = self.fn + '.' + self.ln + '.' + str(cust_id) + '@3aayaam.in'
#         print('Your customer id: ', cust_id)
#         print('Your email id: ', email_id.lower())
#
# fn = input('Enter your first name: ')
# ln = input('Enter your last name: ')
# dob = input('Enter your date of birth (in yyyy-mm-dd format): ')
#
# cust = onboard_cust(fn,ln,dob)
# cust.generate_profile(fn,ln)

#------------------------------------------------------------------------------------
# Hands On 2
#------------------------------------------------------------------------------------
from datetime import date, datetime
#
# class hike_generator:
#
#     def calc_hike(self, hike_table, current_salary, date_of_joining):
#         self.doj = date_of_joining
#         self.hike_table = hike_table
#         self.sal = int(current_salary)
#
#         yrs_of_exp = calc_yrs_of_exp(self.doj)
#         # print(yrs_of_exp)
#
#         if yrs_of_exp > 20:
#             hike_pct = int(self.hike_table['20+'])
#             salary = self.sal + (self.sal * hike_pct/100)
#         elif yrs_of_exp > 10:
#             hike_pct = int(self.hike_table['10+'])
#             salary = self.sal + (self.sal * hike_pct / 100)
#         else:
#             hike_pct = int(self.hike_table['10-'])
#             salary = self.sal + (self.sal * hike_pct / 100)
#
#         return salary
#
#
# def calc_yrs_of_exp(doj):
#     doj = datetime.strptime(doj, '%Y-%m-%d')
#     doj = datetime.date(doj)
#     today = datetime.today()
#     today = datetime.date(today)
#
#     yrs_of_exp = today - doj
#     yrs_of_exp = int(yrs_of_exp.days/365)
#
#     return yrs_of_exp
#
# hike_table = {
#     '20+': 30,
#     '10+': 40,
#     '10-': 50
# }
#
# current_salary = input('Enter current salary of employee: ')
# date_of_joining = input('Enter date of joining (yyyy-mm-dd): ')
#
# current_salary = 100000
# date_of_joining = '2023-01-01'
#
# emp_obj = hike_generator()
# salary_hike = emp_obj.calc_hike(hike_table,current_salary, date_of_joining)
#
# print('Hiked salary of this employee: ', salary_hike)


#------------------------------------------------------------------------------------
# Inheritance
#------------------------------------------------------------------------------------
# class vehicles:
#     vehicle_manufacturer = ['BMW', 'Mercedez', 'Audi']
#
#     def vehicle_type(self):
#         print('you are in vehicle_type method')
#
#     def vehicle_maintenace(self):
#         print('you are in vehicle_maintenace method')
#
# class volkswagen(vehicles):
#     def sister_group(self):
#         print("volkswagen class - sister_group method")
#
# bmw_x1 = volkswagen()
# print(type(bmw_x1))
#
# bmw_x1.vehicle_type()
# bmw_x1.vehicle_maintenace()
# bmw_x1.sister_group()
# print(bmw_x1.vehicle_manufacturer)

