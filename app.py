from flask import Flask, request, render_template, redirect, url_for
import requests
from config import TOKEN, CHAT_ID
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirm', methods=['POST'])
def confirm():
    email = request.form.get('email')
    payment_method = request.form.get('payment_method')
    price = request.form.get('price')
    return render_template('confirm.html', email=email, payment_method=payment_method, price=price)

@app.route('/payment', methods=['POST'])
def payment():
    email = request.form.get('email')
    payment_method = request.form.get('payment_method')
    price = request.form.get('price')
    return redirect(f'https://payment-gateway.com?email={email}&payment_method={payment_method}&price={price}')

if __name__ == '__main__':
    app.run(debug=True)
