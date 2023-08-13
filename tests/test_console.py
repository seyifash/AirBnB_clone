#!/usr/bin/python3
"""
This contains the class for the console test cases
"""
import unittest
import sys
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """represents test case for HBNBCommand"""

    def setUp(self):
        """runs this before the test methods"""
        self.console = HBNBCommand()
        self.storage_cpy = FileStorage()

    def test_prompt(self):
        """test cases for prompt"""
        self.assertEqual('(hbnb) ', self.console.prompt)

    def test_create(self):
        """test cases for create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            """Test case where class name is missing"""
            self.console.onecmd("create")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

            """Test case where class name doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

            """Test case where class name exists (BaseModel)"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            self.assertEqual(str, type(cmd_output))

            """ Check if ID is printed"""
            instance_id = cmd_output.split()[-1]
            self.assertIn(instance_id, cmd_output)

    def test_show(self):
        """test cases for show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 121212")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            instance_id = cmd_output.split()[-1]

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {instance_id}")
            show_output = f.getvalue().strip()

            self.assertIn("BaseModel", show_output)
            self.assertIn(instance_id, show_output)

    def test_destroy(self):
        """Test destroy with valid instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            instance_id = cmd_output.split()[-1]

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {instance_id}")
            destroy_output = f.getvalue().strip()

            self.assertEqual(destroy_output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy SomeModel 1234-1234-1234")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 121212")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** no instance found **")

    def test_all(self):
        """test cases for all commmand"""

        self.console.onecmd("create User")
        self.console.onecmd("create BaseModel")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            all_output = f.getvalue().strip()

            self.assertTrue("[BaseModel]" in all_output)
            self.assertTrue("'created_at':" in all_output)
            self.assertTrue("'id':" in all_output)
            self.assertTrue("'updated_at':" in all_output)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all SomeModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

    def test_quit(self):
        """test cases for quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(f.getvalue().strip(), "")

    def test_EOF(self):
        """test cases for   EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue().strip(), "")

    def test_emptyline(self):
        """test cases for emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue().strip(), "")

    def test_default(self):
        """test cases for default method"""
        with patch('sys.stdout', new=StringIO()) as f:
            uk = "jkj"
            self.console.onecmd(uk)
            output = f.getvalue().strip()
            self.assertEqual(output, "*** Unknown syntax: {}".format(uk))

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id_var = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.all()")
            output = f.getvalue().strip()
            self.assertEqual(output[0], "[")
            self.assertEqual(output[-1], "]")
            self.assertTrue(id_var in output)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('BaseModel.show("{}")'.format(id_var))
            output = f.getvalue().strip()
            self.assertTrue(id_var in output)
            self.assertTrue(output.startswith("[BaseModel]"))
            self.assertIn("datetime", output)
            self.assertIn("updated_at", output)
            self.assertIn("created_at", output)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('BaseModel.show()')
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('BaseModel.show("135)')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            all_objs = len(self.storage_cpy.all())
            self.console.onecmd('BaseModel.destroy("{}")'.format(id_var))
            self.assertEqual(len(self.storage_cpy.all()), all_objs - 1)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('BaseModel.destroy()')
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('BaseModel.destroy("135)')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")


class TestHBNBCommand_help(unittest.TestCase):
    """unittest for testing the help me for each of the command"""

    def test_help_quit(self):
        """Test cases for help quit command"""
        quit_help = "Quit command to exit the program"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(quit_help, f.getvalue().strip())

    def test_help_eof(self):
        """test cases for help eof command"""
        eof_help = "ctrl+D to exit the program"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(eof_help, f.getvalue().strip())

    def test_help_create(self):
        """test cases for help eof command"""
        create_help = "creates the instance of the variable"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(create_help, f.getvalue().strip())

    def test_help_update(self):
        """test case for the helf update command"""
        update_help = "updates an attribute in an object"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(update_help, f.getvalue().strip())

    def test_help_destroy(self):
        """test case for the helf destroy command"""
        destroy_help = "destroys an object from the json database"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(destroy_help, f.getvalue().strip())

    def test_help_count(self):
        """test case for the helf count command"""
        count_help = "counts the number of intsnaces of an object"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(count_help, f.getvalue().strip())

    def test_help_show(self):
        """test case for the helf destroy command"""
        show_help = "shows the object based on id"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(show_help, f.getvalue().strip())

    def test_help(self):
        """Test case for the help command itself"""
        c = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(command_help, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
