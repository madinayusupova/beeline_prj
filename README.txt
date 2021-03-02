Steps to run this project on Linux:

1. activate virtual enviroment 
	source env/bin/activate
2. Install all requirements
	pip install -r requirements.txt
3. OPTIONAL: Create new superuser or use existing {login:beeline, password:1} later at admin panel
	python manage.py createsuperuser
4. Run server
	python manage.py runserver
5. Enjoy!

To open admin panel navigate to localhost:{port}/admin
