# Panduan Pengajar — Pelatihan Pengolahan Data dengan Spark (35 JP)

Based on the supplied 2026 KAP and schedule. Official subject names and JP are preserved; exercises, time allocations *within* sessions, lab infrastructure and synthetic datasets are supplemental training design, not original KAP content.

| Hari / waktu | Mata pelajaran | JP | Notebook / aktivitas |
|---|---|---:|---|
| Senin 16 Nov, 09:00–13:45 (with breaks) | Konsep Dasar Apache Spark | 5 | 01; architecture, DAG/lazy evaluation, UI |
| Senin 16 Nov, 13:45–17:00 (with break) | Spark Data Processing | 4 | 02; SparkSession, schemas, filter/sort |
| Selasa 17 Nov, 08:00–10:15 | Spark Data Processing (continuation) | 3 | 02; groupBy, transformations, tasks |
| Selasa 17 Nov, 10:30–17:00 (with breaks) | Data Integration dan Data Transformation | 7 | 03; CSV, TXT, JSON, Parquet, ORC, JDBC, joins |
| Rabu 18 Nov, 08:00–14:30 (with breaks) | Spark SQL dan Data Analytics | 7 | 04; SQL, functions, aggregations, analytics |
| Rabu 18 Nov, 14:30–16:15 (with break) | Spark Structured Streaming | 2 | 05; architecture, file-stream setup |
| Kamis 19 Nov, 08:00–09:30 | Spark Structured Streaming (continuation) | 2 | 05; windows, watermark, output sinks |
| Kamis 19 Nov, 09:30–14:30 (with breaks) | Spark Optimization dan Best Practices | 5 | 06; shuffle, partitions, broadcast, cache and UI |

**Official additions outside 35 JP:** 16 Nov opening 08:00–08:30 and pretest 08:30–09:00; 19 Nov posttest 14:30–15:00 and evaluation/closure 15:00–15:30.

## Facilitator run-of-show

- Before class: build images, check worker registration, test notebook 01 and PostgreSQL JDBC notebook 03, run a stream demo, reset its checkpoints and emitted files.
- Show one Spark UI observation *per module*, not just slides. Use interactive debugging and stop old notebook SparkSessions when running `spark-app` CLI jobs.
- At the end of each exercise: require a result, validation and explanation. Ask students to name the **grain** of their results and whether `join` can multiply rows.
- The capstone notebook 07 is embedded in module practice periods if time permits; it is not extra JP.
- Use Notebook 05 for the bundled Kafka labs. Verify topic initialization and connector class loading before class; no runtime Maven access is required.
- Discuss NoSQL integration conceptually or extend using an organization-approved connector/service; no NoSQL service was specified in supplied Compose.
- Pre- and post-tests: 25 closed-book MCQs, non-passing program, per KAP. A sample bank and key is provided separately.

## Suggested assessment of practical work

Completeness (30%), correctness and validation (35%), explain-plan/UI interpretation (20%), analytical explanation and limitations (15%). This rubric is an instructor proposal, not an official assessment rule.

## Critical pitfalls to demonstrate

1. Schema inference on CSV vs explicit schema.
2. `count()` triggers a job; `select()` does not.
3. Joining duplicate keys changes row counts.
4. Local host `localhost` differs from service hostname `postgres` inside Compose.
5. Workers must see input/output paths; this distribution uses shared bind mounts.
6. Each notebook should reuse an existing SparkContext; avoid simultaneous Spark applications with fixed ports 4050/4051.
7. Kafka broker is not equivalent to Spark Kafka connector availability.
8. Zscaler CA is supplied by the organization and is never shipped in the archive.
