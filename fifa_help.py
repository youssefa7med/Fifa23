import streamlit as st

def fifa_main_card(overall='90',player_position='RW',nation_img='',background='https://selimdoyranli.com/cdn/fut-player-card/img/card_bg.png',nation_name='Egypt',club_name='Liverpool',player_img = 'https://cdn.sofifa.net/players/209/331/23_60.png',player_name='Mohamed Salah',skill_moves = '4',weak_foot='3',player_pace='90',player_shooting='89',player_passing='82',player_dribbling='90',player_defending='45',player_physicality='75'):

    html_template = """
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

            .player-rating,
            .player-position {{
                font-size: 2rem;
            }}

            .player-nation img,
            .player-club span {{
                width: 2rem;
                height: 25px;
                margin: 0.3rem 0;
            }}

            .player-picture {{
                width: 200px;
                height: 200px;
                margin: 0 auto;
                overflow: hidden;
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
            }}

            .player-name span {{
                display: block;
            }}

            .player-features {{
                margin: 0.5rem auto;
                display: flex;
                justify-content: center;
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
        "background" :f"{background}"
    }

    # Format the HTML code with Player's information
    formatted_html_code = html_template.format(**player_info)

    return st.markdown(formatted_html_code, unsafe_allow_html=True)


def fifa_GK_card(overall='89',player_position='GK',nation_img='https://cdn.sofifa.net/flags/br.png',nation_name='Brazil',club_name='Liverpool',player_img='https://cdn.sofifa.net/players/212/831/23_60.png',player_name='Alisson',skill_moves='1',weak_foot='3',diving='86',background = "https://fonts.googleapis.com/css?family=Saira+Semi+Condensed:300,400,700",handling='85',kicking='85',reflex='89',height='193',positioning='90'):

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FIFA Player Card</title>
        <link rel="stylesheet" href={background}>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            /* Your CSS styles */
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

    # Format the HTML code with Player's information
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
        "diving": f"{diving}",
        "handling": f"{handling}",
        "kicking": f"{kicking}",
        "reflex": f"{reflex}",
        "height": f"{height}",
        "positioning": f"{positioning}",
        'background':f"{background}"
    }
    formatted_html_code = html_template.format(**player_info)
    # Render HTML code
    return st.markdown(formatted_html_code, unsafe_allow_html=True)

fifa_23_card_background = 'https://pdf-service-static.s3.amazonaws.com/static/layout-images/cardstar/thumbnails/rare-gold-23.png'