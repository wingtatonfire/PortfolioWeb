from flask import Flask, render_template, request, url_for
import smtplib
import os


app = Flask(__name__)


def send_email(name, email, message, subject):
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender = os.environ['EMAIL']
    recipient = os.environ['EMAIL']
    mail.login(sender, os.environ['APP'])
    content = f"Subject:New Message:{subject}\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    mail.sendmail(from_addr=sender, to_addrs=recipient, msg=content)
    mail.close()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        subject = request.form['subject']
        send_email(name, email, message, subject)
        return render_template('index.html')
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    return render_template('mywork.html')


if __name__ == '__main__':
    app.run(debug=True)
