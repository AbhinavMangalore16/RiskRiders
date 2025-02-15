import streamlit as st 
import pandas as pd
import pandas_profiling 

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("credit_card_transactions-ibm_v2.csv")
pr = df.profile_report()

st_profile_report(pr)