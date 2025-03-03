import streamlit as st

def distance_converter(from_unit,to_unit,value):
    units={
        "Meters":1,
        "Kilometer":1000,
        "Feet":0.3048,
        "Miles":1609.34
    }
    result=value *units[from_unit]/ units[to_unit]
    return result

def Temperature_converter(from_unit,to_unit,value):
    if from_unit =="Celsius" and to_unit =="fahrenheit":
        result=(value*9/5)+32
    elif from_unit =="Celsius" and to_unit =="fahrenheit":
        result=(value - 32)*9/5
    else :
        result=value
        return result
    
def Weight_converter(from_unit,to_unit,value):
    units={
        "Kilograms":1,
        "grams":0.001,
        "pounds":0.453592
    }
    result=value *units[from_unit]/ units[to_unit]
    return result

    
def pressure_converter(from_unit,to_unit,value):
    units={
        "Kilopascals":1000,
        "Pascals":1,
        "Bar":100000
    }
    result=value *units[from_unit]/ units[to_unit]
    return result

st.title("Unit Converter")
category=st.selectbox("Select Category",["Distance","Temperature","Weight","Pressure"])
if category == "Distance":
    from_unit= st.selectbox("From",["Meters","Kilometer","Feet","Miles"])
    to_unit=st.selectbox("To",["Meters","Kilometer","Feet","Miles"])
    value=st.number_input("Enter value")
    if st.button("Convert"):
       result= distance_converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} ={result:.3f} {to_unit}")

elif category == "Temperature":
    from_unit= st.selectbox("From",["Celsius","fahrenheit"])
    to_unit=st.selectbox("To",["Celsius","fahrenheit"])
    value=st.number_input("Enter value")
    if st.button("Convert"):
       result= Temperature_converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} ={result:.3f} {to_unit}")       

elif category == "Weight":
    from_unit= st.selectbox("From",["Kilograms","grams","pounds"])
    to_unit=st.selectbox("To",["Kilograms","grams","pounds"])
    value=st.number_input("Enter value")
    if st.button("Convert"):
       result= Weight_converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} ={result:.3f} {to_unit}")             


elif category == "Pressure":
    from_unit= st.selectbox("From",["Kilopascals","Pascals","Bar"])
    to_unit=st.selectbox("To",["Kilopascals","Pascals","Bar"])
    value=st.number_input("Enter value")
    if st.button("Convert"):
       result= pressure_converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} ={result:.3f} {to_unit}")             
