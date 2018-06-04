# !/usr/bin/env python
import sys
import unittest # Lib for Python UT
import shopping # Make sure to import .py you're testing on 
import sqlite3

DBNAME = "test8.db"
DBCONN = sqlite3.connect(DBNAME)

def clearDatabase(DBCONN):
    c = DBCONN.cursor()
    c.execute('DELETE FROM accounts')
    c.execute('DELETE FROM items')
    c.execute('DELETE FROM purchases')
    c.execute('DELETE FROM reviews')
    DBCONN.commit()

class TestFactoryInit(unittest.TestCase):
    def test_Init(self):
        factory = shopping.ShoppingFactory(DBNAME)

        with self.assertRaises(Exception):
            factory = shopping.ShoppingFactory("idonotexist.cc")


class TestPageSize(unittest.TestCase):  
    def test_setPageSize(self):
        factory = shopping.ShoppingFactory(DBNAME)
        factory.setPageSize(11)

        self.assertEqual(factory.getPageSize(), 11)
        factory.setPageSize(1)
        self.assertEqual(factory.getPageSize(), 1)
        factory.setPageSize(5)
        self.assertEqual(factory.getPageSize(), 5)

        with self.assertRaises(Exception):
            factory.setPageSize("hello")
        with self.assertRaises(Exception):
            factory.setPageSize(-1)
        with self.assertRaises(Exception):
            factory.setPageSize(101)
        with self.assertRaises(Exception):
            factory.setPageSize(0)
        
class TestGetPage(unittest.TestCase):
    def test_NumOfItems(self):
        clearDatabase(DBCONN)
        c = DBCONN.cursor()
        c.execute('INSERT INTO items VALUES (1, "Name", 1.99, 3, "laptop, mac")')
        c.execute('INSERT INTO items VALUES (2, "Name", 1.99, 3, "laptop, mac")')
        c.execute('INSERT INTO items VALUES (3, "Name", 1.99, 3, "laptop, mac")')
        c.execute('INSERT INTO items VALUES (4, "Name", 1.99, 3, "laptop, mac")')
        c.execute('INSERT INTO items VALUES (5, "Name", 1.99, 3, "laptop, mac")')
        c.execute('INSERT INTO items VALUES (6, "Name", 1.99, 3, "laptop, mac")')
        c.execute('INSERT INTO items VALUES (7, "Name", 1.99, 3, "laptop, mac")')


        DBCONN.commit()

        factory = shopping.ShoppingFactory(DBNAME)
        factory.setPageSize(3)

        self.assertEqual(len(factory.getNextPage()), 3)
        self.assertEqual(len(factory.getNextPage()), 3)
        self.assertEqual(len(factory.getNextPage()), 1)
        self.assertEqual(len(factory.getNextPage()), 0)        

unittest.main()