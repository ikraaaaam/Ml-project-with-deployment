### Introduction About the Data :

**The dataset** The goal is to predict `math_score` of given student features .

There are 7 independent variables :

* `gender` : tells about gender of each student
* `race_ethnicity` : tells about each students ethnicity among 3 groups
* `parental_level_of_education` : level of parental education
* `lunch` : each students lunch category
* `test_preparation_course` : has the student completed the course or not 

* `reading_score` : tells about each students reading score

* `writing_score` : tells about the writing score
Target variable:
* `math_score`: tells about the math score of each student

Dataset Source Link :
https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977

# Microsoft Azure Deployment Link :
https://studentsmathscoreprediction.azurewebsites.net/

# Screenshot of UI
![HomepageUI](./Screenshots/1.png)

# Approach for the project 

1. Data Ingestion : 
    * In Data Ingestion phase the data is first read as csv. 
    
* Then the data is split into training and testing and saved as csv file.


2. Data Transformation : 
    * In this phase a ColumnTransformer Pipeline is created.
    * for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
    * for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
    * This preprocessor is saved as pickle file.

3. Model Training : 
    * In this phase base model is tested . The best model found was catboost regressor.
    * After this hyperparameter tuning is performed on catboost and knn model.
    * A final VotingRegressor is created which will combine prediction of catboost, xgboost and knn models.
    * This model is saved as pickle file.

4. Prediction Pipeline : 
    * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation : 
    * Flask app is created with User Interface to predict the gemstone prices inside a Web Application.
# Exploratory Data Analysis Notebook

Link : [EDA Notebook](./notebook/EDA_STUDENT_PERFORMANCE .ipynb)

# Model Training Approach Notebook

Link : [Model Training Notebook](./notebook/MODEL_TRAINING.ipynb)

