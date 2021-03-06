# !/usr/bin/env python
import sys
import re
import decimal
import sqlite3
import os

class ShoppingFactory():
    def __init__(self, dbpath):
        # If not ints
        if not os.path.exists(dbpath):
            raise Exception("Bad DB path")

        self.dbconn = sqlite3.connect(dbpath)
        self.pageSize = 25
        #make cursor
        self.cursor = self.dbconn.cursor()
        self.cursor.execute('SELECT * FROM items')

    def setPageSize(self, size):
        if size <= 0 or size > 100:
            raise Exception("Invalid Page Size")
        self.pageSize = size


    def getPageSize(self):
        return self.pageSize


    def getNextPage(self):
        # Cursor set in init to retain position
        # Fetch many returns a list of tuples
        data = self.cursor.fetchmany(self.pageSize)
        items = []
        for d in data:
            tags = str(d[4]).split(',')
            reviews = self.constructReviews(d[0])
            items.append(ShoppingItem(d[1], d[2], d[3], reviews, tags, []))

        return items


    def constructReviews(self, itemId):
        # make new cursor just for reviews
        rc = self.dbconn.cursor()
        rc.execute('SELECT * FROM reviews WHERE item_id is %d' % itemId)
        data = rc.fetchall()
        print(data)
        reviews = []
        for d in data:
            reviews.append(BuyerReview(d[1], str(d[2]), str(d[3])))
        return reviews


    def sortMostSold(self):
        self.cursor.execute('SELECT * FROM items ORDER BY sold DESC')


    def sortLowestPrice(self):
        self.cursor.execute('SELECT * FROM items ORDER BY price')


    def setSearchFilter(self, tags):
        query = 'SELECT * FROM items WHERE'
        addtoQuery = ''     
        for tag in tags:
            if addtoQuery:
                addtoQuery += ' OR'
            addtoQuery += ' tags LIKE "%' + tag + '%"'
        # executre query    
        query += addtoQuery
        self.cursor.execute(query)


class BuyerReview():
    # Initializer/Constructor
    def __init__(self, rating, review, userId):
        # If not a int from 1-5
        if rating < 1 or rating > 5 or not isinstance(rating, int):
            raise Exception('Rating must be an int(1-5)')
        self.rating = rating
        # If not a normal sentance with punct/dash
        if not re.fullmatch(r'[\w .?!\-]+', review):
            raise Exception('Review can be alphanumeric, spaces or punctuation')
        self.review = review
        #If not a alpanumeric with underscores
        if not re.fullmatch(r'[\w]+', userId):
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
    def __init__(self, name, price, sold, reviews, tags, buyers):
        # Regex for name formatting
        if not re.fullmatch('^[a-zA-Z ]+$', name):
            raise Exception('Name Formatting')
        self.name = name
        # Number: Currency amount (cents optional) Optional thousands separators; optional two-digit fraction
        if not re.fullmatch(r'^[+]?[\d]{1,3}(?:,?[\d]{3})*(?:.[\d]{2})?$', str('%.2f' % price)):
            raise Exception('Price match a valid USD currency')
        self.price = price
        # int on 0 or higher
        if not re.fullmatch('^[0-9]*$', str(sold)):
            raise Exception('Must be a positive integer')
        self.sold = sold
        # Allow 
        self.reviews = reviews
        self.tags = tags
        self.buyers = buyers


    # Accessors for Class Vars
    def getName(self):
        return self.name

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
        tally = 0         
        for review in self.reviews:
            tally += review.getRating()
        return tally / len(self.reviews)

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

    def addPurchase(self, userId):
        # Check that it matches userId formatting
        if not re.fullmatch(r'[\w]+', userId):
            raise Exception('Name Formatting')
        self.buyers.append(userId)
        self.sold += 1
        # add a purchase of this item from a buyer
        # arguments:
        # userId:  user ID of buyer that purchased the item

    def addReview(self, review):
        # Check if it's a buyreview object
        if not isinstance(review, BuyerReview):
            raise Exception('Can only append buyer review objects')
        self.reviews.append(review)
        # add a review of this item
        # arguments:
        # review:  a BuyerReview object
        # returns:  N/A

    def setPrice(self, price):
        if not re.fullmatch(r'^[+]?[\d]{1,3}(?:,?[\d]{3})*(?:.[\d]{2})?$', str('%.2f' % price)):
            raise Exception('Price match a valid USD currency')
        self.price = price


class ShopperAccount():
    # Initializer/Constructor
    def __init__(self, userId, orderHistory):
        # If not a alpanumeric with underscores
        if not re.fullmatch(r'[\w]+', userId):
            raise Exception('userId (userId can be alphanumeric and underscores')
        self.userId = userId
        
        # try:
        #     [isinstance(order, ShoppingItem) for order in orderHistory]
        # except:
        #     "Orders must be ShoppingItems"

        for order in orderHistory:
            if not isinstance(order, ShoppingItem):
                raise Exception('IOrders must be ShoppingItems')
        self.orderHistory = orderHistory

    # Accessors for Class Vars
    def getUserId(self):
        return self.userId

    def getOrderHistory(self):
        return self.orderHistory

    def addPurchase(self, purchase):
        if not isinstance(purchase, ShoppingItem):
            raise Exception('Orders must be ShoppingItems')
        self.orderHistory.append(purchase)
        


def main():
    return 0


if __name__ == "__main__":
    sys.exit(main())