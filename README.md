### One Minute Pitch Application

## By Agnes K0inange 

## Description 
In life, you only have 60 seconds to impress someone. 1 minute can make or break you. How do you make sure that you use your 1 minute to actually say something meaningful? This Python Flask application allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them. The pitches are organized by category- pickup lines, interview pitch, product pitch, promotion pitch among others.

## User Stories

* As a user, I would like to see the pitches other people have posted.
* As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.
* As a user, I would like to be signed in for me to leave a comment
* As a user, I would like to receive a welcoming email once I sign up.
* As a user, I would like to view the pitches I have created in my profile page.
* As a user, I would like to comment on the different pitches and leave feedback.
* As a user, I would like to submit a pitch in any category.
* As a user, I would like to view the different categories.

## Features
* Built with Python 3.6, Flask microframework
* Shows Posted Pitches, Upvotes & Downvotes, Uer comments and categories.
* Styled using Bootstrap
* Uses Flask WTForms and various validators to arrest CRSF attacks.
* Uses Flask Login extension for authentication management
* Post pitches based on categories (Choose from various pitch categories)
* Uses PostgreSQL DB, SQLAlchemy ORM and Flask Migrate

## SetUp / Installation Requirements

Clone this repo and cd into the folder
$ git clone  https://github.com/Agneskoinange/1-Minute_Pitch.git

$ source virtual/bin/activate

(virtual)$ pip install -r requirements.txt

(virtual)$ python3 run.py server
To run unit tests; (virtual)$ python3 run.py test

***Installation Requirements
* python3.9
* pip
* virtualenv

# Testing the Application

To run the tests for the class files:

$ python3.9 manage.py tests

## Support and contact details

If you have any questions, concerns or comments regarding this project, please contact me through koinangeagnes@gmail.com


# License

MIT License

Copyright (c) 2022 Agnes Koinange

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.