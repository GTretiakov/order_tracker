import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('get_stores'))
    if request.method == 'POST':
        exitsting_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        if exitsting_user:
            if check_password_hash(
                exitsting_user['password'], request.form.get('password')):
                    session['user'] = request.form.get('username').lower()
                    flash('Welcome, {}'.format(request.form.get('username')))
                    return redirect(url_for('get_stores', username=session['user']))
            else:
                flash('Incorrect Username and/or Password')
                return redirect(url_for('login'))

        else:
            flash('Incorrect Username and/or Password')
            return redirect(url_for('login'))
    return render_template('login.html')



@app.route('/get_stores', methods=['GET', 'POST'])
def get_stores():
    if 'user' in session:
        stores = list(mongo.db.stores.find())
        flash("Recent Orders")
        if request.method == 'POST':
            store = {
                'store_name': request.form.get('store_name'),
            }
            store_exists = mongo.db.stores.find_one(store)
            if store_exists is None:
                mongo.db.stores.insert_one(store)
                flash("New Store Created!")
                stores = list(mongo.db.stores.find())
                return render_template(
                    'stores.html', stores=stores, recent_orders=True)
        return render_template('stores.html', stores=stores, recent_orders=True)
    else:
        return render_template('login.html')


@app.route('/get_comp', methods=['GET', 'POST'])
def get_comp():
    if 'user' in session:
        stores = list(mongo.db.stores.find())
        flash("Completed Orders")
        return render_template('stores_comp.html', stores=stores, comp_orders=True)
    else:
        return render_template('login.html')



@app.route('/get_orders/<store_id>', methods=['GET', 'POST'])
def get_orders(store_id):
    store = mongo.db.stores.find_one(
        {'_id': ObjectId(store_id)})
    store_name=mongo.db.stores.find_one(
        {'_id': ObjectId(store_id)})["store_name"]
    orders = list(mongo.db.orders.find())
    progresses = mongo.db.progresses.find()
    if request.method == 'POST':
        invoiced = 'Yes' if request.form.get('invoiced') else 'No'
        order = {
            'store_name': store_name,
            'order_number': request.form.get('order_number'),
            'notes': request.form.get('notes'),
            'date': request.form.get('date'),
            'status': request.form.get('status'),
            'progress': request.form.get('progress'),
            'invoiced': invoiced,
            'user': session['user']
        }
        order_exists = mongo.db.orders.find_one(order)
        if order_exists is None:
            mongo.db.orders.insert_one(order)
            flash("Order Added!")
            orders = list(mongo.db.orders.find())
            return render_template(
                'orders.html', orders=orders, store=store, recent_orders=True)
    return render_template(
        'orders.html', orders=orders, store=store, recent_orders=True)



@app.route('/completed/<store_id>', methods=['GET', 'POST'])
def completed(store_id):
    store = mongo.db.stores.find_one(
        {'_id': ObjectId(store_id)})
    store_name=mongo.db.stores.find_one(
        {'_id': ObjectId(store_id)})["store_name"]
    orders = list(mongo.db.orders.find())
    progresses = mongo.db.progresses.find()
    if request.method == 'POST':
        invoiced = 'Yes' if request.form.get('invoiced') else 'No'
        order = {
            'store_name': store_name,
            'order_number': request.form.get('order_number'),
            'notes': request.form.get('notes'),
            'date': request.form.get('date'),
            'status': request.form.get('status'),
            'progress': request.form.get('progress'),
            'invoiced': invoiced,
            'user': session['user']
        }
        mongo.db.orders.insert_one(order)
        flash("Order Added!")
        orders = list(mongo.db.orders.find())
        return render_template(
            'completed.html', orders=orders, store=store,
             progresses=progresses, comp_orders=True)
    return render_template(
        'completed.html', orders=orders, store=store,
         progresses=progresses, comp_orders=True)




@app.route('/delete_order/<order_id>/<store_id>')
def delete_order(order_id, store_id):
    s_id=store_id
    mongo.db.orders.remove({'_id': ObjectId(order_id)})
    flash('Order Deleted')
    return redirect(url_for('get_orders', store_id=s_id))


@app.route('/delete_store/<store_id>')
def delete_store(store_id):
    mongo.db.stores.remove({'_id': ObjectId(store_id)})
    flash('Store Deleted')
    return redirect(url_for('get_stores'))


@app.route('/edit_order/<order_id>/<store_id>', methods=['POST'])
def edit_order(order_id, store_id):
    if request.method == 'POST':
        s_id=store_id
        invoiced = 'Yes' if request.form.get('invoiced') else 'No'
        submit = {
            'store_name': mongo.db.orders.find_one(
                {'_id': ObjectId(order_id)})['store_name'],
            'order_number': request.form.get('number'+order_id),
            'notes': request.form.get('notes'+order_id),
            'date': request.form.get('date'+order_id),
            'status': request.form.get('status'+order_id),
            'progress': request.form.get('progress'+order_id),
            'invoiced': invoiced,
            'user': session['user']
        }
        mongo.db.orders.update({'_id': ObjectId(order_id)}, submit)
        flash('Order Updated')
        return redirect(url_for('get_orders', store_id=s_id))


@app.route('/edit_comp/<order_id>/<store_id>', methods=['POST'])
def edit_comp(order_id, store_id):
    if request.method == 'POST':
        s_id=store_id
        invoiced = 'Yes' if request.form.get('invoiced') else 'No'
        submit = {
            'store_name': mongo.db.orders.find_one(
                {'_id': ObjectId(order_id)})['store_name'],
            'order_number': request.form.get('number'+order_id),
            'notes': request.form.get('notes'+order_id),
            'date': request.form.get('date'+order_id),
            'status': request.form.get('status'+order_id),
            'progress': request.form.get('progress'+order_id),
            'invoiced': invoiced,
            'user': session['user']
        }
        mongo.db.orders.update({'_id': ObjectId(order_id)}, submit)
        flash('Order Updated')
        return redirect(url_for('completed', store_id=s_id))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        if existing_user:
            flash('Username already exists!')
            return redirect(url_for('register'))

        register = {
            'username': request.form.get('username').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)

        session['user'] = request.form.get('username').lower()
        flash('Registration Successful!')
        return redirect(url_for('get_stores', username=session['user']))
    return render_template('register.html')


@app.route('/logout')
def logout():
    flash('You have been signed out!')
    session.pop('user')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
