def greet_user(username):
    """Greet the user Hello"""
    print("Hello", username)

def main():
    name = print("Enter your name : ")
    greet_user(name)

if __name__ == '__main__':
    main()