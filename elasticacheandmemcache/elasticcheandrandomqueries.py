import time
import MySQLdb

import time

import urllib3

import csv

import memcache

import shutil , sys

start=time.time()

# Connection to rds instance using MySQLdb library

#Creating a connection object to rds instance

db=MySQLdb.connect("rasika.coy3hddcliiz.us-west-2.rds.amazonaws.com","root","rootroot","quakedb",local_infile=1)

cursor=db.cursor()

sql = """CREATE TABLE tab3 (

         
         C_id INT NOT NULL,

         product VARCHAR(50),
         

         subproduct  VARCHAR(40),
         

         issue VARCHAR(20) ,

         subissue  VARCHAR(3),

         State  VARCHAR(20),
         

         Zip_code  INT,
         

         submitted  VARCHAR(20),
         

         Date_received  DATE,
         

         Date_sent  DATE,
         

         Company  VARCHAR(40),
         

         Company_response VARCHAR(50),
         

         Timely_response VARCHAR(4),
         

         Consumer_disputed VARCHAR(4),

         PRIMARY KEY(C_id))"""

cursor.execute(sql)



data =cursor.fetchone()

print data

my_url_load='https://s3.amazonaws.com/mumbai234/concomf.csv' 

c = urllib3.PoolManager()


with c.request('GET',my_url_load, preload_content=False) as resp, open('file_to_rds.csv', 'wb') as out_file:
    shutil.copyfileobj(resp, out_file)
resp.release_conn()


sql="""load data local infile 'file_to_rds.csv'

        into table tab3

        fields terminated by ','

        enclosed by '"'

        lines terminated by '\n'"""

cursor.execute(sql)

cursor.execute("commit")

end=time.time()

print "Time taken for uploading the data to rds is : "

print str(end-start)

# code for executing 1000 random queries and identifying time required for the operation

start=time.time()

query="""select DISTINCT product from tab3 ORDER BY rand() LIMIT 10"""

for i in range(1,1000):

        cursor.execute(query)

end=time.time()

print "Time taken for 1000 queries without using memcache is :"+str(end-start)

# code for executing 5000 random queries and identifying time required for the operation

start=time.time()

query="""select DISTINCT product from tab3 ORDER BY rand() LIMIT 10"""

for i in range(1,5000):

        cursor.execute(query)

end=time.time()

print "Time taken for 5000 queries without using memcache is :"+str(end-start)

# code for executing 20000 random queries and identifying time required for the operation

start=time.time()

query="""select DISTINCT product from tab3 ORDER BY rand() LIMIT 10"""

for i in range(1,20000):

        cursor.execute(query)

end=time.time()

print "Time taken for 20000 queries without using memcache is :"+str(end-start)

# code for executing 1000 random queries and identifying time required for the operation extended limit

start=time.time()

query="""select DISTINCT product from tab3 ORDER BY rand() LIMIT 300"""

for i in range(1,1000):

        cursor.execute(query)

end=time.time()

print "Time taken for 1000 queries without using memcache and extended limit is :"+str(end-start)

# code for executing 5000 random queries and identifying time required for the operation extended limit

start=time.time()

query="""select DISTINCT product from tab3 ORDER BY rand() LIMIT 300"""

for i in range(1,5000):

        cursor.execute(query)

end=time.time()

print "Time taken for 5000 queries without using memcache and extended limit is :"+str(end-start)

# code for executing 20000 random queries and identifying time required for the operation extended limit

start=time.time()

query="""select DISTINCT product from tab3 ORDER BY rand() LIMIT 300"""

for i in range(1,20000):

        cursor.execute(query)

end=time.time()

print "Time taken for 20000 queries without using memcache is :"+str(end-start)


#creating memcache object for loading data into memcache using "Elastic" cache library

memc = memcache.Client(['radha.kxhwlb.cfg.usw2.cache.amazonaws.com'], debug=1)

#code for executing 1000 random queries and identifying time required using memcache

start=time.time()
x=0
for i in range(1,1000):

        random_query=memc.get('random_queries_memcache')

        if not random_query:

                query="""SELECT DISTINCT product from tab3 ORDER BY rand() LIMIT 10"""

                for i in range(1,1000):

                        cursor.execute(query)

                rows=cursor.fetchall()

                memc.set('random_queries_memcache',rows,600)
		print "updated memcached with MySQL data"
	else:
                if(x==0):

                        print "Loaded data from memcached"

                        x=1

end=time.time()

print "Time required for 1000 queries using memcache is :"+str(end-start)

#creating memcache object for loading data into memcache using "Elastic" cache library

memc = memcache.Client(['radha.kxhwlb.cfg.usw2.cache.amazonaws.com'], debug=1)

#code for executing 5000 random queries and identifying time required using memcache

start=time.time()
x=0
for i in range(1,5000):

        random_query=memc.get('random_queries_memcache')

        if not random_query:

                query="""SELECT DISTINCT product from tab3 ORDER BY rand() LIMIT 10"""

                for i in range(1,5000):

                        cursor.execute(query)

                rows=cursor.fetchall()

                memc.set('random_queries_memcache',rows,600)

		print "updated memcached with MySQL data"
        else:

                if(x==0):

                        print "Loaded data from memcached"

                        x=1

end=time.time()

print "Time required for 5000 queries using memcache is :"+str(end-start)

#creating memcache object for loading data into memcache using "Elastic" cache library

memc = memcache.Client(['radha.kxhwlb.cfg.usw2.cache.amazonaws.com'], debug=1)

#code for executing 20000 random queries and identifying time required using memcache

start=time.time()
x=0
for i in range(1,20000):

        random_query=memc.get('random_queries_memcache')

        if not random_query:

                query="""SELECT DISTINCT product from tab3 ORDER BY rand() LIMIT 10"""

                for i in range(1,20000):

                        cursor.execute(query)

                rows=cursor.fetchall()

                memc.set('random_queries_memcache',rows,600)

		print "updated memcached with MySQL data"
        else:

                if(x==0):

                    print "Loaded data from memcached"

                    x=1

end=time.time()

print "Time required for 1000 queries using memcache is :"+str(end-start)
#creating memcache object for loading data into memcache using "Elastic" cache library

memc = memcache.Client(['radha.kxhwlb.cfg.usw2.cache.amazonaws.com'], debug=1)

#code for executing 1000 random queries and identifying time required using memcache extened limit

start=time.time()
x=0
for i in range(1,1000):

        random_query=memc.get('random_queries_memcache')

        if not random_query:

                query="""SELECT DISTINCT product from tab3 ORDER BY rand() LIMIT 300"""

                for i in range(1,1000):

                        cursor.execute(query)

                rows=cursor.fetchall()

                memc.set('random_queries_memcache',rows,600)

		print "updated memcached with MySQL data"
        else:

                if(x==0):

                    print "Loaded data from memcached"

                    x=1

end=time.time()

print "Time required for 1000 queries using memcache and extended limit is :"+str(end-start)

#creating memcache object for loading data into memcache using "Elastic" cache library

memc = memcache.Client(['radha.kxhwlb.cfg.usw2.cache.amazonaws.com'], debug=1)

#code for executing 5000 random queries and identifying time required using memcache

start=time.time()
x=0
for i in range(1,5000):

        random_query=memc.get('random_queries_memcache')

        if not random_query:

                query="""SELECT DISTINCT product from tab3 ORDER BY rand() LIMIT 300"""

                for i in range(1,5000):

                        cursor.execute(query)

                rows=cursor.fetchall()

                memc.set('random_queries_memcache',rows,600)

		print "updated memcached with MySQL data"
        else:

                if(x==0):

                    print "Loaded data from memcached"

                    x=1

end=time.time()

print "Time required for 5000 queries using memcache and extended limit is :"+str(end-start)

#creating memcache object for loading data into memcache using "Elastic" cache library

memc = memcache.Client(['radha.kxhwlb.cfg.usw2.cache.amazonaws.com'], debug=1)

#code for executing 20000 random queries and identifying time required using memcache

start=time.time()

x=0
for i in range(1,20000):

        random_query=memc.get('random_queries_memcache')

        if not random_query:

                query="""SELECT DISTINCT product from tab3 ORDER BY rand() LIMIT 300"""

                for i in range(1,20000):

                        cursor.execute(query)

                rows=cursor.fetchall()

                memc.set('random_queries_memcache',rows,600)
		print "updated memcached with MySQL data"

	
        else:

                if(x==0):

                    print "Loaded data from memcached"

                    x=1

end=time.time()

print "Time required for 20000 queries using memcache and extended limit is :"+str(end-start)

db.close()
