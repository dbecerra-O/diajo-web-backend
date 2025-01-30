from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/diajosac")

meta = MetaData()

conn = engine.connect()