from flask import Flask, render_template, request, jsonify
from send_mail import add_task, show_last_emails

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('send_emails.html')


@app.route('/resp', methods=['GET', 'POST'])
def send_email():
    message = request.form.get('message')
    reciever = request.form.get('reciever')
    subject = request.form.get('subject')
    timer = int(request.form.get('timer'))
    add_task(reciever, subject, message, timer)
    return jsonify({"message": message, "timer": timer}), 200


@app.route('/last-tasks', methods=['GET'])
def last_tasks():
    emails = show_last_emails()
    return render_template('last_emails.html', emails=emails)


if __name__ == '__main__':
    app.run(debug=True, port=8089)
