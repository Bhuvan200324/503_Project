import streamlit as st

# ---------- Custom CSS ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #00c6ff;
    text-align: center;
}
.stButton>button {
    background-color: #00c6ff;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
.stButton>button:hover {
    background-color: #0072ff;
    color: white;
}
.stTextInput>div>div>input, .stNumberInput input {
    border-radius: 10px;
    padding: 10px;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background: linear-gradient(145deg, #1c1f26, #111318);
    box-shadow: 5px 5px 15px #0a0c10, -5px -5px 15px #22252c;
    margin-bottom: 20px;
}
.success-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #1e7e34;
    color: white;
}
.info-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #117a8b;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- Business Logic ----------
class BankApplication:
    bank_name = 'SBI'

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return f"✅ Withdrawn {amount} | Balance: {self.balance}"
        else:
            return "❌ Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"💰 Balance: {self.balance}"

    def update_mobile_number(self, new_number):
        self.mobile_number = new_number
        return f"📱 Updated: {self.mobile_number}"

    def check_balance(self):
        return f"🏦 Balance: {self.balance} | Bank: {BankApplication.bank_name}"

# ---------- UI ----------
st.title("🏦 Smart Bank App")

if "account" not in st.session_state:
    st.session_state.account = None

# ---------- Create Account ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("Create Account")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Name")
    acc_no = st.text_input("Account Number")

with col2:
    age = st.number_input("Age", min_value=1)
    mobile = st.text_input("Mobile Number")

balance = st.number_input("Initial Balance", min_value=0)

if st.button("Create Account"):
    st.session_state.account = BankApplication(name, acc_no, age, mobile, balance)
    st.markdown('<div class="success-box">Account Created Successfully</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Operations ----------
if st.session_state.account:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Operations")

    option = st.selectbox("Choose Operation", ["Deposit", "Withdraw", "Check Balance", "Update Mobile"])

    if option == "Deposit":
        amt = st.number_input("Enter amount", min_value=0, key="dep")
        if st.button("Deposit"):
            result = st.session_state.account.deposit(amt)
            st.markdown(f'<div class="success-box">{result}</div>', unsafe_allow_html=True)

    elif option == "Withdraw":
        amt = st.number_input("Enter amount", min_value=0, key="with")
        if st.button("Withdraw"):
            result = st.session_state.account.withdraw(amt)
            st.markdown(f'<div class="info-box">{result}</div>', unsafe_allow_html=True)

    elif option == "Check Balance":
        if st.button("Check"):
            result = st.session_state.account.check_balance()
            st.markdown(f'<div class="info-box">{result}</div>', unsafe_allow_html=True)

    elif option == "Update Mobile":
        new_mobile = st.text_input("New Mobile Number")
        if st.button("Update"):
            result = st.session_state.account.update_mobile_number(new_mobile)
            st.markdown(f'<div class="success-box">{result}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)