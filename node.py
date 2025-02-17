import hashlib
import math
import os
import time 
import datetime
import uuid
import random
class node:
    def __init__(self, address, balance, hash_val):
        self.left = None
        self.right = None
        self.hash = hash_val
        self.address = address
        self.balance = balance