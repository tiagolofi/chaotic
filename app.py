
import streamlit as st
from drome import Drome
from PIL import Image

d = Drome()

st.set_page_config(
	page_title='CHAOTIC',
	layout = 'wide',
	page_icon = 'logo.png',
	initial_sidebar_state = 'collapsed' 
)

col1, col2, col3 = st.columns(3)

with col1:

    creature = st.selectbox('Creature (Player 1)', d.get_names_creatures())

    data1 = d.get_card(name = creature)

    st.image(Image.open(d.format_image(data1['chaotic_hash'])))

    st.dataframe(data1['stats'])

    col1_1, col1_2 = st.columns(2)

    with col1_1:

        bg = st.selectbox('BattleGear (P1)', d.get_names_bg())

        data_bg = d.get_card(name = bg)

        st.image(Image.open(d.format_image(data_bg['chaotic_hash'])))

    with col1_2:

        mugic = st.selectbox('Mugic (P1)', d.get_names_mugix())

        data_mg = d.get_card(name = mugic)

        st.image(Image.open(d.format_image(data_mg['chaotic_hash'])))

with col2:

    select_local = st.button('Choose Battle Local')

    if select_local:

        st.session_state['location'] = d.location_random()

    try:

        st.image(
            Image.open(
                st.session_state['location']                
            )
        )        

    except:

        st.info('No Local Selected')

with col3:

    creature = st.selectbox('Creature (Player 2)', d.get_names_creatures())

    data2 = d.get_card(name = creature)

    st.image(Image.open(d.format_image(data2['chaotic_hash'])))

    st.dataframe(data1['stats'])

    col2_1, col2_2 = st.columns(2)

    with col2_1:

        bg2 = st.selectbox('BattleGear (P2)', d.get_names_bg())

        data_bg2 = d.get_card(name = bg2)

        st.image(Image.open(d.format_image(data_bg2['chaotic_hash'])))

    with col2_2:

        mugic2 = st.selectbox('Mugic (P2)', d.get_names_mugix())

        data_mg2 = d.get_card(name = mugic2)

        st.image(Image.open(d.format_image(data_mg2['chaotic_hash'])))