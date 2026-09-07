#!/usr/bin/env python3
import csv
from collections import defaultdict
from pathlib import Path

# Use paths relative to this script so it works from any working directory
BASE = Path(__file__).resolve().parent
INPUT = BASE / 'data' / 'sales.csv'
OUTPUT = BASE / 'report.html'

def load_sales(path):
    rows = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            r['quantity'] = int(r['quantity'])
            r['price'] = float(r['price'])
            r['total'] = r['quantity'] * r['price']
            rows.append(r)
    return rows

def summarize(rows):
    by_region = defaultdict(float)
    total = 0.0
    for r in rows:
        by_region[r['region']] += r['total']
        total += r['total']
    return total, by_region

def write_report(total, by_region, rows, outpath):
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write('<html><head><meta charset="utf-8"><title>Sales Report</title></head><body>')
        f.write(f'<h1>Sales Report</h1>')
        f.write(f'<p>Total sales: ${total:,.2f}</p>')
        f.write('<h2>By Region</h2><ul>')
        for r, amt in by_region.items():
            f.write(f'<li>{r}: ${amt:,.2f}</li>')
        f.write('</ul>')
        f.write('<h2>Recent Orders</h2><table border="1" cellpadding="4"><tr><th>order_id</th><th>date</th><th>region</th><th>product</th><th>quantity</th><th>price</th><th>total</th></tr>')
        for row in rows[-10:]:
            f.write('<tr>')
            f.write(f"<td>{row['order_id']}</td><td>{row['date']}</td><td>{row['region']}</td><td>{row['product']}</td><td>{row['quantity']}</td><td>${row['price']:.2f}</td><td>${row['total']:.2f}</td>")
            f.write('</tr>')
        f.write('</table></body></html>')

def main():
    rows = load_sales(INPUT)
    total, by_region = summarize(rows)
    write_report(total, by_region, rows, OUTPUT)
    print(f'Wrote {OUTPUT}')

if __name__ == '__main__':
    main()
