'''
Created on 7 de març 2023

@author: nbuisac
'''
import os
import pprint

print(os.environ["PATH"])
print(os.environ["MongoDBConnection"])
print(os.environ.get("MongoDBUsername"))
# pprint.pprint(dict(os.environ), width = 1)