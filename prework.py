#1
def hello_username(user_name):
    print("Hello " + user_name)

#2
odds = []
counter = 1
while len(odds) <= 100:
    if counter % 2 == 1:
        odds.append(counter)
    counter +=1
print(odds)

#3

def max_num_in_a_list(a_list):
    print(max(a_list))

#or (assuming a list with at least one postive number)

def max_in_list(lst):
    max = 0
    for num in lst:
        if num >= max:
            max = num
    print(max)

#4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                print('Leap Year')
            else:
                print('Not a Leap Year')
        else: 
                print('Leap Year')
    else:
        print('Not a Leap Year')

#5
def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    if a_list == sorted_list:
        print(True)
    else:
        print(False)