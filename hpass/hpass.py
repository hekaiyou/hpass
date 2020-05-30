import sys
import json
import getpass
import argparse
from pathlib import Path
from colorama import init, Fore
# from hpass.hpass_gui import gui_start
# from hpass.random_pass import random_password
from hpass_gui import gui_start
from encryption import random_password, hmac_sha256_digest

init(autoreset=True)


def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser(description='Hello Password')
    parser.add_argument('-v', '--version', help='查看版本信息', action='version', version='%(prog)s v0.0.2')
    parser.add_argument('-r', '--random_password', help='随机生成包含大小写字母/数字/符号的密码 (E.g hpass -r 16)',
                        action='store', dest='password_length')
    parser.add_argument('-i', '--initialization', help='在当前目录下创建一个新的密码存储文件', action='store_true',
                        dest='init_switch')
    parser.add_argument('-g', '--gui', help='启动GUI工作台', action='store', dest='primary_password')
    args = parser.parse_args()

    if args.init_switch:
        _primary_password = getpass.getpass("Your primary password: ")
        _primary = hmac_sha256_digest(value=_primary_password).decode('utf-8')
        config_dir = str(Path(__file__).resolve().parents[0] / 'config.json')
        hello_password_data_dir = str(Path.cwd() / 'helloPasswordData.json')
        config_json = {'primary': _primary, 'hello_password_data_dir': hello_password_data_dir}
        print(config_json)
        hello_password_data_json = {'account': {}}
        with open(config_dir, 'w', encoding='utf-8') as f:
            json.dump(config_json, f, indent=4, ensure_ascii=False)
        with open(hello_password_data_dir, 'w', encoding='utf-8') as f:
            json.dump(hello_password_data_json, f, indent=4, ensure_ascii=False)
        # https://blog.csdn.net/weixin_42296492/article/details/89331841

    if args.password_length:
        try:
            _password_length = int(args.password_length)
            rp = random_password(length=_password_length)
            print(Fore.GREEN + rp)
        except ValueError:
            print(Fore.RED + '参数 password_length 需要一个数字 (E.g hpass -r 16)')

    if args.primary_password:
        gui_start()


if __name__ == '__main__':
    main()
