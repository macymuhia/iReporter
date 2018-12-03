## Project: iReporter
[![Build Status](https://travis-ci.org/macymuhia/iReporter.svg?branch=develop)](https://travis-ci.org/macymuhia/iReporter)
[![Maintainability](https://api.codeclimate.com/v1/badges/4b9eaf8393acf73e8745/maintainability)](https://codeclimate.com/github/macymuhia/iReporter/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/macymuhia/iReporter/badge.svg?branch=develop)](https://coveralls.io/github/macymuhia/iReporter?branch=develop)


## Technologies used.

* **[Python3](https://docs.python.org/3/)**

* **[Flask](flask.pocoo.org/)**

* **[Flask-RESTful](http://flask-restplus.readthedocs.io/en/stable/)**

## [Pivotal Tacker API Stories](https://www.pivotaltracker.com/n/projects/2226997)

## Current endpoints

* #### Post a redflag.

    `POST /api/v1/redflags`:

    ```

    headers = {content_type:application/json}

    {

        "id": 1,
        "name": "Macy Muhia",
        "status": "new",
        "createdOn": "Friday, November 30 2018 12:07:07",
        "comment": "rejected",
        "location": "122,3344"
    }

    ```

* #### Fetch all redflags.

    `GET /api/v1/redflags`

    ```

    headers = {content_type:application/json}

    ```

* #### Fetch a specific redflag.

    `GET /api/v1/redflags/<red-flag-id>`

    ```

    headers = {content_type:application/json}

    ```


* #### Delete a red flag.

    `DELETE /api/v1/redflags/red-flag-id/`:

    ```

    headers = {content_type:application/json}

    ```

## Installation guide and usage

 #### **Clone the repo.**
  ```
   $ git clone https://github.com/macymuhia/iReporter.git
  ```

 #### **Create virtual environment & Activate.**
  ```
   $ virtualenv -p python3 myenv
   $ source myenv/bin/activate
   ```

 #### **Install Dependancies.**
  ```
    (myenv)$ pip install -r requirements.txt
  ```

#### **Run the app**

   ```
    (myenv)$ python run.py
   ```

#### **Run Tests**

  ```
    (myenv)$ pytest --cov=tests
  ```
