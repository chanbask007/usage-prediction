from flask import Flask, render_template, request, jsonify
import datetime
import pickle


app = Flask(__name__)
model= pickle.load('model.pkl','rb');

@app.route('/<string:name>')
def hello_world(name):
    now = datetime.datetime.now()
    is_new_year= now.month==1 and now.day==1
    return render_template("index.html", is_new_year= is_new_year)

@app.route('/hello',methods=["post"])
def hello():
    name= request.form.get("name");
    return render_template("hello.html", name=name)



if __name__ == "__main__":
    app.run(debug=True)
    
