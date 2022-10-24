import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('World Cities')

df = pd.read_csv('worldcities.csv')

# show the population
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()   #先按照country分类，再把相同country的人口加在一起，画成图
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)

# add a slider
pop_slider = st.sidebar.slider('Choose Population', 0.0, 30.0, 20.0)  # 把slider弄在侧面

df = df[df.population >= pop_slider]  # filter dataframe

# add a multi slider
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options
     df.capital.unique())  # defaults
#capital_filter is a list

# filter by capital
df = df[df.capital.isin(capital_filter)]

# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

#filter  by country name
if country_filter!='ALL':
    df = df[df.country == country_filter]

# show the map
st.map(df)

# show df
st.write(df)