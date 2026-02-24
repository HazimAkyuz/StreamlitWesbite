import streamlit as st

# Header
st.title("Contact")
st.subheader("Vragen of problemen?")

with st.form(key="Contact"):
    naam = st.text_input("Wat is uw naam?")
    reden = st.radio(
    "Waarmee wilt u ons contacteren",
    [":rainbow[Compliment]", "Vraag", "Probleem"],
)
    bericht = st.text_area("Uw bericht")

    st.form_submit_button("Verzend")

if reden == ":rainbow[Compliment]":
    st.balloons()