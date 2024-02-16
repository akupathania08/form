import streamlit as st
x=st.radio('are you a student',options =['yes','no'])
if x=='yes':
    st.write('yes i am a student')
else:
    st.write('no,i am not a student')
c1,c2,c3=st.columns(3)
with c1:
    st.write('India')
with c2:
    st.write('Delhi')
with c3:
    st.write('Noida')
with st.form('form'):
    st.write('Please fill the form')
    name=st.text_input('Name')
    college_name=st.text_input('Your college name')
    Percentage=st.number_input('Your Percentage')
    Working=st.checkbox('Are you working')

    submitted=st.form_submit_button('Submit')
    st.write('name:',name)
    st.write('college_name:',college_name)
    st.write('Percentage:',Percentage)
    st.write('Are you working',Working)        
