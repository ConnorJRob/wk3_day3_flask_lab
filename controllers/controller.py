from app import app
from flask import render_template
from models.order_list import *

@app.route('/')
def index():
    return render_template('index.html', title="Order List", orders = orders)

@app.route('/orders/<index>')
def order(index):
    new_order = orders[int(index)]
    return render_template('order.html', order = new_order)