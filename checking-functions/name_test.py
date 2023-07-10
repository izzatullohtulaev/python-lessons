import unittest
from name import get_fullname

class TestName(unittest.TestCase):
    def test_fullname(self):
        name = get_fullname('alijon', 'valiyev')
        self.assertEqual(name, "Alijon Valiyev")
    def test_surname(self):
        name = get_fullname('alijon', 'valiyev', 'olimovich')
        self.assertEqual(name, "Alijon Olimovich Valiyev")

unittest.main()