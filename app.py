
import streamlit as st
from drome import Drome
from PIL import Image
from time import sleep
import pandas

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

    data2 = d.get_card(name = creature)

    st.image(Image.open(d.format_image(data2['chaotic_hash'])))

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

    with st.expander('Reveal Mugic (P1)'):

        st.image(Image.open(d.format_image(data_mg['chaotic_hash'])))

with col1_2:

    bg = st.selectbox('BattleGear (P1)', d.get_names_bg())

    data_bg = d.get_card(name = bg)

    with st.expander('Reveal BattleGear (P1)'):

        st.image(Image.open(d.format_image(data_bg['chaotic_hash'])))

with col1_3:

    with st.expander('Stats (P1)'):

        data1_ed = st.data_editor(pandas.DataFrame(data1).filter(['stats']))

    for k, v in zip(data1_ed.index, data1_ed['stats']):

        st.progress(int(v), text = k + ': '+ str(v))

with col2_1:

    st.write('Stats (P2)')

    # data2_ed = st.data_editor(data2)

    # for k, v in data2_ed['stats'].items():
        
    #     st.progress(v, text = k + ': '+ str(v))

with col2_2:

    bg2 = st.selectbox('BattleGear (P2)', d.get_names_bg())

    data_bg2 = d.get_card(name = bg2)

    with st.expander('Reveal BattleGear (P2)'):

        st.image(Image.open(d.format_image(data_bg2['chaotic_hash'])))

with col2_3:

    mugic2 = st.selectbox('Mugic (P2)', d.get_names_mugix())

    data_mg2 = d.get_card(name = mugic2)

    with st.expander('Reveal Mugic (P2)'):

        st.image(Image.open(d.format_image(data_mg2['chaotic_hash'])))

st.write('''by [@tiagolofi](https://github.com/tiagolofi)''')
