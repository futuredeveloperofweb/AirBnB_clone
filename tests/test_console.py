#!/usr/bin/python3
'''A module to test the console file file and HBNBCommand class'''
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.command = HBNBCommand()

    def test_prompt_string(self):
        self.assertEqual('(hbnb) ', self.command.prompt)

    def test_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(self.command.onecmd(''))
            self.assertEqual('', output.getvalue().strip())


class TestHBNBCommand(unittest.TestCase):
    '''tests for HBNB class'''

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        command = HBNBCommand()
        self.assertTrue(command.onecmd("quit"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        command = HBNBCommand()
        self.assertTrue(command.onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        command = HBNBCommand()
        command.onecmd("destroy")
        self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        command = HBNBCommand()
        command.onecmd('create BaseModel')
        self.assertNotEqual('', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        command = HBNBCommand()
        command.onecmd('show BaseModel')
        self.assertEqual('** instance id missing **\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        command = HBNBCommand()
        command.onecmd('all BaseModel')
        self.assertNotEqual('', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        command = HBNBCommand()
        command.onecmd("update BaseModel")
        self.assertEqual("** instance id missing **\n", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
