import streamlit as st
from utils.dashboard import heatmap_geral, scatterplot_profissao_stress

st.write("Dashboard")
heatmap_geral()

scatterplot_profissao_stress()
