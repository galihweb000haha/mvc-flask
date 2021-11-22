from flask import render_template, request
from app import app
from app.models.customer import Customer

@app.route('/customer', methods = ['GET'])
def customer():
    if request.method == "POST":
        inputan = request.form
    else :
        customer = Customer()
        data = customer.get()
        print(data)
        return render_template('customer.html', data=data)
