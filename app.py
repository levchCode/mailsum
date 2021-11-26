from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin

from src.Mail import Mail
from src.Ml import Ml

app = Flask(__name__)
cors = CORS(app)


@app.route("/")
def index():
    """
    Demonstrate text of the 5 last messages. Number of the last messages change in the src.Mail NUMBER_MESSAGES
    """
    mailer = Mail()
    mail_texts = mailer.list_text_messages()
    return render_template("index.html", texts=mail_texts)


@app.route("/list_email_ids", methods=["GET"])
@cross_origin()
def list_emails():
    """
    Return list of messages's ids and their threads ids
    """
    mailer = Mail()
    mail_ids = mailer.list_messages()
    return jsonify({"results": mail_ids})


@app.route("/email_text", methods=["GET"])
@cross_origin()
def email_text():
    """
    Return text of message by id
    """
    messages_id = request.args.get('id')
    mailer = Mail()
    mail_texts = mailer.list_text_messages(messages_id)
    return jsonify({"results": mail_texts})


@app.route("/task_by_email", methods=["GET"])
@cross_origin()
def task_by_email():
    """
    Return task from email by id
    """
    messages_id = request.args.get('id')
    mailer = Mail()
    mail_texts = mailer.list_text_messages(messages_id)
    model = Ml
    task = model.predict(text=mail_texts)
    return jsonify(task)


if __name__ == "__main__":
    app.run(debug=True)
