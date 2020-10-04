from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error
from sklearn import tree

def model(name):
    #loading data
    if name == 'Atlantic':
        file_name = 'atlantic_cleaned2.0.csv'
    elif name == 'Pacific':
        file_name = 'pacific-cleaned1.0.csv'
    atlantic_data = pd.read_csv(file_name)
    HU = atlantic_data[atlantic_data['status_of_system'] == 'HU'] # (> 64 knots) 
    TS = atlantic_data[atlantic_data['status_of_system'] == 'TS']  # (34-63 knots) 
    TD = atlantic_data[atlantic_data['status_of_system'] == 'TD']  # (< 34 knots) 
    EX = atlantic_data[atlantic_data['status_of_system'] == 'EX'] # Any winds

    frames = [HU, TS, TD, EX]
    atlantic_data = pd.concat(frames)
    atlantic_data = atlantic_data.drop(['id', 'name', 'date', 'latitude', 'longitude'], axis=1)
    atlantic_data = atlantic_data.replace(to_replace="HU",  
                                value = 4) 
    atlantic_data = atlantic_data.replace(to_replace="TS",  
                                value = 3) 
    atlantic_data = atlantic_data.replace(to_replace="TD",  
                                value = 2) 
    atlantic_data = atlantic_data.replace(to_replace="EX",  
                                value = 1)  
    y = atlantic_data.status_of_system
    feature_columns = [ 'maximum_sustained_wind_knots', 'maximum_pressure',
                    '34_kt_ne', '34_kt_se', '34_kt_sw', '34_kt_nw', 
                   '50_kt_ne', '50_kt_se', '50_kt_sw', '50_kt_nw',
                   '64_kt_ne', '64_kt_se', '64_kt_sw', '64_kt_nw',
                   ]
    X = atlantic_data[feature_columns]
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state = 0)
    # Imputation
    my_imputer = SimpleImputer()
    imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
    imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
    atlantic_model = DecisionTreeRegressor(random_state = 1)
    atlantic_model.fit(imputed_X_train,y_train)
    val_predictions = atlantic_model.predict(imputed_X_valid)
    return mean_absolute_error(y_valid, val_predictions)