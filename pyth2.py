def load_users(filename):
    user_db = {}
    with open(filename, 'r') as file:
        for line in file:
            username, password = line.strip().split()
            user_db[username] = password
    return user_db

def login(username, password, user_db):
    if username in user_db and user_db[username] == password:
        return True
    return False

# Main script
if __name__ == '__main__':
    user_db = load_users('users.txt')
    
    username = input('Enter username: ')
    password = input('Enter password: ')
    
    if login(username, password, user_db):
        print('Login successful!')
    else:
        print('Invalid username or password.')
