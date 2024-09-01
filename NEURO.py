import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

def main():

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
   
    background-size: 100%; background-image: url("https://drivesafety.com/wp-content/uploads/2017/08/Neural-network.jpg");
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}"""
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.title("Hello..")
    st.title("Welcome to this Application")

    col11, e, col12= st.columns([2, 2, 2])

    with col11:
        st.markdown(
            """
            <style>
            .element-container:has(style){
                display: none;
            }
            #button-z {
                display: none;
            }
            .element-container:has(#button-z) {
                display: none;
            }
            .element-container:has(#button-z) + div button {
                background-image: url("https://as2.ftcdn.net/v2/jpg/06/92/72/17/1000_F_692721752_dPCjG0L8kQVgUG2rDtqgjXFvq7TtfgVq.jpg");

                background-size: 400px 400px;
                width: 400px;
                height: 300px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-z"></span>', unsafe_allow_html=True)
        if st.button("",):
            st.switch_page("pages/pew.py")
        st.markdown("<h3 style='text-indent: 0px; color: white;'>USE YOUR EYE</h23>", unsafe_allow_html=True)

    with col12:
        st.markdown(
            """
            <style>
            .element-container:has(style){
                display: none;
            }
            #button-l {
                display: none;
            }
            .element-container:has(#button-l) {
                display: none;
            }
            .element-container:has(#button-l) + div button {
                background-image: url("https://www.medstarhealth.org/-/media/project/mho/medstar/services/ankles_1200x628.jpg");

                background-size: 400px 300px;
                width: 400px;
                height: 300px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-l"></span>', unsafe_allow_html=True)
        if st.button(" ",):
            st.switch_page("pages/leg.py")
        st.markdown("<h3 style='text-indent: 0px; color: white;'>CHECK YOUR PROGRESS</h3>", unsafe_allow_html=True)

def get_url(page_name):
    """Generate URL for the given page."""
    return f'<a href="http://localhost:8501/{page_name}">Go to Another Page</a>'

if __name__ == "__main__":
    main()
