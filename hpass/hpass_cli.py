import json
import time
from colorama import init, Fore
from prettytable import PrettyTable
from encryption import random_password, encryption_rc4, decrypt_rc4

init(autoreset=True)


class HPassCli:
    def __init__(self, primary, hello_password_data_dir):
        self.__primary = primary
        self.hello_password_data_dir = hello_password_data_dir
        with open(hello_password_data_dir, 'r', encoding='utf-8') as f:
            password_data_json = json.load(f)
        self.__password_data_json = password_data_json

    def save_data_file(self):
        with open(self.hello_password_data_dir, 'w', encoding='utf-8') as f:
            json.dump(self.__password_data_json, f, indent=4, ensure_ascii=False)
        return

    def get_password_list(self):
        pt_able = PrettyTable('ID Website Notes Username Email Phone'.split(' '))
        for k, v in self.__password_data_json['account'].items():
            _data = decrypt_rc4(key=self.__primary, message=v)
            _data_dict = json.loads(_data)
            _data_list = [_data_dict['id'], _data_dict['website'], _data_dict['notes'], _data_dict['username'],
                          _data_dict['email'], _data_dict['phone']]
            pt_able.add_row(_data_list)
        print(pt_able)
        return

    def add_password(self):
        print(Fore.MAGENTA + 'The following is the information required for the new password :')
        website_input = input('Website = ')
        notes_input = input('Notes = ')
        username_input = input('Username = ')
        email_input = input('Email = ')
        phone_input = input('Phone = ')
        password_input = input('Password = ')
        new_password_dict = {
            'id': self.__password_data_json['gradual'],
            'website': website_input.strip(),
            'notes': notes_input.strip(),
            'username': username_input.strip(),
            'email': email_input.strip(),
            'phone': phone_input.strip(),
            'password': password_input.strip(),
            'time': time.time()
        }
        self.__password_data_json['gradual'] += 1
        _new_password_str = json.dumps(new_password_dict)
        _new_password_encryption = encryption_rc4(key=self.__primary, message=_new_password_str)
        self.__password_data_json['account'][new_password_dict['id']] = _new_password_encryption
        print(Fore.GREEN + 'The new password has been successfully added !')
        self.save_data_file()
        return


def cli_start(primary, hello_password_data_dir):
    h_pass_cli = HPassCli(primary=primary, hello_password_data_dir=hello_password_data_dir)
    while True:
        user_input = input('H-Pass> ')
        if user_input == 'exit' or user_input == 'quit':
            break
        else:
            if user_input == 'filepath':
                print('H-Pass> ' + h_pass_cli.hello_password_data_dir)
            elif user_input == 'list':
                h_pass_cli.get_password_list()
            elif user_input == 'add':
                h_pass_cli.add_password()


if __name__ == '__main__':
    cli_start('123456', 'C:\\Users\hekaiyou\Desktop\hpass\hpass\helloPasswordData.json')