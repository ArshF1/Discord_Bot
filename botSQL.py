import pymysql
import pandas as pd

conn=pymysql.connect(host="localhost",user="root",password="root1234",database="discord",port=3306)
sql="select * from userData"

cmd=
df=pd.read_sql(con=conn,sql=sql)