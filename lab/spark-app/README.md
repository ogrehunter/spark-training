## Running Spark Applications

Open a terminal in JupyterLab and navigate to the Spark application directory:

```bash
cd /home/spark/spark-app
```

Submit each application to the Spark standalone cluster:

```bash
spark-submit --master spark://spark-master:7077 f_taxpayers.py
spark-submit --master spark://spark-master:7077 f_payment.py
spark-submit --master spark://spark-master:7077 f_jdbc.py
```

Run one application at a time during the exercises to avoid resource contention. Stop active notebook SparkSessions when they are no longer needed.

### Structured Streaming

Start the streaming application in one JupyterLab terminal:

```bash
spark-submit --master spark://spark-master:7077 f_streaming.py
```

Open a second terminal and run the event producer:

```bash
cd /home/spark
python3 scripts/emit_stream.py
```

Stop the streaming application using `Ctrl+C`.

### Monitoring

Use the Spark web interfaces to inspect execution:

- **Spark Master UI:** http://localhost:8080
- **Spark Application UI:** http://localhost:4040 (while the application is running)

### Execution Architecture

- The Jupyter container runs the Spark driver in client deployment mode.
- The Spark master schedules work across the worker containers.
- Spark executors run on the worker containers.
- Application files are stored in `/home/spark/spark-app`.
- Files that executors must access directly need to be available at the appropriate paths on the workers, or distributed using Spark's file distribution mechanisms.