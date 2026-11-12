# Spark Training — Ready-to-deploy local lab

**Source basis:** *KAP Pelatihan Pengolahan Data dengan Spark TA 2026* and *Jadwal Pelatihan Pengolahan Data dengan Spark TA 2026*: 16–19 November 2026, 35 JP, six official subjects. This repo extends the source material with synthesized data and practical labs; it is **not** an official redistribution of BPPK materials.

## Prerequisites

Docker Desktop / Docker Engine with Docker Compose v2, internet for the **initial image build** and PostgreSQL JDBC jar download. Allocate approximately 8–10 GB RAM to Docker on a 16 GB laptop. Tested syntactically, but runtime Docker deployment has **not** been executed in the file-generation environment. Use a trusted network; corporate proxy/Zscaler may need additional configuration and registry access.

## Start (standard)

```bash
docker compose config
docker compose up -d --build
docker compose ps
```

## Start (corporate Zscaler TLS inspection)

1. Request a verified PEM-format **corporate CA certificate** from IT/security. Place it at `jupyter/certs/zscaler.crt` (not included; do not commit sensitive/private key material).
2. Confirm its fingerprint and that build traffic can reach the image registry, Python package index, and `jdbc.postgresql.org` through company proxy if applicable.
3. Build with:

```bash
JUPYTER_DOCKERFILE=Dockerfile.zscaler docker compose build jupyter
JUPYTER_DOCKERFILE=Dockerfile.zscaler docker compose up -d
```

Dockerfile.zscaler calls `update-ca-certificates` **before** pip, sets `PIP_CERT`, `REQUESTS_CA_BUNDLE`, `SSL_CERT_FILE` and `CURL_CA_BUNDLE`, and explicitly passes `pip --cert`. No TLS bypass flags. To troubleshoot, compare image build logs and check whether proxy access is also required; trust and proxy settings are different issues. If a proxy is necessary, set Docker Desktop/Engine proxy options and compose build proxy build args as directed by IT; the CA alone does not configure routing.

## Access

| Service | Local URL | Notes |
|---|---|---|
| JupyterLab | http://localhost:8888 | Token disabled **for localhost classroom use only** |
| Spark master | http://localhost:8080 | Worker registration + application listing |
| Worker 1 | http://localhost:8081 | Workers share datasets and output mounts |
| Worker 2 | http://localhost:8082 | Workers share datasets and output mounts |
| Spark application UI | http://localhost:4040 | Available **only when Spark application active** |
| PostgreSQL | localhost:5432 | DB `training`, user/password `spark` **demo only** |

Notebook files and local working directories are writable by the container Spark user for classroom convenience; keep this archive on a trusted machine. All published ports bind to **127.0.0.1**, not the LAN. Do not expose unauthenticated Jupyter or demo database to public networks. Standalone Spark master is internal-only, not published to host.

## Classroom path

Open the six top-level notebooks in `notebooks/` in numeric order. The deck-to-notebook mapping is documented in `../materials/pptx-notebook-alignment.md`; `Ver1` and `Ver2` are alternative archives, not the primary classroom path. PostgreSQL seeds are initialized at first launch only (if the database volume is clean).

**Important:** Only one concurrently active Jupyter/CLI Spark driver is supported by this lab's fixed ports 4050/4051. Shut down the previous notebook's SparkSession (`spark.stop()`) when switching to CLI job execution. Different notebooks in the same Jupyter kernel should reuse the existing session. When in doubt, restart the kernel.

### Spark CLI jobs

```bash
docker compose exec -T jupyter python3 /home/spark/spark-app/f_taxpayers.py
docker compose exec -T jupyter python3 /home/spark/spark-app/f_payment.py
docker compose exec -T jupyter python3 /home/spark/spark-app/f_jdbc.py
```

Outputs are stored in `outputs/` on the host. These applications intentionally illustrate a lightweight ETL job layout, not an industrial orchestration framework.

### Structured Streaming live exercise

```bash
python3 scripts/reset_stream.py
# start notebook 05, and after the query.start() cell:
python3 scripts/emit_stream.py --count 20 --interval 2
```

Notebook 05 uses the bundled Spark 3.5.7 Kafka connector for the primary exercises. `f_streaming.py` remains a terminal-based file-streaming demonstration.

## Stop / reset

```bash
docker compose down
# WARNING: also deletes PostgreSQL volume/data:
docker compose down -v
```

If modifying a streaming query definition, reset its checkpoint using `python3 scripts/reset_stream.py` before starting again. Some output Parquet datasets persist under `outputs/` until manually deleted.

## Caveats and known constraints

- The Spark runtime is based on `apache/spark:3.5.7`; the Kafka connector and its transitive dependencies are resolved during image build and copied into both driver and executor images.
- NoSQL source is in the KAP but absent from initial Compose; discussed conceptually without pretending there's a deployed NoSQL database.
- The sample data is small and fictional; use it for conceptual verification, **not benchmarking**. Streaming timestamps are generated in UTC and files are atomically renamed before ingestion.
- First build needs external access for `pip` and the PostgreSQL JDBC driver. If corporate infrastructure forbids direct outbound downloads, internally mirror the wheels/JAR, amend Dockerfile accordingly, and preserve certificate validation.
- On a 16 GB laptop, do **not** run multiple individual copies of all services per participant on a single shared host without resizing. Each participant can run a copy locally.
- The 25-question bank and instructor answer key are examples created for the course; the KAP specifies the evaluation format but not exact questions.
