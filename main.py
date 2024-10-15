from flask import Flask
app = Flask(__name__)

@app.route('/cron-me')
def cron_me():
    call_my_function_here()
    return 'Success'
