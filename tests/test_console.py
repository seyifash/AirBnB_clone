#!/usr/bin/python3
"""
This contains the class for the console test cases
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommandConsole(unittest.TestCase):

    def setUp(self):
        """runs this before the test methods"""
        self.console = HBNBCommand()
        self.storage_cpy = FileStorage()

    def test_prompt(self):
        """test cases for prompt"""
        self.assertEqual('(hbnb) ', self.console.prompt)

    # def test_help(self):
    #     """test cases for help command"""
    #     quit_help = "Quit command to exit the program"
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         self.console.onecmd("help")
    #         self.assertEqual(f.getvalue().strip(), quit_help)

    def test_create(self):
        """test cases for create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            """# Test case where class name is missing"""
            self.console.onecmd("create")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

            """# Test case where class name doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

            """# Test case where class name exists (BaseModel)"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            self.assertEqual(str, type(cmd_output))

            """# Check if ID is printed"""
            instance_id = cmd_output.split()[-1]
            self.assertIn(instance_id, cmd_output)

    def test_show(self):
        """test cases for show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            # Test case where class name is missing
            self.console.onecmd("show")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

            # Test case where class name doesn't exist
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

            # Test case where instance id is missing
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** instance id missing **")

            # Test case where instance doesn't exist
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 121212")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** no instance found **")

            # Test case where class name exists and instance id exists
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
        """# Test destroy with valid instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            instance_id = cmd_output.split()[-1]

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {instance_id}")
            destroy_output = f.getvalue().strip()

            self.assertEqual(destroy_output, "")

        # Test destroy with missing class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

        # Test destroy with non-existent class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy SomeModel 1234-1234-1234")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

        # Test destroy with missing instance ID
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** instance id missing **")

        # Test destroy with non-existent instance
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 121212")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** no instance found **")

    def test_all(self):
        """test cases for all commmand"""

        self.console.onecmd("create User")
        self.console.onecmd("create BaseModel")

        # Retrieve all instances for a valid class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            all_output = f.getvalue().strip()

            # Check if the output matches the expected format
            self.assertTrue("[BaseModel]" in all_output)
            self.assertTrue("'created_at':" in all_output)
            self.assertTrue("'id':" in all_output)
            self.assertTrue("'updated_at':" in all_output)

        # Test all with non-existent class name
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


if __name__ == "__main__":
    unittest.main()
