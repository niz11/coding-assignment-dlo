from flask import Flask, redirect, request, render_template
from dlo.dlo_url_generator import generate_dlo_url
import os

app = Flask(__name__)
secret = os.getenv("SECRET_KEY")
base_url = os.getenv("BASE_URL")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate_link', methods=['GET'])
def generate_link():
    user_type = request.args.get('user_type')
    path_param = request.args.get('path', '')

    target_url = f"/{user_type}"
    if path_param:
        target_url += f"?path={path_param}"

    return redirect(target_url)
    

@app.route('/careprovider', methods=['GET'])
def careprovider():
    userid = 1
    usertype = "careprovider"
    redirecturl = request.args.get('redirect')
    path = request.args.get('path')
    return redirect(generate_dlo_url(userid, usertype, secret, base_url,path, redirecturl))

@app.route('/client', methods=['GET'])
def client():
    userid = 1
    usertype = "client"
    redirecturl = request.args.get('redirect')
    path = request.args.get('path')
    return redirect(generate_dlo_url(userid, usertype, secret, base_url,path, redirecturl))

if __name__ == '__main__':
    print("Starting server...")
    DEBUG = os.getenv("DEBUG", False)
    app.run(debug=DEBUG, host="0.0.0.0", port=5005)