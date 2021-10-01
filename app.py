import pickle               #with help of picle our data gts stord in form of bytes
from flask import Flask , render_template, request             #al api work is done with hep of flask .
                                                         #flask is a module 

app = Flask(__name__)
loadedModel = pickle.load(open('diabetes.sav','rb'))

@app.route("/")
def home():
    return render_template('form.html')

@app.route("/prediction", methods=['POST'])
def prediction():
    bmi = request.form['bmi']
    age = request.form['age']
    glucose = request.form['glucose']

    prediction = loadedModel.predict([[glucose, bmi, age]])[0]

    if prediction == 0:
        prediction = "Not Diabetic"
    else:
        prediction = "Diabetic"

    return render_template('form.html', output=prediction)

if __name__ == '__main__':
    app.run(debug=True)