#this is gas turbine flask app 

from flask import *
import pickle
import numpy as np 


#Loading Models 
with open('static\models\pred_model_co.pkl','rb') as co_model,open('static\models\pred_model_nox.pkl','rb') as nox_model:
    co_model = pickle.load(co_model)
    nox_model = pickle.load(nox_model)

with open('static\models\class_model_co.pkl','rb') as coc_model,open('static\models\class_model_nox.pkl','rb') as noxc_model:
    coc_model = pickle.load(coc_model)
    noxc_model = pickle.load(noxc_model)


#print(co_model)
#print(nox_model)
#print(coc_model)
#print(noxc_model)
app = Flask(__name__)

#create route for web app 
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        AT = float(request.form['AT'])
        AP = float(request.form['AP'])
        AH = float(request.form['AH'])
        AFDP = float(request.form['AFDP'])
        GTEP = float(request.form['GTEP'])
        TIT = float(request.form['TIT'])
        TAT = float(request.form['TAT'])
        TEY = float(request.form['TEY'])
        CDP = float(request.form['CDP'])

        data = np.array([AT,AP,AH,AFDP,GTEP,TIT,TAT,TEY,CDP]).reshape(1, -1)
        pred = co_model.predict(data)
        pred1 = nox_model.predict(data)

        pred = np.round(pred[0],3)
        pred1 = np.round(pred1[0],3)
        
        data1 = np.array([AT,AP,AH,AFDP,GTEP,TIT,TAT,TEY,CDP,pred,pred1]).reshape(1,-1)
        pred2 = coc_model.predict(data1)
        pred3 = noxc_model.predict(data1)

        pred2 = pred2[0]
        pred3 = pred3[0]

        pred = str(pred)
        pred1 = str(pred1)

        return render_template('index.html',CO = pred,NOX = pred1,COlevel = pred2,NOXlevel = pred3)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contac')
def contac():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)