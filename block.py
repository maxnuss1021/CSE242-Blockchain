import hashlib
import math
import os
import time 
import datetime
import uuid
import random
from header import header
class block():
    def __init__(self,header, ledg_address):
        self.header = header
        self.ledg_address = ledg_address

    def block_output(self,input, print_file):
        f = open(print_file, "r")
        original = f.read()
        f = open(print_file, "w")
        if input == True:
            f.write( "\n " + "BEGIN BLOCK\n BEGIN HEADER\n" + 
                self.header.prev_hash + "\n" + self.header.curr_root + "\n" + str(int(self.header.timestamp)) + "\n" 
                + self.header.diff_target + "\n" + str(self.header.nonce) + "\n END HEADER \n" + str(self.ledg_address) + 
                "\n END BLOCK\n\n" + original)
        