from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key = 'password123'

@app.route('/')         
def index():
    print(request.form)
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def results():
    print(request.form)
    session['name'] = request.form["name"]
    session['location'] = request.form["location"]
    session['language'] = request.form["language"]
    session['comment'] = request.form["comment"]
    return render_template("result.html")


if __name__=="__main__":
    app.run(debug=True)