import streamlit as st
import pandas as pd
import json
import time
import os

st.set_page_config(page_title="IMMORTAL SOC", layout="wide", page_icon="🛡️")

st.markdown("<h1 style='text-align: center; color: #4AF626;'>🛡️ IMMORTAL NETWORK: OMNI-SOC</h1>", unsafe_allow_complete_html=True)

# Sidebar Metrics
st.sidebar.title("System Status")
st.sidebar.success("MESH ONLINE")
st.sidebar.metric("Agents Active", "10/10")

col_log, col_chart = st.columns([2, 1])

def load_logs():
    if os.path.exists("data/logs/system_audit.json"):
        with open("data/logs/system_audit.json", "r") as f:
            try:
                return pd.DataFrame(json.load(f))
            except:
                return pd.DataFrame()
    return pd.DataFrame()

while True:
    df = load_logs()
    with col_log:
        st.subheader("🤖 Live Agent Intelligence")
        if not df.empty:
            st.dataframe(df.tail(15), use_container_width=True, hide_index=True)
    
    with col_chart:
        st.subheader("📊 Activity Distribution")
        if not df.empty:
            st.bar_chart(df['sender'].value_counts())
            
    time.sleep(2)
    st.rerun()