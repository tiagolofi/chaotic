
import streamlit as st
from drome import Drome
from time import sleep

st.set_page_config(
	page_title='CHAOTIC',
	layout = 'wide',
	page_icon = 'logo.png',
	initial_sidebar_state = 'collapsed' 
)

css = '''
<style>
section.main > div:has(~ footer ) {
    padding-bottom: 0px;
}
</style>
'''
st.markdown(css, unsafe_allow_html=True)

drome = Drome()

st.title('CHAOTIC')
st.write('''by [@tiagolofi](https://github.com/tiagolofi)''')

col1, col2, col3, col4, col5 = st.columns(5)

CREATURES, ATTACKS, MUGICX, BATTLEGEAR = drome.ls_names()

with col1:

    creature = st.selectbox('Creature:', CREATURES)
    creature_data = drome.get_data(creature)
    st.image(drome.get_creature(creature))
    st.write(creature_data['text_card'])

    for k, v in creature_data['stats'].items():

        st.progress(value = v, text = f'{k}: {v}')

with col2:  

    choose_local = st.button('Local')

    if choose_local:
        st.image('gifs/choose_local.gif')
        st.session_state.local = drome.get_location()
        sleep(2)
        st.rerun()

    if 'local' in st.session_state:
        st.image(st.session_state.local)

with col3:

    attack = st.button('Attack')

    if attack:
        st.image('gifs/spin_attack.gif')
        st.session_state.attack = drome.get_attack()
        sleep(1)
        st.rerun()
        
    if 'attack' in st.session_state:
        st.image(st.session_state.attack)

with col4:

    mugic = st.button('Mugic')

    if mugic:
        st.image('gifs/spin_mugic.gif')
        st.session_state.mugic = drome.get_mugic()
        sleep(3)
        st.rerun()

    if 'mugic' in st.session_state:
        st.image(st.session_state.mugic)

with col5:

    bg = st.button('BattleGear')
    
    if bg:
        st.session_state.bg = drome.get_bg()
    
    if 'bg' in st.session_state:
        st.image(st.session_state.bg)

# with col2_1:
# 
#     with st.expander('Stats (P2)'):
# 
#         data2_ed = st.data_editor(pandas.DataFrame({k: v for k, v in data2.items() if k == "stats"}).filter(['stats']), key = 'd2')
# 
#         df_elem2 = pandas.DataFrame(
#             [
#                 {'element': 'Fire', 'active': type_element('Fire', data2['elements']), 'damage': ''},
#                 {'element': 'Water', 'active': type_element('Water', data2['elements']), 'damage': ''},
#                 {'element': 'Earth', 'active': type_element('Earth', data2['elements']), 'damage': ''},
#                 {'element': 'Air', 'active': type_element('Air', data2['elements']), 'damage': ''}
#             ]
#         )
# 
#         elem2 = st.data_editor(df_elem2, key = 'd4', hide_index = True)
# 
#     for k2, v2 in zip(data2_ed.index, data2_ed['stats']):
#         
#         st.progress(int(v2), text = k2 + ': '+ str(v2))
# 
