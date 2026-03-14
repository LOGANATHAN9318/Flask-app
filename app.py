from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/v1/app/info')
def app_info():
    info = {'app_version': '1.0.0',
            'app_name': 'Flask-App',
            'app_author': 'Loganathan',}

    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)