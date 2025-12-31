#End-to-End Data Science Project

Company Name: Codtech 
Intern Name: Hamsa Varshini S  
Intern ID: CT04DR2747
Domain: Data Science  
Batch Duration: December 1st, 2025 to January 1st, 2026 


## Project Description
This project demonstrates a complete end-to-end data science workflow. The objective of this task is to build a machine learning model that predicts whether a student will pass or fail based on academic and attendance-related factors. The project covers all major phases of a data science pipeline, including data collection, preprocessing, model training, saving the trained model, API creation, and testing using real-time inputs.

The dataset used for this project contains student-related attributes such as hours studied, attendance percentage, and previous academic scores. These features were used to predict the target variable, which indicates whether a student has passed or failed. Python was used as the primary programming language due to its rich ecosystem of data science libraries.

For data handling and preprocessing, the Pandas library was used. The dataset was loaded from a CSV file, and relevant features were selected for model training. A machine learning classification model was trained using scikit-learn to learn patterns from the data. After training, the model was saved using the pickle module, allowing it to be reused without retraining.

To deploy the trained model, a Flask web framework was used to create a REST API. The API accepts input values in JSON format and returns predictions in real time. This makes the model usable as a web service and demonstrates how machine learning models can be integrated into real-world applications.

The API was tested using the curl command from the command line. Input values such as hours studied, attendance, and previous score were sent to the API endpoint, and the model successfully returned predictions. This confirms that the complete pipeline, from model training to deployment and testing, works as expected.

This project highlights the practical applicability of data science concepts in building predictive systems and deploying them using web technologies. It provides a strong foundation for understanding real-world machine learning deployment scenarios.

## Output

### Flask Server Running
![Flask Running](output/flask_running.png)

### API Running in Browser
![Browser Output](output/browser_output.png)

### API Prediction Output
![Prediction Output](output/api_prediction.png)
