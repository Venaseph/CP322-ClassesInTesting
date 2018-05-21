# !/usr/bin/env python
import sys
import unittest
import shopping

#subclasses of test case call methods of that function for t4esting
class TestBuyerReviewInit(unittest.TestCase):
    # Test initializon
    def test_BuyerReviewInit(self):
        review = shopping.BuyerReview(1, 'This sucks', 'chris')
        #assertEqual checks two values, if not flags it as failing
        self.assertEqual(review.getRating(), 1)
        self.assertEqual(review.getReview(), "This sucks")
        self.assertEqual(review.getUserid(), 'chris')

        review2 = shopping.BuyerReview(4, 'This is Great', "brent")
        self.assertEqual(review2.getRating(), 4)
        self.assertEqual(review2.getReview(), "This is Great")
        self.assertEqual(review2.getUserid(), "brent")


    def test_Rating(self):
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('abc', '', '')
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
            review = shopping.BuyerReview('', 'a', '')
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('', '1 0', '')
        with self.assertRaises(Exception):
            review = shopping.BuyerReview('', 1.5, '')         

            


unittest.main()