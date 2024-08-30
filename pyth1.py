# Sample user database (username: password)
user_db = {
    'user1': 'password1',
    'user2': 'password2'
}

def login(username, password):
    if username in user_db and user_db[username] == password:
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
