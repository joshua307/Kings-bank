import streamlit as st

def render_homepage(savings, current):
    st.title("🏦 KINGS BANK")
    st.markdown("#### View Balances")
    col1, col2 = st.columns(2)
    col1.metric("💰 Savings Balance", f"₦{savings.get_balance():,.2f}")
    col2.metric("💳 Current Balance", f"₦{current.get_balance():,.2f}")

    st.divider()
    st.markdown("### 🧾 Transactions")

    with st.form("transaction_form"):
        action = st.selectbox("Select Action", ["Deposit", "Withdraw"])
        account_type = st.selectbox("Account Type", ["Savings", "Current"])
        amount = st.number_input("Amount", min_value=0, step=100)
        submitted = st.form_submit_button("Submit")

        if submitted:
            if account_type == "Savings":
                result = savings.deposit(amount) if action == "Deposit" else savings.withdraw(amount)
            else:
                result = current.deposit(amount) if action == "Deposit" else current.withdraw(amount)
            st.success(result)
