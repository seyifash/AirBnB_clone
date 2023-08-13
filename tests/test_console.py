#!/usr/bin/python3
"""
This contains the class for the console test cases
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class Test_HBNBCommandConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            # Test case where class name is missing
            self.console.onecmd("create")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

            # Test case where class name doesn't exist
            self.console.onecmd("create MyModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

            # Test case where class name exists (BaseModel)
            self.console.onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            self.assertIn("BaseModel", cmd_output)

            # Check if ID is printed
            instance_id = cmd_output.split()[-1]
            self.assertIn(instance_id, cmd_output)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            # Test case where class name is missing
            self.console.onecmd("show")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

            # Test case where class name doesn't exist
            self.console.onecmd("show MyModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

            # Test case where instance id is missing
            self.console.onecmd("show BaseModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** instance id missing **")

            # Test case where instance doesn't exist
            self.console.onecmd("show BaseModel 121212")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** no instance found **")

            # Test case where class name exists and instance id exists
            self.console.onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            instance_id = cmd_output.split()[-1]

            self.console.onecmd(f"show BaseModel {instance_id}")
            show_output = f.getvalue().strip()

            self.assertIn("BaseModel", show_output)
            self.assertIn(instance_id, show_output)

    def test_destroy(self):
        # Test destroy with valid instance
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            instance_id = cmd_output.split()[-1]

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
        # Create instances
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create User")

        # Retrieve all instances for a valid class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            all_output = f.getvalue().strip()

            # Check if the output matches the expected format
            self.assertTrue(all_output.startswith("["))
            self.assertTrue("{'created_at':" in all_output)
            self.assertTrue("'id':" in all_output)
            self.assertTrue("'updated_at':" in all_output)

        # Test all with non-existent class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all SomeModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(f.getvalue().strip(), "")

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue().strip(), "")

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue().strip(), "")


if __name__ == "__main__":
    unittest.main()
