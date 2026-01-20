from services.user_service import (
    get_all_users, get_user_by_id, create_user, save_users
)

def menu():
    print('1. Get all users')
    print('2. Get user by id')
    print('3. Create user')
    # print('4. Save user')
    print('5. Exit')

while True:
    menu()
    option = input('Select an option: ')

    if option == "1":
        users = get_all_users()
        for user in users:
            print(user)
        
    elif option == "2":
        user_id = int(input('Enter user id: '))
        user = get_user_by_id(user_id)
        if user:
            print(user)
        else:
            print('User not found')

    elif option == "3":
        name = input('Enter name: ')
        email = input('Enter email: ')
        user = create_user(name, email)
        print('user created successfully: ', user.to_dict())
    
    # elif option == "4":
    #     user_id = input('Enter user id: ')
    #     user = get_user_by_id(user_id)
    #     save_users(user)
    
    elif option == "5":
        break

    else:
        print('Invalid option')