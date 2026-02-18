import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score


# Load dataset (e.g., Titanic) and preprocess it here

df = pd.read_csv('titanic.csv')

df = df[['Age', 'Sex', 'Fare']]  # Select relevant features for this example

df.loc[df['Age'].isnull(), 'Age'] = df['Age'].median()  # Impute missing age values with the median

df['Sex'] = (df['Sex'] == 'male').astype(int)  # Convert sex to numerical, male=1 and female=0

X = df[['Age', 'Fare']]

y = df['Survived']


# Split dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize logistic regression model with regularization strength 'C' of 1.0

model = LogisticRegression(C=1.0, solver='liblinear')


# Train the model on training data

model.fit(X_train, y_train)


# Predictions for test set and calculate accuracy score using sklearn function call outside of main to keep it clean as per instructions not included here but can be done similarly if needed: 

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print('Model Accuracy is', accuracy)