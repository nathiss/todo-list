import os
import sys
import json
import tempfile
import unittest

class TestTodoList(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTodoList, self).__init__(*args, **kwargs)
        self._test_file_name = '.todo-list.json'
        self.todo = todo.todo(self._test_file_name)
        with open(self._test_file_name) as f:
            self._test_file_content = f.read()


    def testPrepairFile(self):
        tmp_handler, tmp_path = tempfile.mkstemp()
        self.todo._prepair_file(tmp_path)
        with open(tmp_path, 'r') as f:
            tmp_content = f.read()
        self.assertEqual(tmp_content, '{"todo-list":[]}')


    def testReadData(self):
        self.assertEqual(self._test_file_content,
                self.todo._read_data(self._test_file_name))
        self.assertRaises(FileNotFoundError,
                lambda: self.todo._read_data('ForSureThisDoesNotExist'))


    def testParseData(self):
        self.assertEqual(self.todo._parse_data(''), '')
        self.assertEqual(self.todo._parse_data(self._test_file_content),
                json.loads(self._test_file_content))


    def testAddTask(self):
        self.todo._parsed_data = json.loads(self._test_file_content)
        self.todo._add_task('Foo bar')
        self.assertTrue(self.todo._changed)
        d = self.todo._parsed_data['todo-list']
        self.assertTrue(any((x['text'] == 'Foo bar' and x['is_done'] == False)
            for x in d))


    def testDeleteTask(self):
        self.todo._parsed_data = json.loads(self._test_file_content)
        l = len(self.todo._parsed_data['todo-list'])
        for i in range(1, l):
            self.todo._delete_task(0)
            self.assertEqual(len(self.todo._parsed_data), l-i)
        self.assertTrue(self.todo._changed)


    def testDoneTask(self):
        self.todo._parsed_data = json.loads(self._test_file_content)
        self.assertTrue(self.todo._parsed_data['todo-list'][0]['is_done'])
        self.assertFalse(self.todo._parsed_data['todo-list'][1]['is_done'])
        for i in range(2):
            self.todo._done_task(i)
            self.assertTrue(self.todo._parsed_data['todo-list'][i]['is_done'])


    def testUndoneTask(self):
        self.todo._parsed_data = json.loads(self._test_file_content)
        self.assertTrue(self.todo._parsed_data['todo-list'][0]['is_done'])
        self.assertFalse(self.todo._parsed_data['todo-list'][1]['is_done'])
        for i in range(2):
            self.todo._undone_task(i)
            self.assertFalse(self.todo._parsed_data['todo-list'][i]['is_done'])


    def testSaveChanges(self):
        tmp_handler, tmp_path = tempfile.mkstemp()
        data = json.loads(self._test_file_content)
        self.todo._save_changes(data, tmp_path)
        with open(tmp_path, 'r') as f:
            tmp_content = f.read()
        self.assertTrue(len(tmp_content))
        self.assertEqual(data, json.loads(tmp_content))


def main():
    # set env
    install_dir = os.path.realpath(os.path.dirname(__file__))
    os.chdir(install_dir)
    sys.path.append('..')
    global todo
    import todo

    unittest.main()


if __name__ == "__main__":
    main()
