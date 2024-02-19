import streamlit as st
st.title('LOVE TEST')
x=st.text_input('enter name')
if x=='alka':
   st.success(f'you are passed')
   st.balloons()
   st.write("🎈❤️") 
else:
   st.error(f'you dont love her')
   st.write("😞")   

