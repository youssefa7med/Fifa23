import streamlit as st
import pandas as pd
import numpy  as np
import plotly.express as px

import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Players",initial_sidebar_state = 'expanded')

st.markdown('<h1 style="text-align: center; color: #D8DACC; font-size: 40px; font-weight: bold;">Fifa 23 Analysis</h1>', unsafe_allow_html=True)

df = pd.read_csv("Fifa_23_clear.csv",index_col = "Unnamed: 0")
# st.image("nations.jpeg",width = 60, use_column_width = True)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

animation = load_lottieurl('https://lottie.host/ac702572-d14f-4b61-a49d-6bf94cda44f3/Xty5XVptrx.json')
st_lottie(animation,speed = .75,quality = 'high')

df.drop_duplicates(inplace = True)
def playerlocation(x):
    if x in ['ST', 'CF', 'LF', 'RF', 'RS', 'LS', 'RW', 'LW']:
        return 'Attacking'
    elif x in  ['RCM', 'LCM', 'CM', 'RDM', 'CDM', 'LDM', 'CAM', 'RAM', 'LAM', 'LM', 'RM']:
        return 'Midfielder'
    elif x in ['RCB', 'CB', 'LCB', 'LB', 'RWB', 'LWB']:
        return 'Defending'
    else:
        return 'Goalkeeper'
df['Player Main Position'] = df.apply(lambda x : playerlocation(x['Best Position']),axis=1)
num_cols = df.select_dtypes(include='number').columns
cat_cols = df.select_dtypes(include='O').columns
def change_illegal_nations(x):
    if x == '-':
        x = 'Stateless'
    return x
df['National Team Name'] = df['National Team Name'].apply(lambda x :change_illegal_nations(x))

# first row ------------------------------------------------------------------
st.divider()
selected = st.selectbox('Select a Column to filter by ',num_cols,help ='Get Max , Min and Avg' )
st.write('\n\n\n')

top = df.groupby(['National Team Name','Nationality','National Team Image Link'])[selected].mean().sort_values().reset_index()

col1,col2,col3 = st.columns(3)
# card1 -----------------------------------------------------------
card1 = col1.container(border = True)
card1.metric(label=f'Min {selected}',value = top.nsmallest(1,selected)[selected].values[0].round(2),delta = (top.nsmallest(1,selected)[selected].values[0].round(2)-top[selected].mean()).round(2))
try :
    card_min_img = top.nsmallest(1,selected)['National Team Image Link'][0]
    card1.image(card_min_img)

except :
    card1.write('No Data To Show')

card_min_name_nat = top.nsmallest(1,selected)['Nationality'].values[0]
card1.write(f'Min mean of {selected} in {card_min_name_nat}')

# card2 -----------------------------------------------------------
card2 = col2.container(border = True)
card2.write('\n\n\n\n')
card2.write('\n\n\n\n')
card2.write('\n\n\n\n')
card2.write('\n\n\n\n')
card2.metric(label=f'Avg {selected}',value = top[selected].mean().round(2))
card2.write('\n\n\n\n')
card2.write('\n\n\n\n')
card2.write('\n\n\n\n')
card2.write('\n\n\n\n')

# card3 ------------------------------------------------------------
card3 = col3.container(border = True)
card3.metric(label=f'Max {selected}',value = top.nlargest(1,selected)[selected].values[0].round(2),delta = (top.nlargest(1,selected)[selected].values[0]-top[selected].mean()).round(2))
try :
    card_max_img = top.nlargest(1,selected)['National Team Image Link'].values[0]
    card3.image(card_max_img)

except :
    card3.write('No Data To Show')

card_max_name_nat =  top.nlargest(1,selected)['Nationality'].values[0]
card3.write(f'Max mean of {selected} in {card_max_name_nat}')
#  ------------------------------------------------------------------
st.divider()
#
column1,column2 = st.columns([6,4])

column = column1.selectbox('Select a Numerical filter to apply ',num_cols)
number = column2.number_input('Enter the number of Nations to display.',min_value = 10, max_value = 100, step = 1,help='Count of nations do you want to display in histogram')
agg_selected = column1.radio('Select aggregation function do  you want to apply !', ['mean','sum','count'],horizontal = True)
high_low = column2.radio('Select Max or Min nation', ['Max','Min'],horizontal = True,help = 'Default value is Max')
if high_low =='Max':
    top_nations = df.groupby(['National Team Name','National Team Image Link'])[column].agg(agg_selected).reset_index().nlargest(number,column).reset_index()
    fig = px.histogram(top_nations,y = column,x = "National Team Name",color = 'National Team Name',text_auto = True,title = f'Histogram of Top{number} Nations in {agg_selected} of {column}',template ='simple_white',color_discrete_sequence=px.colors.sequential.RdBu )
    st.plotly_chart(fig)

else:
    top_nations = df.groupby('National Team Name')[column].agg(agg_selected).reset_index().nsmallest(number,column).reset_index()
    fig = px.histogram(top_nations,y = column,x = "National Team Name",color = 'National Team Name',text_auto = True,title = f'Histogram of Top{number} Nations in {agg_selected} of {column}',template ='simple_white',color_discrete_sequence=px.colors.sequential.RdBu )
    st.plotly_chart(fig)
# --------------------------------------------------------------------------------
st.divider()

nations = ['Argentina', 'France', 'Poland', 'Belgium', 'Germany',
    'Portugal', 'Netherlands', 'England', 'Norway', 'Italy', 'Croatia',
    'Spain', 'Scotland', 'Austria', 'Czech Republic', 'Hungary',
    'Ghana', 'Morocco', 'Canada', 'Denmark', 'Finland',
    'Ukraine', 'Mexico', 'United States', 'Sweden', 'Wales',
    'Northern Ireland', 'Australia', 'Republic of Ireland', 'Qatar',
    'New Zealand', 'Romania', 'China PR', 'Iceland']

n1,n2 = st.columns([6,4])
nation = n1.selectbox('Select Nation to filter by :',nations)
numric = n2.selectbox('Select Numeric Filter',num_cols)
min_max = n1.radio('Select Max or Min filter ', ['Max','Min'],horizontal = True,help = 'Default value is Max')
top_bottom = 'Top'

if min_max == 'Max':
    top_nations = df[df['National Team Name'] == nation].sort_values(by = numric,ascending=False).head(5)

else:
    top_nations = df[df['National Team Name'] == nation].sort_values(by = numric,ascending=True).head(5)
    top_bottom ='Bottom'

st.subheader(f'{top_bottom} 5 Players in {nation} per {numric}')

col1,col2,col3,col4,col5= st.columns(5)
card1 = col1.container(border = True)
card1_img = (top_nations['Image Link'].reset_index()['Image Link'][0])
card1.image(card1_img)
card1_name = (top_nations['Known As'].reset_index()['Known As'][0])
card1.write(card1_name)

card2 = col2.container(border = True)
card2_img = (top_nations['Image Link'].reset_index()['Image Link'][1])
card2.image(card2_img)
card2_name = (top_nations['Known As'].reset_index()['Known As'][1])
card2.write(card2_name)

card3 = col3.container(border = True)
card3_img = (top_nations['Image Link'].reset_index()['Image Link'][2])
card3.image(card3_img)
card3_name = (top_nations['Known As'].reset_index()['Known As'][2])
card3.write(card3_name)

card4 = col4.container(border = True)
card4_img = (top_nations['Image Link'].reset_index()['Image Link'][3])
card4.image(card4_img)
card4_name = (top_nations['Known As'].reset_index()['Known As'][3])
card4.write(card4_name)

card5 = col5.container(border = True)
card5_img = (top_nations['Image Link'].reset_index()['Image Link'][4])
card5.image(card5_img)
card5_name = (top_nations['Known As'].reset_index()['Known As'][4])
card5.write(card5_name)

if st.checkbox('Show DataFrame',help='Show Data frame about the selected Nation') :
    st.dataframe(df[df['National Team Name']==nation])


# ------------------------------------------------------------------------
st.divider()
c1,c2 = st.columns(2)

column_num = c1.selectbox('Select a Numerical Feature to filter by',num_cols)
aggregation_selected = c1.radio('Select aggregation function do  you want to apply !!', ['mean','sum'])
column_cat = c2.selectbox('Select a Categorical Feature to filter by',cat_cols)

Top_nat = df.groupby('National Team Name')[column_num].agg(aggregation_selected).reset_index().sort_values(by=column_num,ascending=False).head(10)
fig = px.histogram(df.groupby([column_cat,Top_nat['National Team Name']])[column_num].agg(aggregation_selected).reset_index()
        ,x=column_cat,y=column_num,template='simple_white',text_auto=True,color='National Team Name',color_discrete_sequence=px.colors.sequential.RdBu
            ,title = f'The histogram about {aggregation_selected} of {column_num} in Top {10} Nation per {column_cat}',barmode='group')

st.plotly_chart(fig)


