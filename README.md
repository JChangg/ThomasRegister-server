    _____________________              .__          __                
    \__    ___/\______   \ ____   ____ |__| _______/  |_  ___________ 
      |    |    |       _// __ \ / ___\|  |/  ___/\   __\/ __ \_  __ \
      |    |    |    |   \  ___// /_/  >  |\___ \  |  | \  ___/|  | \/
      |____|    |____|_  /\___  >___  /|__/____  > |__|  \___  >__|   
                       \/     \/_____/         \/            \/       

**Warning**: This server is a prototype.
## Description
The TRegister server is a python server, it uses postgresql backend with Django.

## Installation
### Python 2.7
Figure it out! (make sure python is added to path, google that!)
### Postgresql
1. Download EnterpriseDB from the postgresql website https://www.postgresql.org/download/windows/. 
2. Open Pygadmin:
    1. Set up user TREG_SERVER with password making sure it has the highest privileges.
    2. Set up new database TREG with user as TREG_SERVER.
### Git
1. Download git bash https://git-for-windows.github.io/
2. In the desired directory right click, click on git-bash. 
3. In the git bash terminal type the following:
```
    $ git clone https://github.com/JChangg/ThomasRegister-server.git
    # Enter user name + password for github if prompted
    $ git checkout b_production
    $ git pull
```

### Install requirements
In the same bash terminal type the following: 

```
$ pip install -r requirements.txt
```
### Test the server
    $ python manage.py test

### Possible step
If you see an error mentioning psycopg2 then you also need to install it from http://www.stickpeople.com/projects/python/win-psycopg/

Be sure to select the correct version for python 2.7 and your machine (x86/x64). 

### Starting from the Terminal
If all goes well then we have ourselves a working server run it by: 

    $ python manage.py runserver 0.0.0.0:8000
    
