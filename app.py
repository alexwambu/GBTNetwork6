import streamlit as st
import requests
import json

# RPC nodes to fetch data from
RPC_ENDPOINTS = [
    "http://localhost:8545",
    "http://GBTNetwork:8545"
]

st.set_page_config(page_title="GBTNetwork RPC Proxy", layout="centered")
st.title("GBTNetwork RPC Proxy")

st.markdown("""
Send raw JSON-RPC requests to your local or hosted GBT blockchain nodes.
This proxy will attempt to fetch from `localhost:8545` and `GBTNetwork:8545`.
""")

payload = st.text_area("Enter JSON-RPC Payload", value='{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}', height=200)

if st.button("Send Request"):
    headers = {"Content-Type": "application/json"}
    success = False

    for url in RPC_ENDPOINTS:
        try:
            res = requests.post(url, data=payload, headers=headers, timeout=5)
            if res.status_code == 200:
                st.success(f"✅ Success from: {url}")
                st.json(res.json())
                success = True
                break
        except Exception as e:
            st.warning(f"⚠️ Failed to fetch from: {url} ({str(e)})")

    if not success:
        st.error("❌ All endpoints failed.")
