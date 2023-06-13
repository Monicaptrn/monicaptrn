import streamlit as st
import numpy as np
from scipy.stats import f


def variance_test(var1, var2):
    # Menghitung jumlah observasi dan derajat kebebasan
    n1, n2 = len(var1), len(var2)
    df1, df2 = n1 - 1, n2 - 1

    # Menghitung varians
    var1, var2 = np.var(var1, ddof=1), np.var(var2, ddof=1)

    # Menghitung rasio varians
    f_ratio = var1 / var2

    # Menghitung nilai p-value
    p_value = f.sf(f_ratio, df1, df2)

    return f_ratio, p_value


# Tampilan web menggunakan Streamlit
st.title("Uji Varians untuk Dua Variabel")

# Input data variabel pertama
var1 = st.text_input(
    "Masukkan data variabel pertama (dipisahkan dengan koma)",
    "0.86, 0.82, 0.75, 0.61, 0.89, 0.64, 0.81, 0.68, 0.65",
)

# Input data variabel kedua
var2 = st.text_input(
    "Masukkan data variabel kedua (dipisahkan dengan koma)",
    "0.84, 0.74, 0.63, 0.55, 0.76, 0.70, 0.69, 0.57, 0.53",
)

# Mengubah input menjadi array
var1 = np.array([float(x.strip()) for x in var1.split(",")])
var2 = np.array([float(x.strip()) for x in var2.split(",")])

# Hipotesis
st.write("Ho: var1 = var2")
st.write("H1: var1 != var2")
st.write("Alpha = 5% = 0.05s")

# Memastikan jumlah observasi yang sama
if len(var1) != len(var2):
    st.warning("Jumlah observasi pada kedua variabel harus sama.")
else:
    # Menghitung rasio varians dan nilai p-value
    f_ratio, p_value = variance_test(var1, var2)

    # Menampilkan hasil
    st.write("Rasio Varians:", f_ratio)
    st.write("Nilai p-value:", p_value)
    if p_value < 0.05:
        st.write("Keputusan: Hipotesis nol ditolak.")
        st.write(
            "Kesimpulan: Terdapat perbedaan yang signifikan antara varians kedua variabel."
        )
    else:
        st.write("Hipotesis nol diterima.")
        st.write(
            "Kesimpulan: Tidak terdapat perbedaan yang signifikan antara varians kedua variabel."
        )
