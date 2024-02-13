import streamlit as st
import pandas as pd
import numpy  as np
import plotly.express as px

import json
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Fifa 23",initial_sidebar_state = 'expanded',page_icon = '🥅')


st.markdown('<h1 style="text-align: center; color: #D8DACC; font-size: 40px; font-weight: bold;">Fifa 23 Analysis</h1>', unsafe_allow_html=True)

df = pd.read_csv("Fifa_23_clear.csv",index_col = "Unnamed: 0")
st.image("peakpx.jpg",width = 60, use_column_width = True)

st.divider()
tap1,tap2 = st.tabs(['About Fifa 23','About Fifa 23 Analysis'])
with tap1:
    st.markdown("""

    <h1 style="text-align: center; color: #D8DACC; font-size: 30px; font-weight: bold;">About Fifa 23</h1>

    * FIFA 23 is a football simulation video game published by Electronic Arts. It is the 30th and final installment in the FIFA series that is developed by EA Sports, and released worldwide on 30 September 2022 for PC, Nintendo Switch, PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S and Google Stadia.

    * The role of performance analysis within football is more important than ever. Whether it’s the opposition, potential transfer targets or last weekend’s fixture, analysing performances and data can be the difference between success and failure.

    ### Overall:

    FIFA 23 offered some noteworthy gameplay advancements but didn't revolutionize the series. The mixed reception highlights the desire for more substantial innovation and improvements in areas like online gameplay and career mode. Whether future iterations address these concerns remains to be seen.

    ### Additional Points to Consider:

    * The upcoming switch to the "EA SPORTS FC" franchise in 2024 might bring significant changes.
    * Player performance data and in-game tactics could be analyzed for deeper insights.
    * The impact of FIFA 23 on esports and competitive gaming could be explored.
    * The upcoming switch to the "EA SPORTS FC" franchise in 2024 might bring significant changes.
    ### References:
    * Download the Dataset from here: [Kaggle](https://www.kaggle.com/datasets/sanjeetsinghnaik/fifa-23-players-dataset)
    * This is a web application created using Streamlit and Plotly Express to display information about the FIFA 23.
    * This web application is designed to provide an easy and intuitive way for users to explore the data of Fifa 23.

                            """, unsafe_allow_html=True)

    st.divider()

with tap2:
    st.markdown("""

<h1 style="text-align: center; color: #D8DACC; font-size: 30px; font-weight: bold;">About the Dataset:</h1>
- The attributes provided in the "FIFA 23 Players Dataset" offer a comprehensive overview of the characteristics and skills of football players featured in the FIFA 23 video game. Here's a detailed description of the key attributes included in the dataset:

- Player ID: A unique identifier assigned to each player in the dataset.

- Name: The name of the football player.

- Age: The age of the player, indicating how old they are in the game.

- Nationality: The nationality of the player, representing the country they are associated with.

- Club: The football club that the player belongs to in the game.

- Position: The playing position of the player on the field, such as forward, midfielder, defender, or goalkeeper.

- Overall Rating: An overall assessment of the player's skill level and performance, represented by a numerical rating.

- Physical Attributes:

- Height: The height of the player in centimeters.
- Weight: The weight of the player in kilograms.
- Skill Ratings:

    - Pace: The speed and acceleration of the player.
    - Shooting: The accuracy and power of the player's shots.
    - Passing: The accuracy and effectiveness of the player's passes.
    - Dribbling: The player's ability to control the ball while dribbling.
    - Defending: The player's proficiency in defensive actions.
    - Physicality: The player's strength, stamina, and aggression on the field.
    - Weak Foot and Skill Moves: Ratings indicating the player's proficiency with their weaker foot and their ability to perform skill moves, respectively.

- Preferred Foot: The preferred foot of the player, indicating whether they are primarily left or right footed.

- Work Rate: The player's work rate, indicating their level of activity and involvement during matches.

- Player Traits: Specific characteristics or behaviors attributed to the player, such as "Speed Dribbler" or "Clinical Finisher."

- Value and Wage: The in-game value and wage of the player, representing their market worth and salary within the game economy.

- These attributes collectively provide a detailed profile of each football player in the dataset, enabling analysis and comparison of their skills, performance, and overall contribution to the game. Researchers, analysts, and gamers can leverage this information for various purposes, including team building, strategy development, and performance evaluation within the virtual football environment of FIFA 23.

    """,unsafe_allow_html=True)

    st.divider()

    if st.button("Click here to take a look",use_container_width = True,help='Head about Fifa 23 Dataset'):

        st.dataframe(df.head(5))



