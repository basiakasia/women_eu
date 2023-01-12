import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Seats held by women in national parliaments and governments %",
	page_icon=":bar_chart:",
	layout="wide"
	)

df = pd.read_csv('static/women_EU2.csv', sep = ',')


# ---- SIDEBAR ----

st.sidebar.header("Please filter here:")

selected_country = st.sidebar.selectbox(
	"Select the Country:",
	options=df.country.unique(),
	)

year_max = df['year'].max()
year_min = df['year'].min()

selected_years = st.sidebar.select_slider(
	"Select years:",
	options=df.year.unique(),
	value=(year_max,year_min)
	)

selected_year_min, selected_year_max = list(selected_years)[0], list(selected_years)[1]

# ---- MAINPAGE ----

st.title(":bar_chart: Seats held by women in national parliaments and governments %")
st.markdown("---")

# ---- SELECTED DATA ----

mask = df['year'].between(selected_year_min, selected_year_max)
country_data = df[mask & (df['country'] == selected_country)]
print(country_data['GOV'])
print(country_data['PARL'])
print(country_data)

st.dataframe(country_data, width=400)

# ---- COLUMNS -----

col1, col2 = st.columns(2)

# ---- CHARTS ----

# goverment

with col1:

	plt.style.use('ggplot')
	default_x_ticks = list(range(len(country_data['year']))) # create an index for each tick position
	fig, ax1 = plt.subplots()
	plt.axis([None,None,0, 100]) # plt size (0, 100) to show the percentage properly

	ax1.bar(default_x_ticks, country_data['GOV'])
	plt.title("Goverment", fontsize=10)
	plt.xticks(default_x_ticks, country_data['year'], rotation='vertical') # replacing indexes with years 
	st.pyplot(fig)

# parlament

with col2:
	plt.style.use('ggplot')
	default_x_ticks = list(range(len(country_data['year']))) # # create an index for each tick position
	fig, ax2 = plt.subplots()
	plt.axis([None,None,0, 100]) # plt size (0, 100) to show the percentage properly

	ax2.bar(default_x_ticks, country_data['PARL'], color='dodgerblue') 
	plt.title("Parlament", fontsize=10)
	plt.xticks(default_x_ticks, country_data['year'], rotation='vertical') # replacing indexes with years
	st.pyplot(fig)

