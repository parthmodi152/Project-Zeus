import streamlit as st
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
from streamlit_functions import model
from model_predictor import predictor
import random
from visualizations import plotwind64, plotwind34, plotwind50, Correlator, countplotter

st.image('logo.jpeg', width = 360)
#st.markdown("<img src= 'logo.jpeg' style='display:block; width: 30; margin: auto'></img>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; color: #08081f;'>Project Zeus Web App</h1>", unsafe_allow_html=True)
st.write("Data Analysis and Modeling")
dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('Atlantic', 'Pacific')
)
st.sidebar.markdown("### Definitions")

st.sidebar.markdown("### HU – Tropical cyclone of hurricane intensity (> 64 knots)")
st.sidebar.markdown("### TS – Tropical cyclone of tropical storm intensity (34-63 knots)")
st.sidebar.markdown("### TD – Tropical cyclone of tropical depression intensity (< 34 knots)")
st.sidebar.markdown("### EX – Extratropical cyclone (of any intensity)")

classifications = {"1":"EX", "2":"TD", "3":"TS", "4":"HU"}

feature_columns = ['maximum_sustained_wind_knots', 'maximum_pressure',
                    '34_kt_ne', '34_kt_se', '34_kt_sw', '34_kt_nw', 
                   '50_kt_ne', '50_kt_se', '50_kt_sw', '50_kt_nw',
                   '64_kt_ne', '64_kt_se', '64_kt_sw', '64_kt_nw']

def get_dataset(name):
    data = None
    if name == 'Atlantic':
        data = pd.read_csv('atlantic_cleaned2.0.csv')
    elif name == 'Pacific':
        data = pd.read_csv('pacific-cleaned1.0.csv')
    X = data[feature_columns]
    y = data.status_of_system
    return X, y



def show_raw_data(name):
    if name == 'Atlantic':
        data = pd.read_csv('atlantic_cleaned2.0.csv')
        return data.head()
    elif name == 'Pacific':
        data = pd.read_csv('pacific-cleaned1.0.csv')   
        return data.head()


X, y = get_dataset(dataset_name)
st.write('Shape of dataset:', X.shape)
st.write('number of classes:', len(np.unique(y)))

if st.checkbox('Let us analyse the information'):
    Correlator(X)
    countplotter(y)
    plotwind64(X)



if st.checkbox("Let us look at the data"):
    st.write(show_raw_data(dataset_name))
    if dataset_name == 'Atlantic':
        st.write('Accuracy:', 100 * (1 - (model(dataset_name))), '%')
        
    elif dataset_name == 'Pacific':
        st.write('Accuracy:', 100 * (1 - (model(dataset_name))), '%')


def randomrow(X, y):
    n = random.randint(8000, 8298)
    features = X.iloc[n,:]
    label = y[n]
    return features, label

if st.button("Try it yourself!"):
    randX, randy = randomrow(X, y)
    st.sidebar.write("Features")
    st.sidebar.write(pd.DataFrame(randX))
    st.sidebar.write("Expected Label")
    st.sidebar.write(randy)
    val = classifications[str(int(round(predictor('Atlantic', randX)[0])))]
    st.write("The model has given: ")
    if randy in ['HU', 'TS', 'TD', 'EX']:
        st.write(val)
    else:
        st.write("The entered storm " + str(randy) + " is not in the scope of being a hurricane")