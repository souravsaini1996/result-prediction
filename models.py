from peewee import *
from db import db


class BaseModel(Model):
	class Meta:
		database = db


class User(BaseModel):
	username = CharField(unique=True)
	password = CharField()


class Information(BaseModel):
	name = CharField()
	gender = CharField(default='M', max_length=1)
	age = IntegerField()
	family_members = IntegerField()
	parent_cohabitation_status = CharField(max_length=1, default='t')
	address = CharField(default='U') 
	father_education = IntegerField(default=0)
	mother_education = IntegerField(default=0)
	father_job = CharField()
	mother_job = CharField()
	reason = CharField()
	guardian = CharField()
	travel_time= IntegerField(default=1)
	study_time= IntegerField(default=1)
	failures= IntegerField(default=1)
	schoolsup= BooleanField(default=False)
	famsup = BooleanField(default=True)
	paid = BooleanField(default=False)  # irrelevant?
	activities = BooleanField(default=True)
	nursery= BooleanField(default=True) # irrelevant?
	higher = BooleanField(default=False)
	internet = BooleanField(default=True)
	romantic =BooleanField(default=False)
	famrel= IntegerField(default=1)
	freetime= IntegerField(default=1)
	go_out= IntegerField(default=1)
	dalk= IntegerField(default=1)  #daily alcohol consumption
	walk= IntegerField(default=1)  #weekly alcohol consumption
	health= IntegerField(default=5)
	absences = IntegerField(default=1)
	user = ForeignKeyField(User)


class Grade(BaseModel):
	mst_1 = DecimalField(default=0)
	mst_2 = DecimalField(default=0)
	mst_3 = DecimalField(default=0)
	final = DecimalField(default=0)
	user = ForeignKeyField(User)
	info = ForeignKeyField(Information)