"""Deterministically rebuild the fictional training data (no personal data)."""
import csv
import datetime
import json
import random
from pathlib import Path

out = Path(__file__).resolve().parents[1] / 'datasets'
out.mkdir(exist_ok=True)
rng = random.Random(2026)
regions = ['Jakarta', 'Bandung', 'Surabaya', 'Medan', 'Semarang']
sectors = ['Retail', 'Manufacturing', 'Services', 'Technology']

def write_csv(filename, rows):
    with (out / filename).open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

taxpayers = [{
    'taxpayer_id': f'TP{i:04d}', 'taxpayer_name': f'Entitas Sintetis {i:04d}',
    'region': regions[i % 5], 'sector': sectors[i % 4],
    'registration_year': str(2017 + i % 9),
    'active': 'true' if i % 13 else 'false'
} for i in range(1, 301)]
write_csv('taxpayers.csv', taxpayers)

payments = []
for i in range(1, 1801):
    payments.append({
        'payment_id': f'PAY{i:06d}', 'taxpayer_id': f'TP{rng.randint(1, 300):04d}',
        'payment_date': (datetime.date(2026, 1, 1) + datetime.timedelta(days=rng.randrange(300))).isoformat(),
        'amount': rng.choice([100000, 250000, 500000, 1500000, 3000000, 12000000]),
        'channel': rng.choice(['Bank', 'Online', 'Counter']),
        'status': 'VOID' if i % 29 == 0 else 'PAID'
    })
write_csv('payments.csv', payments)
with (out / 'filings.jsonl').open('w', encoding='utf-8') as f:
    for i in range(1, 501):
        record = {
            'filing_id': f'FIL{i:05d}', 'taxpayer_id': f'TP{rng.randint(1, 300):04d}',
            'tax_year': 2025, 'filing_type': rng.choice(['Annual', 'Monthly']),
            'declared_amount': rng.randint(1, 600) * 100000,
            'metadata': {'source': 'simulated', 'batch': i % 5}
        }
        f.write(json.dumps(record, ensure_ascii=False) + '\n')
print('Generated 300 taxpayers, 1800 payments and 500 filings')
