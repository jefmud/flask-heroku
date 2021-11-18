# Flask-Heroku

My first flask app on Heroku

Demonstrates the use of templates and static assets

notes:

You can run it on the command line by first changing into the top-level directory and running the app.

`$ python run.py`

You can also run the app with waitress (on the PC), set the threads to 8 to avoid a warning

`$ pip install waitress`

`$ waitress-serve --threads=8 flaskapp.main:app`
