from flask import Flask
from flask import request
from flask import send_file
import smtplib
import datetime

tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)

orderResponses = {
    'lysol spray': 'https://www.amazon.com/Lysol-Disinfectant-Spray-Crisp-Linen/dp/B003M5JR9K/ref=sr_1_4?dchild=1&keywords=lysol+spray+disinfectant&qid=1602998039&sr=8-4',
    'clorox wipes': 'https://www.amazon.com/Clorox-Disinfecting-Wipes-4460030208-CLO30208PK/dp/B00B71EKSY/ref=sr_1_11?dchild=1&keywords=clorox+wipes&qid=1602998116&sr=8-11',
    'hand sanitizer': 'https://www.amazon.com/Germ-x-Sanitizer-Original-fresh-citrus/dp/B0889WWM49/ref=sr_1_6?dchild=1&keywords=hand+sanitizer&qid=1602998225&sr=8-6',
    'masks': 'https://www.amazon.com/TCP-Global-Breathable-Disposable-Protective/dp/B088P7RC65/ref=sr_1_1_sspa?dchild=1&keywords=masks&qid=1602998282&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNFNWOUpNRVVOSUhPJmVuY3J5cHRlZElkPUEwNDAwNDYxMVZCRkNTV05CUDdZQSZlbmNyeXB0ZWRBZElkPUEwNjU0NTY0MU04WVJXV1VVRzA0SCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

}

protect_purdue_dashboard = 'https://tableau.itap.purdue.edu/views/PublicCOVIDTestingDashboard/Testing?%3Aembed=y&%3AshowVizHome=no&%3Ahost_url=https%3A%2F%2Ftableau.itap.purdue.edu%2F&%3Aembed_code_version=3&%3Atabs=no&%3Atoolbar=no&%3AshowAppBanner=false&%3Adisplay_spinner=no&%3AloadOrderID=0'

zoomLink = 'https://zoom.us/j/4280521951?pwd=akRENkhtRFBuenJRYWhESW01S3hkdz09'
password = '44gzqD'

def send_mail():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        
        smtp.login('hw00005dummy@gmail.com', "xintkyvkqllzxyku")

        subject = 'Covid Test Scheduling'
        body = f'Hello TREC team! I have been feeling COVID-19 Symptomatic and would like to schedule a test for {tomorrow_date} at 1:00 PM. Send me a confirmation email if this time works!'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('hw00005dummy@gmail.com', 'avidpatel1@gmail.com', msg)



app = Flask(__name__)

@app.route('/scheduling', methods=['POST'])
def scheduling():
    send_mail()
    return {
        'actions': [
            {'say': f'Your appointment has been scheduled for {tomorrow_date}!'},
            {'listen': True},
        ]
    }

@app.route('/ordering', methods=['POST'])
def ordering():
    item = request.form.get('Field_items_Value')
    return {
        'actions': [
            {'say': f'Here is an Amazon link to some {orderResponses[item]}!'},
            {'listen': True},
        ]
    }

@app.route('/symptoms', methods=['POST'])
def symptoms():
    return {
        'actions': [
            {'say': 'Here are the COVID19-19 Symptoms:\n -Fever or chills\n -Cough\n -Shortness of breath or difficulty breathing\n -Fatigue\n -Muscle or body aches\n -Headache\n -New loss of taste or smell\n -Sore throat\n -Congestion or runny nose\n -Nausea or vomiting\n -Diarrhea'},
            {'listen': True},
        ]
    }

@app.route('/meeting', methods=['POST'])
def meeting():
    return {
        'actions': [
            {'say': f'Zoom Link of a COVID-19 First Responder: {zoomLink} \nPassword:{password}'},
            {'listen': True},
        ]
    }
    


@app.route('/dashboard', methods=['POST'])
def dashboard():
    return {
        'actions': [
            {'say': f'Protect COVID-19 Case Dashboard: {protect_purdue_dashboard}'},
            {'listen': True},
        ]
    }

@app.route('/tasks', methods=['POST'])
def tasks():
    return {
        'actions': [
            {'say': 'I can schedule a COVID-19 test, help you order Masks/Santizer/Clorox/Lysol Spray Wipes/Lysol Spray, display COVID-19 Symptoms, send a Zoom link to a COVID-19 first responder, and display the Purdue COVID-19 Dashboard'},
            {'listen': True},
        ]
    }

