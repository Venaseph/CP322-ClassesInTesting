# !/usr/bin/env python
import sys


class BuyerReview():
    # Class Vars
    rating = None # An integer for # of starts (valued values are 1-5)
    review = None # A string with the review describing the buyer's experience.
    userId = None # User ID of user that is reviewing the item
    # Initializer/Constructor
    def __init__(self, rating, review, userId):
        self.rating = rating
        self.review = review
        self.userId = userId
    # Accessors for Class Vars
    def getRating(self):
        return self.rating 
        # get the rating in # of stars provided as part of this review
        # args  = None return 1-5

    def getReview(self):
        return self.review
        # getReview:  get text describing buyer's experience
        # arguments:  none
        # returns:  string that describes buyer's experience

    def getUserid(self):
        return self.userId
        # getUserId:  get the userId of the user that made this review
        # arguments:  none
        # returns:  string that is the user Id




class ShoppingItem():
    # Class Variables
    price = None # price of the item (float value)
    sold = None # number of items sold
    reviews = None # # list of BuyerReview objects, which are reviews for this item
    tags = None # list of keywords that are used to find this object when searching
    buyers = None # list of user ID's of buyers that have purchased this item
    # Initializer/Constructor
    def __init__(self, price,sold, reviews, tags, buyers):
        self.price = price 
        self.sold = sold 
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

    def geAverageRating(self):
        pass
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

    def addPurchase(self):
        pass
        # add a purchase of this item from a buyer
        # arguments: 
        # userId:  user ID of buyer that purchased the item

    def addReview(self):
        pass
        # add a review of this item
        # arguments:
        # review:  a BuyerReview object 
        # returns:  N/A

    def setPrice(self):
        pass


class ShopperAccount(self):
    # Class Variables
    userId = None
    orderHistory = None
    addPurchase = None
    # Initializer/Constructor
    def __init__(self, ):
        pass

    # Accessors for Class Vars
    def getPrice(self):
        return self.price


def main():
    pass

if __name__ == "__main__":
    sys.exit(main())