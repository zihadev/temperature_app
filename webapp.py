# coding=utf-8
# pimport streamlit as st
import plotly.express as px
import pandas

df = pandas.read_csv("data.txt")

figure = px.line(x=df["date"], y=df["temperature"],
                 labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)

if __name__ == "__main__":
    pass
