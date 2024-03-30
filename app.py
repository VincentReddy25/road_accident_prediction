from flask import Flask, render_template, request
import joblib
import numpy as np
from twilio.rest import Client



app = Flask(__name__)
model = joblib.load('model.sav')
# Twilio account credentials
account_sid = "AC48b8442ca1a1bdfb07a788e334e53412"
auth_token = "0a913298f60a7dc4e93c055a396a2ec3"
twilio_phone_number = "+13027516269"  # Your Twilio phone number
verified_recipient_number = "+919553495889"  # Your verified recipient number

# Initialize Twilio client
client = Client(account_sid, auth_token)

def send_sms(data):
    from_number = "+13027516269"  # Your Twilio phone number
    verified_number = "+919553495889"
    message_body = data

    try:
        message = client.messages.create(body=message_body, from_="+13027516269", to="+919553495889")
        print("Message sent successfully! SID:", message.sid)
    except Exception as e:
        print("Failed to send message:", str(e))

def cal(ip):
    input_data = dict(ip)
    # Extract and process input_data here...

    # For demonstration, let's assume 'result_int' is the predicted severity
    result_int = 1
    return str(result_int)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/map', methods=['GET'])
def map():
    return render_template('map.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/', methods=['POST'])
def get():
    a = cal(request.form)
    if a == '1':
        send_sms("Your Accident Severity Prediction was 'Fatal'. ")
    elif a == '2':
        send_sms("Your Accident Severity Prediction was 'Serious'. ")
    else:
        send_sms("Your Accident Severity Prediction was 'Slight'. ") 
    return a



if __name__ == '__main__':
    app.run(debug=True)

