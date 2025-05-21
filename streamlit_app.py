import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open(r"travel_insurance_best_model.sav", 'rb'))

st.title("🧳 Prediksi Klaim Asuransi Perjalanan")

st.markdown("""
Aplikasi ini memprediksi apakah **klaim asuransi** kemungkinan akan disetujui atau tidak.
Anda dapat:
- Mengisi data secara manual, **atau**
- Mengunggah file **CSV** untuk prediksi banyak data sekaligus.
""")

# Tab: Pilihan input
tab1, tab2 = st.tabs(["📝 Input Manual", "📁 Upload CSV"])

# --- TAB 1: MANUAL ---
with tab1:
    with st.form("form_manual"):
        col1, col2 = st.columns(2)

        with col1:
            agency = st.selectbox("Agency", ['ADM', 'ART', 'C2B', 'CBH', 'CCR', 'CSR', 'CWT', 'JZI', 'KML', 'LWC', 'RAB', 'TST', 'TTW'])
            agency_type = st.selectbox("Agency Type", ['Travel Agency', 'Airlines'])
            distribution_channel = st.selectbox("Distribution Channel", ['Online', 'Offline'])
            product_name = st.selectbox("Product Name", [
                '24 Protect', 'Annual Gold Plan', 'Annual Silver Plan','Annual Travel Protect Gold', 'Annual Travel Protect Platinum',
                'Annual Travel Protect Silver', 'Basic Plan', 'Bronze Plan', 'Child Comprehensive Plan', 'Comprehensive Plan',
                'Gold Plan', 'Individual Comprehensive Plan', 'Premier Plan', 'Rental Vehicle Excess Insurance',
                'Silver Plan', 'Single Trip Travel Protect Gold', 'Single Trip Travel Protect Platinum',
                'Single Trip Travel Protect Silver', 'Spouse or Parents Comprehensive Plan', 'Travel Cruise Protect',
                'Travel Cruise Protect Family', 'Value Plan'
            ])

        with col2:
            destination = st.selectbox("Destination", [
                'Angola', 'Argentina', 'Australia', 'Austria', 'Bahrain','Bangladesh', 'Belarus', 'Belgium', 'Bhutan', 'Brazil',
                'Brunei Darussalam', 'Bulgaria', 'Cambodia', 'Canada', 'China', 'Croatia', 'Cyprus', 'Czech Republic',
                'Denmark', 'Egypt', 'Estonia', 'Finland', 'France', 'Germany', 'Guinea', 'Hong Kong', 'Hungary', 'India',
                'Indonesia', 'Iran, Islamic Republic Of', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kenya',
                'Korea, Republic Of', "Lao People's Democratic Republic", 'Macao', 'Malaysia', 'Mali', 'Mauritius',
                'Mongolia', 'Morocco', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Norway', 'Oman',
                'Pakistan', 'Papua New Guinea', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Russian Federation',
                'Singapore', 'South Africa', 'Spain', 'Sri Lanka', 'Sweden', 'Switzerland', 'Taiwan, Province Of China',
                'Thailand', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'United Kingdom', 'United States', 'Viet Nam'
            ])
            duration = st.number_input("Durasi Perjalanan (hari)",  min_value=0, value=0)
            age = st.number_input("Usia Pelanggan", min_value=0, value=0)
            net_sales = st.number_input("Net Sales ($)", min_value=-100.0, value=0.0)
            commission = st.number_input("Commission Value ($)", min_value=0.0, value=0.0)

        submit_manual = st.form_submit_button("Prediksi Manual")

    if submit_manual:
        input_df = pd.DataFrame([{
            "Agency": agency,
            "Agency Type": agency_type,
            "Distribution Channel": distribution_channel,
            "Product Name": product_name,
            "Destination": destination,
            "Duration": duration,
            "Age": age,
            "Net Sales": net_sales,
            "Commision (in value)": commission
        }])

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        st.subheader("📊 Hasil Prediksi")
        if prediction == 1:
            st.success(f"✅ Klaim Anda kemungkinan **DISETUJUI**")
        else:
            st.error(f"❌ Klaim Anda kemungkinan **TIDAK DISETUJUI**")
        st.markdown(f"**Probabilitas Disetujui:** {probability:.2%}")

# --- TAB 2: CSV UPLOAD ---
with tab2:
    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

    if uploaded_file:
        csv_data = pd.read_csv(uploaded_file)

        # Validasi kolom
        expected_columns = ['Agency', 'Agency Type', 'Distribution Channel',
                            'Product Name', 'Destination', 'Duration', 'Age',
                            'Net Sales', 'Commision (in value)']

        if all(col in csv_data.columns for col in expected_columns):
            st.success("✅ File diterima. Siap melakukan prediksi.")

            predictions = model.predict(csv_data)
            probabilities = model.predict_proba(csv_data)[:, 1]

            csv_data['Claim Prediction'] = ["Disetujui" if p == 1 else "Tidak Disetujui" for p in predictions]
            csv_data['Probabilitas Klaim (%)'] = (probabilities * 100).round(2)

            # Statistik hasil
            total = len(predictions)
            approved = (predictions == 1).sum()
            rejected = (predictions == 0).sum()
            approved_pct = approved / total * 100
            rejected_pct = rejected / total * 100

            st.subheader("📊 Ringkasan Prediksi")
            st.markdown(f"""
            - Total Data: **{total}**
            - ✅ Disetujui: **{approved}** ({approved_pct:.2f}%)
            - ❌ Tidak Disetujui: **{rejected}** ({rejected_pct:.2f}%)
            """)

            st.markdown("### 🔍 Detail Prediksi")
            st.dataframe(csv_data[['Agency', 'Product Name', 'Destination', 'Claim Prediction', 'Probabilitas Klaim (%)']])

            # Unduh hasil
            csv_result = csv_data.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Hasil Prediksi", csv_result, "hasil_prediksi.csv", "text/csv")
        else:
            st.error(f"❌ Kolom tidak sesuai. Pastikan file memiliki kolom berikut:\n{expected_columns}")
