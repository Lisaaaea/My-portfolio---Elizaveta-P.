import streamlit as sl

mainpage = sl.Page(page='streamlit.py', title='about me', default=True, icon=':material/face:')
secondpage = sl.Page(page='secondpage.py', title='page 2', icon=':material/face:')
nav = sl.navigation(pages=[mainpage, secondpage])
nav.run()


