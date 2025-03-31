from flask import Flask , redirect,url_for
# WSGI application is created
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the flask learing"
# @app.route('/members')
# def members():
#     return "Welcome to the flask learing this is members page"

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the score is "+ str(score)
@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the score is "+ str(score)
@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "success"

    return redirect(url_for(result,score=marks))
    


if __name__ == '__main__':
    app.run(debug = True)