from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('wind.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/login',methods = ['post','get'])
def login():
    get_WD = float(request.form['a'])
    get_WS = float(request.form['b'])
    get_AP = float(request.form['c'])
    
    final_data = [[get_WD,get_AP,get_WS]]
    y_pred = model.predict(np.array(final_data))
    y= str(y_pred[0][0])
    return render_template('index.html' ,abc = y)


if __name__== '__main__':
    app.run(debug = True)