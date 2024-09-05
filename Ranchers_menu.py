#*********************************
# *** All the itemsin the menu ***
#*********************************

chicken_burger={1:'Bronco chicken burger',2:'cronco chicken burger',3:'chee haww chicken',4:'mighty rodeo chicken',5:'big bang',6:'big ben',7:'fajita',8:'pablito',9:'cowboy',10:'kruch'}
price_chicken_burger={"Bronco chicken burger":[499,675],'cronco chicken burger':[499,675],'chee haww chicken':[799,949],'mighty rodeo chicken':[799,975],'big bang':[799,975],'big ben':[725,899],'fajita':[575,775],'pablito':[499,699],'cowboy':[525,699],'kruch':249}
beef_burger={1:'rancheronii',2:'chee haww beef',3:'mighty rodeo beef',4:'Butcher',5:'taxes jack',6:'beef steak'}
price_beef_burger={'rancheronii':[799,975],'chee haww beef':[799,975],'mighty rodeo beef':[799,975],'Butcher':[699,875],'taxes jack':[699,875],'beef steak':[575,795]}
pizza={1:'thin crust pizza',2:'crown pizza',3:'chicken tikka pan',4:'chicken fajita pan',5:'ranch special pan',6:'margherita dop',7:'pepperoni pizza'}
price_pizza={'thin crust pizza':{'medium':[1,1049],'large':[2,1399],'xxl':[3,1699]},'crown pizza':{'medium':[1,1299],'large':[2,1699],'16 inches':[3,2299]},'chicken tikka pan':{'small':[1,499],'medium':[2,999],'large':[3,1299]},'chicken fajita pan':{'small':[1,499],'medium':[2,999],'large':[3,1299]},'ranch special pan':{'small':[1,499],'medium':[2,999],'large':[3,1299]},'margherita dop':{'small':[1,499],'medium':[2,999],'large':[3,1299]},'pepperoni pizza':{'small':[1,499],'medium':[2,999],'large':[3,1299]}}
fries = {1:'rancheese',2:'fries',3:'cheeky fries',4:'frizza'}
price_fries={'rancheese':649,'fries':{'regular':[1,199],'bucket':[2,299]},'cheeky fries':{'small':[1,499],'medium':[2,999]},'frizza':{'small':[1,499],'medium':[2,1099],'large':[3,1499]}}
drinks={1:'Dew',2:'7up',3:'mirinda',4:'pepsi'}
price_drinks={'Dew':110,'7up':110,'mirinda':110,'pepsi':110}
quick_bites={1:'chicken pieces',2:'whackerr',3:'kids meal',4:'messy wings'}
price_quick_bites={'chicken pieces':{'1 piece':[1,225],'3 piece':[2,649]},'whackerr':399,'kids meal':499,'messy wings':499}
deal={1:'grub on the go',2:'trio feast',3:'any 2 deal'}
price_deal={'grub on the go':{'4 krunch burgers,1 ltr. drink':[1,999]},'trio feast':{'3 cowboys,1 small frizza,3 regular drinks':[1,1699]},'any 2 deal':{'any two burgers, any two drinks':[1,1299]}}
any_2_deal_burger={1:'Bronco chicken burger',2:'cronco chicken burger',3:'mighty rodeo chicken',4:'big bang',5:'big ben(+99)',6:'fajita',7:'pablito',8:'cowboy',9:'mighty rodeo beef',10:'Butcher',11:'taxes jack',12:'beef steak'}
any_2_deal_drinks={1:'mirinda',2:'pepsi'}

#****************************************
#*** Function to order chicken burger ***
#****************************************

def order_chicken_burger(bill,dic):
    ls=[]
    inp=int(input("Enter your order no :"))
    while True:
        if inp<=10 and inp>0:
            break
        else:
            inp = int(input("Wrong Input. Please Enter your order no again:"))
    q=int(input("Enter Quantity : "))
    if inp>=1 and inp<=9:
        print("combo or regular")
        print("Enter 'c' for combo","Enter 'r' for regular")
        a=input()
        while True:
            if a == 'c' or a == 'r':
                break
            else:
                print("Wrong Input.Please Enter 'c' for combo and 'r' for regular")
                a = input()
        if a=='c':
            for k , v in chicken_burger.items():
                if k == inp:
                    ls.append(v+'(combo)')
                    ls.append(q)
                    for c,d in price_chicken_burger.items():
                        if v == c:
                            ls.append(d[1])
                            bill[0]=bill[0] + q*d[1]
        elif a=='r':
            for k , v in chicken_burger.items():
                if k == inp:
                    ls.append(v + "(regular)")
                    ls.append(q)
                    for c,d in price_chicken_burger.items():
                        if v == c:
                            ls.append(d[0])
                            bill[0]=bill[0] + q *d[0]
    if inp == 10:
        for k, v in chicken_burger.items():
            if k == inp:
                ls.append(v)
                ls.append(q)
                for c, d in price_chicken_burger.items():
                    if v == c:
                        ls.append(d)
                        bill[0] = bill[0] + q *d
    dic[len(dic)+1]=ls
    return bill

#*************************************
#*** Function to order beef burger ***
#*************************************

def order_beef_burger(bill,dic):
    ls=[]
    inp=int(input("Enter the order number :"))
    while True:
        if inp <= 6 and inp > 0:
            break
        else:
            inp = int(input("Wrong Input. Please Enter your order no again:"))
    q=int(input("Enter the quantity :"))
    if inp>=1 and inp<=6:
        print("combo or regular")
        print("Enter 'c' for combo", "Enter 'r' for regular")
        a = input()
        while True:
            if a == 'c' or a == 'r':
                break
            else:
                print("Wrong Input.Please Enter 'c' for combo and 'r' for regular")
                a = input()
        if a == 'c':
            for k, v in beef_burger.items():
                if k == inp:
                    ls.append(v + "(combo)")
                    ls.append(q)
                    for c, d in price_beef_burger.items():
                        if v == c:
                            ls.append(d[1])
                            bill[0] = bill[0] + q * d[1]
        if a == 'r':
            for k, v in beef_burger.items():
                ls.append(v + "(regular)")
                ls.append(q)
                if k == inp:
                    for c, d in price_beef_burger.items():
                        if v == c:
                            ls.append(d[0])
                            bill[0] = bill[0] + q * d[0]
    dic[len(dic)+1]=ls
    return bill

#*******************************
#*** Function to order pizza ***
#*******************************

def order_pizza(bill,dic):
    ls=[]
    inp = int(input("Enter your order no :"))
    while True:
        if inp <= 7 and inp > 0:
            break
        else:
            inp = int(input("Wrong Input. Please Enter your order no again:"))
    q = int(input("Enter Quantity : "))
    if inp >= 0 and inp <= 7:
        for k, v in pizza.items():
            if k == inp:
                ls.append(v)
                ls.append(q)
                for c, d in price_pizza.items():
                    if v == c:
                        for e,f in d.items():
                            print("Enter",f[0],"for",e)
                        a=int(input("Enter the size number :"))
                        for e, f in d.items():
                            if a==f[0]:
                                ls.append(f[1])
                                bill[0] = bill[0] + q* f[1]
    else:
        print("WRONG INPUT")
    dic[len(dic)+1]=ls
    return bill

#*******************************
#*** Function to order fries ***
#*******************************

def order_fries(bill,dic):
    ls=[]
    inp = int(input("Enter your order no :"))
    while True:
        if inp <= 4 and inp > 0:
            break
        else:
            inp = int(input("Wrong Input. Please Enter your order no again:"))
    q = int(input("Enter Quantity : "))
    if inp >= 2 and inp <= 4:
        for k, v in fries.items():
            if k == inp:
                ls.append(v)
                ls.append(q)
                for c, d in price_fries.items():
                    if v == c:
                        for e, f in d.items():
                            print("Enter", f[0], "for", e)
                        a = int(input("Enter the size number :"))
                        for e, f in d.items():
                            if a == f[0]:
                                ls.append(f[1])
                                bill[0] = bill[0] + q * f[1]
    elif inp == 1:
        for k, v in fries.items():
            if k == inp:
                ls.append(v)
                ls.append(q)
                for c, d in price_fries.items():
                    if v == c:
                        ls.append(d)
                        bill[0] = bill[0] + q * d
    else:
        print('WRONG INPUT')
    dic[len(dic)+1]=ls
    return bill

#********************************
#*** Function to order drinks ***
#********************************

def order_drinks(bill,dic):
    ls=[]
    inp = int(input("Enter your order no :"))
    while True:
        if inp <= 4 and inp > 0:
            break
        else:
            inp = int(input("Wrong Input. Please Enter your order no again:"))
    q = int(input("Enter Quantity : "))
    if inp >= 1 and inp <= 4:
        for k, v in drinks.items():
            if k == inp:
                ls.append(v)
                ls.append(q)
                for c, d in price_drinks.items():
                    if v == c:
                        ls.append(d)
                        bill[0] = bill[0] + q * d
    dic[len(dic)+1]=ls
    return bill

#*************************************
#*** Function to order quick bites ***
#*************************************

def order_quick_bites(bill,dic):
    inp = int(input("Enter your order no :"))
    while True:
        if inp <= 4 and inp > 0:
            break
        else:
            inp = int(input("Wrong Input. Please Enter your order no again:"))
    q = int(input("Enter Quantity : "))
    if inp >= 2 and inp <= 4:
        for k, v in quick_bites.items():
            if k == inp:
                ls = []
                ls.append(v)
                ls.append(q)
                for c, d in price_quick_bites.items():
                    if v == c:
                        ls.append(d)
                        bill[0] = bill[0] + q * d
    elif inp == 1:
        for k, v in quick_bites.items():
            if k == inp:
                for c, d in price_quick_bites.items():
                    if v == c:
                        for e,f in d.items():
                            if f[0] == 1:
                                bill[0] = bill[0] + int(q%3) * f[1]
                                if int(q%3) != 0:
                                    ls=[]
                                    ls.append(v)
                                    ls.append(int(q%3))
                                    ls.append(f[1])
                                    dic[len(dic)+1]=ls
                            if f[0] == 2:
                                bill[0] = bill[0] + int(q/3) * f[1]
                                if int(q/3) != 0:
                                    ls=[]
                                    ls.append(v + ' X3')
                                    ls.append(int(q/3))
                                    ls.append(f[1])
                                    dic[len(dic)+1]=ls
    return bill

#*******************************
#*** Function to order deals ***
#*******************************

def order_deal(bill,dic):
    inp = int(input("Enter deal no :"))
    while True:
        if inp <= 3 and inp > 0:
            break
        else:
            inp = int(input("Wrong Input. Please Enter your order no again:"))
    q = int(input("Enter Quantity : "))
    if inp >= 1  and inp <= 2:
        for k, v in deal.items():
            if k == inp:
                ls = []
                ls.append(v)
                ls.append(q)
                for c, d in price_deal.items():
                    if v == c:
                        for e,f in d.items():
                            ls.append(f[1])
                            bill[0] = bill[0] + q * f[1]
    elif inp == 3:
        for k, v in deal.items():
            if k == inp:
                ls=[]
                ls.append(v)
                ls.append(q)
                for c, d in price_deal.items():
                    if v == c:
                        for e,f in any_2_deal_burger.items():
                            print(e, "\t", f)
                        inp1=int(input('Enter the order number of 1st burger:'))
                        if inp1 == 5:
                            bill[0]=bill[0]+ q * 99
                            ls.append(99)
                        inp2 = int(input('Enter the order number of 2nd burger:'))
                        if inp2 == 5:
                            bill[0] = bill[0] +q * 99
                            ls.append(99)
                        for e,f in any_2_deal_drinks.items():
                            print(e, "\t", f)
                        inp3 = int(input('Enter the order number of 1st drink:'))
                        inp4 = int(input('Enter the order number of 2nd drink:'))
                        for g,h in d.items():
                            ls.append(h[1])
                            bill[0]=bill[0]+q * h[1]
    dic[len(dic)+1]=ls
    return bill

#**********************************
#*** Function to print the menu ***
#**********************************

def print_menu(a,b):
    print("ord.no\t\tmenu")
    for k, v in a.items():
        for c,d in b.items():
            if v == c:
                print(k, "\t", v )
                if str(type(d)) == '<class \'int\'>':
                    print('\tPRICE:',d)
                if str(type(d)) == '<class \'list\'>':
                    print('\tPRICE:\tregular:',d[0],'\tcombo:',d[1])
                if str(type(d)) == '<class \'dict\'>':
                    for e,f in d.items():
                        print('\tPRICE:',f[1],'   ',e)
    return

#**********************************
#*** Function to print all menu ***
#**********************************

def print_all_menu():
    print('::::::::::::::::CHICKEN BURGERS::::::::::::::::::')
    print_menu(chicken_burger,price_chicken_burger)
    print('::::::::::::::::::BEEF BURGERS:::::::::::::::::::')
    print_menu(beef_burger,price_beef_burger)
    print(':::::::::::::::::::::PIZZA:::::::::::::::::::::::')
    print_menu(pizza,price_pizza)
    print(':::::::::::::::::::::DRINKS::::::::::::::::::::::')
    print_menu(drinks,price_drinks)
    print('::::::::::::::::::::::FRIES::::::::::::::::::::::')
    print_menu(fries,price_fries)
    print(':::::::::::::::::::QUICK BITES:::::::::::::::::::')
    print_menu(quick_bites,price_quick_bites)
    print('::::::::::::::::::::::DEALS::::::::::::::::::::::')
    print_menu(deal,price_deal)
    return


import csv
import pandas as pd
import numpy as np
from datetime import datetime

#************************************
#*** Saving and printing the bill ***
#************************************

def print_bill(bill,dic):
    print('YOUR BILL:')
    arr1 = np.loadtxt('orders.csv', delimiter=",", dtype='str')
    row1 = len(arr1)
    with open('orders.csv','a',newline='') as file:
        a = input("Enter custumer id :")
        for k,v in dic.items():
            now=datetime.now()
            if len(v) == 3:
                ls = [a,str(now.date()),str(now.time()),str(now.weekday()),k]+v + [0]
                f=csv.writer(file)
                f.writerow(ls)
            elif len(v)== 4:
                b=v[2]
                v.pop(2)
                ls = [a,str(now.date()),str(now.time()),str(now.weekday()), k] + v + [b]
                f = csv.writer(file)
                f.writerow(ls)
            else:
                b = v[2]+v[3]
                v.pop(2)
                v.pop(3)
                ls = [a, str(now.date()),str(now.time()),str(now.weekday()), k] + v + [b]
                f = csv.writer(file)
                f.writerow(ls)
    arr2 = np.loadtxt('orders.csv', delimiter=",", dtype='str')
    row2 =len(arr2)
    print(arr2[0,:])
    print(arr2[row1:row2,:])
    print('Total\t',bill[0])
    return

#*********************
#*** Main program ***
#********************

print_all_menu()
bill=[0]
order={}
inp1 = 'y'
while inp1 != 'q':
    print("Enter 1 to order chicken burger")
    print("Enter 2 to order beef burger")
    print("Enter 3 to order pizza")
    print("Enter 4 to order fries")
    print("Enter 5 to order drinks")
    print("Enter 6 to order quick bites")
    print("Enter 7 to order deal")
    print("Enter d if you are done ordering")
    print("Enter q to Quit")
    inp1=input("Enter no accordingly:")
    if inp1 == '1':
        inp2 = 'y'
        while inp2 != 'n':
            a = input('Do you want to see the menu for chicken burgers[y/n]:')
            if a == 'y':
                print_menu(chicken_burger,price_chicken_burger)
                order_chicken_burger(bill, order)
                inp2 = input('Do you want to order another burger[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            elif a == 'n':
                order_chicken_burger(bill, order)
                inp2 = input('Do you want to order another burger[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            else:
                print("WRONG INPUT")
                continue
    elif inp1 == '2':
        inp2 = 'y'
        while inp2 != 'n':
            a = input('Do you want to see the menu for beef burgers[y/n]:')
            if a == 'y':
                print_menu(beef_burger, price_beef_burger)
                order_beef_burger(bill, order)
                inp2 = input('Do you want to order another burger[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            elif a == 'n':
                order_beef_burger(bill, order)
                inp2 = input('Do you want to order another burger[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            else:
                print("WRONG INPUT")
                continue
    elif inp1 == '3':
        inp2 = 'y'
        while inp2 != 'n':
            a = input('Do you want to see the menu of pizza[y/n]:')
            if a == 'y':
                print_menu(pizza, price_pizza)
                order_pizza(bill, order)
                inp2 = input('Do you want to order another pizza[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            elif a == 'n':
                order_pizza(bill, order)
                inp2 = input('Do you want to order another pizza[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            else:
                print("WRONG INPUT")
                continue
    elif inp1 == '4':
        inp2 = 'y'
        while inp2 != 'n':
            a = input('Do you want to see the menu of fries[y/n]:')
            if a == 'y':
                print_menu(fries, price_fries)
                order_fries(bill, order)
                inp2 = input('Do you want to order another from fries menu[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            elif a == 'n':
                order_fries(bill, order)
                inp2 = input('Do you want to order another from fries menu[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            else:
                print("WRONG INPUT")
                continue
    elif inp1 == '5':
        inp2 = 'y'
        while inp2 != 'n':
            a = input('Do you want to see the menu for drinks[y/n]:')
            if a == 'y':
                print_menu(drinks, price_drinks)
                order_drinks(bill, order)
                inp2 = input('Do you want to order another drink[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            elif a == 'n':
                order_drinks(bill, order)
                inp2 = input('Do you want to order another drink[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            else:
                print("WRONG INPUT")
                continue
    elif inp1 == '6':
        inp2 = 'y'
        while inp2 != 'n':
            a = input('Do you want to see the menu of quick bites[y/n]:')
            if a == 'y':
                print_menu(quick_bites, price_quick_bites)
                order_quick_bites(bill, order)
                inp2 = input('Do you want to order another from quick bites menu[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            elif a == 'n':
                order_quick_bites(bill, order)
                inp2 = input('Do you want to order another from quick bites menu[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            else:
                print("WRONG INPUT")
                continue
    elif inp1 == '7':
        inp2 = 'y'
        while inp2 != 'n':
            a = input('Do you want to see the menu of deals[y/n]:')
            if a == 'y':
                print_menu(deal, price_deal)
                order_deal(bill, order)
                inp2 = input('Do you want to order another deal [y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            elif a == 'n':
                order_deal(bill, order)
                inp2 = input('Do you want to order another deal[y/n]:')
                if inp2 == 'y':
                    continue
                elif inp2 == 'n':
                    break
                else:
                    print('WRONG INPUT')
                    continue
            else:
                print("WRONG INPUT")
                continue
    elif inp1 == 'd':
        print_bill(bill,order)
        a = input("Enter q to quit")
        while a != 'q':
            print('WRONG INPUT')
            a = input("Enter q to quit:")
        else:
            break
    elif inp1 == 'q':
        break
    else:
        print("WRONG INPUT")
        continue