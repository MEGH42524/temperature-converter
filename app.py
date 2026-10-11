
import streamlit as st

st.title("🌡️ Temperature Converter")
st.write("Convert Celsius, Fahrenheit, and Kelvin easily!")

# Enter temperature
temperature = st.number_input(
    "Enter Temperature",
    value=25.0
)

# Select conversion units
from_unit = st.selectbox(
    "Convert From",
    ["Celsius", "Fahrenheit", "Kelvin"]
)

to_unit = st.selectbox(
    "Convert To",
    ["Celsius", "Fahrenheit", "Kelvin"]
)

if st.button("Convert Temperature"):

    # Convert input to Celsius first
    if from_unit == "Celsius":
        celsius = temperature
    elif from_unit == "Fahrenheit":
        celsius = (temperature - 32) * 5 / 9
    else:
        celsius = temperature - 273.15

    # Convert Celsius to target unit
    if to_unit == "Celsius":
        result = celsius
    elif to_unit == "Fahrenheit":
        result = (celsius * 9 / 5) + 32
    else:
        result = celsius + 273.15

    # Validate absolute zero
    if celsius < -273.15:
        st.error("Temperature cannot be below absolute zero!")
    else:
        st.success(
            f"{temperature}° {from_unit} = "
            f"{result:.2f}° {to_unit}"
        )