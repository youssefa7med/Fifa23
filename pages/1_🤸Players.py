import streamlit as st
import pandas as pd
import numpy  as np
import plotly.express as px

import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Players",initial_sidebar_state = 'expanded')

st.markdown('<h1 style="text-align: center; color: #D8DACC; font-size: 40px; font-weight: bold;">Fifa 23 Analysis</h1>', unsafe_allow_html=True)

df = pd.read_csv("Fifa_23.csv")
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

animation = load_lottieurl('https://lottie.host/c64c8726-95fb-43ea-b29b-76f0e734f01d/AHXFno3qcT.json')
st_lottie(animation,quality = 'high',speed = .80)
# st.image("players.jpeg",width = 60, use_column_width = True)
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

#  ------------------------------------------------------------------
st.divider()

tab1,tab2 = st.tabs(['📊 Player Analysis',':frame_with_picture: Fifa Card'])
with tab1:
    selected = st.selectbox('Select a Column to filter by ',num_cols,help ='Get Max , Min and Avg' )
    st.write('\n\n\n')


    col1,col2,col3 = st.columns(3)

    card1 = col1.container(border = True)
    card1.metric(label=f'Min {selected}',value = df[selected].min(),delta = (df[selected].min()-df[selected].mean()).round(2))
    try :
        card_min_img = df['Image Link'].loc[df[selected]==df[selected].min()].reset_index().head(1)['Image Link'][0]
        card1.image(card_min_img)
        card_min_name = df['Known As'].loc[df[selected]==df[selected].min()].reset_index().head(1)['Known As'][0]
        card1.write(card_min_name)
    except :
        card1.write('No Data To Show')


    card2 = col2.container(border = True)
    card2.metric(label=f'Avg {selected}',value = df[selected].mean().round(0))
    card2.write('\n\n\n\n')
    try :
        card_avg_img = df['Image Link'].loc[df[selected]==df[selected].median()].reset_index().head(1)['Image Link'][0]
        card2.image(card_avg_img)
        card_avg_name = df['Known As'].loc[df[selected]==df[selected].median()].reset_index().head(1)['Known As'][0]
        card2.write(card_avg_name)
    except :
        card2.write('No Data To Show')

    card3 = col3.container(border = True)
    card3.metric(label=f'Max {selected}',value = df[selected].max(),delta = (df[selected].max()-df[selected].mean()).round(2))
    try :
        card_max_img = df['Image Link'].loc[df[selected]==df[selected].max()].reset_index().head(1)['Image Link'][0]
        card3.image(card_max_img)
        card_max_name = df['Known As'].loc[df[selected]==df[selected].max()].reset_index().head(1)['Known As'][0]
        card3.write(card_max_name)
    except :
        card3.write('No Data To Show')

    st.divider()

    col1,col2 = st.columns(2)
    with col1:
        option = st.selectbox('Select a Position to filter by ',['ST Rating', 'LW Rating', 'LF Rating', 'CF Rating', 'RF Rating','RW Rating', 'CAM Rating', 'LM Rating', 'CM Rating', 'RM Rating','LWB Rating', 'CDM Rating', 'RWB Rating', 'LB Rating', 'CB Rating','RB Rating', 'GK Rating'],help = 'Position Rating')

    with col2:
        number = st.number_input('Enter the number of players to display .',min_value = 5, max_value = 100, step = 1,help='Count of player to display')

    high_low = st.radio('Select High or Low',['High','Low'],horizontal = True,help = 'Get Max or Min players')

    if high_low == 'High':
        st.dataframe(df.sort_values(by =option,ascending=False).head(number).reset_index())
    else:
        st.dataframe(df.sort_values(by =option,ascending=True).head(number).reset_index())

    if st.checkbox('Show Images',help = 'Get images of 5  highest/ lowest players'):
        col1,col2,col3,col4,col5= st.columns(5)
        if high_low == 'High':
            card1 = col1.container(border = True)
            card1_img = (df.sort_values(by = option,ascending=False).head(5)['Image Link'].reset_index()['Image Link'][0])
            card1.image(card1_img)
            card1_name = (df.sort_values(by = option,ascending=False).head(5)['Known As'].reset_index()['Known As'][0])
            card1.write(card1_name)

            card2 = col2.container(border = True)
            card2_img = (df.sort_values(by = option,ascending=False).head(5)['Image Link'].reset_index()['Image Link'][1])
            card2.image(card2_img)
            card2_name = (df.sort_values(by = option,ascending=False).head(5)['Known As'].reset_index()['Known As'][1])
            card2.write(card2_name)

            card3 = col3.container(border = True)
            card3_img = (df.sort_values(by = option,ascending=False).head(5)['Image Link'].reset_index()['Image Link'][2])
            card3.image(card3_img)
            card3_name = (df.sort_values(by = option,ascending=False).head(5)['Known As'].reset_index()['Known As'][2])
            card3.write(card3_name)

            card4 = col4.container(border = True)
            card4_img = (df.sort_values(by = option,ascending=False).head(5)['Image Link'].reset_index()['Image Link'][3])
            card4.image(card4_img)
            card4_name = (df.sort_values(by = option,ascending=False).head(5)['Known As'].reset_index()['Known As'][3])
            card4.write(card4_name)

            card5 = col5.container(border = True)
            card5_img = (df.sort_values(by = option,ascending=False).head(5)['Image Link'].reset_index()['Image Link'][4])
            card5.image(card5_img)
            card5_name = (df.sort_values(by = option,ascending=False).head(5)['Known As'].reset_index()['Known As'][4])
            card5.write(card5_name)

        else:
            card1 = col1.container(border = True)
            card1_img = (df.sort_values(by = option,ascending=True).head(5)['Image Link'].reset_index()['Image Link'][0])
            card1.image(card1_img)
            card1_name = (df.sort_values(by = option,ascending=True).head(5)['Known As'].reset_index()['Known As'][0])
            card1.write(card1_name)

            card2 = col2.container(border = True)
            card2_img = (df.sort_values(by = option,ascending=True).head(5)['Image Link'].reset_index()['Image Link'][1])
            card2.image(card2_img)
            card2_name = (df.sort_values(by = option,ascending=True).head(5)['Known As'].reset_index()['Known As'][1])
            card2.write(card2_name)

            card3 = col3.container(border = True)
            card3_img = (df.sort_values(by = option,ascending=True).head(5)['Image Link'].reset_index()['Image Link'][2])
            card3.image(card3_img)
            card3_name = (df.sort_values(by = option,ascending=True).head(5)['Known As'].reset_index()['Known As'][2])
            card3.write(card3_name)

            card4 = col4.container(border = True)
            card4_img = (df.sort_values(by = option,ascending=True).head(5)['Image Link'].reset_index()['Image Link'][3])
            card4.image(card4_img)
            card4_name = (df.sort_values(by = option,ascending=True).head(5)['Known As'].reset_index()['Known As'][3])
            card4.write(card4_name)

            card5 = col5.container(border = True)
            card5_img = (df.sort_values(by = option,ascending=True).head(5)['Image Link'].reset_index()['Image Link'][4])
            card5.image(card5_img)
            card5_name = (df.sort_values(by = option,ascending=True).head(5)['Known As'].reset_index()['Known As'][4])
            card5.write(card5_name)

    if st.checkbox('Select by specific stats',False,help = 'Specific stats like(Long shots ,Pass accuracy,etc..)'):
        col1,col2 = st.columns(2)
        with col1:
            option = st.selectbox('Select column to filter by ',['Pace Total', 'Shooting Total',
            'Passing Total', 'Dribbling Total', 'Defending Total',
            'Physicality Total', 'Crossing', 'Finishing', 'Heading Accuracy',
            'Short Passing', 'Volleys', 'Dribbling', 'Curve', 'Freekick Accuracy',
            'LongPassing', 'BallControl', 'Acceleration', 'Sprint Speed', 'Agility',
            'Reactions', 'Balance', 'Shot Power', 'Jumping', 'Stamina', 'Strength',
            'Long Shots', 'Aggression', 'Interceptions', 'Positioning', 'Vision',
            'Penalties', 'Composure', 'Marking', 'Standing Tackle',
            'Sliding Tackle', 'Goalkeeper Diving', 'Goalkeeper Handling',
            ' GoalkeeperKicking', 'Goalkeeper Positioning', 'Goalkeeper Reflexes'])
        with col2:
            number = st.number_input('Enter the number of players to display.',min_value = 5, max_value = 100, step = 1,help='Count of player to display')

        high_or_low = st.radio('Select High or Low .',['High','Low'],horizontal = True,help = 'Get Max or Min players')

        if high_or_low == 'High':
            st.dataframe(df.sort_values(by =option,ascending=False).head(number).reset_index())
        else:
            st.dataframe(df.sort_values(by =option,ascending=True).head(number).reset_index())

        if st.checkbox('Show Images .',help = 'Get images of 5  highest/ lowest players'):
            col1,col2,col3,col4,col5= st.columns(5)
            if high_or_low == 'High':
                card1 = col1.container(border = True)
                card1_img = (df.sort_values(by = option,ascending=False).head(5)['Image Link'].reset_index()['Image Link'][0])
                card1.image(card1_img)
                card1_name = (df.sort_values(by = option,ascending=False).head(5)['Known As'].reset_index()['Known As'][0])
                card1.write(card1_name)

                card2 = col2.container(border = True)
                card2_img = (df.sort_values(by = option,ascending=False).head(5)['Image Link'].reset_index()['Image Link'][1])
                card2.image(card2_img)
                card2_name = (df.sort_values(by = option,ascending=False).head(5)['Known As'].reset_index()['Known As'][1])
                card2.write(card2_name)

                card3 = col3.container(border = True)
                card3_img = (df.sort_values(by = option,ascending=False).head(5)['Image Link'].reset_index()['Image Link'][2])
                card3.image(card3_img)
                card3_name = (df.sort_values(by = option,ascending=False).head(5)['Known As'].reset_index()['Known As'][2])
                card3.write(card3_name)

                card4 = col4.container(border = True)
                card4_img = (df.sort_values(by = option,ascending=False).head(5)['Image Link'].reset_index()['Image Link'][3])
                card4.image(card4_img)
                card4_name = (df.sort_values(by = option,ascending=False).head(5)['Known As'].reset_index()['Known As'][3])
                card4.write(card4_name)

                card5 = col5.container(border = True)
                card5_img = (df.sort_values(by = option,ascending=False).head(5)['Image Link'].reset_index()['Image Link'][4])
                card5.image(card5_img)
                card5_name = (df.sort_values(by = option,ascending=False).head(5)['Known As'].reset_index()['Known As'][4])
                card5.write(card5_name)

            elif high_or_low =='Low':
                card1 = col1.container(border = True)
                card1_img = (df.sort_values(by = option,ascending=True).head(5)['Image Link'].reset_index()['Image Link'][0])
                card1.image(card1_img)
                card1_name = (df.sort_values(by = option,ascending=True).head(5)['Known As'].reset_index()['Known As'][0])
                card1.write(card1_name)

                card2 = col2.container(border = True)
                card2_img = (df.sort_values(by = option,ascending=True).head(5)['Image Link'].reset_index()['Image Link'][1])
                card2.image(card2_img)
                card2_name = (df.sort_values(by = option,ascending=True).head(5)['Known As'].reset_index()['Known As'][1])
                card2.write(card2_name)

                card3 = col3.container(border = True)
                card3_img = (df.sort_values(by = option,ascending=True).head(5)['Image Link'].reset_index()['Image Link'][2])
                card3.image(card3_img)
                card3_name = (df.sort_values(by = option,ascending=True).head(5)['Known As'].reset_index()['Known As'][2])
                card3.write(card3_name)

                card4 = col4.container(border = True)
                card4_img = (df.sort_values(by = option,ascending=True).head(5)['Image Link'].reset_index()['Image Link'][3])
                card4.image(card4_img)
                card4_name = (df.sort_values(by = option,ascending=True).head(5)['Known As'].reset_index()['Known As'][3])
                card4.write(card4_name)

                card5 = col5.container(border = True)
                card5_img = (df.sort_values(by = option,ascending=True).head(5)['Image Link'].reset_index()['Image Link'][4])
                card5.image(card5_img)
                card5_name = (df.sort_values(by = option,ascending=True).head(5)['Known As'].reset_index()['Known As'][4])
                card5.write(card5_name)

    st.divider()

    option = st.radio('Select the type of column to visualization',['Numerical','Categorical'])


    if option == 'Numerical':
        selected = st.selectbox('Select a column to visualize numerical data about players',['Overall', 'Potential', 'Value(in Euro)', 'Age', 'Height(in cm)',
            'Weight(in kg)', 'TotalStats', 'BaseStats', 'Wage(in Euro)', 'Pace Total', 'Shooting Total',
            'Passing Total', 'Dribbling Total', 'Defending Total',
            'Physicality Total', 'Crossing', 'Finishing', 'Heading Accuracy',
            'Short Passing', 'Volleys', 'Dribbling', 'Curve', 'Freekick Accuracy',
            'LongPassing', 'BallControl', 'Acceleration', 'Sprint Speed', 'Agility',
            'Reactions', 'Balance', 'Shot Power', 'Jumping', 'Stamina', 'Strength',
            'Long Shots', 'Aggression', 'Interceptions', 'Positioning', 'Vision',
            'Penalties', 'Composure', 'Marking', 'Standing Tackle',
            'Sliding Tackle', 'Goalkeeper Diving', 'Goalkeeper Handling',
            ' GoalkeeperKicking', 'Goalkeeper Positioning', 'Goalkeeper Reflexes',
            'ST Rating', 'LW Rating', 'LF Rating', 'CF Rating', 'RF Rating',
            'RW Rating', 'CAM Rating', 'LM Rating', 'CM Rating', 'RM Rating',
            'LWB Rating', 'CDM Rating', 'RWB Rating', 'LB Rating', 'CB Rating',
            'RB Rating', 'GK Rating'
            ,'Release Clause'])
        # avg = df[selected].mean()
        fig = px.histogram(data_frame=df,x=selected,color = selected,template='simple_white',color_discrete_sequence=px.colors.sequential.RdBu,title = f'Numerical data about {selected}',text_auto = True)
        # fig.add_hline(y=avg ,annotation_text=f'Average {selected}: {avg.round(2)}')
        st.plotly_chart(fig)
    else:
        selected = st.selectbox('Select a column to visualize top 10 categorical data about players per overall',['Best Position','Attacking Work Rate', 'Defensive Work Rate', 'Preferred Foot','Week Foot','Skill Moves','International Reputation'],help = 'select one column')
        agg_selected = st.radio('Select aggregation function you want to apply !', ['count','mean','sum'])
        if agg_selected != 'count':
            fig = (px.bar(data_frame=df.groupby(selected)['Overall'].agg(agg_selected).reset_index().nlargest(10,'Overall')
            ,x=selected,y='Overall',template='simple_white',text_auto=True,color=selected,color_discrete_sequence=px.colors.sequential.RdBu
            ,title = f'The barplot about {agg_selected} of Overall per each {selected}'))
            st.plotly_chart(fig)
        else :
            column1,column2 = st.columns(2)
            with column1:
                fig = (px.scatter(df,y='Overall',x=selected,size='Overall',color='Overall',title=f'Scatter Chart about Overall and {selected}',template='simple_white',color_discrete_sequence=px.colors.sequential.RdBu))
                st.plotly_chart(fig)
            with column2:
                fig = (px.pie(df,values='Overall',names=selected,title=f'Pie Chart about {selected}',template='simple_white',color_discrete_sequence=px.colors.sequential.RdBu,hole = 0.34))
                st.plotly_chart(fig)

    st.divider()
with tab2:
    playername = st.selectbox('Select Your favourite Player',df['Known As'].unique(),help = 'select one player to display his information')

    player_img = df['Image Link'].loc[df['Known As'] == playername].reset_index()['Image Link'][0]
    nation_img = df['National Team Image Link'].loc[df['Known As'] == playername].reset_index()['National Team Image Link'][0]
    nation_name = df['Nationality'].loc[df['Known As'] == playername].reset_index()['Nationality'][0]
    player_name = df['Full Name'].loc[df['Known As'] == playername].reset_index()['Full Name'][0]
    team_name = df['Club Name'].loc[df['Known As'] == playername].reset_index()['Club Name'][0]
    overall = df['Overall'].loc[df['Known As'] == playername].reset_index()['Overall'][0]
    player_pace = df['Pace Total'].loc[df['Known As'] == playername].reset_index()['Pace Total'][0]
    player_shooting = df['Shooting Total'].loc[df['Known As'] == playername].reset_index()['Shooting Total'][0]
    player_passing = df['Passing Total'].loc[df['Known As'] == playername].reset_index()['Passing Total'][0]
    player_dribbling = df['Dribbling Total'].loc[df['Known As'] == playername].reset_index()['Dribbling Total'][0]
    player_defending =  df['Defending Total'].loc[df['Known As'] == playername].reset_index()['Defending Total'][0]
    player_physicality = df['Physicality Total'].loc[df['Known As'] == playername].reset_index()['Physicality Total'][0]
    player_position = df['Best Position'].loc[df['Known As'] == playername].reset_index()['Best Position'][0]
    club_name = df['Club Name'].loc[df['Known As'] == playername].reset_index()['Club Name'][0]
    skill_moves = df['Skill Moves'].loc[df['Known As'] == playername].reset_index()['Skill Moves'][0]
    player_physicality = df['Physicality Total'].loc[df['Known As'] == playername].reset_index()['Physicality Total'][0]
    weak_foot = df['Weak Foot Rating'].loc[df['Known As'] == playername].reset_index()['Weak Foot Rating'][0]


    card_type = st.radio('Select the Type of Card ',['TOTY ICON','TOTY','TOTS','TOTW',"POTM",'Flashback','Gold Rare'],horizontal = True,help = 'Select the Type of Card')
    if card_type =='Gold Rare':
        background = 'https://pdf-service-static.s3.amazonaws.com/static/layout-images/cardstar/thumbnails/rare-gold-23.png'
        color_card_type = '#000000'

    elif card_type == 'POTM':
        background = 'https://creatufut.com/wp-content/uploads/2021/10/POTM_LALIGA_FIFA_22-496x800.png'
        color_card_type = '#FFFFFF'
        overall = overall + 1

    elif card_type == 'TOTS':
        background = 'https://creatufut.com/wp-content/uploads/2023/09/TOTS_FIFA-23.png'
        color_card_type = '#FF'
        overall = overall + 4

    elif card_type == 'TOTY':
        background = 'https://creatufut.com/wp-content/uploads/2023/09/TOTY_FIFA_23.png'
        color_card_type = '#FF'
        overall = overall + 5

    elif card_type == 'TOTY ICON':
        background = 'https://creatufut.com/wp-content/uploads/2023/09/TOTY-ICON_FIFA_23.png'
        color_card_type = '#000000'
        overall = overall + 6


    elif card_type == 'Flashback':
        background = 'https://creatufut.com/wp-content/uploads/2023/09/FLASHBACK_FIFA_23.png'
        color_card_type = '#FFFFFF'
        overall = overall + 3

    elif card_type == 'TOTW':
        background = 'https://creatufut.com/wp-content/uploads/2023/09/IF_FIFA_23.png'
        color_card_type = '#FFFFFF'
        overall = overall + 2

    if st.checkbox('Custom Card',help='Make Your Custom Player :smile:'):
        cs1,cs2 = st.columns(2)
        player_name = cs1.text_input('Enter Your Name :')
        club_name = cs1.text_input('Enter Your Favorite Club :')
        player_position = cs1.text_input('Enter Your Position :')
        nation_name = cs1.selectbox('Enter Your Nation :',df['National Team Name'].unique())
        nation_img = df[df['National Team Name']==nation_name]['National Team Image Link'].reset_index()['National Team Image Link'][0]
        overall = cs1.number_input('Enter Your Overall Rating :',1,99,step = 1)
        weak_foot = cs1.number_input('Enter Your Rating of Weak Foot :',1,5,step = 1)
        skill_moves = cs1.number_input('Enter Your Rating of Skill Moves :',1,5,step = 1)

        player_pace = cs2.number_input('Enter Your Pace Rating :',1,99,step = 1)
        player_shooting = cs2.number_input('Enter Your Shooting Rating :',1,99,step = 1)
        player_passing = cs2.number_input('Enter Your Passing Rating :',1,99,step= 1)
        player_dribbling = cs2.number_input('Enter Your Dribbling Rating',1,99,1)
        player_defending = cs2.number_input('Enter Your Defending Rating',1,99,1)
        player_physicality = cs2.number_input('Enter Your Physical Rating',1,99,1)
        player_img = cs2.text_input('Enter Photo Link')

        color_card_type = st.color_picker('Pick A Color')
        st.write('The current color is', color_card_type)

    if player_position != 'GK':
        html_code = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>FIFA Player Card</title>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Saira+Semi+Condensed:300,400,700">
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}

                body {{
                    font-family: 'Saira Semi Condensed', sans-serif;
                    font-weight: 400;
                    background: url("https://user-images.githubusercontent.com/22690563/67150939-14a0b180-f2c7-11e9-8016-a993a397e1c5.jpg") no-repeat center center / cover;
                    color: {color_card_type};
                }}

                .wrapper {{
                    position: relative;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    width: 100%;
                    height: 100vh;
                    min-height: 500px;
                }}

                .fut-player-card {{
                    position: relative;
                    width: 300px;
                    height: 485px;
                    background-image: url({background});
                    background-position: center center;
                    background-size: 100% 100%;
                    background-repeat: no-repeat;
                    padding: 3.8rem 0;
                    z-index: 2;
                    transition: 200ms ease-in;
                }}

                .player-card-top {{
                    position: relative;
                    display: flex;
                    color: #e9cc74;
                    padding: 0 1.5rem;
                }}

                .player-master-info {{
                    position: absolute;
                    line-height: 2.2rem;
                    font-weight: 300;
                    padding: 1.5rem 0;
                    text-transform: uppercase;
                }}

                .player-rating {{
                    font-size: 2rem;
                    color: {color_card_type};
                }}

                .player-position {{
                    font-size: 1.4rem;
                    color: {color_card_type};
                }}

                .player-nation img,
                .player-club span {{
                    width: 2rem;
                    height: 25px;
                    margin: 0.3rem 0;
                    color: {color_card_type};
                }}

                .player-picture {{
                    width: 200px;
                    height: 200px;
                    margin: 0 auto;
                    overflow: hidden;
                    color: {color_card_type};
                }}

                .player-picture img {{
                    width: 100%;
                    height: 100%;
                    object-fit: contain;
                    position: relative;
                    right: -1.5rem;
                    bottom: 0;
                    color: {color_card_type};
                }}

                .player-extra {{
                    position: absolute;
                    right: 0;
                    bottom: -0.5rem;
                    overflow: hidden;
                    font-size: 1rem;
                    font-weight: 700;
                    text-transform: uppercase;
                    width: 100%;
                    height: 2rem;
                    padding: 0 1.5rem;
                    text-align: right;
                    color: {color_card_type};
                }}

                .player-name {{
                    width: 100%;
                    display: block;
                    text-align: center;
                    font-size: 1.6rem;
                    text-transform: uppercase;
                    border-bottom: 2px solid rgba(233, 204, 116, 0.1);
                    padding-bottom: 0.3rem;
                    overflow: hidden;
                    color: {color_card_type};
                }}

                .player-name span {{
                    display: block;
                    color: {color_card_type};
                }}

                .player-features {{
                    margin: 0.5rem auto;
                    display: flex;
                    justify-content: center;
                    color: {color_card_type};
                }}

                .player-features-col {{
                    border-right: 2px solid rgba(233, 204, 116, 0.1);
                    padding: 0 2.3rem;
                    color: {color_card_type};
                }}

                .player-features-col:last-child {{
                    border: 0;
                }}

                .player-features-col span {{
                    display: flex;
                    font-size: 1.2rem;
                    text-transform: uppercase;
                    color: {color_card_type};
                }}

                .player-feature-value {{
                    margin-right: 0.3rem;
                    font-weight: 700;
                    color: {color_card_type};
                }}

                .player-feature-title {{
                    font-weight: 300;
                    color: {color_card_type};
                }}
            </style>
        </head>
        <body>
            <div class="wrapper">
                <div class="fut-player-card">
                    <div class="player-card-top">
                        <!-- Player Master Info -->
                        <div class="player-master-info">
                            <div class="player-rating"><span>{rating}</span></div>
                            <div class="player-position"><span>{position}</span></div>
                            <div class="player-nation"><img src="{nation_img}" alt="{nation}" draggable="false"></div>
                            <!-- Club Name -->
                            <div class="player-club"><span>{club}</span></div>
                        </div>
                        <!-- Player Picture -->
                        <div class="player-picture">
                            <img src="{player_img}" alt="{player_name}" draggable="false">
                            <div class="player-extra">
                                <span>{skill_moves}</span>
                                <span>{weak_foot}</span>
                            </div>
                        </div>
                    </div>
                    <div class="player-card-bottom">
                        <!-- Player Info -->
                        <div class="player-info">
                            <!-- Player Name -->
                            <div class="player-name"><span>{player_name}</span></div>
                            <!-- Player Features -->
                            <div class="player-features">
                                <div class="player-features-col">
                                    <span>
                                        <span class="player-feature-value">{pace}</span>
                                        <span class="player-feature-title">PAC</span>
                                    </span>
                                    <span>
                                        <span class="player-feature-value">{shooting}</span>
                                        <span class="player-feature-title">SHO</span>
                                    </span>
                                    <span>
                                        <span class="player-feature-value">{passing}</span>
                                        <span class="player-feature-title">PAS</span>
                                    </span>
                                </div>
                                <div class="player-features-col">
                                    <span>
                                        <span class="player-feature-value">{dribbling}</span>
                                        <span class="player-feature-title">DRI</span>
                                    </span>
                                    <span>
                                        <span class="player-feature-value">{defending}</span>
                                        <span class="player-feature-title">DEF</span>
                                    </span>
                                    <span>
                                        <span class="player-feature-value">{physicality}</span>
                                        <span class="player-feature-title">PHY</span>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

        # Define Player's information
        player_info = {
            "rating": f'{overall}',
            "position": f"{player_position}",
            "nation_img": f"{nation_img}",
            "nation": f"{nation_name}",
            "club": f"{club_name}",
            "player_img": f'{player_img}',
            "player_name": f'{player_name}',
            "skill_moves": f"{skill_moves}*SM",
            "weak_foot": f"{weak_foot}*WF",
            "pace": f"{player_pace}",
            "shooting": f"{player_shooting}",
            "passing": f"{player_passing}",
            "dribbling": f"{player_dribbling}",
            "defending": f"{player_defending}",
            "physicality": f"{player_physicality}",
            "background": f"{background}",
            "color_card_type" :f"{color_card_type}"
        }

        # Format the HTML code with Player's information
        formatted_html_code = html_code.format(**player_info)

        st.markdown(formatted_html_code, unsafe_allow_html=True)


    else:
        player_diving = df['Goalkeeper Diving'].loc[df['Known As'] == playername].reset_index()['Goalkeeper Diving'][0]
        player_handling = df['Goalkeeper Handling'].loc[df['Known As'] == playername].reset_index()['Goalkeeper Handling'][0]
        player_kicking = df[' GoalkeeperKicking'].loc[df['Known As'] == playername].reset_index()[' GoalkeeperKicking'][0]
        player_reflexes = df['Goalkeeper Reflexes'].loc[df['Known As'] == playername].reset_index()['Goalkeeper Reflexes'][0]
        player_Height = df['Height(in cm)'].loc[df['Known As'] == playername].reset_index()['Height(in cm)'][0]
        player_positioning = df['Goalkeeper Positioning'].loc[df['Known As'] == playername].reset_index()['Goalkeeper Positioning'][0]

        html_code = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>FIFA Player Card</title>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Saira+Semi+Condensed:300,400,700">
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}

                body {{
                    font-family: 'Saira Semi Condensed', sans-serif;
                    font-weight: 400;
                    background: url("https://user-images.githubusercontent.com/22690563/67150939-14a0b180-f2c7-11e9-8016-a993a397e1c5.jpg") no-repeat center center / cover;
                }}

                .wrapper {{
                    position: relative;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    width: 100%;
                    height: 100vh;
                    min-height: 500px;
                }}

                .fut-player-card {{
                    position: relative;
                    width: 300px;
                    height: 485px;
                    background-image: url({background});
                    background-position: center center;
                    background-size: 100% 100%;
                    background-repeat: no-repeat;
                    padding: 3.8rem 0;
                    z-index: 2;
                    transition: 200ms ease-in;
                }}

                .player-card-top {{
                    position: relative;
                    display: flex;
                    color: #e9cc74;
                    padding: 0 1.5rem;
                }}

                .player-master-info {{
                    position: absolute;
                    line-height: 2.2rem;
                    font-weight: 300;
                    padding: 1.5rem 0;
                    text-transform: uppercase;
                }}

                .player-rating {{
                    font-size: 2rem;
                    color: {color_card_type};
                }}

                .player-position {{
                    font-size: 1.4rem;
                    color: {color_card_type};
                }}

                .player-nation img,
                .player-club span {{
                    width: 2rem;
                    height: 25px;
                    margin: 0.3rem 0;
                    color: {color_card_type};

                }}

                .player-picture {{
                    width: 200px;
                    height: 200px;
                    margin: 0 auto;
                    overflow: hidden;
                    color: {color_card_type};

                }}

                .player-picture img {{
                    width: 100%;
                    height: 100%;
                    object-fit: contain;
                    position: relative;
                    right: -1.5rem;
                    bottom: 0;
                }}

                .player-extra {{
                    position: absolute;
                    right: 0;
                    bottom: -0.5rem;
                    overflow: hidden;
                    font-size: 1rem;
                    font-weight: 700;
                    text-transform: uppercase;
                    width: 100%;
                    height: 2rem;
                    padding: 0 1.5rem;
                    text-align: right;
                    color: {color_card_type};

                }}

                .player-name {{
                    width: 100%;
                    display: block;
                    text-align: center;
                    font-size: 1.6rem;
                    text-transform: uppercase;
                    border-bottom: 2px solid rgba(233, 204, 116, 0.1);
                    padding-bottom: 0.3rem;
                    overflow: hidden;
                    color: {color_card_type};

                }}

                .player-name span {{
                    display: block;
                    color: {color_card_type};

                }}

                .player-features {{
                    margin: 0.5rem auto;
                    display: flex;
                    justify-content: center;
                    color: {color_card_type};

                }}

                .player-features-col {{
                    border-right: 2px solid rgba(233, 204, 116, 0.1);
                    padding: 0 2.3rem;
                }}

                .player-features-col:last-child {{
                    border: 0;
                }}

                .player-features-col span {{
                    display: flex;
                    font-size: 1.2rem;
                    text-transform: uppercase;
                }}

                .player-feature-value {{
                    margin-right: 0.3rem;
                    font-weight: 700;
                }}

                .player-feature-title {{
                    font-weight: 300;
                }}
            </style>
        </head>
        <body>
            <div class="wrapper">
                <div class="fut-player-card">
                    <div class="player-card-top">
                        <!-- Player Master Info -->
                        <div class="player-master-info">
                            <div class="player-rating"><span>{rating}</span></div>
                            <div class="player-position"><span>{position}</span></div>
                            <div class="player-nation"><img src="{nation_img}" alt="{nation}" draggable="false"></div>
                            <!-- Club Name -->
                            <div class="player-club"><span>{club}</span></div>
                        </div>
                        <!-- Player Picture -->
                        <div class="player-picture">
                            <img src="{player_img}" alt="{player_name}" draggable="false">
                            <div class="player-extra">
                                <span>{skill_moves}</span>
                                <span>{weak_foot}</span>
                            </div>
                        </div>
                    </div>
                    <div class="player-card-bottom">
                        <!-- Player Info -->
                        <div class="player-info">
                            <!-- Player Name -->
                            <div class="player-name"><span>{player_name}</span></div>
                            <!-- Player Features -->
                            <div class="player-features">
                                <div class="player-features-col">
                                    <span>
                                        <span class="player-feature-value">{diving}</span>
                                        <span class="player-feature-title">DiV</span>
                                    </span>
                                    <span>
                                        <span class="player-feature-value">{handling}</span>
                                        <span class="player-feature-title">HAN</span>
                                    </span>
                                    <span>
                                        <span class="player-feature-value">{kicking}</span>
                                        <span class="player-feature-title">KIC</span>
                                    </span>
                                </div>
                                <div class="player-features-col">
                                    <span>
                                        <span class="player-feature-value">{reflex}</span>
                                        <span class="player-feature-title">REF</span>
                                    </span>
                                    <span>
                                        <span class="player-feature-value">{height}</span>
                                        <span class="player-feature-title">HT</span>
                                    </span>
                                    <span>
                                        <span class="player-feature-value">{positioning}</span>
                                        <span class="player-feature-title">POS</span>
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

        # Define Player's information
        player_info = {
            "rating": f'{overall}',
            "position": f"{player_position}",
            "nation_img": f"{nation_img}",
            "nation": f"{nation_name}",
            "club": f"{club_name}",
            "player_img": f'{player_img}',
            "player_name": f'{player_name}',
            "skill_moves": f"{skill_moves}*SM",
            "weak_foot": f"{weak_foot}*WF",
            "diving": f"{player_diving}",
            "handling": f"{player_handling}",
            "kicking": f"{player_kicking}",
            "reflex": f"{player_reflexes}",
            "height": f"{player_Height}",
            "positioning": f"{player_positioning}",
            "color_card_type" :f"{color_card_type}",
            "background": f"{background}"
        }

        # Format the HTML code with Player's information
        formatted_html_code = html_code.format(**player_info)

        st.markdown(formatted_html_code, unsafe_allow_html=True)