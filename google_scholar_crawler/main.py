import json
from datetime import datetime
import os
from scholarly import scholarly

print("Step 1: reading GOOGLE_SCHOLAR_ID...")
scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
print(f"Scholar ID: {scholar_id}")

print("Step 2: loading author by scholar ID...")
author = scholarly.search_author_id(scholar_id)
print("Author loaded.")

print("Step 3: filling author profile (without publications)...")
author = scholarly.fill(author, sections=["basics", "indices", "counts"])
print("Author profile filled.")

author["updated"] = str(datetime.now())

print("Step 4: creating results directory...")
os.makedirs("results", exist_ok=True)

print("Step 5: writing gs_data.json...")
with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

print("Step 6: writing gs_data_shieldsio.json...")
shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(author.get("citedby", 0)),
}
with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print("Done.")
