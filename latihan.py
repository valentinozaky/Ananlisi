import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('nilai_siswa.csv')
print(data.info())
print(data.head())
print(data.describe())

print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])
 
matematika = data[data['Matpel'] == 'Matematika']
print(matematika)

bahasa_Inggris = data[data['Matpel'] == 'Inggris']
print(bahasa_Inggris)

bahasa_Indonesia = data[data['Matpel'] == 'Indonesia']
print(bahasa_Indonesia)

produktif = data[data['Matpel'] == 'Produktif']
print(produktif)

data.groupby('Matpel')['Nilai'].agg(['max','min'])

rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar', color=['blue', 'orange', 'green', 'red'])
plt.title('Rata-Rata Nilai per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.tight_layout()
plt.show()

# "Mapel mana yang memiliki rata-rata nilai tertinggi? Mapel Matematika memiliki rata-rata nilai tertinggi dibandingkan dengan mapel lainnya."
# "Mapel mana yang memiliki nilai terendah? Mapel Produktif memiliki nilai terendah dibandingkan dengan mapel lainnya."
# "Bagaimana visualisasi membantu dalam memahami data? Visualisasi seperti grafik batang dan boxplot membantu dalam memahami distribusi nilai, rata-rata, serta variasi nilai antar mata pelajaran dengan lebih jelas dan intuitif."
# "Apa hal baru yang kamu pelajari dari kegiatan analisis dan visualisasi data? Saya belajar menggunakan library Python (Pandas, Seaborn, Matplotlib) untuk meringkas data statistik (mean, median, modus) dan membuat grafik informatif secara otomatis dari dataset."
# "Kesulitan apa yang kamu alami dalam membuat grafik? Awalnya kesulitan memahami sintaks untuk mengatur label sumbu, judul, dan warna grafik. Kesalahan penulisan nama variabel (seperti "Matpel" vs "Mapel") juga sempat menyebabkan error."
# "Menurtu kamu AI apa membantu dalam analysis sebuah data? Menurut saya, AI sangat membantu dalam analisis data karena dapat memproses data dalam jumlah besar dengan cepat, mengidentifikasi pola yang mungkin tidak terlihat oleh manusia, serta memberikan wawasan yang berharga untuk pengambilan keputusan."
