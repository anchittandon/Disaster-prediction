# Disaster-prediction
# Abstract.
In this Project we aim to predict any potential flood or drought chances, that might arise due to the rainfall happening at a particular place in india. Flood and Drought are two related calamities, though seem unrelated at first sight but are highly affected and decided by the amount of rainfall at a place. The rainfall which will be mesaured in mm has a lot of attributes associated with it.For an instance The rainfall could be the daily rainfall, monthly rainfall, seasonal rainfall or the annual rainfall, each representing and affecting various biological events.



# Need.
As it is quite clear that flood and drought are indeed important and devastating calamities which affects a large population of a demographic every year. So in this situation, if can make a system, or for large user, an app, which analyses the rainfall of the region a person is living in, and can raise alarm for the person if there might can arise a situation of flood, he/ she can take useful measures to ensure least damage to him and his property. Same thing could be used by the Indian Meteorological Department of India to plan and process these events and make sure less people are affected by the calamity.


# Process
So how are we going to do it? We are going to use machine learning, deep learning and statistical learning theory to train our model to predict the calamity. We have got our data from Indian Govt Website (https://data.gov.in/resources/district-rainfall-normal-mm-monthly-seasonal-and-annual-data-period-1951-2000), it contains the monthly, annual and seasonal rainfall data of each state and their major district of India. The data is 50 years, from 1951-2000. Also we are getting instantaneous data of rainfall (visually data after each day) from Indian Meteorological Department (http://hydro.imd.gov.in/hydrometweb/(S(4py24b55cjhnute4evewhr55))/landing.aspx).The data looks like this.

Phase 1:

Simple Prediction using the above stated model. Independent analysis of the data( independent in the sense that rainfall in Uttrakhand will not have any effect on the people living in Delhi)

Phase 2:

Correlational Analysis:
It is quite possible that a heavy rainfall in North can bring flood in all the areas which are in the vicinity of that area, and it is also important to analyse that part. So after making the basic model, we'll try to incorporate this aspect also in our model.


# Methodology
We will decide the class labels or the threshold for flood or drought from previous flood or drought event to make accurate predictions. We are going to use parametric, non-parametric, supervised and non supervised learning method to make our model more flexible and robust.

After that for # UI experience we are going to make an Android App for the same. The android app will the geolocation API of android to detect the location of the user and will fetch the rainfall from Meteorogical Department, then on the back-end we will run the algorithm to predict the chances of any calamity in the area and will notify the user simultaneously in Real Time.


# Summary
1.Training the model on previous data.

2.Taking USER's Location from the APP.

3.Running the algo at back-end.

4.Predicting the chances of flood.

5.Notifying the User.


# Conclusion
We believe that this system is going to help a lot of people as well as the govt in predicting the disaster and also in reducing its impact on general people. Every year people won't have to suffer the same, and hence we'll be able to make society a little better with this.


