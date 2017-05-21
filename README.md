# TODO list

Simple TODO manager written in Python3.

## Requirements
- Unix[-like] system
- Python >= 3.3

## Installation
1. Create `.todo-list.json` in the project's root.
2. Move `todo.py` to your `$PATH` or use symlink.

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
