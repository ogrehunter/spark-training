# Paket Lab Pelatihan Pengolahan Data dengan Spark TA 2026

Paket ini dibuat agar praktik mengikuti urutan dan kompetensi pada enam presentasi training.

## Notebook

1. `01_Lab_Konsep_Dasar_Apache_Spark.ipynb`  
   Arsitektur, partition/task, lazy evaluation, DAG, execution plan, Spark UI.
2. `02_Lab_Spark_Data_Processing.ipynb`  
   DataFrame dasar, select/filter/sort, null/cast, kategori, agregasi, mini-case.
   - Demo instruktur terpisah: `demo/02_Demo_Spark_Data_Processing.ipynb` untuk seluruh slide DEMONSTRASI di Deck 02.
3. `03_Lab_Data_Integration_dan_Transformation.ipynb`  
   CSV/JSON/Parquet/ORC, schema, data quality, JDBC, join/union, lineage, curated dataset.
4. `04_Lab_Spark_SQL_dan_Data_Analytics.ipynb`  
   SQL vs DataFrame, built-ins, aggregation, window, KPI, plan, mini project.
5. `05_Lab_Spark_Structured_Streaming.ipynb`  
   Rate/file streaming, progress, event time, window, watermark, checkpoint, Kafka preflight.
   - Demo instruktur terpisah: `demo/05_Demo_Spark_Structured_Streaming.ipynb` untuk seluruh slide DEMO di Deck 05.
6. `06_Lab_Spark_Optimization_dan_Best_Practices.ipynb`  
   Baseline/evidence, reduce-before-shuffle, broadcast join, shuffle partitions, cache, skew.

## Menjalankan

```bash
docker compose up -d --build
```

Buka JupyterLab di `http://localhost:8888`. Copy notebook ke folder `notebooks/` pada project training bila paket diekstrak di luar folder project.

UI yang digunakan saat lab:
- Spark Master: `http://localhost:8080`
- Worker 1: `http://localhost:8081`
- Worker 2: `http://localhost:8082`
- Spark Application UI: `http://localhost:4040` selama aplikasi aktif

## Catatan dependency

- **JDBC PostgreSQL:** notebook Topik 3 melakukan preflight `org.postgresql.Driver`. Untuk kelas offline, JDBC JAR sebaiknya sudah dibake ke image driver/executor.
- **Kafka:** connector `spark-sql-kafka-0-10_2.12:3.5.7` beserta dependency transitif dibundel ke image driver dan executor saat build. Notebook Topik 5 tidak mengunduh Maven package saat kelas.
- **JDBC PostgreSQL:** Notebook 03 membaca `public.taxpayer_reference`; kegagalan JDBC diperlakukan sebagai kegagalan environment, bukan diganti diam-diam dengan fallback sintetis.

## Pola fasilitasi

Gunakan ritme: **prediksi → jalankan → amati → jelaskan**. Pada Topik 6, wajib catat evidence sebelum dan sesudah perubahan agar optimasi tidak berubah menjadi trial-and-error.
