from mysql_config import get_connection  # pastikan file mysql_config.py ada
import hashlib
import streamlit as st
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import re
import emoji
import time
import io
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.chart import BarChart, Reference
import tempfile

# Download required NLTK data
nltk_data_dir = "./resources/nltk_data_dir/"
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir, exist_ok=True)

nltk.data.path.clear()
nltk.data.path.append(nltk_data_dir)
nltk.download("stopwords", download_dir=nltk_data_dir)
nltk.download("punkt", download_dir=nltk_data_dir)

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.email = ""

# Fungsi untuk hashing password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Form Login/Register
if not st.session_state.logged_in:
    st.sidebar.header("🔐 Login / Register")
    form_type = st.sidebar.radio("Pilih Aksi", ["Login", "Register"])

    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if form_type == "Login":
        if st.sidebar.button("Login"):
            try:
                conn = get_connection()
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
                user = cursor.fetchone()
                if user and user["password"] == hash_password(password):
                    st.session_state.logged_in = True
                    st.session_state.email = email
                    st.success("Login berhasil!")
                    st.experimental_rerun()
                else:
                    st.error("Email atau password salah.")
            except Exception as e:
                st.error(f"Gagal login: {str(e)}")
            finally:
                cursor.close()
                conn.close()

    elif form_type == "Register":
        if st.sidebar.button("Register"):
            try:
                conn = get_connection()
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
                if cursor.fetchone():
                    st.warning("Email sudah terdaftar.")
                else:
                    cursor.execute(
                        "INSERT INTO users (email, password) VALUES (%s, %s)",
                        (email, hash_password(password))
                    )
                    conn.commit()
                    st.success("Registrasi berhasil! Silakan login.")
            except Exception as e:
                st.error(f"Gagal register: {str(e)}")
            finally:
                cursor.close()
                conn.close()

    st.stop()

# Tombol Logout setelah login
st.sidebar.caption(f"Login sebagai: {st.session_state.email}")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.email = ""
    st.experimental_rerun()

# ... [lanjutkan dengan isi analisis kamu seperti sebelumnya]
# Tempel seluruh isi analisis mulai dari `st.set_page_config` sampai akhir
