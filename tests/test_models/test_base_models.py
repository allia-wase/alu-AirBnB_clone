import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_instance(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_id(self):
        bm = BaseModel()
        self.assertTrue(hasattr(bm, 'id'))

    def test_save(self):
        bm = BaseModel()
        old_updated = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated, bm.updated_at)

    def test_to_dict(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', bm_dict)

if __name__ == '__main__':
    unittest.main()
