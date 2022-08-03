import EmployeeDatabase as ed

menu_options = {
    1: 'Salary',
    2: 'Job Title',
    3: 'Home Address',
    4: 'Contact Info',
}

def menu():
    print("Welcome!")
    name = input("Please Enter Employee Name: ").title()
    emp = ed.companyRegistery(name)
    if emp is None:
        print("No Employee Found!")
    else:
        while True:
            print("Please select which information do you want to see about "+name)
            for key in menu_options.keys():
                print (key, '--', menu_options[key] )
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except:
                print('Wrong input. Please enter a number ...')
            #Check what choice was entered and act accordingly
            if option == 1:
                print(name+"'s Salary = "+emp['salary'])
                break
            elif option == 2:
                print(name+"'s Job Title = "+emp['title'])
                break
            elif option == 3:
                print(name+"'s Home Address = "+emp['address'])
                break
            elif option == 4:
                print(name+"'s Contact Info = "+emp['contact'])
                break
            else:
                print('Invalid option. Please enter a number between 1 and 4.')

menu()