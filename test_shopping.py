# !/usr/bin/env python
import sys
import unittest # Lib for Python UT
import shopping # Make sure to import .py you're testing on 

#subclasses of test case call methods of that function for testing
class TestBuyerReviewInit(unittest.TestCase):
    # Test initializon and positive result testing
    def test_BuyerReviewInit(self):
        review = shopping.BuyerReview(1, 'This sucks-?', 'chris')
        #assertEqual checks two values, if not flags it as failing. Get Testing
        self.assertEqual(review.getRating(), 1) 
        self.assertEqual(review.getReview(), "This sucks-?")
        self.assertEqual(review.getUserid(), 'chris')

        review2 = shopping.BuyerReview(4, 'This is Great.', 'brent_test')
        self.assertEqual(review2.getRating(), 4)
        self.assertEqual(review2.getReview(), 'This is Great.')
        self.assertEqual(review2.getUserid(), 'brent_test')

    # Test Rating
    def test_Rating(self):
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('abc.  ', '', '')
        with self.assertRaises(Exception):
            review = shopping.BuyerReview(-1, '', '')
        with self.assertRaises(Exception):
            review = shopping.BuyerReview(' ', '', '')
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('1 2', '', '')            


    def test_Review(self):
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('', 99, '')
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('', ' ', '')
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('', '1 0', '')
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('', 1.5, '')

    def test_UserId(self):
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('', '', 'this way')       
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('', '', 'brent_ test')     
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('', '', 1)     
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('', '', -45)       
            
class TestShoppingItemInit(unittest.TestCase):
    # Test initializon and positive result testing
    def test_ShoppingItemInit(self):
        shoppingItem = shopping.ShoppingItem(5.99, 1, ['review1', 'review2'], ['games', 'fun'], ['john', 'mike', 'ashley'])
        #assertEqual checks two values, if not flags it as failing. Get Testing.
        self.assertEqual(shoppingItem.getPrice(), 5.99)
        self.assertEqual(shoppingItem.getNumberSold(), 1)
        self.assertEqual(shoppingItem.getAverageRating(), 0)
        self.assertEqual(shoppingItem.getReviews(), ['review1', 'review2'])
        self.assertEqual(shoppingItem.getTags(), ['games', 'fun'])
        self.assertEqual(shoppingItem.getBuyers(), ['john', 'mike', 'ashley'])    

        shoppingItem2 = shopping.ShoppingItem(7.00, 5, ['review1', 'review2', 'review3'], ['tag1', 'tag2', 'tag3'], ['tyler', 'brent', 'Tony'])
        self.assertEqual(shoppingItem2.getPrice(), 7.00)
        self.assertEqual(shoppingItem2.getNumberSold(), 5)
        self.assertEqual(shoppingItem2.getAverageRating(), 0)
        self.assertEqual(shoppingItem2.getReviews(), ['review1', 'review2', 'review3'])
        self.assertEqual(shoppingItem2.getTags(), ['tag1', 'tag2', 'tag3'])
        self.assertEqual(shoppingItem2.getBuyers(), ['tyler', 'brent', 'Tony'])
    
    def test_GetPrice(self):
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem(-5.99, 1, [], [], [])
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem('6.02', 1, [], [], [])
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem('$0.50', 1, [], [], [])
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem('a', 1, [], [], [])

    def test_GetNumberSold(self):
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem(5.00, 'a', [], [], [])
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem(5.00, -5, [], [], [])
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem(5.00, 1.5, [], [], [])

unittest.main()