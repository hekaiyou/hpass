import sys
import argparse
import configparser
from pathlib import Path
from colorama import init, Fore

h_pass_dir = Path(__file__).resolve().parents[0]
config_dir = h_pass_dir / 'config.ini'


def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser(description='Hello Password')
    parser.add_argument('-v', '--version', help='查看版本信息', action='version', version='%(prog)s v0.0.1')
    parser.add_argument('-i', '--initialization', help='在当前目录下创建一个新的密码存储文件', action='store', dest='file_name')
    args = parser.parse_args()
    if args.file_name:
        file_name = args.file_name
        cf = configparser.ConfigParser()
        cf.add_section("deploy")
        cf.set('deploy', 'file', file_name)
        with open(str(config_dir), "w+") as f:
            cf.write(f)


if __name__ == '__main__':
    main()
