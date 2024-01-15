#!/usr/bin/python3
"""Defines tests for the Place of the project"""
import io
import os
import sys
import unittest
from datetime import datetime
from models.place import Place
from models import storage
from time import sleep


class TestPlace_Init(unittest.TestCase):
    """Tests for the initialization of the Place class"""
    def test_instance_type(self):
        """tests that the instance is of Place"""
        self.assertEqual(Place, type(Place()))

    def test_init_none(self):
        """tests that whether an instance's dict
        includes None if passed during initialization"""
        self.assertNotIn(None, Place(None).__dict__.values())

    def test_init_args(self):
        """checks that *args isn't used if passed during initialization"""
        dt = datetime.now()
        obj = Place('abc123', dt)
        self.assertNotIn('abc123', obj.__dict__.values())
        self.assertNotIn(repr(dt), obj.__dict__.values())

    def test_instance_id_is_str(self):
        "tests that an instance's id is a string"
        self.assertEqual(str, type(Place().id))

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        date = datetime.now()
        date_iso = date.isoformat()
        obj = Place("12", id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(obj.id, "345")
        self.assertEqual(obj.created_at, date)
        self.assertEqual(obj.updated_at, date)

    def test_instance_id_unique(self):
        "tests that an instance id is unique"
        obj1 = Place()
        obj2 = Place()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_instance_created_type(self):
        "tests that an instance's createdAt attr is a datetime obj"
        self.assertEqual(datetime, type(Place().created_at))

    def test_two_instances_created_at(self):
        "tests that two instance's createdAt attr are different"
        obj1 = Place()
        sleep(1)
        obj2 = Place()
        self.assertNotEqual(obj1.created_at, obj2.created_at)

    def test_instance_updated_type(self):
        "tests that an instance's updatedAt attr is a datetime obj"
        self.assertEqual(datetime, type(Place().updated_at))

    def test_two_instances_created_at(self):
        "tests that two instance's updatedAt attr are different"
        obj1 = Place()
        sleep(1)
        obj2 = Place()
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_newly_created_instance_is_stored_in_storage(self):
        """tests that a newly created instance has
        been added to file storage"""
        self.assertIn(Place(), storage.all().values())

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == 'print':
            print(rect)
        else:
            rect.__str__()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method(self):
        date = datetime.now()
        date_repr = repr(date)
        obj = Place()
        obj.id = "123456"
        obj.created_at = obj.updated_at = date
        objstr = obj.__str__()
        self.assertIn("[Place] (123456)", objstr)
        self.assertIn("'id': '123456'", objstr)
        self.assertIn("'created_at': " + date_repr, objstr)
        self.assertIn("'updated_at': " + date_repr, objstr)

    def test_name_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'name'))

    def test_city_id_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'city_id'))

    def test_state_id_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'state_id'))

    def test_desc_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'description'))

    def test_number_rooms_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'number_rooms'))

    def test_number_bathrooms_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'number_bathrooms'))

    def test_max_guest_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'max_guest'))

    def test_price_by_night_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'price_by_night'))

    def test_latitude_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'latitude'))

    def test_longitude_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'longitude'))

    def test_amenity_attr_exists(self):
        obj = Place()
        self.assertTrue(hasattr(obj, 'amenity_ids'))


class TestPlace_Save(unittest.TestCase):
    """Tests the save method of the Place class"""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        obj = Place()
        sleep(0.05)
        original_time = obj.updated_at
        obj.save()
        self.assertLess(original_time, obj.updated_at)

    def test_two_saves(self):
        obj = Place()
        sleep(0.05)
        original_time = obj.updated_at
        obj.save()
        second_time = obj.updated_at
        self.assertLess(original_time, second_time)
        sleep(0.05)
        obj.save()
        self.assertLess(second_time, obj.updated_at)

    def test_save_with_arg(self):
        obj = Place()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_save_updates_file(self):
        obj = Place()
        obj.save()
        obj_id = "Place." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Tests for the to_dict method of the Place class"""

    def test_to_dict_type(self):
        obj = Place()
        self.assertTrue(dict, type(obj.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        obj = Place()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_to_dict_contains_added_attributes(self):
        obj = Place()
        obj.name = "Holberton"
        obj.my_number = 98
        self.assertIn("name", obj.to_dict())
        self.assertIn("my_number", obj.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        obj = Place()
        obj_dict = obj.to_dict()
        self.assertEqual(str, type(obj_dict["created_at"]))
        self.assertEqual(str, type(obj_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        obj = Place()
        obj.id = "123456"
        obj.created_at = obj.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(obj.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        obj = Place()
        self.assertNotEqual(obj.to_dict(), obj.__dict__)

    def test_to_dict_with_arg(self):
        obj = Place()
        with self.assertRaises(TypeError):
            obj.to_dict(None)


if __name__ == "__main__":
    unittest.main()
