import hashlib

# Sample user database (username: hashed_password)
user_db = {
    'user1': hashlib.sha256('password1'.encode()).hexdigest(),
    'user2': hashlib.sha256('password2'.encode()).hexdigest()
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(username, password):
    hashed_password = hash_password(password)
    if username in user_db and user_db[username] == hashed_password:
        return True
    return False

# Main script
if __name__ == '__main__':
    username = input('Enter username: ')
    password = input('Enter password: ')
    
    if login(username, password):
        print('Login successful!')
    else:
        print('Invalid username or password.')
