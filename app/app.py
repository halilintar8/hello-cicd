from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello halilintar8, welcome to OpenShift CI/CD pipeline with Tekton!"

