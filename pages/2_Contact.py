import streamlit as st

# Header
st.title("Contact")
st.subheader("Vragen of problemen?")

with st.form(key="Contact"):
    naam = st.text_input("Wat is uw naam?")
    reden = st.radio(
    "Waar wilt u ons mee contacteren?",
    [":rainbow[Compliment]", "Vraag", "Probleem"],
)
    bericht = st.text_area("Uw bericht")
    tevreden = st.slider("Hoe tevreden bent u ment onze service?",0,10,5,1)

    if st.form_submit_button("Verzend"):
        if reden == ":rainbow[Compliment]":
            st.balloons()