## Enabling the study of Academic Performance through Machine Learning Techniques  
  
  
Goal of this project is to create a functional website that can recommend technical courses to students based on multiple parameters using machine learning techniques.  
  
The proposed system gets various inputs from the user which are used in a machine learning model. The machine learning models consists of a classification algorithm in which the best results for a certain input is mapped called training data. The output from the machine learning is accurate and based on the result the user is recommended a technical course that is best suited to them along with tips on how to pursue the course.  
  
This project uses the Flask microframework to host the machine learning model on the web. Packages such as scikitlearn and pandas are used to create and manipulate the machine learning classifier.  

The file "classifier.py" is used to create a machine learning classifier in the form of a pickle file named "NBClassifier.pkl". 

The "NBClassifier.pkl" pickle file is then imported into the flask project to be used on the web. This is dont to ensure that the system doest take excess time to classify the data everytime a user wants a recommendation.  

The data in the Final Dataset are the numerical iterpretation of the data that has been extracted from the " [Stackoverflow Developer Survey 2019](https://insights.stackoverflow.com/survey/2019) "    

Requirements =>

Flask 1.0.2  
Flask-Bootstrap 3.3.7.1  
Scikit-learn 0.19.1  
Pandas 0.23.4


