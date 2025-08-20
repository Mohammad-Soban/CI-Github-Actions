import streamlit as st

st.title("POWER and SQRT Calculator")
st.write("Please enter a number:")
n = st.number_input("Number", value=1, step=1)

square = n ** 2
cube = n ** 3
sqrt = n ** 0.5

# Button for getting the square
if st.button("Get Square"):
    st.write("Square: ", square)

if st.button("Get Cube"):
    st.write("Cube: ", cube)

if st.button("Get Square Root"):
    st.write("Square Root: ", sqrt)

