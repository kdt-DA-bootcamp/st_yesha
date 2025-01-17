import streamlit as st
st.title('Deploye App')
st.write('MyFirstDeployApp')

import os 
key = os.environ.get('MY_SECRET',"NOT SET YET")
st.write(f'Sever Key : {key}')