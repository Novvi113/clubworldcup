import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Новая статистика", layout="wide")

st.title("📊 Дополнительная статистика")
st.write("Здесь будет твоя новая категория данных!")

# Пример простого графика для проверки plotly
df = pd.DataFrame({
    "Игрок": ["Messi", "Ronaldo", "Neymar"],
    "Голы": [20, 18, 15]
})

fig = px.bar(df, x="Игрок", y="Голы", title="Тестовый график Plotly")
st.plotly_chart(fig)