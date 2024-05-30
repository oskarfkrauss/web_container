from flask import Flask, send_file
import os

app = Flask(__name__)


@app.route('/')
def hello():
    # display simple content
    pdf_path = os.path.join(os.getcwd(), 'general_election_odds.pdf')
    return send_file(pdf_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
