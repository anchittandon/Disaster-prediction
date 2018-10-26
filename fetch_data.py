import pandas as pd
import numpy as np
import flood_predictor as fp
import geocoder
import time

tables = pd.read_html("http://hydro.imd.gov.in/hydrometweb/(S(ht2dew45izstmbyyphslh455))/landing.aspx#")
states={'ANDAMAN & NICOBAR ISLANDS': 0, 'ARUNACHAL PRADESH': 1, 'ASSAM':2, 'MEGHALAYA': 2, 'BIHAR': 3, 'CHHATTISGARH': 4, 'ANDHRA PRADESH': 5, 
'KARNATAKA': 6, 'MADHYA PRADESH': 7, 'RAJASTHAN': 8, 'UTTAR PRADESH': 9, 'WEST BENGAL': 10, 'GUJARAT': 11, 
'HARYANA': 12,'DELHI': 12, 'HIMACHAL PRADESH': 13, 'JAMMU & KASHMIR': 14, 'JHARKHAND': 15, 'KERALA': 16, 'GOA': 17, 
'LAKSHADWEEP': 18, 'MADHYA MAHARASHTRA': 19, 'MATATHWADA': 20, 'NAGALAND':21, 'MANIPUR':21, 'MIZORAM':21, 'TRIPURA': 21, 'KARNATAKA': 22, 
'ODISSA': 23, 'PUNJAB': 24, 'RAYALSEEMA': 25, 'SAURASHTRA & KUTCH': 26, 'SOUTH INTERIOR KARNATAKA': 27, 'SUB HIMALAYAN WEST BENGAL & SIKKIM': 28, 
'TAMIL NADU': 29, 'TELANGANA': 30, 'UTTARAKHAND': 31, 'VIDARBHA': 32, 'WEST MADHYA PRADESH': 33, 'WEST RAJASTHAN': 34, 'WEST UTTAR PRADESH': 35}

tables=np.array(tables[4])
tables=np.array(tables[1:])
# print(tables)
def get_location():
    g = geocoder.ip('me')
    state_cur=g.state
    # print(g.state)
    state_cur=state_cur.upper()
    # print(str(state_cur))
    return state_cur
def get_rain():
    a=max(tables[tables[:,0]==get_location()][:,2].flatten())
    return a
# print(max(tables[tables[:,0]==get_location()][:,2].flatten()))
#print(get_location)
def predict():
    # print(states[get_location()])
    # print(get_rain())
    return fp.prediction1([[states[get_location()],get_rain()]])
def alert():
    var=predict()
    if(var==0):
        return "You are completely safe"
    elif(var==1):
        return "Moderate rain falling, keep your umbrella with you, but you're safe"
    elif(var==2):
        return "Heavy raining, chances of floods increasing. Please take necessary precations "
    else:
        return "Flood chances are at peak.Stay in your house"
        

# print(len(sorted(set(tables[1:,0]))))