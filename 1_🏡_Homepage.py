# IMPORTS

from streamlit_lottie import st_lottie
import streamlit as st
import requests

# PAGE SETTINGS

st.set_page_config(
    page_title="Naomi Lago",
    page_icon='./src/img/favicon.ico',
)

# LOTTIE ANIMATIONS

def load_lottie(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

datascience_animation = load_lottie('https://assets10.lottiefiles.com/packages/lf20_qp1q7mct.json')

# NAVIGATION

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #9C73F8;">
  <a class="navbar-brand" href="https://naomilago.com" target="_blank">Naomi Lago</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a target='_self' class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a target='_self' class="nav-link" href="/About_Me">About me</a>
      </li>
      <li class="nav-item">
        <a target='_self' class="nav-link" href="/Work_Experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a target='_self' class="nav-link" href="/Projects">Projects</a>
      </li>
      <li class="nav-item">
        <a target='_self' class="nav-link" href="/Contact">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# HEADER

with st.container():
    st.write('<h1>Hi, I\'m <spam style="color: #9C73F8">Naomi Lago</spam></h1>', unsafe_allow_html=True)
    st.write('<h4 style="margin-bottom:10%;">A Data Science Analyst</spam></h4>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.write('''
        <p>I've been studying technology for about 5 years and I'm always looking for new ways to improve.
        Now, I currently undergraduate in Mathematics and work as Data Science Analyst @ <a href='https://nestle.com' style="color: #C4B3EC">Nestlé</a>.</p>
        ''', unsafe_allow_html=True)

        st.markdown('''
            > Things that I'm also interested in:  <br />
            > • Cybersecurity; <br />
            > • Cloud Computing; <br /> 
            > • Machine Learning; <br /> 
            > • Artificial Intelligence. <br />
        ''', unsafe_allow_html=True)

    with col2:
        st_lottie(
            datascience_animation, 
            key="data-science-animation",
            loop=False, 
            speed=.8
            )    
    


