![alt text](https://github.com/parthmodi152/Project-Zeus/blob/master/logo.jpeg)
# Project Zeus: Storm Predicting Web-app

## Introduction
This is a web-app created for the NASA Space Challenge (https://www.spaceappschallenge.org/). <br />
It uses a model trained using data from the National Oceanic and Atmospheric Administration(NOAA) to classify storms in 4 major categories

## Data Source
The Atlantic dataset (known as Atlantic HURDAT2) has a comma-delimited, text format with six-hourly information on the location, maximum winds, central pressure, and (beginning in 2004)
size of all known tropical cyclones and subtropical cyclones. <br />
The Pacific dataset was provided on 23 April 2020 to include the best track for 2018's Walaka in the Central Pacific. The best track provided in this database for the Erick (EP062019) in the Central Pacific Hurricane Center's area of responsibility (between 140 and 180W longitude) is an operational estimate and has not yet been post-storm analyzed.
The final best track for this system will be updated when it becomes available.<br />
Atlantic Data: https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2019-052520.txt<br />
Pacific Data: https://www.nhc.noaa.gov/data/hurdat/hurdat2-nepac-1949-2019-042320.txt<br />

The status of system labels we are looking at are:<br />
HU – Tropical cyclone of hurricane intensity (> 64 knots)<br />
TS – Tropical cyclone of tropical storm intensity (34-63 knots)<br />
TD – Tropical cyclone of tropical depression intensity (< 34 knots)<br />
EX – Extratropical cyclone (of any intensity)<br />

source: https://www.nhc.noaa.gov/data/


## Machine Learning Model
We trained the data using a Decision Tree Regressor from the Scikitlearn library. It was trained completely using the Atlantic HURDAT Dataset and had an accuracy of ~86%.
When tested with previously unseen data of the Pacific HURDAT dataset, it reached near 90% Accuracy. This proves that if given data from various sources, it should have a high prediction capability. <br />
The Model takes windspeeds, maximum air pressure and maximum sustained wind knots as features and predicts the status of the storm based on NOAA classifications.

## Web Application 
https://project-zeus-space-apps.herokuapp.com/
The web application is made using Streamlit.  You can press the **Let us analyze button** to view
the data in more detail. You can press the **Let us look at the data** to view either the Pacific or Atlantic Dataset and accuracy our model predicts at. <br />
The main feature of the website is the **Try it yourself!** button which takes a random array form teh dataet and shows you the attached label as well as the label predicted by our model.<br />
###### Disclaimer: No model is perfect, hence the model CAN deviate from the actual value very occasionally. Please click the button again and compare values again if it happens 

## Future applications
We hope to have an upload tab where researchers can upload their data and make accurrate predictions using our model. In addition we hope to improve our accuracy to a very high degree at a later stage using greater amounts of data
and better algorithms.


## Creators
This web app is created by Ojas Sharma, Parth Modi and Raihan Abdul Vaheed. We are First year Honors Computer Science Students at the University of Waterloo during the inital stage of the app (Oct 2020)
