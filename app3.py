import streamlit as st

st.title("Portfolio -MHbN")

left , right = st.beta_columns(2)

#Image Insertion
with left:
    from PIL import Image
    image = Image.open('images/dp.jpg')
    st.image(image , caption="Hi. I'm Mohammed Haaris bin Naveed")
with right:
    st.markdown("Socials")
    st.markdown("LinkedIn:[_Mohammed Haaris_](https://www.linkedin.com/in/mohammed-haaris-376a29158/)")
    st.markdown("GitHub:[_MHbN98_](https://github.com/MHbN98/)")
    st.markdown("Discord:[_MHbN_](https://discord.com/)")
    st.markdown("Instagram:[_ haaris _](https://www.instagram.com/l_haaris_l/)")
st.header("Skills")

l1,l2,l3,l4,l5 = st.beta_columns(5)

with l1:
    from PIL import Image
    image = Image.open('images/py.jpg')
    st.image(image,width=70)
    click = st.button('Python')
    if(click == True):
        st.balloons()


with l2:
    from PIL import Image
    image = Image.open('images/np.jpeg')
    st.image(image,width=70)
    click = st.button('NumPy')
    if(click == True):
        st.balloons()

with l3:
    from PIL import Image
    image = Image.open('images/jp.jpg')
    st.image(image,width=70)
    click = st.button('Jupyter')
    if(click == True):
        st.balloons()

with l4:
    from PIL import Image
    image = Image.open('images/exc.jpg')
    st.image(image,width=70)
    click = st.button('Ecxel')
    if(click == True):
        st.balloons()

with l5:
    from PIL import Image
    image = Image.open('images/sql.jpg')
    st.image(image,width=90)
    click = st.button('SQL')
    if(click == True):
        st.balloons()
