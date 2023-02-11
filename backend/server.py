from flask import Flask
import datetime 

x = datetime.datetime.now()

# Init the flask app
app = Flask(__name__)

@app.route("/")
def time():

    return {
        'Name': 'MK',
        "Date": x
    }

if __name__ == '__main__':
    app.run()

    