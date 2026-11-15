from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Deployed by halilintar8 with github, openshift, and Tekton ci/cd"
