import streamlit as st 

st.title("Simaple WebApp for calculation:")

n = st.number_input("Enter an integer: eg: 5")

st.write(f"Square of {n}: {n**2}")
st.write(f"Cuve of {n}: {n**3}")
st.write(f"five of {n}: {n**5}")


