import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def get_uniq_items(df, max_uniq=10):
    '''
    for every column in dataframe, get the unique values
    if unique values is > max_uniq, then display the count of unique values
    '''
    return {
        col:list(df[col].unique())  # display unique values in column
            if df[col].nunique()<=max_uniq
            else [df[col].nunique()]  # display count of unique values in column
        for col in list(df.columns)
        }


def evaluate_model_performance(pipe, X_train, y_train, X_test, y_test):
    pipe.fit(X_train, y_train)
    
    y_train_pred = pipe.predict(X_train)
    y_test_pred = pipe.predict(X_test)
    
    print(f"\nModel performance on TRAINING data")
    ConfusionMatrixDisplay(confusion_matrix(y_train, y_train_pred)).plot.show()
    print(f"\nModel performance on VALIDATION data")
    ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_pred)).plot().show()