import hashlib
import math
import os
import time 
import datetime
import uuid
import random
from node import node
from tree import tree
from header import header
from block import block

#actually creates the blockchain
blockchain = []
def create_Blockchain():
    counter = 0
    output_name = "null"
    prev_header = hex(0)
    current_path = os.getcwd()
    directory = os.scandir(current_path)
    nonce = 0
    for file in directory:
        if (file.name.endswith(".block.txt")):
            os.remove(current_path + "/" + file.name)
    current_path = os.getcwd()
    directory = os.scandir(current_path)
    for file in directory:
        if(file.name.endswith(".txt")):
            if (counter == 0):
                output_name = os.path.splitext(file.name)[0] + ".block.txt"
                f = open(output_name, "x")
                f = output_name
                counter = 1
            else: 
                f = output_name
            file_path = current_path + "/" + file.name
            with open(file_path, 'r') as test_data:
                leaves = []
                address_list = []
                for line in test_data:
                    line = str(line)
                    address_list.append(line)
                    split_line = line.split()
                    address = split_line[0]
                    balance = split_line[1]
                    address_hash = hashlib.sha256(address.encode('utf-8')).hexdigest()
                    balance_hash = hashlib.sha256(balance.encode('utf-8')).hexdigest()
                    cat_hash = address_hash+balance_hash
                    cat_hash = hashlib.sha256(cat_hash.encode('utf-8')).hexdigest()
                    x = node(address, balance, cat_hash)
                    leaves.append(x)
                merkle = tree()
                merkle.build_tree(leaves)
                
                presentDate = datetime.datetime.now()
                unix_timestamp = int(datetime.datetime.timestamp(presentDate))
                diff_target = hex(int(math.pow(2,255)))
                diff_target = hashlib.sha256(diff_target.encode('utf-8')).hexdigest()
                nonce = uuid.uuid4()
                nonce_hash = str(nonce) + merkle.root
                nonce_hash = hashlib.sha256(nonce_hash.encode('utf-8')).hexdigest()

                while nonce_hash > diff_target:
                    nonce = str(uuid.uuid4())
                    nonce_hash = str(nonce) + merkle.root
                    nonce_hash = hashlib.sha256(nonce_hash.encode('utf-8')).hexdigest()

                head = header(prev_header, merkle.root, unix_timestamp, diff_target, nonce)
                head_hash = head.prev_hash + head.curr_root + str(hex(head.timestamp)) + head.diff_target + str(head.nonce)
                prev_header = hashlib.sha256(head_hash.encode('utf-8')).hexdigest()
                b = block(head, address_list)
                b.block_output(True, f)
                blockchain.append(b)
                
# prompt for validate block, validate chain, proof of membership, proof of non-membership, and balance
def prompt_User():
    print_out = input("Would you like to print out the blockchain? (y/n)")
    if print_out == ("y"):
        current_path = os.getcwd()
        directory = os.scandir(current_path)
        for file in directory:
            if (file.name.endswith(".block.txt")):
                file_path = current_path + "/" + file.name
                with open(file_path, 'r') as test_data:
                    for line in test_data:
                        print(line)
    answer = input("Please indicate what you want to do: Validate a block (1), proof of membership (2)")
    if (answer == '1'):
        file_name = input("pleas provide the file name of the block you want to validate:")
        current_path = os.getcwd()
        directory = os.scandir(current_path)
        for file in directory: 
            if (file.name == (file_name)):
                file_path = current_path + "/" + file_name
                with open(file_path, 'r') as test_data:
                    address_ledger = []
                    for line in test_data:
                        address_ledger.append(line)
        if validate_block(address_ledger):
            print("block validated")
        else:
            print("block invalidated")

    elif (answer == '2'):
        account_name = input("what is the name for your account?")
        if proof_of_memebrship(account_name) == False:
            print("membership not found")
        else:
            print(proof_of_membership)



def hash_lines(hash_val1, hash_val2):
            val1 = hash_val1.hash 
            val2 = hash_val2.hash 
            cat_hash = val1 + val2
            hashF = hashlib.sha256(cat_hash.encode('utf-8')).hexdigest()
            return hashF




#take in a block and get the merkle root. Then go through the entire chain and see if there is a merkle root that matches
def validate_block(ledger):
    leaves = []
    i = 0
    merkle = tree()
    while i < len(ledger):
        line = ledger[i]
        split_line = line.split()
        address = split_line[0]
        balance = split_line[1]
        address_hash = hashlib.sha256(address.encode('utf-8')).hexdigest()
        balance_hash = hashlib.sha256(balance.encode('utf-8')).hexdigest()
        cat_hash = address_hash+balance_hash
        cat_hash = hashlib.sha256(cat_hash.encode('utf-8')).hexdigest()
        x = node(address, balance, cat_hash)
        leaves.append(x)
        i += 1
    merkle.build_tree(leaves)
    i = 0
    while i != len(blockchain):
        if blockchain[i].header.curr_root == merkle.root:
            return (True)
        i += 1
    return (False)


def proof_of_membership(account_name):
    i = 0
    level = 1
    return_list = []
    ledger = []
    while i != len(blockchain):
        ledger = blockchain[i].ledg_address
        for x in ledger:
            address1 = ledger[x]
            line = address1.split()
            address = line[0]
            if address == account_name:
                return_list.append(account_name)
                if x%2 == 0:
                    address2 = ledger[x+1]
                    line = address2.split()
                    address = line[0]
                    return_list.append(address)
                elif x%2 != 0:
                    address2 = ledger[x-1]
                    line = address2.split()
                    address = line[0]
                    return_list.append(address)

create_Blockchain()
prompt_User()