#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# vim: expandtab shiftwidth=4 softtabstop=4
#

import json
import sys
import os


class todo(object):
    def __init__(self, fname):
        self._file_name = fname
        self._data_file = None
        self._changed = False
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.cclear = '\033[0m'

    def _prepair_file(self, path):
        structure = '{"todo-list":[]}'
        with open(path, 'w') as f:
            f.write(structure)
        return structure

    def _read_data(self, fname):
        while not os.path.isfile(fname):
            os.chdir('..')
            if os.getcwd() == '/':
                raise FileNotFoundError(
                        'File %s does not exist in path' % fname)
        self._data_file = os.path.join(os.getcwd(), fname)
        with open(os.path.join(os.getcwd(), fname))as f:
            data = f.read()
        if len(data):
            return data
        return self._prepair_file(self._data_file)

    def _parse_data(self, data):
        if data:
            return json.loads(data)
        return ''

    def cprint(self, txt, color):
        if color == 'red':
            print(self.red + txt + self.cclear)
        elif color == 'green':
            print(self.green + txt + self.cclear)
        else:
            print(txt)

    def _show_data(self, data):
            if not (data and len(data['todo-list'])):
                print('Nothing to show.')
            else:
                for idx, task in enumerate(data['todo-list']):
                    if task['is_done']:
                        self.cprint(
                                '%s.\t[x] %s' % (idx, task['text']), 'green')
                    else:
                        self.cprint('%s.\t[ ] %s' % (idx, task['text']), 'red')

    def _add_task(self, task):
        tmp = {
                'text': task,
                'is_done': False
            }
        self._parsed_data['todo-list'].append(tmp)
        self._changed = True

    def _delete_task(self, idx):
        if len(self._parsed_data['todo-list']) <= idx:
            print('Out of range.')
        else:
            data = self._parsed_data['todo-list']
            self._parsed_data['todo-list'] = data[:idx] + data[idx+1:]
        self._changed = True

    def _done_task(self, idx):
        if len(self._parsed_data['todo-list']) <= idx:
            print('Out of range')
        else:
            self._parsed_data['todo-list'][idx]['is_done'] = True
        self._changed = True

    def _undone_task(self, idx):
        if len(self._parsed_data['todo-list']) <= idx:
            print('Out of range')
        else:
            self._parsed_data['todo-list'][idx]['is_done'] = False
        self._changed = True

    def _save_changes(self, data, fname):
        dump = json.dumps(data)
        with open(fname, 'w') as f:
            f.write(dump)

    def _print_usage(self):
        print('Usage: python todo.py [COMMAND] [DATA]\n',
              '\tCOMMAND:\n',
              '\t\tadd - add task(DATA will be added)\n',
              '\t\tdelete - delete task at DATA index\n',
              '\t\tdone - mark task at index DATA as done\n',
              '\t\tundone - mark task at index DATA as undone\n',
              '\tIf none was given tasks will be listed.')

    def run(self):
        self._raw_data = self._read_data(self._file_name)
        self._parsed_data = self._parse_data(self._raw_data)

        if len(sys.argv) == 1:
            self._show_data(self._parsed_data)
        elif len(sys.argv) == 2:
            self._print_usage()
        elif sys.argv[1] == 'add':
            self._add_task(' '.join(sys.argv[2:]))
        elif sys.argv[1] == 'delete':
            self._delete_task(int(sys.argv[2]))
        elif sys.argv[1] == 'done':
            self._done_task(int(sys.argv[2]))
        elif sys.argv[1] == 'undone':
            self._undone_task(int(sys.argv[2]))
        else:
            self._print_usage()

        if self._changed:
            self._save_changes(self._parsed_data, self._data_file)


def main():
    _todo = todo('.todo-list.json')
    _todo.run()

if __name__ == '__main__':
    main()
