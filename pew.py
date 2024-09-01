import streamlit as st
from PIL import Image
import subprocess
import os
from twilio.rest import Client
import webbrowser
import time
#import threading


water = ["20:50", "12:00", "15:00", "18:00"]
medicine = ["19:54", "12:00", "15:00", "18:00"]

def continuously_check_time(interval, water):
    while True:
        current_time = time.strftime("%H:%M", time.localtime())
        if current_time in water:
            st.toast("Time to drink some water!")
        if current_time in medicine:
            st.toast("Time to drink some medicine!")
        st.toast(current_time)
        time.sleep(interval)

def handle_sos():
    # Function to handle the SOS action
    account_sid = 'AC8d115d03e5c9a226877458ff3e7cd205'
    auth_token = '490720d5441af81b94dd81a66fc61dbd'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Emergency now.',
        to='whatsapp:+916364251225'
    )
    
    print(message.sid)
    st.error("SOS triggered! Emergency response initiated.")

def keyb():
    subprocess.Popen(["C:/Users/91636/OneDrive/Attachments/Desktop/PROJECT/pages/vkeyboard.pyw"], shell=True)

def autostart_audio():
    audio_html = f"""
    <audio src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" preload="auto" autoplay controls>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .element-container:has(style){
        display: none;
    }
    #button-bell {
        display: none;
    }
    .element-container:has(#button-bell) {
        display: none;
    }
    .element-container:has(#button-bell) + div button {
        background-image: url("https://www.freestock.com/450/freestock_427814677.jpg");
        #background-image: url("C:/Users/91636/OneDrive/Pictures/Saved Pictures/SOS.jpg");
        background-size: 200px 125px;
        background-color: red;
        width: 200px;
        height: 125px;
        position: fixed;
        top: 50px;
        left: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<span id="button-bell"></span>', unsafe_allow_html=True)
if st.button("",):
    handle_sos()

st.markdown(
    """
    <style>
    .element-container:has(style){
        display: none;
    }
    #button-after {
        display: none;
    }
    .element-container:has(#button-after) {
        display: none;
    }
    .element-container:has(#button-after) + div button {
        background-image: url("https://img.freepik.com/free-vector/illustrationn-megaphone-monochrome-style-isolated-white-background_1284-38767.jpg?w=740&t=st=1712998339~exp=1712998939~hmac=ee62549d16d26f5e31a44af0a1deafdc3cd6aee3590bd26dc6878af140fb187a");
        background-size: 200px 125px;
        background-color: red;
        width: 200px;
        height: 125px;
        position: fixed;
        top: 50px;
        right: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
audio_file = open("C:/Users/91636/OneDrive/Attachments/Desktop/PROJECT/pages/Cat-meow-free-sound-effect.mp3", "rb")
audio_bytes = audio_file.read()


if st.button("Buzz",):
    autostart_audio()

st.markdown(
    """
    <style>
    .element-container:has(style){
        display: none;
    }
    #button-water {
        display: none;
    }
    .element-container:has(#button-water) {
        display: none;
    }
    .element-container:has(#button-water) + div button {
        background-image: url("https://www.bing.com/images/search?view=detailV2&ccid=XlF90wNM&id=A8A2BF09895284C4796F498F5D99CDCCD4BDB602&thid=OIP.XlF90wNMTpVk9X82aruyHgAAAA&mediaurl=https%3A%2F%2Fwww.shutterstock.com%2Fimage-vector%2Fred-flasher-siren-text-sos-260nw-2255084739.jpg&exph=280&expw=390&q=SOS+ALARM+IMAGES&simid=608013867732775850&form=IRPRST&ck=4796293B3AA92BA669B5E1EBCA46FE4E&selectedindex=0&itb=0&ajaxhist=0&ajaxserp=0&pivotparams=insightsToken%3Dccid_U6zheK6z*cp_7CBF3087D765BBB84473F514F83BFA2E*mid_A8A2BF09895284C4796FBD80313ACF2F2B44D3ED*simid_607999105917734417*thid_OIP.U6zheK6zR-CxsLnxsti2gQAAAA&vt=0&sim=11&iss=VSI");
        background-size: 200px 125px;
        background-color: red;
        width: 200px;
        height: 125px;
        position: fixed;
        top: 50px;
        left: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():

    # interval = 5
    # continuously_check_time(interval, water)
    # check_time_thread = threading.Thread(target=continuously_check_time, args=(interval, water_times))
    # check_time_thread.start()

    subprocess.Popen(["python", "C:/Users/91636/OneDrive/Attachments/Desktop/PROJECT/pages/neweye.py"], shell=True)

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://directlinedev.com/media/cases/rooney/header/background_1_zM58lsj.wide.jpeg");
    background-size: 100%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}"""
    st.markdown(page_bg_img, unsafe_allow_html=True)

    col11, e, col12, z, col13 = st.columns([1, 0.25, 1, 0.25, 1])
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    col21, e, col22, z, col23 = st.columns([1, 0.25, 1, 0.25, 1])
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    col31, e, col32, z, col33 = st.columns([1, 0.25, 1, 0.25, 1])

    with col11:
        st.markdown(
            """
            <style>
            .element-container:has(style){
                display: none;
            }
            #button-note {
                display: none;
            }
            .element-container:has(#button-note) {
                display: none;
            }
            .element-container:has(#button-note) + div button {
                background-image: url("https://mspoweruser.com/wp-content/uploads/2021/03/Microsoft-Notepad-new-icon.jpg");

                background-size: 200px 125px;
                width: 200px;
                height: 125px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-note"></span>', unsafe_allow_html=True)
        if st.button("Notepad",):
            subprocess.Popen("C:/Windows/notepad.exe")
            st.write(f"   ")
            keyb()
            
    st.markdown("<div class='grid-item'></div>", unsafe_allow_html=True)

    with col12:
        st.markdown(
            """
            <style>
            .element-container:has(style){
                display: none;
            }
            #button-you {
                display: none;
            }
            .element-container:has(#button-you) {
                display: none;
            }
            .element-container:has(#button-you) + div button {
                background-image: url("https://b3300814.smushcdn.com/3300814/wp-content/uploads/2023/06/YouTube-1200x675-1-1024x576.webp?lossy=2&strip=1&webp=1");

                background-size: 200px 125px;
                width: 200px;
                height: 125px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-you"></span>', unsafe_allow_html=True)
        if st.button("Youtube",):
            webbrowser.open('https://youtube.com/')
            keyb()

    with col13:
        st.markdown(
            """
            <style>
            .element-container:has(style){
                display: none;
            }
            #button-s {
                display: none;
            }
            .element-container:has(#button-s) {
                display: none;
            }
            .element-container:has(#button-s) + div button {
                background-image: url("https://th.bing.com/th/id/OIP.4Y6VPOgrQhRpFHknWmjTuwHaEK?rs=1&pid=ImgDetMain");

                background-size: 200px 125px;
                width: 200px;
                height: 125px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-s"></span>', unsafe_allow_html=True)
        if st.button("Spotify",):
            webbrowser.open('https://spotify.com/')
    
    with col21:
        st.markdown(
            """
            <style>
            .element-container:has(style){
                display: none;
            }
            #button-c {
                display: none;
            }
            .element-container:has(#button-c) {
                display: none;
            }
            .element-container:has(#button-c) + div button {
                background-image: url("https://miro.medium.com/v2/resize:fit:1358/format:webp/1*GrYJT1Whf1kpIBRUll_Bsw.png");

                background-size: 200px 125px;
                width: 200px;
                height: 125px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-c"></span>', unsafe_allow_html=True)
        if st.button("chrome",):
            webbrowser.open('https://chrome.com/')
    
    with col22:
        st.markdown(
            """
            <style>
            .element-container:has(style){
                display: none;
            }
            #button-w {
                display: none;
            }
            .element-container:has(#button-w) {
                display: none;
            }
            .element-container:has(#button-w) + div button {
                background-image: url("https://techengage.com/wp-content/uploads/2019/03/whatsapp-dark-mode-703x410.webp");

                background-size: 200px 125px;
                width: 200px;
                height: 125px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-w"></span>', unsafe_allow_html=True)
        if st.button("Whatsapp",):
            webbrowser.open('https://web.whatsapp.com/')
            keyb()

    with col23:
        st.markdown(
            """
            <style>
            .element-container:has(style){
                display: none;
            }
            #button-n {
                display: none;
            }
            .element-container:has(#button-n) {
                display: none;
            }
            .element-container:has(#button-n) + div button {
                background-image: url("https://nettv4u.com/fileman/Uploads3/Top-10-OTT-Platforms-In-India-2022/Netflix.jpg");

                background-size: 200px 125px;
                width: 200px;
                height: 125px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-n"></span>', unsafe_allow_html=True)
        if st.button("Netflix",):
            webbrowser.open('https://netflix.com/')
    
    with col31:
        st.markdown(
            """
            <style>
            .element-container:has(style){
                display: none;
            }
            #button-b {
                display: none;
            }
            .element-container:has(#button-b) {
                display: none;
            }
            .element-container:has(#button-b) + div button {
                background-image: url("https://images.gizbot.com/img/2021/12/myntra-1640001998.jpg");

                background-size: 200px 125px;
                width: 200px;
                height: 125px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-b"></span>', unsafe_allow_html=True)
        if st.button("Myntra",):
            webbrowser.open('https://myntra.com/')
    
    with col32:
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
                background-image: url(https://cn.technode.com/wp-content/blogs.dir/18/files/2020/02/swiggy.jpg);

                background-size: 200px 125px;
                width: 200px;
                height: 125px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-z"></span>', unsafe_allow_html=True)
        if st.button("Swiggy",):
            webbrowser.open('https://swiggy.com/')

    with col33:
        st.markdown(
            """
            <style>
            .element-container:has(style){
                display: none;
            }
            #button-f {
                display: none;
            }
            .element-container:has(#button-f) {
                display: none;
            }
            .element-container:has(#button-f) + div button {
                background-image: url("https://i.pinimg.com/736x/de/5e/73/de5e73c9ca4b5edf5b261389c4e9c6ad.jpg");

                background-size: 200px 125px;
                width: 200px;
                height: 125px;
                position: fixed;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-f"></span>', unsafe_allow_html=True)
        if st.button("File Explorer",):
            #webbrowser.open('C:/Windows/notepad.exe')
            subprocess.Popen("C:\Windows\explorer.exe")

    interval = 5
    continuously_check_time(interval, water)
    #check_time_thread = threading.Thread(target=continuously_check_time, args=(interval, water))
    #check_time_thread.start()


    

if __name__ == "__main__":
    main()
