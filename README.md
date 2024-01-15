# [Django Rest API]
Django API Boiler Plate

<br />
> Features:

- ✅ `Up-to-date Dependencies`

- ✅ `User's registration`

- ✅ `User's SignIn`

- ✅ `User's SignOut`

- ✅ `Basic User Profile Edit`


<br />

## Manual Build
> Download the code
```bash
$ git clone https://github.com/CamCoder337/django-rest-api.git
$ cd django-rest-api
```
<br />

> Setup for 'Unix', 'MacOs' > Install modules via 'env'
```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```
<br />

> Setting up .env files
<br />
Set them up according to your needs (Check the sample) 🙂

<br />

> Set Up Database
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
<br />

> Set Up Frontend Server
```
Go in core/settings.py
Update the following line with  your frontend Server address:
```
```python
CORS_ALLOWED_ORIGINS = ["Your_Frontend_Address"]
```

> Example
```python
CORS_ALLOWED_ORIGINS = ["http://localhost:3000",]
```

> Start the API Server
```bash
$ python manage.py runserver 5000     # start api
```

Use the API  at `localhost:5000` via:
<br />
#### [POSTMAN](https://www.postman.com/grey-star-293238/workspace/django-rest-api/overview) or `Swagger Dashboard`

<br />

### [Django Rest API] - provided **[Camcoder337](https://github.com/CamCoder337/)**.
