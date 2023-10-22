from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
import forms
from flask_bcrypt import Bcrypt
from flask import redirect
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import check_password_hash 

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment_from_Finn',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)

from db import db, Todo, List, insert_sample, User  # (1.)

bootstrap = Bootstrap5(app)

@app.route('/index')
@app.route('/')
@login_required
def index():
    return redirect(url_for('todos'))

@app.route('/todos/', methods=['GET', 'POST'])
@login_required
def todos():
    form = forms.CreateTodoForm()
    if request.method == 'GET':
        #todos = db.session.execute(db.select(Todo).order_by(Todo.id)).scalars()  # !!
        todos = db.session.query(Todo).filter_by(user_id=current_user.id)
        return render_template('todos.html', todos=todos, form=form)
    else:  # request.method == 'POST'
        if form.validate():
            todo = Todo(description=form.description.data, user_id=current_user.id)  # !!
            db.session.add(todo)  # !!
            db.session.commit()  # !!
            flash('Todo has been created.', 'success')
        else:
            flash('No todo creation: validation error.', 'warning')
        return redirect(url_for('todos'))

@app.route('/todos/<int:id>', methods=['GET', 'POST'])
@login_required
def todo(id):
    #todo = db.session.get(Todo, id, )  # !!
    todo = db.session.query(Todo).filter_by(user_id=current_user.id, id=id).first()
    print(todo)
    form = forms.TodoForm(obj=todo)  # (2.)  # !!
    if request.method == 'GET':
        if todo:
            if todo.lists: form.list_id.data = todo.lists[0].id  # (3.)  # !!
            #choices = db.session.execute(db.select(List).order_by(List.name)).scalars()  # !!
            choices = db.session.query(List).filter_by(user_id = current_user.id)
            form.list_id.choices = [(0, 'List?')] + [(c.id, c.name) for c in choices]  # !!
            return render_template('todo.html', form=form)
        else:
            abort(404)
    else:  # request.method == 'POST'
        if form.method.data == 'PATCH':
            if form.validate():
                form.populate_obj(todo)  # (4.)
                todo.populate_lists([form.list_id.data])  # (5.)  # !!
                db.session.add(todo)  # !!
                db.session.commit()  # !!
                flash('Todo has been updated.', 'success')
            else:
                flash('No todo update: validation error.', 'warning')
            return redirect(url_for('todo', id=id))
        elif form.method.data == 'DELETE':
            db.session.delete(todo)  # !!
            db.session.commit()  # !!
            flash('Todo has been deleted.', 'success')
            return redirect(url_for('todos'), 303)
        else:
            flash('Nothing happened.', 'info')
            return redirect(url_for('todo', id=id))

@app.route('/lists/')
@login_required
def lists():
    lists = db.session.execute(db.select(List).order_by(List.name)).scalars()  # (6.)  # !! #mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm hier auch user spezifisch?
    return render_template('lists.html', lists=lists)

@app.route('/lists/<int:id>')
@login_required
def list(id):
    list = db.session.get(List, id)  # !! #mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm hier auch user spezifisch?
    if list is not None:
        return render_template('list.html', list=list)
    else:
        return redirect(url_for('lists'))

@app.route('/insert/sample')
@login_required
def run_insert_sample():
    insert_sample()
    return 'Database flushed and populated with some sample data.'

@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500

@app.get('/faq/<css>')
@app.get('/faq/', defaults={'css': 'default'})
def faq(css):
    return render_template('faq.html', css=css)

@app.get('/ex/<int:id>')
@app.get('/ex/', defaults={'id':1})
def ex(id):
    if id == 1:
        return render_template('ex1.html')
    elif id == 2:
        return render_template('ex2.html')
    else:
        abort(404)

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                if request.args :
                    #testing = request.args.get('next')[1:-1]
                    #print(testing)
                    routing = request.args.get('next').replace('/', '')
                    flash('Login successful!', 'success')
                    print(routing)
                    return redirect(url_for(routing))
                else:
                    flash('Login successful!', 'success')
                    return redirect(url_for('todos'))
            else:
                flash('Incorrect password. Please try again.', 'danger')
        else:
            flash('Username not found. Please try again, or register if you don\'t have an account.', 'danger')

    return render_template('login.html', form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
       
    if request.method=='POST':

        existing_user = User.query.filter_by(
        username = form.username.data).first()
        print(existing_user)    

        #if len(form.password.data) < 4:
        #        flash('Password must be at least 4 characters long.', 'danger')
        #    # Validate username length
        #elif len(form.username.data) < 2:
        #        flash('Username must be at least 2 characters long.', 'danger')

        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(username = form.username.data, password = hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username is already taken. Please choose a different one.', 'danger')
    return render_template('register.html', form = form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/delete_account', methods=['GET', 'POST'])
@login_required  
def delete_account():
    if request.method == 'GET':
        return render_template('delete_account.html')

    if request.method == 'POST':
        
        user = current_user
        entered_password = request.form['password']

        if check_password_hash(user.password, entered_password):

            user_id = user.id
            db.session.query(Todo).filter_by(user_id=user_id).delete()
            db.session.query(List).filter_by(user_id=user_id).delete()
            db.session.commit()

            db.session.delete(user)
            db.session.commit()

            logout_user()

            return render_template('delete_confirmation.html')

        else:#bbb
            flash('Incorrect password. Please try again.', 'danger')
            return render_template('delete_account.html')

    #return render_template('delete_account.html') nicht nötig

#@app.route('/delete_confirmation')
#def delete_confirmation():
#    return render_template('delete_confirmation.html')

#if __name__ == '__main__':
#    db.create_all()
#    app.run(debug=True)