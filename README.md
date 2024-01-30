# TODO list
[![Build Status](https://travis-ci.org/nathiss/todo-list.svg?branch=master)](https://travis-ci.org/nathiss/todo-list)  
Simple TODO manager written in Python3.  

## Requirements  
- Unix[-like] system  
- Python >= 3.3  

## Installation  
1. Create `.todo-list.json` file. It initially checks your home directory `~/.config/todo/`, then in the project's root, then in parent directories.  
2. Move `todo.py` to your `$PATH` or use symlink.  

## Installation: Add an alias  
If you are a bash users, you can add an alias to your `~/.bash_aliases` file to *more easily* run this application.  Here is an example:  
```bash
# Run the `todo` script.  
# Depends on a data file ~/.config/todo/.todo-list.json (or other location)  
# Replace `user_name` with your Linux username in the example below:  
if [ -x /home/user_name/bin/todo.py ]; then
        alias todo='/usr/bin/python3 /home/user_name/bin/todo.py $*'
fi

```

## Usage
* To list tasks just type:
```bash
$ todo.py
```
* To add new task 'Foo bar' type:
```bash
$ todo.py add Foo bar
```
* To delete task type:
```bash
$ todo.py delete <id>
```
* To mark some task as done type:
```bash
$ todo.py done <id>
```
* To mark some task as undone type:
```bash
$ todo.py undone <id>
```

## License
MIT
