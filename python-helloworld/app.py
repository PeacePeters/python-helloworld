from flask import Flask
from flask import json
import logging
from datetime import datetime

app = Flask(__name__)

@app.route('/status')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    ## log line
    app.logger.info('Timestamp {dt} , Status endpoint is reached.'.format(dt=datetime.now()))
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    ## log line
    app.logger.info('Timestamp {dt} , Metrics endpoint is reached.'.format(dt=datetime.now()))
    return response

@app.route("/")
def hello():
    ## log line
    app.logger.info('Timestamp {dt} , Main request successfull.'.format(dt=datetime.now()))

    return "Hello World!"

if __name__ == "__main__":

    ## stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0', port=8080)
