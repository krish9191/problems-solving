import psycopg2
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
metadata = MetaData()
engine = create_engine('postgresql://postgres:1234@localhost:5432/loginsystem')
# con = psycopg2.connect(
#     host="krishnaPC",
#     database="loginsystem",
#     user="postgres",
#     password="1234"
# )

user = Table('user',metadata,
       Column('user_id',Integer,primary_key=True,nullable=False),
       Column('username',String,unique=True,nullable=False),
       Column('password',String,nullable=False)
    )
metadata.create_all(engine)
# con.close()




