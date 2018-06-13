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
        # Empty for testing
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

    
    def test_getItems(self):
        clearDatabase(DBCONN)
        c = DBCONN.cursor()
        c.execute('INSERT INTO items VALUES (1, "Macbook", 3000.00, 300, "laptop, mac")')
        c.execute('INSERT INTO items VALUES (2, "Dell", 30.00, 2, "laptop, pc")')
        DBCONN.commit()

        factory = shopping.ShoppingFactory(DBNAME)
        items = factory.getNextPage()
        self.assertEqual(len(items), 2)

        self.assertTrue(isinstance(items[0], shopping.ShoppingItem))
        self.assertTrue(isinstance(items[1], shopping.ShoppingItem))

    def test_itemValues(self):
        clearDatabase(DBCONN)
        c = DBCONN.cursor()
        c.execute('INSERT INTO items VALUES (1, "Macbook", 3000.00, 300, "laptop,mac")')
        DBCONN.commit()

        factory = shopping.ShoppingFactory(DBNAME)
        item = factory.getNextPage()
        self.assertEqual(len(item), 1)

        self.assertEqual(item[0].getName(), "Macbook")
        self.assertEqual(item[0].getPrice(), 3000.00)
        self.assertEqual(item[0].getNumberSold(), 300)

        tags = item[0].getTags()
        self.assertEqual(len(tags), 2)
        self.assertTrue("laptop" in tags and "mac" in tags)

    # Make Sure to test reviews and buyers

    def test_SortMostSold(self):
        clearDatabase(DBCONN)
        c = DBCONN.cursor()
        c.execute('INSERT INTO items VALUES (1, "Macbook", 3000.00, 2, "laptop,mac")')
        c.execute('INSERT INTO items VALUES (2, "PC", 3000.00, 9, "laptop,mac")')
        c.execute('INSERT INTO items VALUES (3, "Phone", 3000.00, 7, "laptop,mac")')
        DBCONN.commit()

        factory = shopping.ShoppingFactory(DBNAME)
        factory.sortMostSold()

        items = factory.getNextPage()

        self.assertEqual(len(items), 3)

        self.assertEqual(items[0].getName(), "PC")
        self.assertEqual(items[1].getName(), "Phone")
        self.assertEqual(items[2].getName(), "Macbook")

    def test_SortLowestPrice(self):
        clearDatabase(DBCONN)
        c = DBCONN.cursor()
        c.execute('INSERT INTO items VALUES (1, "Macbook", 3000.00, 2, "laptop,mac")')
        c.execute('INSERT INTO items VALUES (2, "PC", 2000.00, 9, "laptop,mac")')
        c.execute('INSERT INTO items VALUES (3, "Phone", 1000.00, 7, "laptop,mac")')
        DBCONN.commit()

        factory = shopping.ShoppingFactory(DBNAME)
        factory.sortLowestPrice()

        items = factory.getNextPage()

        self.assertEqual(items[0].getPrice(), 1000.00)

    def test_SearchFilter(self):
        clearDatabase(DBCONN)
        c = DBCONN.cursor()
        c.execute('INSERT INTO items VALUES (1, "Macbook", 3000.00, 2, "laptop, mac")')
        c.execute('INSERT INTO items VALUES (2, "PC", 3000.00, 9, "windows, dell")')
        c.execute('INSERT INTO items VALUES (3, "Phone", 3000.00, 7, "phone")')
        DBCONN.commit()

        factory = shopping.ShoppingFactory(DBNAME)
        factory.setSearchFilter(["laptop"])
        items = factory.getNextPage()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].getName(), "Macbook")

    def test_reviews(self):
        clearDatabase(DBCONN)
        c = DBCONN.cursor()
        c.execute('INSERT INTO reviews VALUES (1, 4, "Review I", "Chris")')
        c.execute('INSERT INTO reviews VALUES (1, 2, "Review II", "Brent")')
        c.execute('INSERT INTO reviews VALUES (1, 4, "Review III", "Tyler")')
        c.execute('INSERT INTO reviews VALUES (1, 2, "Review IV", "Mike")')
        DBCONN.commit

        factory = shopping.ShoppingFactory(DBNAME)
        items = factory.getNextPage()
        self.assertEqual(len(items), 0)

        reviews = items[0].getReviews()
        self.assertEqual(len(reviews), 4)

        


unittest.main()