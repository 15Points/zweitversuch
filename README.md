<<<<<<< HEAD
# fswd-examples

Full-stack web development: code examples as additional resource to notebooks.

First, fork this repository.

> **Important**: make sure to **uncheck** the option *"copy the `main` branch only"*.

Then select a particular branch and `pull` the resources from that branch to get access to code examples:

+ [`intro`](https://github.com/hwrberlin/fswd-examples/tree/intro) contains example code from the "[Intro to full-stack web development with Flask](https://hwrberlin.github.io/fswd/02-fswd-intro.html)" session.
+ [`flask`](https://github.com/hwrberlin/fswd-examples/tree/flask) contains example code from the "[Flask framework: URL path routing deep dive](https://hwrberlin.github.io/fswd/07-flask.html)" session.
+ [`html+css`](https://github.com/hwrberlin/fswd-examples/tree/html+css) contains example code from the "[Introduction to HTML and CSS](https://hwrberlin.github.io/fswd/09-html-css.html)" session.
+ [`ui`](https://github.com/hwrberlin/fswd-examples/tree/ui) contains example code from the "[User interfaces with WTForms and Bootstrap](https://hwrberlin.github.io/fswd/11-user-interfaces.html)" session.
+ [`sqlalchemy`](https://github.com/hwrberlin/fswd-examples/tree/sqlalchemy) contains example code from the "[Relational databases with Flask-SQLAlchemy](https://hwrberlin.github.io/fswd/13-sqlalchemy.html)" session.
=======
# Contents of this repository

You are on the **`sqlalchemy`** branch of this repository. It contains example code from the "[Relational databases with Flask-SQLAlchemy](https://hwrberlin.github.io/fswd/13-sqlalchemy.html)" session.

## Steps to execute the example code

**Step 1:** set up and activate a [Python Virtual Environment](https://hwrberlin.github.io/fswd/01-python-vscode.html#32-use-the-python-virtual-environment-as-default-for-this-workspace).

**Step 2:** install the required Python packages from the terminal with the command `pip install -r requirements.txt`:

```shell
(venv) C:\Users\me\projects\webapp> pip install -r requirements.txt
```

> I created the file `📄requirements.txt` with this command: `pip freeze > requirements.txt`

**Step 3:** initialize the app's SQLite database via `flask init-db`:

```shell
(venv) PS C:\Users\me\projects\webapp> flask init-db
Database has been initialized.
```

**Step 4:** start the web server via `flask run --reload`:

```shell
(venv) PS C:\Users\me\projects\webapp> flask run --reload
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
```

**Step 5:** visit <http://127.0.0.1:5000/insert/sample> to populate the app's database with some sample data.

**Step 6:** visit <http://127.0.0.1:5000/> to view the landing page.
>>>>>>> origin/sqlalchemy
