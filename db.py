from peewee import MySQLDatabase

db = MySQLDatabase(
	'predictions',
	host='localhost',
	port=3306,
	user='root',
	password='sourav'	
)