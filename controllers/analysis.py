# coding: utf8

import pandas as pd
import matplotlib
from pandas import DataFrame
from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine('mssql+pyodbc://bitsuser:bits@192.168.0.162/MISServer')
conn = engine.connect()

metadata = MetaData(conn)
table = Table("tMISData", metadata, autoload = True, schema = "dbo")

sql = table.select()

result = conn.execute(sql)

df = DataFrame(data = list(result), columns = result.keys())

def fetch_data():
	data = db(db.tMISData).select()
	return data


def index(): 
	response.title = "Required Dataset"
	data = fetch_data()
	return locals()

def summary():
	data = df
	rows = data.head()
	meanAging = data.Aging.mean()
	meanQty = data.Qty.mean()
	time_taken_per_entity = (data.Qty/data.Aging)[1:50]
	summary = data.describe()
	return locals()

def graphs():
	return locals()