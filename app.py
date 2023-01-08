import streamlit as st
import pickle

st.title('Online Payments Fraud Deduction')
model=pickle.load(open('model.pkl','rb'))

col1,col2=st.columns(2)
type=col1.number_input('Enter Type')
amount=col2.number_input('Enter Amount')
oldbalance=col1.number_input('Enter Old Balance')
newbalance=col2.number_input('Enter New Balance')

if st.button('Predict'):
    data=[[type,amount,oldbalance,newbalance]]
    result=model.predict(data)[0]
    st.success(result)

