import streamlit as st

# Header
st.title("Broden", text_alignment="center")
st.subheader("Zoek naar allerlei brood", text_alignment="center")

st.divider()

# body
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image("https://www.koopmans.com/_default_upload_bucket/Brood%20nieuw.png", caption="koopmans", width=150)
with col2:
    st.image("https://www.bakkerijvangronsveld.be/wp-content/uploads/2023/08/Klein_Brood_Wit_400gr_img.png", caption="bakkerijvangronsveld", width=150)
with col3:
    st.image("https://biaform-provital.com/wp-content/uploads/2024/12/1-biaform-header-3-brood.png", caption="biaform provital", width=150)
with col4:
     st.image("https://www.bakkerijlanckriet.be/sites/default/files/styles/product_categories_portrait/public/2020-02/Groot%20platine%20grof.png?itok=kXKszGlP", caption="bakkerijlanckriet", width=150)
with col5:
     st.image("https://www.aldi.be/content/aldi/belgium/promotions/source-localenhancement/2019/2019-01/2019-01-02/vast_assortiment/8761/1/0/_jcr_content/assets/imported-images/BILD_INTERNET4/8761_proteinerijk_brood_op_plankje_24-4.png/_jcr_content/renditions/opt.1250w.png.res/1734741426009/opt.1250w.png", caption="bakkerijdehavik", width=150)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image("https://shop.pro10.be/wp-content/uploads/2012/03/products-brood-losgesneden-1024x506_1.png", caption="shop pro10", width=150)
with col2:
    st.image("https://www.chaupain.nl/wp-content/uploads/2025/12/2537-Melkbol-1600x1200.png", caption="chaupain", width=150)
with col3:
    st.image("https://broodenco.com/wp-content/uploads/2025/05/brood.png", caption="broodenco", width=150)
with col4:
     st.image("https://www.limburgsmaaktnaarmeer.be/site/data/images/product/thumb_brood.png", caption="limburgsmaaktnaarmeer", width=150)
with col5:
     st.image("https://www.bakkerijholland.nl/wp-content/uploads/2023/11/Witbrood-Gesneden-NL-0081.png", caption="bakkerijholland", width=150)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image("https://broodenbanketsascha.be/wp-content/uploads/2021/07/brood.png", caption="broodenbanketsascha", width=150)
with col2:
    st.image("https://www.food5.nl/cdn/shop/files/7492_-_Brioche_-_VV_580x.png?v=1750664224", caption="food5", width=150)
with col3:
    st.image("brood.webp", caption="biaform provital", width=150)
with col4:
     st.image("https://cdn.ekoplaza.nl/ekoplaza/categorieen/cat207_s.png", caption="ekoplaza", width=150)
with col5:
     st.image("https://www.bakkerijarickx.be/pages/links/producten/brood_speciaal_belgischmeergranen.png", caption="bakkerijarickx", width=150)