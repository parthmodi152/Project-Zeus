
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

data = pd.read_csv('atlantic_cleaned2.0.csv')

winds_34 = ['34_kt_ne', '34_kt_se',
       '34_kt_sw', '34_kt_nw']
winds_50 = ['50_kt_ne', '50_kt_se',
       '50_kt_sw', '50_kt_nw']
winds_64 = ['64_kt_ne', '64_kt_se',
       '64_kt_sw', '64_kt_nw']


def Correlator(df):
    '''
    Plots a correlator to show how related features are to each other
    '''
    st.markdown("### **Correlation Matrix**")
    st.markdown('#### We made a correlation matrix to see how each feature relates to each other')
    corrmat = df.corr()
    f, ax = plt.subplots(figsize=(20, 9))
    sns.heatmap(corrmat, vmax=.8, annot=True)
    
    st.pyplot(f)
    st.markdown("### **INSIGHTS**")
    st.markdown("#### We can seee there is a clear correlation between wind speeds.  ")
    st.markdown("#### In addition we can see a clear negative correlation between winds and pressure.")
    st.markdown("#### This is evident because hurricanes occur when there is lower pressure.")
    st.markdown("#### We also see there's a correlation between maximum wind speed and wind speeds.")

def plotwind34(df):
    '''
    Plots a line plot for all the winds in the list winds_34 in relation to the maximum_sustained_wind_knots
    '''
    f, ax = plt.subplots(figsize=(20, 9))
    for i in winds_34:
        sns.lineplot(x = df[i],y = df["maximum_sustained_wind_knots"], legend=False)
    plt.legend( loc='upper left', labels=winds_34)
    st.pyplot(f)
    st.markdown("### **INSIGHTS**")
    st.markdown("#### Hence, we can conclude that there is a strong correlation between the wind speeds and the sustained wind.")
    st.markdown("#### Hurricanes are generated generally when there are high sustained wind speeds so we can see that when directional winds increase, there is a higher chance of a storm")

def plotwind50(df):
    '''
    Plots a line plot for all the winds in the list winds_50 in relation to the maximum_sustained_wind_knots
    '''
    f, ax = plt.subplots(figsize=(20, 9))
    for i in winds_50:
        sns.lineplot(x = df[i],y = df["maximum_sustained_wind_knots"], legend=False)
    plt.legend( loc='upper left', labels=winds_50)
    st.pyplot(f)
    st.markdown("### **INSIGHTS**")
    st.markdown("#### Hence, we can conclude that there is a strong correlation between the wind speeds and the sustained wind.")
    st.markdown("#### Hurricanes are generated generally when there are high sustained wind speeds so we can see that when directional winds increase, there is a higher chance of a storm")


def plotwind64(df):
    '''
    Plots a line plot for all the winds in the list winds_64 in relation to the maximum_sustained_wind_knots
    '''
    f, ax = plt.subplots(figsize=(20, 9))
    for i in winds_64:
        sns.lineplot(x = df[i],y = df["maximum_sustained_wind_knots"], legend=False)
    plt.legend( loc='upper left', labels=winds_64)
    st.pyplot(f)
    st.markdown("### **INSIGHTS**")
    st.markdown("#### Hence, we can conclude that there is a strong correlation between the wind speeds and the sustained wind.")
    st.markdown("#### Hurricanes are generated generally when there are high sustained wind speeds so we can see that when directional winds increase, there is a higher chance of a storm")


def countplotter(y_values):
    '''
    Plots a countplot of all the categorical features. Input the Y array
    '''
    st.write("Lets see the distribution of the data")
    f, ax = plt.subplots(figsize=(20, 9))
    sns.countplot(x=y_values)
    st.pyplot(f)
    st.markdown("### **INSIGHTS**")
    st.markdown("#### Hence, we can conclude that there is a strong correlation between the wind speeds and the sustained wind.")
    st.markdown("#### Hurricanes are generated generally when there are high sustained wind speeds so we can see that when directional winds increase, there is a higher chance of a storm")
