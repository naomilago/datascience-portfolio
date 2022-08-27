import streamlit as st

# PAGE SETTINGS

st.set_page_config(
    page_title="NL | Contact",
    page_icon="📊",
)

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

st.header('Contact')