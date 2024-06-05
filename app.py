from flask import Flask, send_file
import os

app = Flask(__name__)


@app.route('/')
def hello():
    # display simple content
    return """
    <a href='/most_seats'>Most Seats</a>
    <a href='/overall_majority'>Overall Majority</a>
    """


@app.route('/overall_majority')
def majority():
    pdf_path = os.path.join(os.getcwd(), 'majority.pdf')
    return send_file(pdf_path)


@app.route('/most_seats')
def most_seats():
    pdf_path = os.path.join(os.getcwd(), 'most_seats.pdf')
    return send_file(pdf_path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
