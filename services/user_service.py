import json 
from models.user import User
import os

FILE_PATH = 'data/users.json'

# read users
def get_all_users():
    if not os.path.exists(FILE_PATH):
        return []
    
    try:
        with open(FILE_PATH, 'r') as file:
            users = json.load(file)
            return users
        
    except json.JSONDecodeError:
        return []
    
# get user by id
def get_user_by_id(user_id):
    users = get_all_users()
    for user in users:
        if user['id'] == user_id:
            return user

    return None

# save user
def save_users(users):
    with open(FILE_PATH, 'w') as file:
        # users = get_all_users()
        # users.append(user.to_dict())
        json.dump(users, file, indent=2)

# create user
def create_user(name, email):
    users = get_all_users()

    new_id = len(users) + 1
    user = User(new_id, name, email)

    users.append(user.to_dict())
    save_users(users)

    return user

# update user
def update_user(user_id, name=None, email=None):
    users = get_all_users()
    for user in users:
        if user['id'] == user_id:
            user['name'] = name
            user['email'] = email
            save_users(users)
            return user

    return None