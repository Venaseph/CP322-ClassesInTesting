# !/usr/bin/env python
import sys
import unittest
import shopping

#subclasses of test case call methods of that function for t4esting
class TestBuyerReviewInit(unittest.TestCase):
    # Test initializon
    def test_SimpleInit(self):
        review = shopping.BuyerReview(1, "This sucks", "chris")
        #assertEqual checks two values, if not flags it as failing
        self.assertEqual(review.getRating(), 1)
        self.assertEqual(review.getReview(), "This sucks")
        self.assertEqual(review.getUserid(), 'chris')

        review2 = shopping.BuyerReview(4, "This is Great", "brent")
        self.assertEqual(review2.getRating(), 4)
        self.assertEqual(review2.getReview(), "This is Great")

    def test_RatingWithLetters(self):
        with self.assertRaises(Exception):
            review = shopping.BuyerReview("abc", "", "")

    def test_ReviewWithNum(self):
        with self.assertRaises(Exception):
            review = shopping.BuyerReview(2, 99, 100)

            


unittest.main()