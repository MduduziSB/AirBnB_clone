#!/usr/bin/env python3
"""BaseModel class unitttests"""

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """super class BaseModel test cases """

    def setUp(self):
        """class setup tests"""
        self.model1 = BaseModel()
        args_test = {'created_at': datetime(2017, 2, 10, 2, 6, 55, 258849),
                     'updated_at': datetime(2017, 2, 10, 2, 6, 55, 258966),
                     'id': '46458416-e5d5-4985-aa48-a2b369d03d2a',
                     'name': 'model1'}
        self.model2 = BaseModel(args_test)
        self.model2.save()

    def class_doc_test(self):
        """class documentation test"""
        self.assertIsNotNone(BaseModel.__doc__)

    def method_doc_test(self):
        """ BaseModel's method documentation test"""
        methods = [
            BaseModel.__init__, BaseModel.__str__,
            BaseModel.save, BaseModel.to_dict
        ]
        for meth in methods:
            self.assertIsNotNone(meth.__doc__)

    def initial_attribute_test(self):
        """id attribute  Test"""
        model = BaseModel()
        model2 = BaseModel()

        self.assertTrue(hasattr(test_model, 'id'))
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.id, str)

        self.assertTrue(uuid.UUID(model.id))
        self.assertNotEqual(model.id, model2.id)
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertIsNotNone(model.created_at)
        self.assertIsInstance(model.created_at, datetime)

        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsNotNone(model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

        self.assertGreater(model.updated_at, model.created_at)

        test_with_arg = BaseModel("args")
        self.assertNotIn("args", test_with_arg.__dict__)

        str_ = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(test_model), str_)

    def test_kwargs_input(self):
        """BaseModel construction with kwargs test"""
        dic = {
            'id': 'test_id',
            'created_at': '2023-08-09T12:34:56.789012',
            'updated_at': '2023-08-09T13:45:12.345678',
            'name': 'Wills',
            'value': 42
        }
        model = BaseModel(**dic)

        self.assertEqual(model.id, "test_id")
        self.assertEqual(model.name, "Wills")
        self.assertEqual(model.value, 42)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict_data_type(self):
        """data type tests """
        model = BaseModel()
        model.name = "Peter"
        model.age = "27"
        model.num = 12
        model.float_num = 12.00
        model.bool_val = True

        test_dict = model.to_dict()

        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict["__class__"], "BaseModel")
        self.assertEqual(test_dict["id"], model.id)
        self.assertEqual(test_dict["name"], "Peter")
        self.assertEqual(test_dict["age"], "27")
        self.assertEqual(test_dict["num"], 12)
        self.assertEqual(test_dict["float_num"], 12.00)
        self.assertEqual(test_dict["bool_val"], True)

    def test_instantiation(self):
        """Instinitiation tests"""
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertTrue(hasattr(self.model1, "updated_at"))

    def test_reinstantiation(self):
        """reinstantiation"""
        self.assertIsInstance(self.model2, BaseModel)

    def test_save(self):
        """saving test"""
        self.assertTrue(hasattr(self.model1, "updated_at"))
        self.model1.save()
        self.assertTrue(hasattr(self.model1, "updated_at"))
        old_time = self.model2.updated_at
        self.model2.save()
        self.assertNotEqual(old_time, self.model2.updated_at)


if __name__ == "__main__":
    unittest.main()
