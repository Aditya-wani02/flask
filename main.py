# Integrate Html with flask
# HTTP GEt and Post
from flask import Flask ,request, redirect,url_for,render_template
# WSGI application is created
app = Flask(__name__)


'''
{%...%} contitions for statements
{{   }} expression to print
{#....#} comments

'''



@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >=50:
        res = 'PASS'
    else:
        res = 'FAIL'
    exp = {'score':score,'res':res}
    
    return render_template("result.html" ,result = exp)


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
    
@app.route('/submit',methods = ['POST','GET'])
def submit():
    total_score =0
    if request.method =="POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = (maths+c+science+datascience)/4

    result = ''

    return redirect(url_for('success',score=total_score))




if __name__ == '__main__':
    app.run(debug = True)