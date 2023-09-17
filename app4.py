
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

medals =  pd.read_csv('data.csv')

fig, ax = plt.subplots()
medals.plot.bar(x='Country', y = ['Gold','Silver','Bronze'],ax=ax)
st.pyplot(fig)