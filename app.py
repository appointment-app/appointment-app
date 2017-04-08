from flask import Flask, render_template, request, flash, redirect
# from twilio.rest import TwilioRestClient
import os
from config import app, db

# client = TwilioRestClient(account=app.config['TWILIO_ACCOUNT_SID'], token=app.config['TWILIO_AUTH_TOKEN'])

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        form = request.form
        if "@" in form['email'] and "." in form['email']:
            db.subscribers.insert({"email" : form['email'], "plan" : form['plan']})
            print "Email: %s Plan: %s" % (form['email'], form['plan'])
            flash("<b>Thank you!</b> We'll contact you as soon as possible.", "success")
            return redirect('/')
        else:
            flash('Please enter a valid email.', "warning")
            return redirect('/')
    return render_template("home.html")

# @app.route("/new", methods=['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#         r = client.messages.create(
#             body=request.form['body'],
#             to=request.form['phone_number'],
#             from_="2015618328"
#         )
#         print r
#     return render_template("new.html")

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)