
import streamlit as st
from drome import Drome
from PIL import Image
from time import sleep

d = Drome()

st.set_page_config(
	page_title='CHAOTIC',
	layout = 'wide',
	page_icon = 'logo.png',
	initial_sidebar_state = 'collapsed' 
)

st.markdown('''<h1 align="center"><b>CHAOTIC</b></h1>''', unsafe_allow_html=True)

col1, col1x, col2, col3, col3x = st.columns(5)

with col1:

    creature = st.selectbox('Creature (Player 1)', d.get_names_creatures())

    data1 = d.get_card(name = creature)

    st.image(Image.open(d.format_image(data1['chaotic_hash'])))

with col1x:

    attack = st.button('Attack (P1)')

    if attack:

        st.image(
            Image.open(
                d.attack_random()               
            )
        )

with col2:

    select_local = st.button('Choose Battle Local')

    if select_local:

        with st.spinner('Wait...'):

            sleep(3)

            st.session_state['location'] = d.location_random()

    try:

        st.image(
            Image.open(
                st.session_state['location']                
            )
        )        

    except:

        st.info('No Local Selected')

with col3x:

    creature = st.selectbox('Creature (Player 2)', d.get_names_creatures())

    st.session_state['d2'] = d.get_card(name = creature)

    st.image(Image.open(d.format_image(st.session_state['d2']['chaotic_hash'])))

    st.write(st.session_state['d2'])

with col3:

    attack2 = st.button('Attack (P2)')

    if attack2:

        st.image(
            Image.open(
                d.attack_random()               
            )
        )

col1_1, col1_2, col1_3, col2_1, col2_2, col2_3 = st.columns(6)

with col1_1:

    mugic = st.selectbox('Mugic (P1)', d.get_names_mugix())

    data_mg = d.get_card(name = mugic)

    st.image(Image.open(d.format_image(data_mg['chaotic_hash'])))

with col1_2:

    bg = st.selectbox('BattleGear (P1)', d.get_names_bg())

    data_bg = d.get_card(name = bg)

    st.image(Image.open(d.format_image(data_bg['chaotic_hash'])))

with col1_3:

    st.write('Stats (P1)')

    for k, v in data1['stats'].items():

        st.progress(v, text = k + ': '+ str(v))

    var = st.selectbox('Attribute (P1)', ['Courage', 'Power', 'Wisdom', 'Speed', 'Energy'])

    value_debit = st.number_input('Debit (P1)', step = 1)

    value_credit = st.number_input('Credit (P1)', step = 1)

    action = st.button('Action (P1)')

    if action:

        data1['stats'][var] += value_credit
        data1['stats'][var] -= value_debit

    # st.write(data1['stats'])

with col2_1:

    st.write('Stats (P2)')

    for k, v in st.session_state['d2']['stats'].items():
        
        st.progress(v, text = k + ': '+ str(v))

    var2 = st.selectbox('Attribute (P2)', ['Courage', 'Power', 'Wisdom', 'Speed', 'Energy'])

    value_debit2 = st.number_input('Debit (P2)', step = 1)

    value_credit2 = st.number_input('Credit (P2)', step = 1)

    action2 = st.button('Action (P2)')

    if action2:

        st.session_state['d2']['stats'][var2] += value_credit2
        st.session_state['d2']['stats'][var2] -= value_debit2

with col2_2:

    bg2 = st.selectbox('BattleGear (P2)', d.get_names_bg())

    data_bg2 = d.get_card(name = bg2)

    st.image(Image.open(d.format_image(data_bg2['chaotic_hash'])))

with col2_3:

    mugic2 = st.selectbox('Mugic (P2)', d.get_names_mugix())

    data_mg2 = d.get_card(name = mugic2)

    st.image(Image.open(d.format_image(data_mg2['chaotic_hash'])))

st.write('''by [@tiagolofi](https://github.com/tiagolofi)''')
