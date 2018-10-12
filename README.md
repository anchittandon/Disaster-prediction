# Disaster-prediction
# Abstract.
In this Project we aim to predict any potential flood or drought chances, that might arise due to the rainfall happening at a particular place in india. Flood and Drought are two related calamities, though seem unrelated at first sight but are highly affected and decided by the amount of rainfall at a place. The rainfall which will be mesaured in mm has a lot of attributes associated with it.For an instance The rainfall could be the daily rainfall, monthly rainfall, seasonal rainfall or the annual rainfall, each representing and affecting various biological events.
# Need.
As it is quite clear that flood and drought are indeed important and devastating calamities which affects a large population of a demographic every year. So in this situation, if can make a system, or for large user, an app, which analyses the rainfall of the region a person is living in, and can raise alarm for the person if there might can arise a situation of flood, he/ she can take useful measures to ensure least damage to him and his property. Same thing could be used by the Indian Meteorological Department of India to plan and process these events and make sure less people are affected by the calamity.
# Process
So how are we going to do it? We are going to use machine learning, deep learning and statistical learning theory to train our model to predict the calamity. We have got our data from Indian Govt Website (https://data.gov.in/resources/district-rainfall-normal-mm-monthly-seasonal-and-annual-data-period-1951-2000), it contains the monthly, annual and seasonal rainfall data of each state and their major district of India. The data is 50 years, from 1951-2000. Also we are getting instantaneous data of rainfall (visually data after each day) from Indian Meteorological Department (http://hydro.imd.gov.in/hydrometweb/(S(4py24b55cjhnute4evewhr55))/landing.aspx) The data looks like this.
STATE/UT	DISTRICT	JAN	FEB	MAR	APR	MAY	JUN	JUL	AUG	SEP	OCT	NOV	DEC	ANNUAL	JAN+FEB	MAM	JJAS	OND
ANDAMAN And NICOBAR ISLANDS	NICOBAR	107.3	57.9	65.2	117	358.5	295.5	285	271.9	354.8	326	315.2	250.9	2805.2	165.2	540.7	1207.2	892.1
ANDAMAN And NICOBAR ISLANDS	SOUTH ANDAMAN	43.7	26	18.6	90.5	374.4	457.2	421.3	423.1	455.6	301.2	275.8	128.3	3015.7	69.7	483.5	1757.2	705.3
ANDAMAN And NICOBAR ISLANDS	N & M ANDAMAN	32.7	15.9	8.6	53.4	343.6	503.3	465.4	460.9	454.8	276.1	198.6	100	2913.3	48.6	405.6	1884.4	574.7
ARUNACHAL PRADESH	LOHIT	42.2	80.8	176.4	358.5	306.4	447	660.1	427.8	313.6	167.1	34.1	29.8	3043.8	123	841.3	1848.5	231
ARUNACHAL PRADESH	EAST SIANG	33.3	79.5	105.9	216.5	323	738.3	990.9	711.2	568	206.9	29.5	31.7	4034.7	112.8	645.4	3008.4	268.1
ARUNACHAL PRADESH	SUBANSIRI F.D	28	48.3	85.3	101.5	140.5	228.4	217.4	182.8	159.8	75.9	20.9	11.6	1300.4	76.3	327.3	788.4	108.4
ARUNACHAL PRADESH	TIRAP	42.2	72.7	141	316.9	328.7	614.7	851.9	500.6	418.3	218.7	42.9	22.9	3571.5	114.9	786.6	2385.5	284.5
ARUNACHAL PRADESH	ANJAW (LOHIT)	42.2	80.8	176.4	358.5	306.4	447	660.1	427.8	313.6	167.1	34.1	29.8	3043.8	123	841.3	1848.5	231

