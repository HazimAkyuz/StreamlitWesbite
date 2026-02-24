import streamlit as st
import sqlite3

#Database voor broodweetjes
conn = sqlite3.connect('brood.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS broodweetjes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weetje TEXT NOT NULL
    )
''')

# weetjes in brood.db
c.execute("INSERT INTO broodweetjes (weetje) VALUES ('Brood is een van de oudste voedingsmiddelen die door mensen worden geconsumeerd.')")
c.execute("INSERT INTO broodweetjes (weetje) VALUES ('Er zijn duizenden verschillende soorten brood over de hele wereld, elk met unieke ingrediënten en bereidingsmethoden.')")
c.execute("INSERT INTO broodweetjes (weetje) VALUES ('Brood kan worden gemaakt van verschillende soorten meel, zoals tarwe, rogge, maïs en haver.')")
c.execute("INSERT INTO broodweetjes (weetje) VALUES ('Brood is een belangrijke bron van koolhydraten, die energie leveren aan het lichaam.')")
c.execute("INSERT INTO broodweetjes (weetje) VALUES ('Brood kan worden verrijkt met zaden, noten, gedroogd fruit en kruiden voor extra smaak en voedingswaarde.')")
conn.commit()
conn.close()    



# Header
st.title("Brood", text_alignment="center")
st.subheader("De website voor brood!", text_alignment="center")



# Body
st.divider()
st.subheader("Featured brood", text_alignment="center")

with st.container(border=True):
    col1, col2= st.columns(2)
    with col1:
        st.image("https://www.koopmans.com/_default_upload_bucket/Brood%20nieuw.png", caption="koopmans", width=150)
    with col2:
        st.image("https://www.bakkerijvangronsveld.be/wp-content/uploads/2023/08/Klein_Brood_Wit_400gr_img.png", caption="bakkerijvangronsveld", width=150)

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://biaform-provital.com/wp-content/uploads/2024/12/1-biaform-header-3-brood.png", caption="biaform provital", width=150)
    with col2:
        st.image("https://www.bakkerijlanckriet.be/sites/default/files/styles/product_categories_portrait/public/2020-02/Groot%20platine%20grof.png?itok=kXKszGlP", caption="bakkerijlanckriet", width=150)

st.divider()

st.subheader("Weetjes", text_alignment="center")

if st.button("Broodweetje"):
    conn = sqlite3.connect('brood.db')
    c = conn.cursor()
    c.execute("SELECT weetje FROM broodweetjes ORDER BY RANDOM() LIMIT 1")
    weetje = c.fetchone()[0]
    with st.container(border=True):
        st.write(weetje)
    conn.close()