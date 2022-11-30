import streamlit as st
st.title("Greater of Three Numbers:")

a=st.number_input("Enter First Number:")
b=st.number_input("Enter Second Number:")
c=st.number_input("Enter Third Number:")

if (a>b) and (a>c):
  st.write("a is greater")
elif (b>a) and (b>c):
  st.write("b is greater")
else:
  st.write("c is greater")