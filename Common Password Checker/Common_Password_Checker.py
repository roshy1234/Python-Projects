import sys

def check_password(password: str):
        if password == '':
            raise Exception
        with open('passwords.txt',"r") as file:
            common_passwords: list[str] = file.read().splitlines()

        for i,common_password in enumerate(common_passwords,start=1):
            if password.lower() == common_password:
                print(f'{password}: ❌ (#{i})')
                return
        print(f'{password}: ✅ (Unique) ')






if __name__ == '__main__':

    passwd = input('Enter password: ')
    if passwd == '':
        print('>>> Password is empty!')
        sys.exit()
    check_password(passwd)
