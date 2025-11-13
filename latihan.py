import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')
print(data.head())
print(data.info())
print(data.describe())

print("rata-rata:", data['Nilai'].mean())
print("median:",data ['Nilai'].median())
print("modus:",data ['Nilai'].mode()[0])

matematika = data[data['Matpel'] == 'Matematika']
print("matematika")

bahasa_inggris = data[data['Matpel'] == 'Bahasa Inggris']
print("bahasa inggris")

data.groupby('Matpel')['Nilai'].agg(['max','min'])
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Matpel')
plt.xlabel('Matpel')
plt.ylabel('Nilai Rata-Rata')
plt.show()


"Mapel mana yang memiliki rata-rata nilai tertinggi? Mapel Matematika memiliki rata-rata nilai tertinggi dibandingkan dengan mapel lainnya."
"Mapel mana yang memiliki nilai terendah? Mapel Produktif memiliki nilai terendah dibandingkan dengan mapel lainnya."
"Bagaimana visualisasi membantu dalam memahami data? Visualisasi seperti grafik batang dan boxplot membantu dalam memahami distribusi nilai, rata-rata, serta variasi nilai antar mata pelajaran dengan lebih jelas dan intuitif."
"Apa hal baru yang kamu pelajari dari kegiatan analisis dan visualisasi data? Saya belajar bagaimana menggunakan pandas untuk analisis data dasar dan matplotlib serta seaborn untuk visualisasi data, yang membantu dalam interpretasi hasil analisis dengan cara yang lebih mudah dipahami."
"Kesulitan apa yang kamu alami dalam membuat grafik? Salah satu kesulitan yang saya alami adalah memilih jenis grafik yang paling sesuai untuk data yang saya miliki agar informasi yang ingin disampaikan dapat tersampaikan dengan efektif."
"Menurtu kamu AI apa membantu dalam analysis sebuah data? Menurut saya, AI sangat membantu dalam analisis data karena dapat memproses data dalam jumlah besar dengan cepat, mengidentifikasi pola yang mungkin tidak terlihat oleh manusia, serta memberikan wawasan yang berharga untuk pengambilan keputusan."

