#!/usr/bin/python3
"""Defines BaseModel class unittest"""
import os
import models
from datetime import datetime
import unittest
from models.base_model import BaseModel
from time import sleep


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for BaseModel class"""

    def no_args_test(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def new_instance_saved_in_objects_test(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def public_attribute_id_type_tests(self):
        self.assertEqual(str, type(BaseModel().id))

    def public_attribute_created_at_type_test(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def public_attribute_updated_at_type_test(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def two_models_created_at_diff_time_test(self):
        ins1 = BaseModel()
        sleep(0.1)
        ins2 = BaseModel()
        self.assertLess(ins1.created_at, ins2.created_at)

    def two_models_updated_at_diff_time_test(self):
        ins1 = BaseModel()
        sleep(0.1)
        ins2 = BaseModel()
        self.assertLess(ins1.updated_at, ins2.updated_at)

    def two_models_unique_ids_test(self):
        instance_1 = BaseModel()
        instance_2 = BaseModel()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def str_representation_test(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        ins = BaseModel()
        ins.id = "00-11-01"
        ins.created_at = dt
        ins.updated_at = dt
        ins_str = ins.__str__()
        self.assertIn("[BaseModel] (00-11-01)", ins_str)
        self.assertIn("'id': '00-11-01'", ins_str)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def unused_args_test(self):
        ins = BaseModel(None)
        self.assertNotIn(None, ins.__dict__.values())

    def constructing_with_kwargs_test(self):
        td = datetime.today()
        isof_td = td.isoformat()
        ins = BaseModel(id="00-22", created_at=isof_td, updated_at=isof_td)
        self.assertEqual(ins.id, "00-22")
        self.assertEqual(ins.created_at, td)
        self.assertEqual(ins.updated_at, td)

    def initializing_with_None_kwargs_test(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        td = datetime.today()
        isof_td = td.isoformat()
        ins = BaseModel("03", id="02", created_at=isof_td, updated_at=isof_td)
        self.assertEqual(ins.id, "02")
        self.assertEqual(ins.created_at, td)
        self.assertEqual(ins.updated_at, td)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

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

    def save_method_first_test(self):
        ins = BaseModel()
        sleep(0.1)
        update_t = ins.updated_at
        ins.save()
        self.assertLess(update_t, ins.updated_at)

    def save_method_second_test(self):
        ins = BaseModel()
        sleep(0.1)
        update_t = ins.updated_at
        ins.save()
        update_s = ins.updated_at
        self.assertLess(update_t, updated_s)
        sleep(0.1)
        ins.save()
        self.assertLess(update_t, ins.updated_at)

    def save_with_arg_test(self):
        ins = BaseModel()
        with self.assertRaises(TypeError):
            ins.save(None)

    def save_updates_file_test(self):
        ins = BaseModel()
        ins.save()
        new_ins = "BaseModel." + ins.id
        with open("file.json", "r") as jsonf:
            self.assertIn(new_ins, jsonf.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def to_dict_type_test(self):
        ins = BaseModel()
        self.assertTrue(dict, type(ins.to_dict()))

    def to_dict_keys_test(self):
        ins = BaseModel()
        self.assertIn("id", ins.to_dict())
        self.assertIn("created_at", ins.to_dict())
        self.assertIn("updated_at", ins.to_dict())
        self.assertIn("__class__", ins.to_dict())

    def to_dict_added_attributes_test(self):
        ins = BaseModel()
        ins.name = "Johannesburg"
        ins.my_number = 207
        self.assertIn("name", ins.to_dict())
        self.assertIn("my_number", ins.to_dict())

    def to_dict_datetime_attrib_type_test(self):
        ins = BaseModel()
        ins_dict_f = bm.to_dict()
        self.assertEqual(str, type(ins_dict_f["created_at"]))
        self.assertEqual(str, type(ins_dict_f["updated_at"]))

    def to_dict_output_test(self):
        dt = datetime.today()
        ins = BaseModel()
        ins.id = "111-000"
        ins.created_at = dt
        ins.updated_at = dt
        dictf = {
            'id': '111-000',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(ins.to_dict(), dicf)

    def test_to_dict_with_arg(self):
        ins = BaseModel()
        with self.assertRaises(TypeError):
            ins.to_dict(None)


if __name__ == "__main__":
    unittest.main()
