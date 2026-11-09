from pathlib import Path
root=Path(__file__).resolve().parents[1]
for p in (root/'stream-input').glob('event_*.json'):p.unlink()
for p in (root/'outputs').glob('stream_checkpoint*'):
 import shutil
 if p.is_dir():shutil.rmtree(p)
print('Stream demo files/checkpoints reset.')
