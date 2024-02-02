import pandas as pd
import streamlit as st
import joblib

#modelo = joblib.load('modelo.joblib')


numerical_x = {
    "host_listings_count": 0,
    "latitude": 0,
    "longitude": 0,
    "accommodates": 0,
    "bathrooms": 0,
    "bedrooms": 0,
    "beds": 0,
    "extra_people": 0,
    "minimum_nights": 0,
    "n_amenities": 0,    
}

tf_x = {
    "host_is_superhost_f": 0, 
    "host_is_superhost_t": 0,
    "instant_bookable_f": 0,
    "instant_bookable_t": 0,
    "property_type_Apartment": 0,
    "property_type_Bed and breakfast": 0,
    "property_type_Condominium": 0,
    "property_type_House": 0,
    "property_type_Loft": 0,
    "property_type_Other": 0,
    "room_type_Entire home/apt": 0,
    "room_type_Private room": 0,
    "bed_type_Others Beds": 0,    
    "bed_type_Real Bed": 0,
    "cancellation_policy_flexible": 0,    
    "cancellation_policy_moderate": 0,
    "cancellation_policy_strict_14_with_grace_period": 0
}     
        
      
for item in numerical_x:
    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step = 0.00001, format = '%.5f', value = 0.00000)
        
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step = 0.01, format = '%.2f', value = 0.00)
         
    else:
        valor = st.number_input(f'{item}', value = 0, format = '%d', step = 1)        

    numerical_x[item] = valor

for item in tf_x:
    valor = st.selectbox(f'{item}', ('True', 'False'))    
    if valor == 'True':
        tf_x[item] = 1
    else:
        tf_x[item] = 0


button = st.button('Prever preço')
dicts = {}
if button:
    dicts.update(numerical_x)
    dicts.update(tf_x)
    df = pd.DataFrame(dicts, index=[0])
    modelo = joblib.load('model_rf.pkl')
    price = modelo.predict(df)
    st.write(f'Preço estimado: {round(price[0], 2)}')