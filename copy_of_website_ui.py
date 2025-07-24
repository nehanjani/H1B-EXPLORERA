import streamlit as st

# Competitive H-1B Sponsors
competitive_companies = {
    "Technology": [
        "Amazon", "Google", "Microsoft", "Meta", "Apple",
        "IBM", "Intel", "Oracle", "NVIDIA", "Salesforce",
        "Cisco", "Uber", "Lyft", "ServiceNow", "VMware",
        "Palantir", "Adobe", "Stripe", "Airbnb", "Pinterest"
    ],
    "Finance": [
        "JPMorgan Chase", "Goldman Sachs", "Citigroup", "Capital One", "Morgan Stanley",
        "Bank of America", "Wells Fargo", "UBS", "Fidelity", "Barclays",
        "American Express", "PayPal", "Visa", "Mastercard", "Charles Schwab",
        "Bloomberg", "BlackRock", "Discover", "HSBC", "SoFi"
    ],
    "Healthcare": [
        "UnitedHealth Group", "CVS Health", "Pfizer", "Moderna", "Roche",
        "Thermo Fisher", "IQVIA", "AbbVie", "GE Healthcare", "Amgen",
        "Eli Lilly", "Bristol Myers Squibb", "Novartis", "GSK", "Merck & Co",
        "Siemens Healthineers", "Medtronic", "Boston Scientific", "Becton Dickinson", "DaVita"
    ],
    "Consulting": [
        "Deloitte", "EY", "PwC", "KPMG", "Accenture",
        "Cognizant", "TCS", "Infosys", "Capgemini", "HCL",
        "Wipro", "IBM Consulting", "Bain & Company", "McKinsey & Company", "BCG",
        "ZS Associates", "Genpact", "LTI", "Slalom Consulting", "Booz Allen Hamilton"
    ]
}

# Less Competitive H-1B Sponsors (Different 20)
non_competitive_companies = {
    "Technology": [
        "Amplitude", "Alteryx", "Elastic", "Braze", "C3.ai",
        "MongoDB", "Confluent", "HashiCorp", "GitLab", "DigitalOcean",
        "NetApp", "Freshworks", "Sprinklr", "Outreach", "Segment",
        "BigCommerce", "Dataiku", "Looker", "Cockroach Labs", "HackerRank"
    ],
    "Finance": [
        "Zest AI", "Upstart", "LendUp", "ClearBank", "Kabbage",
        "Affirm", "Brex", "Chime", "Blend", "Robinhood",
        "Tala", "Varo Bank", "Plaid", "Greenlight", "Current",
        "Nova Credit", "Stash", "Ramp", "Petal", "TrueAccord"
    ],
    "Healthcare": [
        "Flatiron Health", "Clarify Health", "Health Catalyst", "CureMD", "Redox",
        "Zocdoc", "Tempus", "Ginger", "Spring Health", "Carbon Health",
        "Cityblock Health", "Color Genomics", "Butterfly Network", "Babylon Health", "Cue Health",
        "Bright Health", "Oscar Health", "Headspace Health", "CareRev", "Collectly"
    ],
    "Consulting": [
        "Tiger Analytics", "Fractal Analytics", "Mu Sigma", "ZS Associates", "Thorogood",
        "Brillio", "LatentView", "AbsolutData", "Bridgei2i", "Cartesian",
        "EXL Service", "Mindtree", "Virtusa", "Sonata Software", "Savigent",
        "Trianz", "SG Analytics", "Neudesic", "NIIT Technologies", "Utegration"
    ]
}

# Streamlit App UI
st.set_page_config(page_title="H-1B Sponsor Explorer", layout="centered")
st.title("🌎 H-1B Sponsoring Companies Explorer")

tab1, tab2 = st.tabs(["🏆 Top Competitive Sponsors", "🧠 Less Competitive Sponsors"])

# Tab 1 – Competitive
with tab1:
    st.header("Top Competitive H-1B Sponsors by Domain")
    domain = st.selectbox("Select a Domain", list(competitive_companies.keys()), key="competitive")
    st.subheader(f"Top Sponsors in {domain}")
    for company in competitive_companies[domain]:
        st.markdown(f"✅ {company}")

# Tab 2 – Less Competitive
with tab2:
    st.header("Less Competitive H-1B Sponsors by Domain")
    domain_nc = st.selectbox("Select a Domain", list(non_competitive_companies.keys()), key="noncompetitive")
    st.subheader(f"Less Competitive Sponsors in {domain_nc}")
    for company in non_competitive_companies[domain_nc]:
        st.markdown(f"🔹 {company}")
