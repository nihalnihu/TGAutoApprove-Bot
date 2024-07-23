from pymongo import MongoClient
from config import MONGO

client = MongoClient(MONGO)

users = client['main']['users']
groups = client['main']['groups']

def already_db(user_id):
        user = users.find_one({"user_id" : str(user_id)})
        if not user:
            return False
        return True

def already_dbg(chat_id):
        group = groups.find_one({"chat_id" : str(chat_id)})
        if not group:
            return False
        return True

def add_user(user_id):
    in_db = already_db(user_id)
    if in_db:
        return
    return users.insert_one({"user_id": str(user_id)}) 

def remove_user(user_id):
    in_db = already_db(user_id)
    if not in_db:
        return 
    return users.delete_one({"user_id": str(user_id)})
    
def add_group(chat_id, username=None, name=None):
    in_db = already_dbg(chat_id)
    if in_db:
        return
    group_data = {"chat_id": str(chat_id)}
    if username:
        group_data["username"] = username
    if name:
        group_data["name"] = name
    return groups.insert_one(group_data)
        
def all_users():
    user = users.find({})
    usrs = len(list(user))
    return usrs

def all_groups():
    group_cursor = groups.find({})
    groups_list = list(group_cursor)
    group_count = len(groups_list)
    usernames = [group.get("username", "No Username") for group in groups_list]
    names = [group.get("name", "No Name") for group in groups_list]
    return group_count, usernames, names
