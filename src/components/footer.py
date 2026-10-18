# import streamlit as st

# def footer_home():
#     st.markdown("""
#     <hr>
#     <div style="
#         text-align:center;
#         color:white;
#         font-size:16px;
#         font-weight:600;">
#         © 2026 Smart AI Attendance System <br>
#         Created with ❤️ by Satendra Sharma
#     </div>
#     """, unsafe_allow_html=True)


# def footer_dashboard():
#     st.markdown("""
#     <hr>
#     <div style="
#         text-align:center;
#         color:black;
#         font-size:16px;
#         font-weight:600;">
#         © 2026 Smart AI Attendance System <br>
#         Created with ❤️ by Satendra Sharma
#     </div>
#     """, unsafe_allow_html=True)

import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)