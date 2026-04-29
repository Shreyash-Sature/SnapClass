from src.database.config import supabase
import bcrypt


def hash_pass(pwd):
    #hashes the password using bcrypt and returns the hashed password
    return bcrypt.pw(pwd.encode(), bcrypt.gensalt()).decode()
    # encode() is used to convert the password string to bytes, which is required by bcrypt. 
    # The hashed password is then decoded back to a string for storage in the database.
    # gensalt() generates a random salt for each password, enhancing security by ensuring 
    # that even identical passwords will have different hashes.

def check_pass(pwd, hashed):
     #checks if the password matches the hashed password
    return bcrypt.checkpw(pwd.encode(), hashed.encode())
    #check_pass() takes the plain password and the hashed password, 
    #encodes them to bytes, and returns True if they match, otherwise False.


def check_teacher_exist(username):
    # check for uniquie usrname , return false when username is already taken
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0

def create_teacher(username, password, name):
    data = {"username" : username,
            "password": hash_pass(password),
            "name" : name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data():
        teacher = response.data[0] #response returns array values
        
        if check_pass(password, teacher["password"]):
            return teacher
    return None