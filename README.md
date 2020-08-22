# TIMETABLE REMINDERS #
```
Not complete, updating...
```

### Development Installation ###
- Install python package
```
python3 -m venv env
source env/bin/activate
cd apps
pip install -r requirements.txt
```
- Install new package
```
pip install <package_name>
```
- Export python package
```
pip freeze > requirements.txt
```
- Create migrations files
```
python manage.py makemigrations <module_name>
```
- Migrate database
```
python manage.py migrate
```
- Start project
```
python manage.py runserver <port>
```
