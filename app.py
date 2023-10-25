
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

with col2:

    select_local = st.button('Choose Battle Local')

    if select_local:

        st.session_state['location'] = d.location_random()

    st.image(
        Image.open(
            st.session_state['location']                
        )
    )        

with col3:

    creature = st.selectbox('Creature (Player 2)', d.get_names_creatures())

    data2 = d.get_card(name = creature)

    st.image(Image.open(d.format_image(data2['chaotic_hash'])))
