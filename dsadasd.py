import random
import phonenumbers

stringara = '+561348220344'

parser = phonenumbers.parse(stringara)

phonenum = phonenumbers.is_valid_number(parser)

print(phonenum)