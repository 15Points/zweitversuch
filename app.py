from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
import forms
from flask_bcrypt import Bcrypt
from flask import redirect
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import check_password_hash
from flask import jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with #for RESTful API

app = Flask(__name__)
api = Api(app)          #for RESTful API

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

############################################################################################### API code chunk start
todo_parser = reqparse.RequestParser()
todo_parser.add_argument('description', type=str, required=True, help="This field is required")
todo_parser.add_argument('complete', type=bool)

todo_fields = {
    'id': fields.Integer,
    'description': fields.String,
    'complete': fields.Boolean,
    'user_id': fields.Integer,
}

class TodoResource(Resource):
    @marshal_with(todo_fields)
    def get(self, id=None):
        if id is None:  # Return all todos
            todos = db.session.query(Todo).filter_by(user_id=current_user.id).all()
            return todos
        else: # return single todos
            todo = db.session.query(Todo).filter_by(user_id=current_user.id, id=id).first()
            if not todo:
                abort(404, message="Todo not found")
            return todo

    @marshal_with(todo_fields)
    def post(self):
        args = todo_parser.parse_args()
        todo = Todo(description=args['description'], user_id=current_user.id)
        db.session.add(todo)
        db.session.commit()
        return todo, 201

    @marshal_with(todo_fields)
    def patch(self, id):
        args = todo_parser.parse_args()
        todo = db.session.query(Todo).filter_by(user_id=current_user.id, id=id).first()
        if not todo:
            abort(404, message="Todo not found")
        if args.description:
            todo.description = args['description']
        if args.complete:
            todo.complete = args['complete']
        db.session.commit()
        return todo

    def delete(self, id):
        todo = db.session.query(Todo).filter_by(user_id=current_user.id, id=id).first()
        if not todo:
            abort(404, message="Todo not found")
        db.session.delete(todo)
        db.session.commit()
        return '', 204

api.add_resource(TodoResource, '/api/todos', '/api/todos/<int:id>')
############################################################################################### API code chunk end

@app.route('/todos/', methods=['GET', 'POST'])
@login_required
def todos():
    form = forms.CreateTodoForm()
    if request.method == 'GET':
        #todos = db.session.execute(db.select(Todo).order_by(Todo.id)).scalars()  # !!
        todos = db.session.query(Todo).filter_by(user_id=current_user.id) # now user specific
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
    todo = db.session.query(Todo).filter_by(user_id=current_user.id, id=id).first() # now user specific
    print(todo)
    form = forms.TodoForm(obj=todo)  # (2.)  # !!
    if request.method == 'GET':
        if todo:
            if todo.lists: form.list_id.data = todo.lists[0].id  # (3.)  # !!
            #choices = db.session.execute(db.select(List).order_by(List.name)).scalars()  # !!
            choices = db.session.query(List).filter_by(user_id = current_user.id) # now user specific
            form.list_id.choices = [(0, 'List?')] + [(c.id, c.name) for c in choices]  # !!
            return render_template('todo.html', form=form)
            #todo_dict = {"id":todo.id,                              #At first, I misunderstood the api and json tasks
            #             "complete":todo.complete,
            #             "description":todo.description,
            #             "user_id":todo.user_id,
            #             "lists":todo.lists}
            #return jsonify(todo_dict)
        else:
            abort(404)
    else:  # request.method == 'POST'
        if form.method.data == 'PATCH':
            print(form.data)
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

@app.route('/lists/', methods=['GET', 'POST']) # POST added
@login_required
def lists():
    form = forms.CreateListForm()

    if request.method == 'POST':                                # Code for creation of lists (similar to the creation of todos)
        if form.validate_on_submit():
            new_list = List(name=form.list_name.data, user_id=current_user.id)
            db.session.add(new_list)
            db.session.commit()
            flash('List has been created.', 'success')
        else:
            flash('List creation failed: validation error.', 'danger')

    lists = db.session.query(List).filter_by(user_id=current_user.id)
    return render_template('lists.html', lists=lists, form=form)

@app.route('/lists/<int:id>')
@login_required
def list(id):
    list = db.session.get(List, id)  # !!
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


######################################################### everything from here onwards is for the account handling
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST']) # login
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
                    return redirect(url_for('todos')) # redirection to todos which acts as home page after successful login
            else:
                flash('Incorrect password. Please try again.', 'danger')
        else:
            flash('Username not found. Please try again, or register if you don\'t have an account.', 'danger')

    return render_template('login.html', form = form)

@app.route('/register', methods=['GET', 'POST']) # registration
def register():
    form = forms.RegisterForm()
       
    if request.method=='POST':

        existing_user = User.query.filter_by(
        username = form.username.data).first()
        print(existing_user)    

        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(username = form.username.data, password = hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login')) # redirection to login after successful registration
        else:
            flash('Username is already taken. Please choose a different one.', 'danger')
    return render_template('register.html', form = form)

@app.route('/logout', methods=['GET', 'POST']) # logout
@login_required
def logout():
    logout_user()
    return redirect(url_for('login')) # redirection to login after logout

@app.route('/delete_account', methods=['GET', 'POST']) # delete account
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

            return render_template('delete_confirmation.html') # confirmation that account has been deleted
                                                               # delete_confirmation.html contains a button that redirects back to login
        else:
            flash('Incorrect password. Please try again.', 'danger')
            return render_template('delete_account.html')

    #return render_template('delete_account.html') # unnecessary

#@app.route('/delete_confirmation')                          # not necessary (now also in /delete_account)
#def delete_confirmation():
#    return render_template('delete_confirmation.html')

#if __name__ == '__main__':  # at some points when I got errors I wanted to see whether I can run a main method 
#    db.create_all()
#    app.run(debug=True)