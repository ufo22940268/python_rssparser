import sys
sys.path.append("/home/ccheng/workspace_tb/python_rssparser")

import unittest
import converttime
import dbutils

class datetimetest(unittest.TestCase):
    def test_convert(self):
        t = "Sat, 21 Jul 2012 00:30:00 EST"
        self.assertTrue(converttime.convert(t) > 1000)

class datebasetest(unittest.TestCase):
    def setUp(self):
        self.clear_data()
        self.insert_data()
        pass        

    def test_cursor(self):
        self.assertIsNotNone(dbutils.connect())

    def test_date(self):
        conn = dbutils.connect()
        c = conn.cursor()
        c.execute("select * from data")
        conn.commit()
        #self.assertEqual(1, c.rowcount);

    def clear_data(self):
        c = dbutils.connect()
        c.execute("delete from data")

    def insert_data(self):
        c = dbutils.connect()
        c.execute("insert into data values('1', '1', '1')")

if __name__ == '__main__':
    unittest.main()
