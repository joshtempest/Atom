import hashlib
import os

users = {}

username = input('username ')
password = input('password ')

salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {'salt':salt,'key':key}

username = 'jish'
password = 'biss'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
