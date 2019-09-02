from flask import Flask,render_template,url_for,request,redirect
from flask_bootstrap import Bootstrap
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
import pandas as pd
import numpy as np

#ML Packges
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'
Bootstrap(app)

twitter_blueprint = make_twitter_blueprint(api_key='RN8Io0llB0lUf6NhfEKMhKPxh',api_secret='65Xq4ZfvqmABNsu6fhi49U2ZQpdyagdh1wnI8OiB2Of0SkHxda')
app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')


@app.route('/twitter')
def twitter_login():
        if not twitter.authorized:
            return redirect(url_for('twitter.login'))
        account_info = twitter.get('account/settings.json')

        if account_info.ok:
            account_info_json = account_info.json()
            return '<h1>Your twitter name is @{}'.format(account_info_json['screen_name'])

        return '<h1>Request Failed</h1>'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    naivebayes_model = open("models/NBClassifier.pkl","rb")
    clf = joblib.load(naivebayes_model)

    if request.method == 'POST':
        namequery = request.form['namequery']
        emailid = request.form['emailid']
        country = request.form['country']
        employement = request.form['employement']
        education = request.form['education']
        major = request.form['major']
        devtype = request.form['devtype']

#COUNTRIES NUMERICAL

    if country == "Argentina":
        countryx = 0
    elif country == "Australia":
        countryx = 1
    elif country == "Austria":
        countryx = 2
    elif country == "Belgium":
        countryx = 3
    elif country == "Brazil":
        countryx = 4
    elif country == "Canada":
        countryx = 5
    elif country == "Chile":
        countryx = 6
    elif country == "Colombia":
        countryx = 7
    elif country == "Croatia":
        countryx = 8
    elif country == "Denmark":
        countryx = 9
    elif country == "France":
        countryx = 10
    elif country == "Germany":
        countryx = 11
    elif country == "Greece":
        countryx = 12
    elif country == "India":
        countryx = 13
    elif country == "Indonesia":
        countryx = 14
    elif country == "Ireland":
        countryx = 15
    elif country == "Israel":
        countryx = 16
    elif country == "Italy":
        countryx = 17
    elif country == "Kenya":
        countryx = 18
    elif country == "Lebanon":
        countryx = 19
    elif country == "Netherlands":
        countryx = 20
    elif country == "Nigeria":
        countryx = 21
    elif country == "Poland":
        countryx = 22
    elif country == "Russian":
        countryx = 23
    elif country == "Slovakia":
        countryx = 24
    elif country == "South Africa":
        countryx = 25
    elif country == "Spain":
        countryx = 26
    elif country == "Sweden":
        countryx = 27
    elif country == "Thailand":
        countryx = 28
    elif country == "Turkey":
        countryx = 29
    elif country == "Ukraine":
        countryx = 30
    elif country == "United Kingdom":
        countryx = 31
    elif country == "United States":
        countryx = 32
    elif country == "Vietnam":
        countryx = 33


#EMPLOYEMENT NUMERICAL
    if employement == "Full Time":
            employementx = 0
    elif employement == "Part Time":
            employementx = 1

#EDUCATION NUMERICAL
    if education == "Associate degree":
            educationx = 0
    elif education == "Bachelor's degree (BA, BS, B.Eng., etc.)":
            educationx = 1
    elif education == "Master’s degree (MA, MS, M.Eng., MBA, etc.)":
            educationx = 2
    elif education == "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)":
            educationx = 3
    elif education == "Some college/university study without earning a degree":
            educationx = 4

#MAJOR NUMERICAL
    if major == "Computer science, computer engineering, or software engineering":
            majorx = 0
    elif major == "Another engineering discipline (ex. civil, electrical, mechanical)":
            majorx = 1
    elif major == "A business discipline (ex. accounting, finance, marketing)":
            majorx = 2
    elif major == "A humanities discipline (ex. literature, history, philosophy)":
            majorx = 3
    elif major == "A natural science (ex. biology, chemistry, physics)":
            majorx = 4
    elif major == "A social science (ex. anthropology, psychology, political science)":
            majorx = 5
    elif major == "Fine arts or performing arts (ex. graphic design, music, studio art)":
            majorx = 6
    elif major == "Information systems, information technology, or system administration":
            majorx = 7
    elif major == "Mathematics or statistics":
            majorx = 8

#DEVTYPE NUMERICAL

    if devtype == "Python, TensorFlow, PyTorch":
            devtypex = 0
    elif devtype == "HTML, CSS, JavaScript, SQL":
            devtypex = 1
    elif devtype == "PHP, Ruby, Java":
            devtypex = 2
    elif devtype == "HTML, CSS, SASS":
            devtypex = 3
    elif devtype == "React Native, Android Studio":
            devtypex = 4
    elif devtype == "Art, Illustration":
            devtypex = 5
    elif devtype == "MySQL, Oracle":
            devtypex = 6
    elif devtype == "OOP, Scrum":
            devtypex = 7

#FEATURE SCALING

    sc = StandardScaler()
    X_Test = pd.DataFrame([[countryx,employementx,educationx,majorx,devtypex]], columns = [countryx,employementx,educationx,majorx,devtypex])
    ScaleX = sc.fit_transform(X_Test)
    myprediction = clf.predict(ScaleX)



        #data = [namequery]
        #vect = cv.transform(data).toarray()
        #my_prediction = clf.predict(vect)
    return render_template('result.html',name = namequery,email = emailid,country = country,employement = employement,
                                        education = education, major = major, devtype = devtype, myprediction = myprediction)

@app.route('/backend.html')
def backend():
    return render_template('backend.html')

@app.route('/dataanalytics.html')
def dataanalytics():
    return render_template('dataanalytics.html')

@app.route('/fullstack.html')
def fullstack():
    return render_template('fullstack.html')

@app.route('/frontend.html')
def frontend():
    return render_template('frontend.html')

@app.route('/mobile.html')
def mobile():
    return render_template('mobile.html')

@app.route('/design.html')
def design():
    return render_template('design.html')

@app.route('/database.html')
def database():
    return render_template('database.html')

@app.route('/software.html')
def software():
    return render_template('software.html')

if __name__ == '__main__':
    app.run(debug=True)
