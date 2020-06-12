[![PyPI](https://img.shields.io/pypi/v/1)](https://pypi.org/project/hpass/)

# Hello Password

**Why?** Because I can't believe the current password management software. In addition, the fact that the data file cannot be exported bothers me.

## Quickstart

### Use `hpass` enter Workbench

```powershell
$ hpass
Your primary password:
H-Pass>
```

#### Use `help` view help information

```powershell
H-Pass> help
filepath           - Print the absolute path of the password storage file
all                - View the basic information of all password data
add                - Enter a new password data
search <keyword>   - Find password data by keyword
random <length>    - Generate a secure password of specified length
get <id>           - View the password data of the specified id
del <id>           - Delete the password data of the specified id
set <id> <key>     - Modify the key value of the password data of specified id
```

## Installation

As usual, the easiest way is with pip:

```powershell
$ pip install hpass
```

Alternatively you can [download](https://pypi.org/project/hpass/#files) the `hpass-x.x.x.tar.gz` installation file:

```powershell
$ pip install hpass-x.x.x.tar.gz
```

Pip will install dependencies *([colorama](https://pypi.org/project/colorama/) and [PrettyTable](https://pypi.org/project/PrettyTable/))* for you. Alternatively you can clone the repository:

```powershell
$ git clone https://github.com/hekaiyou/hpass.git --recursive
$ cd hpass
$ python setup.py install
```

## Philosophy

## Features

## Useful links

## License

`hpass` is free and open-source software licensed under the [MIT License](https://github.com/hekaiyou/hpass/blob/master/LICENSE).