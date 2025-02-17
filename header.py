import hashlib
import math
import os
import time 
import datetime
import uuid
import random
class header():
    def __init__(self, prev_hash, curr_root, timestamp, diff_target, nonce):
        self.prev_hash = prev_hash
        self.curr_root = curr_root
        self.timestamp = timestamp
        self.diff_target = diff_target
        self.nonce = nonce
