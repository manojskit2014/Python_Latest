class fiveFunctions:
    # 1st Function
    def Subfields():
        l = eval(input('Enter the List : '))
        print('Sub-fields in AI are :')
        #message = 'Sub-fields in AI are :'
        for each_element in l:
            print(each_element)
        #return message

    # 2nd Function
    def oddEven():
        num = int(input('Enter the Number : '))
        if num % 2 == 0:
            print(num, 'is Even Number')
        else:
            print(num, 'is Odd Number')

    # 3rd Function
    def marriage():
        gender = input('Enter Your Gender :')
        age = int(input('Enter Your Age :'))
        if gender == 'male' and age >= 21:
            print('Eligible For Marriage')
        elif gender == 'female' and age >= 18:
            print('Eligible for Marriage')
        else:
           print('Not Eligible For Marriage')

    # 4th Function
    def percentage():
        sub_1 = int(input('Enter Subject 1 Marks : '))
        sub_2 = int(input('Enter Subject 2 Marks : '))
        sub_3 = int(input('Enter Subject 3 Marks : '))
        sub_4 = int(input('Enter Subject 4 Marks : '))
        sub_5 = int(input('Enter Subject 5 Marks : '))
        Total = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
        print('The Total Marks is : ', Total)
        Percentage = Total / 5
        print('The Percentage is : ', Percentage)
        return Percentage

    # 5th Function
    def triangle():
        height = int(input('Enter the Height : '))
        breadth = int(input('Enter the Breadth : '))
        Area = height * breadth / 2
        print('The Area of triangle is : ', Area)
        side_1 = int(input('Enter the Side 1 : '))
        side_2 = int(input('Enter the Side 2 : '))
        side_3 = int(input('Enter the Side 3 : '))
        Perimeter = side_1 + side_2 + side_3
        print('The Perimeter of triangle is : ', Perimeter)
        return Area, Perimeter