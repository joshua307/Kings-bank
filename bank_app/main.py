import streamlit as st
from accounts.savings_account import SavingsAccount
from accounts.current_account import CurrentAccount
from homepage import render_homepage

# Create account instances
if 'savings' not in st.session_state:
    st.session_state.savings = SavingsAccount()

if 'current' not in st.session_state:
    st.session_state.current = CurrentAccount()

# Render homepage
render_homepage(st.session_state.savings, st.session_state.current)
