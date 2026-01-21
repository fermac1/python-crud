from services.user_service import (
    get_all_users, get_user_by_id, create_user, update_user, delete_user
)

def menu():
    print('1. Get all users')
    print('2. Get user by id')
    print('3. Create user')
    print('4. Update user')
    print('5. Delete user')
    print('6. Exit')

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
    
    elif option == "4":
        user_id = int(input('Enter user id: '))
        name = input('Enter name: ')
        email = input('Enter email: ')
        user = update_user(user_id, name or None, email or None)
        if user:
            print('user updated successfully: ', user)
        else:
            print('User not found')
    
    elif option == "5":
        user_id = int(input('Enter user id: '))
        deleted = delete_user(user_id)
        if deleted:
            print('user deleted successfully')
        else:
            print('User not found')

    elif option == "6":
        break

    else:
        print('Invalid option')