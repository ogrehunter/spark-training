"""Emit new JSON event files for Structured Streaming (run from host)."""
import json, pathlib, time, datetime, random, argparse
p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=12);p.add_argument('--interval',type=float,default=2.0);a=p.parse_args()
out=pathlib.Path(__file__).resolve().parents[1]/'stream-input'
out.mkdir(exist_ok=True)
rng=random.Random(401)
for i in range(a.count):
 event={'event_id':f'EVT{i:05d}','taxpayer_id':f'TP{rng.randint(1,30):04d}','event_time':datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),'amount':rng.randint(1,50)*100000,'channel':rng.choice(['Bank','Online'])}
 tmp=out/f'.event_{i:05d}.tmp';final=out/f'event_{i:05d}.json';tmp.write_text(json.dumps(event)+'\n');tmp.rename(final)
 print('Emitted',final.name,flush=True);time.sleep(a.interval)
