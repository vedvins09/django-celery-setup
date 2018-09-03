# django-celery-setup
Celery setup for Django Project for Periodic Task and Normal Task


# Quadrant Candidate Micro Service


### Prerequisite:

    * Python 3.5.2
    * PostgreSQL (9.5+)
    * python-pip

### System Setup:

1. Installing Required tools :

     * Install database
         - Ubuntu:-
            * Client:- sudo apt-get install -y postgresql-9.5 postgresql-contrib-9.5
            * Server:-  sudo apt-get install -y postgresql-doc-9.5 postgresql-server-dev-9.5

         - OSX:- brew install postgresql@9.5

2. Environment setup:

    * Install pip and virtualenv:
        - sudo apt-get install python3-pip
        - pip install --upgrade pip
        - sudo pip3 install virtualenv or sudo pip install virtualenv

    * Create virtual environment:
        - virtualenv env

        OPTIONAL:- In case finding difficulty in creating virtual environment by
                  above command , you can use the following commands too.

            *   Create virtualenv using Python3:-
                    - virtualenv -p python3 env
            *   Instead of using virtualenv you can use this command in Python3 for creating virtual environment:-
                    - python3 -m venv env

    * Activate environment:
        - source env/bin/activate

    * Clone project:
        - git clone https://github.com/vinodkiwi/django-celery-setup.git

    * Checkout to branch
	    - cd "project-name"
        - git checkout "branch_name"

    * Install the requirements by using command:
        - pip3 install -r requirements.txt or pip install -r requirements.txt

3. Database Setup

     * Create database with proper permissions to the db-user:
         * create user user_name;
         * \password user_name;
         * create database db_name;
         * grant all privileges on database db_name to user_name;

     * Add following information in .env file,to get the actual values, please contact to project owner.

          - DB_NAME="******"
          - DB_USERNAME="******"
          - DB_PASSWORD="******!"
          - DB_HOST="******"
          - DB_PORT=******
          - DEBUG=******
          - SECRET_KEY="******"
          - SETTINGS="******"
          - AWS_ACCESS_KEY_ID = "**********"
          - AWS_SECRET_ACCESS_KEY = "**********"
          - AWS_STORAGE_BUCKET_NAME = "*********"
          - LOGENTRIES_TOKEN = "******************"

     * DB migrations:
         * python manage.py migrate
         

4. Run servers:

     * python manage.py runserver

# run celery and celery beat for periodic task

# Celery terminal cmd

Open another terminal and run one of the below command

    1 - celery -A project_name worker -l info

# Celery beat terminal cmd

Open another new terminal for beat scheduling and run one of the below command.

    1 - celery -A project_name beat
    or
    2- celery -A project_name worker -B
    or
    3- celery -A project_name beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
   
