# Pemetaan PPTX dan Notebook Utama

Enam notebook top-level adalah jalur praktik resmi. Folder `Ver1`, `Ver2`, dan `.ipynb_checkpoints` bukan bagian dari pemetaan ini.

| Modul | Slide praktik | Notebook | Bukti selesai |
|---|---:|---|---|
| 01 — Konsep Dasar | 27–45 | `01_Lab_Konsep_Dasar_Apache_Spark.ipynb`, Labs 1–5 | Cluster teridentifikasi; partition/task, lazy evaluation, `Exchange`, dan eksperimen partisi dapat dijelaskan. |
| 02 — Data Processing | 17, 28, 36, 43, 48–50 | `02_Lab_Spark_Data_Processing.ipynb`, Labs 1–5 | Transformasi dasar, quality handling, agregasi, dan mini case menghasilkan validasi yang diharapkan. |
| 03 — Integration | 13, 27, 36, 48, 57–58 | `03_Lab_Data_Integration_dan_Transformation.ipynb`, Labs 1–5 | CSV/TXT-JSON diselaraskan, JDBC membaca `taxpayer_reference`, join mempertahankan grain, dan curated/quarantine terbentuk. |
| 04 — SQL Analytics | 57–62 | `04_Lab_Spark_SQL_dan_Data_Analytics.ipynb`, Labs 1–5 + mini project | KPI dan window benar, insight memiliki keterbatasan, dan plan menunjukkan satu `Scan csv`. |
| 05 — Streaming | 37–40 | `05_Lab_Spark_Structured_Streaming.ipynb`, Labs 1–3 + capstone | Progress rate source terbaca, Kafka offset meningkat, checkpoint resume, dan watermark/state teramati. |
| 06 — Optimization | 52–58 | `06_Lab_Spark_Optimization_dan_Best_Practices.ipynb`, Labs 1–6 | Setiap rekomendasi memiliki baseline, evidence, satu perubahan, verifikasi, dan trade-off. |

## Prasyarat

- Jalankan `docker compose up -d --build` dari `lab/`.
- Gunakan Spark 3.5.7, dua worker, PostgreSQL, dan Kafka yang disediakan Compose.
- Connector Kafka Spark SQL dibundel ketika image dibangun; runtime kelas tidak mengunduh package Maven.
- Modul 03 memakai shared local filesystem: input di `/home/spark/datasets`, output di `/home/spark/outputs`.
- HDFS bukan prasyarat enam notebook utama; gunakan latihan HDFS terpisah bila diperlukan.

## Aturan Fasilitasi

1. Prediksi hasil sebelum action.
2. Jalankan dan validasi jumlah baris, schema, atau checksum.
3. Cocokkan physical plan dengan Spark UI pada minimal satu lab per modul.
4. Minta peserta menjelaskan hasil dan keterbatasannya, bukan hanya menunjukkan output.
5. Hentikan semua streaming query sebelum meninggalkan Notebook 05.
