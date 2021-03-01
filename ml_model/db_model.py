import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Read data
df = pd.read_csv('diabetes_csv.csv')

class_map = {
    'tested_positive': 1,
    'tested_negative': 0
}

df['class'] = df['class'].map(class_map)


def null_check(data):
    ans = data.isna().sum() / len(data)
    return ans


def skewness(data):
    skw = data.skew()
    return skw


def correlation(data):
    cor = data.corr()
    return cor


def describe(data):
    desc = data.describe()
    return desc


X = df.drop('class', axis=1)
y = df['class']


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20)

log_reg = SVC()
log_reg.fit(X, y)
print(log_reg.predict(X))


#didn't do lots of data processing thou
# Pickle the model
joblib.dump(log_reg, 'model.pkl')
