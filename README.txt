Steps to run this project on Linux from zip folder:

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


Steps to run this project from github

1. clone project to your computer 
	git clone <repo> <directory>

2. create virtual environment 
	python3 -m venv myenv
3. Install all requirements
	pip install -r requirements.txt
4. Create new superuser
	python manage.py createsuperuser
5. Run server 
6. Enjoy!

