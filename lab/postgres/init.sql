CREATE TABLE IF NOT EXISTS taxpayer_reference (
  taxpayer_id VARCHAR(12) PRIMARY KEY,
  taxpayer_name VARCHAR(100) NOT NULL,
  region VARCHAR(30) NOT NULL,
  sector VARCHAR(30) NOT NULL
);
INSERT INTO taxpayer_reference (taxpayer_id,taxpayer_name,region,sector) VALUES
('TP0001','PT Contoh Nusantara','Jakarta','Retail'),
('TP0002','CV Simulasi Barat','Bandung','Manufacturing'),
('TP0003','PT Latihan Timur','Surabaya','Services'),
('TP0004','PT Demo Selatan','Jakarta','Technology'),
('TP0005','CV Sampel Utara','Medan','Retail'),
('TP0006','PT Praktik Raya','Semarang','Manufacturing')
ON CONFLICT (taxpayer_id) DO NOTHING;
CREATE TABLE IF NOT EXISTS payment_summary (
  taxpayer_id VARCHAR(12) PRIMARY KEY,
  payment_total BIGINT NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
