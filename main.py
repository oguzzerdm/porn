import streamlit as st
from PIL import Image
st.set_page_config(page_title="Oğuz Erdem İpek", page_icon="⚡", layout="wide")

with st.container():
    st.subheader("Ozzy The Musician 🎶")
    st.title("Merhaba Ben Oğuz Erdem İpek 🙋‍ ")
    st.write("Müzik tutkumun peşinden gidiyorum ve Instagram hesabımda bunları paylaşıyorum.")
    st.write("[Instagram Hesabım >](https://www.instagram.com/oguzz_erdm/)")

img_gang = Image.open("photo/gang.png")

with st.container():
    st.write("---")
    st.header("Videolarım")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_gang)

    with text_column:
        st.subheader("🎹-Ay Tenli Kadın-🎹")
        st.markdown("[Linke tıklayarak Ufuk Beydemir''in Ay Tenli Kadın parçasını çaldığım videoma ulaşabilirsiniz](https://www.instagram.com/p/Cw-owYGMKq9/)")

    with text_column:
        st.subheader("🎸-Mavi Duvar-🎸 ")
        st.markdown(
            "[Linke tıklayarak Hüseyin Demirtaş ile 'Mavi Duvar' parçasını seslendirdiğimiz videoma ulaşabilirsiniz](https://www.instagram.com/p/Cw5p_M8tJ2M/)")

    with text_column:
        st.subheader("🎹-Sezen Aksu • Vay-🎹 ")
        st.markdown("[Linke tıklayarak Sezen Aksu'nun 'Vay' parçasını çaldığım videoma ulaşabilirsiniz](https://www.instagram.com/p/Cw0a950NAdH/)")

    with text_column:
        st.subheader("🎹-İçimdeki Duman-🎹")
        st.markdown("[Linke tıklayarak İlyas Yalçıntaş'ın 'İçimdeki Duman' parçasını çaldığım videoma ulaşabilirsiniz](https://www.instagram.com/p/Cs9b23RAYT/)")

    with text_column:
        st.subheader("🎹- Her Şey Seninle Güzel-🎹")
        st.markdown("[Linke tıklayarak 'Her Şey Seninle Güzel' parçasını' çaldığım videoma ulaşabilirsiniz](https://www.instagram.com/p/CsmSzKRJiHo/)")