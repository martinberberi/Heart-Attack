from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods = ['GET', 'POST'])
def Home():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['age'])
        
        Sex = request.form['sex']
        if (Sex == "0"):
            Sex = 0
        else:
            Sex = 1
        
        Chest_pain = request.form['chest_pain']
        if (Chest_pain == '0'):
            Chest_pain = 0
        elif (Chest_pain == '1'):
            Chest_pain = 1
        elif (Chest_pain == '2'):
            Chest_pain = 2
        else:
            Chest_pain = 3
            
        Blood_pressure = int(request.form['blood_pressure'])
        Chol = int(request.form['cholesterol'])
        
        Blood_sugar = request.form['blood_sugar']
        if (Blood_sugar == '0'):
            Blood_sugar = 0
        else:
            Blood_sugar = 1
            
        Electro = request.form['electrocardiographic']
        if (Electro == '0'):
            Electro = 0
        elif (Electro == '1'):
            Electro = 1
        else:
            Electro = 2
            
        Heart_rate = int(request.form['heart_rate'])
        
        Exercise = request.form['exercise']
        if (Exercise == '0'):
            Exercise = 0
        else:
            Exercise = 1
            
        Peak = float(request.form['old_peak'])
        
        Slope = request.form['slope']
        if (Slope == '0'):
            Slope = 0
        elif (Slope == '1'):
            Slope = 1
        else:
            Slope = 2
            
            
        Vessels = request.form['number_vessels']
        if (Vessels == '0'):
            Vessels = 0
        elif (Vessels == '1'):
            Vessels = 1
        elif (Vessels == '2'):
            Vessels = 2
        elif (Vessels == '3'):
            Vessels = 3
        else:
            Vessels = 4
            
        Thal = request.form['thal_rate']
        if (Thal == '0'):
            Thal = 0
        elif (Thal == '1'):
            Thal = 1
        elif (Thal == '2'):
            Thal = 2
        else:
            Thal = 3
            
            
        pred = model.predict([[Age, Sex, Chest_pain, Blood_pressure, Chol, Blood_sugar, Electro, Heart_rate, Exercise,
                               Peak, Slope, Vessels, Thal]])
        output = pred[0]
        if output == 0:
            text = "Positive"
            return render_template('home.html', prediction = "The output is: {}".format(text))
        else:
            text = 'Negative'
            return render_template('home.html', prediction = "The output is: {}".format(text))
    
    else:
        return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug =True)
            
            
            
            
        
