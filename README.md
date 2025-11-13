# 📊 Analisis Nilai Siswa

Proyek ini melakukan analisis statistik dan visualisasi data nilai siswa dari berbagai mata pelajaran menggunakan Python.

## 📁 File Struktur

```
project-folder/
├── nilai_siswa.csv          # Dataset nilai siswa
├── latihan.py              # Script analisis Python
├── Screenshot (232).png    # Grafik batang rata-rata nilai
├── Screenshot (234).png    # Boxplot sebaran nilai
└── README.md               # Dokumentasi ini
```

## 📋 Dataset

Dataset `nilai_siswa.csv` berisi informasi tentang:
- **Nama**: Nama siswa
- **Matpel**: Mata pelajaran (Bahasa Indonesia, Bahasa Inggris, Matematika, Fisika, Produktif)
- **Nilai**: Nilai siswa (skala 0-100)

## 🔧 Teknologi yang Digunakan

- **Python 3**
- **Pandas** - untuk manipulasi data
- **Matplotlib** - untuk visualisasi dasar
- **Seaborn** - untuk visualisasi statistik yang lebih advanced

## 📊 Hasil Analisis

### Statistik Deskriptif
- **Rata-rata keseluruhan**: 86.36
- **Median**: 87.0
- **Modus**: 85

### Rata-rata per Mata Pelajaran
1. **Matematika**: 91.5
2. **Fisika**: 88.25  
3. **Bahasa Inggris**: 84.33
4. **Bahasa Indonesia**: 84.25
5. **Produktif**: 84.0

### Visualisasi yang Dihasilkan

1. **Bar Chart** (`Screenshot (232).png`)
   - Menampilkan perbandingan rata-rata nilai antar mata pelajaran
   - Matematika memiliki rata-rata tertinggi

2. **Boxplot** (`Screenshot (234).png`)
   - Menunjukkan sebaran nilai, median, dan outlier
   - Memvisualisasikan variasi nilai dalam setiap mata pelajaran

## 🚀 Cara Menjalankan

1. Pastikan Python dan library required terinstall:
```bash
pip install pandas matplotlib seaborn
```

2. Jalankan script:
```bash
python latihan.py
```

## 📈 Insights

- **Matematika** merupakan mata pelajaran dengan performa terbaik
- **Produktif** memiliki rata-rata terendah namun variasi nilai yang kecil
- Sebaran nilai cukup merata di semua mata pelajaran
- Tidak terdapat outlier yang signifikan dalam data

## 🎯 Tujuan Pembelajaran

Proyek ini membantu dalam:
- Pengolahan data menggunakan Pandas
- Analisis statistik deskriptif
- Visualisasi data dengan Matplotlib dan Seaborn
- Interpretasi hasil analisis data pendidikan

## 📝 Catatan

Script asli memiliki beberapa kesalahan penulisan nama mata pelajaran yang telah diperbaiki dalam analisis untuk memastikan akurasi hasil.
