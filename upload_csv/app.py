from flask import Flask,request, url_for, redirect, render_template, request, send_file
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    # int_features=[int(x) for x in request.form.values()]
    # final=[np.array(int_features)]
    
    # print(int_features)
    # print(final)
    # prediction=model.predict_proba(final)
    # output='{0:.{1}f}'.format(prediction[0][1], 2)
    
    if request.method == 'POST':
        uploaded_file = request.files['file']

        if not uploaded_file:
            return render_template('home.html', error_message='Please upload a file')

        try:
            data = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
        except:
            return render_template('home.html', error_message='Invalid file format. Please upload a CSV file')
        
        # data['finall']=data['Oxygen']

        
        model = pickle.load(open('model.pkl', 'rb'))
        
     
        X = data.iloc[:, 1:-1].astype('int')
        
        predictions = model.predict_proba(X)
        
        data['Prediction'] = predictions[:, 1]
        
        data.to_csv('predictions.csv', index=False)

        # output='{0:.{1}f}'.format(prediction[0][1], 2)


        return send_file('predictions.csv', as_attachment=True)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
