

import time 

from boto.s3.key import Key

from boto.s3.connection import S3Connection

conn = S3Connection('AKIAJZJFK55M7GYXHAVQ', 'qEuX5hu6jStWqHw4HZWtiC8U+0JQGt35Xd9v0luN')

bucket = conn.create_bucket('mumbai234')

k = Key(bucket)

k.key = 'concomf.csv'

start = time.time()

k.set_contents_from_filename('concomf.csv')

end=time.time()

print "Time taken for uploading file to AWS s3 is : "+str(end-start)

start = time.time()

k.get_contents_to_filename('bar.csv')

end = time.time()

print " Time taken for downloading  file from AWS s3 is "+str(end - start)

conn.close()
