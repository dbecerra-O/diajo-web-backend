from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv('DATABASE_URL'))

meta = MetaData()

conn = engine.connect()