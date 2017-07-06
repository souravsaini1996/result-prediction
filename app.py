from flask import (
	Flask, render_template, 
	request, url_for, redirect, session
	)
from db import db
from models import User, Information, Grade


#App created
app = Flask(__name__)


@app.before_request
def before_request():
	db.connect()


@app.teardown_request
def teardown_request(response):
	db.close()
	return response


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
	#POST method
	if request.method =='POST':
		username=request.form['username']
		password=request.form['password']
		user = User.get(User.username == username & User.password == password)
		if user:
			session['username']=username
			session['id']=user.id
			return redirect(url_for('attr_form'))
		else:
			return redirect(url_for('login'))
	#GET method		
	return render_template('login.html')


@app.route('/register', methods=['GET','POST'])
def register():
	#POST method
	if request.method =='POST':
		username=request.form['username']
		password=request.form['password']
		User.create(username = username, password = password)	
		#print(username, password)
		return redirect(url_for('login'))
	#GET method
	return render_template('register.html')	


@app.route('/attr_form', methods=['GET','POST'])
def attr_form():
	#POST method
	# if request.method == 'POST':
		# name = request.form['name'].upper()

		# gender = document.querySelector('input[name="gender"]:checked').value;
		# if gender == 'Male':
		# 	gender='M'
		# else:
		# 	gender='F'

		# age = request.form['age']

		# address = document.querySelector('input[name="area"]:checked').value;
		# if address == 'URBAN':
		# 	address='U'
		# else:
		# 	address='R'

		# family_members = request.form['fmembers']
		
		# parent_cohabitation_status = document.querySelector('#cohabitation:checked').value;	
		# if parent_cohabitation_status == 'Together':
		# 	parent_cohabitation_status='T'
		# else:
		# 	parent_cohabitation_status='A'

		# father_education = document.querySelector('#father_edu:checked').value;
		# if father_education == 'None':
		# 	father_education=0;
		# elif father_education == 'Primary':
		# 	father_education=1;
		# elif father_education == 'Matriculation':
		# 	father_education=2;
		# elif father_education == 'Secondary':
		# 	father_education=3;
		# else:
		# 	father_education=4;			

		# mother_education = document.querySelector('#mother_edu:checked').value;
		# if mother_education == 'None':
		# 	mother_education=0;
		# elif mother_education == 'Primary':
		# 	mother_education=1;
		# elif mother_education == 'Matriculation':
		# 	mother_education=2;
		# elif mother_education == 'Secondary':
		# 	mother_education=3;
		# else:
		# 	mother_education=4;
	if request.method == 'POST':
		gender = request.form['father_edu']
		return render_template('form.html', gender=gender)


	#GET method
	return render_template('form.html')	


@app.route('/logout')
def logout():
	session.pop('username')
	session.pop('id')
	return redirect(url_for('login'))

if __name__ == '__main__':
	db.create_tables([User, Information, Grade], safe=True)
	app.secret_key = 'DG33KLLKN4525KLNKrwr23;24423*78'
	app.run(debug=True, port=5000)	