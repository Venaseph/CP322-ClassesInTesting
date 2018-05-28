# !/usr/bin/env python
import sys
import unittest # Lib for Python UT
import shopping # Make sure to import .py you're testing on 

#subclasses of test case call methods of that function for testing
class TestBuyerReview(unittest.TestCase):
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
            review = shopping.BuyerReview('xabc.  ', '', '')
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
            
class TestShoppingItem(unittest.TestCase):
    # Test initializon and positive result testing
    def test_ShoppingItemInit(self):
        reviews = [shopping.BuyerReview(1, 'This sucks-?', 'chris'),
                   shopping.BuyerReview(2, 'This is Great.', 'brent_test'),
                   shopping.BuyerReview(3, 'This is Great.', 'brent_test')]
        tags = ['computer', 'laptop', 'mac']
        buyers = ['chris', 'brent', 'aaron']
        shoppingItem = shopping.ShoppingItem('name', 5.99, 1, reviews, tags, buyers)

        # AssertEqual checks two values, if not flags it as failing. Get Testing.
        self.assertEqual(shoppingItem.getName(), 'name')
        self.assertEqual(shoppingItem.getPrice(), 5.99)
        self.assertEqual(shoppingItem.getNumberSold(), 1)
        self.assertEqual(shoppingItem.getAverageRating(), 2)
        self.assertEqual(shoppingItem.getReviews(), reviews)
        self.assertEqual(shoppingItem.getTags(), tags)
        self.assertEqual(shoppingItem.getBuyers(), buyers)   
    
    def test_GetPrice(self):
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem('name', -5.99, 1, [], [], [])
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem('name', '6.02', 1, [], [], [])
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem('name', '$0.50', 1, [], [], [])
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem('name', 'a', 1, [], [], [])

    def test_GetNumberSold(self):
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem('name', 5.00, 'a', [], [], [])
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem('name', 5.00, -5, [], [], [])
        with self.assertRaises(Exception):
            shoppingItem = shopping.ShoppingItem('name', 5.00, 1.5, [], [], [])

    # def test_Gets(self):
    #     reviews = [shopping.BuyerReview(1, 'This Sucks', 'chris'),
    #                shopping.BuyerReview(2, 'This Sucks', 'Brent'),
    #                shopping.BuyerReview(3, 'This Sucks', 'Aaron'),]

    #     item = shopping.ShoppingItem('name', 1.00, 0, reviews, [], [])
    #     self.assertEqual(item.getAverageRating(), 2)

        # # Check len of lists for match
        # self.assertEqual(len(reviews), len(shoppingItem.getReviews()))
        # # Make sure objects match
        # for review in reviews:
        #     self.assertTrue(review in shoppingItem.getReviews())
        
        # # Check len of lists for match
        # self.assertEqual(len(tags), len(shoppingItem.getTags()))
        # # Make sure objects match
        # for tag in tags:
        #     self.assertTrue(tag in shoppingItem.getTags())

        # self.assertEqual(len(buyers), len(shoppingItem.getBuyers()))
        # # Make sure objects match
        # for buyer in buyers:
        #     self.assertTrue(buyer in shoppingItem.getBuyers())  

    def test_AddPurchase(self):
        reviews = [shopping.BuyerReview(1, 'This sucks-?', 'chris'),
        shopping.BuyerReview(2, 'This is Great.', 'brent_test'),
        shopping.BuyerReview(3, 'This is Great.', 'brent_test')]
        tags = ['computer', 'laptop', 'mac']
        buyers = ['chris', 'brent', 'aaron']
        shoppingItem = shopping.ShoppingItem('name', 5.99, 1, reviews, tags, buyers)

        shoppingItem.addPurchase('Chris')
        self.assertEqual(shoppingItem.getBuyers()[-1], 'Chris')
        self.assertEqual(shoppingItem.getNumberSold(), 2)

        with self.assertRaises(Exception):
            testPurchase = shoppingItem.addPurchase(25)
        with self.assertRaises(Exception):
            testPurchase = shoppingItem.addPurchase(-5)
        with self.assertRaises(Exception):
            testPurchase = shoppingItem.addPurchase('??!_SDJM||')

    def test_AddReview(self):
        reviews = [shopping.BuyerReview(1, 'This sucks-?', 'chris'),
        shopping.BuyerReview(2, 'This is Great.', 'brent_test'),
        shopping.BuyerReview(3, 'This is Great.', 'brent_test')]
        tags = ['computer', 'laptop', 'mac']
        buyers = ['chris', 'brent', 'aaron']
        shoppingItem = shopping.ShoppingItem('name', 5.99, 1, reviews, tags, buyers)

        addSample = shopping.BuyerReview(4, 'This is a new review', 'Mark')
        shoppingItem.addReview(addSample)
        self.assertEqual(shoppingItem.getReviews()[-1], addSample)

        with self.assertRaises(Exception):
            testReview = shoppingItem.addReview('great review')
        with self.assertRaises(Exception):
            testReview = shoppingItem.addReview(25)
        with self.assertRaises(Exception):
            testReview = shoppingItem.addReview(shoppingItem)

    def test_SetPrice(self):
        reviews = [shopping.BuyerReview(1, 'This sucks-?', 'chris'),
        shopping.BuyerReview(2, 'This is Great.', 'brent_test'),
        shopping.BuyerReview(3, 'This is Great.', 'brent_test')]
        tags = ['computer', 'laptop', 'mac']
        buyers = ['chris', 'brent', 'aaron']
        shoppingItem = shopping.ShoppingItem('name', 5.99, 1, reviews, tags, buyers)

        shoppingItem.setPrice(1.99)
        self.assertEqual(shoppingItem.getPrice(), 1.99)

        with self.assertRaises(Exception):
            testPrice = shoppingItem.setPrice("this one")
        with self.assertRaises(Exception):
            testPrice = shoppingItem.setPrice(-1000.00)
        with self.assertRaises(Exception):
            testPrice = shoppingItem.setPrice("this one")
        
class TestShopperAccount(unittest.TestCase):
    # Test initializon and positive result testing, gave up copy and past for self.asserts
    def test_ShopperAccountInit(self):
        reviews = [shopping.BuyerReview(1, 'This sucks-?', 'chris'),
                   shopping.BuyerReview(2, 'This is Great.', 'brent_test'),
                   shopping.BuyerReview(3, 'This is Great.', 'brent_test')]
        tags = ['computer', 'laptop', 'mac']
        buyers = ['chris', 'brent', 'aaron']
        sampleHistory = [shopping.ShoppingItem('name', 4.99, 5, reviews, tags, buyers,), shopping.ShoppingItem('name', 5.99, 1, reviews, tags, buyers,), shopping.ShoppingItem('name', 5.99, 1, reviews, tags, buyers,)]
        shopperAccount = shopping.ShopperAccount('Chris', sampleHistory)

        self.assertEqual(shopperAccount.getUserId(), 'Chris')
        self.assertEqual(shopperAccount.getOrderHistory(), sampleHistory)

    def test_GetUserId(self):
        reviews = [shopping.BuyerReview(1, 'This sucks-?', 'chris'),
                   shopping.BuyerReview(2, 'This is Great.', 'brent_test'),
                   shopping.BuyerReview(3, 'This is Great.', 'brent_test')]
        tags = ['computer', 'laptop', 'mac']
        buyers = ['chris', 'brent', 'aaron']
        sampleHistory = [shopping.ShoppingItem('name', 4.99, 5, reviews, tags, buyers,), shopping.ShoppingItem('name', 5.99, 1, reviews, tags, buyers,), shopping.ShoppingItem('name', 5.99, 1, reviews, tags, buyers,)]
        shopperAccount = shopping.ShopperAccount('Chris', sampleHistory)
       
        with self.assertRaises(Exception):
            shopperAccount = shopping.ShopperAccount(35, sampleHistory)
        with self.assertRaises(Exception):
            shopperAccount = shopping.ShopperAccount('ggh32[]', sampleHistory)
        with self.assertRaises(Exception):
            shopperAccount = shopping.ShopperAccount('Chr', ['this', 'that'])            
        
    


unittest.main()