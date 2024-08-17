import random
import string
pass_len=8
char_val=string.ascii_uppercase+string.digits+string.punctuation
password="".join([random.choice(char_val)for i in range(pass_len)])
print("your random password is :",password)