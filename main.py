import streamlit as st
st.title("Greater of Three Numbers:")

a=st.number_input("Enter First Number:")
b=st.number_input("Enter Second Number:")
c=st.number_input("Enter Third Number:")

if (a>b) and (a>c):
  st.write("a is greater")  
elif (b>a) and (b>c):
  st.write("b is greater")
elif (b==a) and (b>c):
  st.write("a,b is greater")
elif (b==c) and (c>a):
  st.write("b,c is greater")
elif (a==c) and (a>b):
  st.write("a,c is greater")
elif (a==b) and (b==c) and (a==c):
  st.write("a,b,c is equal")
else:
  st.write("c is greater")
