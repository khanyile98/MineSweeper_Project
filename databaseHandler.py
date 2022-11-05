import sqlite3


def create_profile(username, password):
    con = sqlite3.connect("data.db")

    con.execute(f"""\
        INSERT INTO LOGIN_INFORMATION (USERNAME, PASSWORD)
        VALUES ('{username}', '{password}')""");
    
    con.commit()
    con.close()
    return True


def check_if_profile_exists(username, password):
    my_data = []
    con = sqlite3.connect('data.db')

    data = con.execute(f"""\
        SELECT USERNAME, PASSWORD 
        FROM LOGIN_INFORMATION 
        WHERE USERNAME = '{username}' AND PASSWORD = '{password}'
        """)

    for item in data:
        my_data.append((item[0], item[1]))
    con.close()

    if len(my_data) == 1:
        return True
    return False


def Handler(username, password, command):
    if command == 'create':
        return create_profile(username, password)

    if command == 'login':
        return check_if_profile_exists(username, password)


if __name__ == "__main__":
    username = input("username: ")
    password = input("password: ")

    print(check_if_profile_exists(username, password))

    # if Handler(username, password, "create"):
    #     print('Your profile has successfuly been created.')
