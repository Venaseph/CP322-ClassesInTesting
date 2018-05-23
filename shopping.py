# !/usr/bin/env python
import sys
import re
import decimal


class BuyerReview():

    # Initializer/Constructor
    def __init__(self, rating, review, userId):
        # If not a int from 1-5
        if rating < 1 or rating > 5:
            raise Exception('Rating must be an int(1-5)')
        self.rating = rating

        if not re.fullmatch('[\w .?!\-]+', review):
            raise Exception('Review can be alphanumeric, spaces or punctuation')
        self.review = review

        if not re.fullmatch('[\w]+', userId):
            raise Exception('userId (userId can be alphanumeric and underscores')
        self.userId = userId


    # Accessors for Instance Vars
    def getRating(self):
        return self.rating

    def getReview(self):
        return self.review

    def getUserid(self):
        return self.userId


class ShoppingItem():
    # Initializer/Constructor
    def __init__(self, price, sold, reviews, tags, buyers):
        # Number: Currency amount (cents optional) Optional thousands separators; optional two-digit fraction
        if not re.fullmatch('^[+]?[0-9]{1,3}(?:,?[0-9]{3})*(?:.[0-9]{2})?$', str('%.2f' % price)):
            raise Exception('Price match a valid USD currency')
        self.price = price
        # int on 0 or higher
        if not re.fullmatch('^[0-9]*$', str(sold)):
            raise Exception('Must be a positive integer')
        self.sold = sold
        # 
        self.reviews = reviews
        self.tags = tags
        self.buyers = buyers

    # Accessors for Class Vars
    def getPrice(self):
        return self.price
        # getPrice:  get the current price of the item
        # arguments:  none
        # returns:  price of the item (float value)

    def getNumberSold(self):
        return self.sold
        # getNumberSold:  get number of this item sold
        # arguments:  none
        # returns:  integer number sold

    def getAverageRating(self):
        return 0
        # getAverageRating:  get the average star rating of this item
        # arguments:  none
        # returns:  average star rating (float value)

    def getReviews(self):
        return self.reviews
        # get list of reviews for this product
        # arguments:  none
        # returns:  a list of BuyerReview objects

    def getTags(self):
        return self.tags
        # get list of all tags that can be used to find this item in a search
        # arguments:  none
        # returns:  list of strings that are tags

    def getBuyers(self):
        return self.buyers
        # get list of buyers that have purchased this item
        # arguments:  none
        # returns:  list of user ID's of buyers that purchased this item

#     def addPurchase(self):
#         pass
#         # add a purchase of this item from a buyer
#         # arguments: 
#         # userId:  user ID of buyer that purchased the item

#     def addReview(self):
#         pass
#         # add a review of this item
#         # arguments:
#         # review:  a BuyerReview object 
#         # returns:  N/A

#     def setPrice(self):
#         pass


# class ShopperAccount():
#     # Class Variables
#     userId = None
#     orderHistory = None
#     addPurchase = None
#     # Initializer/Constructor
#     def __init__(self, ):
#         pass

#     # Accessors for Class Vars
#     def getPrice(self):
#         return self.price


def main():
    return 0

if __name__ == "__main__":
    sys.exit(main())