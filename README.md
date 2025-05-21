# MachineLearning_Travel_Insurance

**Latar Belakang**

Sebuah perusahaan asuransi perjalanan internasional menghadapi tantangan besar dalam menangani klaim pelanggan yang diajukan selama perjalanan internasional. Setiap tahunnya, puluhan ribu nasabah membeli polis untuk melindungi perjalanan mereka dari risiko seperti pembatalan, kecelakaan, atau kehilangan barang. Namun hanya sebagian kecil klaim yang benar-benar layak diproses, sementara sebagian besar tidak memenuhi kriteria kelayakan.

hal ini menimbulkan tantangan besar seperti:
- Beban kerja tinggi: verifikasi manual memakan waktu dan tenaga.
- Kualitas layanan turun: keterlambatan dalam menyetujui klaim memicu ketidakpuasan.
- Risiko finansial: pembayaran klaim tidak valid berdampak langsung pada keuangan perusahaan.
- Kurangnya akurasi: sulit mengidentifikasi klaim valid dari ribuan pengajuan.

**Problem Statement**

Bagaimana membangun model prediktif yang dapat membantu mengidentifikasi mana klaim asuransi perjalanan yang layak disetujui atau tidak dengan cepat dan efisien berdasarkan informasi dari data historis polis.

**Goals**
- Otomatisasi penilaian klaim untuk menghemat waktu dan biaya operasional.
- Meningkatkan akurasi prediksi klaim valid berdasarkan data historis.
- Mengurangi risiko kerugian dari pembayaran klaim tidak valid.
- Memberikan pelayanan lebih cepat dan adil kepada pelanggan.

**Analytical Approach**

- Exploratory Data Analysis (EDA): Menjelajahi distribusi data, deteksi imbalance, dan pola klaim.
- Data Preprocessing: Mempersiapkan data dengan baik agar bisa digunakan untuk pemodelan.
- Pemodelan Machine Learning : Membangun beberapa model klasifikasi (Logistic Regression, Random Forest, XGBoost, LGBM) dan mengevaluasi performanya dengan cross-validation dan ROC AUC.
- Feature Importance & Interpretasi: Menggali fitur mana yang paling banyak berkontribusi terhadap keputusan klaim.
- Exporting Best Model & Rekomendasi: Menyimpan model terbaik dan memberikan strategi implementasi.

**Kesimpulan Berdasarkan Hasil Classification Report (Setelah Tuning):**
1.  Class 0 – Tidak Berhak untuk Klaim:
- Model menunjukkan performa yang sangat baik dalam mengidentifikasi pelanggan yang tidak berhak menerima klaim, dengan precision sempurna (1.00). Hal ini berarti seluruh prediksi terhadap kategori ini dapat dipercaya sepenuhnya.
Selain itu, recall sebesar 0.60 menunjukkan bahwa model mampu mengenali sebagian besar dari mereka yang memang tidak berhak, dengan ruang untuk peningkatan agar dapat menangkap lebih banyak kasus serupa. F1-score sebesar 0.75 menandakan keseimbangan yang cukup baik antara presisi dan sensitivitas.

2. Class 1 – Berhak untuk Klaim:
- Model memiliki recall tinggi sebesar 0.94, menandakan kemampuannya yang sangat kuat dalam mendeteksi hampir seluruh klaim yang benar-benar valid. Ini menjadi keunggulan tersendiri, khususnya dalam konteks layanan pelanggan dan keadilan pemberian klaim.
Meskipun nilai precision masih berada di angka 0.07, hal ini membuka peluang bagi pengembangan lanjutan untuk memperbaiki akurasi dalam memprediksi klaim yang benar-benar sah, misalnya melalui penyesuaian threshold atau metode penyeimbangan data.
