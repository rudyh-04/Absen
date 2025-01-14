import streamlit as st
import pandas as pd
import numpy as np
import csv
from PIL import Image
from datetime import datetime

st.title('Welcome')
st.image('Pentachem.jpg')

st.header('Absensi')
st.subheader('Supply Chain Departement')
st.subheader('Cikarang Plant')
st.text('JI. Industri Selatan 1, Blok OO No.3G. JABABEKA Phase II')

#fungsi untuk menyimpan data ke csv
def save_data(df):
    df.to_csv("absen.'csv', mode='w', header=false, index=false")
    
# Data pengguna (username dan password)
usernames = ['user1', 'user2']
passwords = ['password1', 'password2']
names = ['User    One', 'User    Two']

    # Inisialisasi data absensi
if 'absensi_data' not in st.session_state:
        st.session_state.absensi_data = []

    # Form untuk input absensi
with st.form(key='absensi_form'):
        nama = st.text_input("Nama:")
        tanggal_masuk = st.date_input("Tanggal Masuk:", datetime.today())
        jam_masuk = st.time_input("Jam Masuk:")
        tanggal_keluar = st.date_input("Tanggal Keluar:", datetime.today())
        jam_keluar = st.time_input("Jam Keluar:")

        # Hitung lembur
        lembur = 0
        if tanggal_keluar and jam_keluar and tanggal_masuk and jam_masuk:
            # Menghitung total jam kerja
            masuk = datetime.combine(tanggal_masuk, jam_masuk)
            keluar = datetime.combine(tanggal_keluar, jam_keluar)
            total_jam_kerja = (keluar - masuk).total_seconds() / 3600  # dalam jam
            
            # Asumsi lembur jika total jam kerja lebih dari 8 jam
            lembur = max(0, total_jam_kerja - 9)
            keterangan_lembur = st.text_input("Keterangan Lembur:")

        lembur_checkbox = st.checkbox("Lembur (jam):", value=lembur)

        submit_button = st.form_submit_button(label='Save')

        if submit_button:
            # Menyimpan data absensi
            absensi_entry = {
                'Nama': nama,
                'Tanggal Masuk': tanggal_masuk,
                'Jam Masuk': jam_masuk,
                'Tanggal Keluar': tanggal_keluar,
                'Jam Keluar': jam_keluar,
                'Lembur (jam)': lembur,
                'Keterangan Lembur': keterangan_lembur
            }
            st.session_state.absensi_data.append(absensi_entry)
            st.success("Data absensi berhasil disimpan!")

    # Simpan data ke file CSV
        df = pd.DataFrame(st.session_state.absensi_data)
        df.to_csv('absensi_data.csv', index=False)  # Simpan ke file CSV

save-data(df)
st.success("Data absensi berhasil disimpan")

    # Menampilkan data absensi
if st.session_state.absensi_data:
        st.subheader("Data Absensi")
        df = pd.DataFrame(st.session_state.absensi_data)
        st.dataframe(df)
    st.write(absensi_data)

        # Fitur untuk mengedit data
        edit_index = st.selectbox("Pilih entri untuk diedit:", range(len(st.session_state.absensi_data)), format_func=lambda x: f"{st.session_state.absensi_data[x]['Nama']} - {st.session_state.absensi_data[x]['Tanggal Masuk']}")

        if st.button("Edit"):
            selected_entry = st.session_state.absensi_data[edit_index]
            nama_edit = st.text_input("Nama:", value=selected_entry['Nama'])
            tanggal_masuk_edit = st.date_input("Tanggal Masuk:", value=selected_entry['Tanggal Masuk'])
            jam_masuk_edit = st.time_input("Jam Masuk:", value=selected_entry['Jam Masuk'])
            tanggal_keluar_edit = st.date_input("Tanggal Keluar:", value=selected_entry['Tanggal Keluar'])
            jam_keluar_edit = st.time_input("Jam Keluar:", value=selected_entry['Jam Keluar'])
            
             # Hitung lembur
            lembur_edit = 0
            if tanggal_keluar_edit and jam_keluar_edit and tanggal_masuk_edit and jam_masuk_edit:
                masuk = datetime.combine(tanggal_masuk_edit, jam_masuk_edit)
                keluar = datetime.combine(tanggal_keluar_edit, jam_keluar_edit)
                total_jam_kerja = (keluar - masuk).total_seconds() / 3600  # dalam jam
                lembur_edit = max(0, total_jam_kerja - 9)

            if st.button("Simpan Perubahan"):
                # Memperbarui data absensi
                st.session_state.absensi_data[edit_index] = {
                    'Nama': nama_edit,
                    'Tanggal Masuk': tanggal_masuk_edit,
                    'Jam Masuk': jam_masuk_edit,
                    'Tanggal Keluar': tanggal_keluar_edit,
                    'Jam Keluar': jam_keluar_edit,
                    'Lembur': lembur_edit
                }
                st.success("Data absensi berhasil diperbarui!")

        # Fitur untuk mengunduh data ke CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Unduh Data Absensi",
            data=csv,
            file_name='absensi_data.csv',
            mime='text/csv',
        )



