# file lấy đoạn văn bản từ list_list_law_texts.py, gọi LLM để tạo triples RDF/OWL, và lưu vào file triples.ttl

import os
from openai import OpenAI
from owlready2 import get_ontology
from dotenv import load_dotenv
import list_law_texts  

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
model = os.getenv('MODEL')
onto = get_ontology("criminal_law_updated.owl").load()

OUTPUT_FILE = "triples.ttl"

# Xoá file cũ nếu tồn tại
if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

for attr in dir(list_law_texts):
    if attr.startswith("law_"):
        law_text = getattr(list_law_texts, attr)  # lấy nội dung điều luật

        prompt = f"""
Bạn là chuyên gia RDF/OWL. Tôi có ontology pháp luật với các class và property sau:

Classes:
- Crime
- LegalProvision
- Condition
- Punishment
...

Object properties:
- definedIn (Crime → LegalProvision)
- hasCondition (Crime → Condition)
- isPunishedBy (Crime → Punishment)
...

Data property:
- hasText (LegalProvision → string)
...

Prefix trong Turtle:
@prefix ns1: <http://example.org/criminal-law.owl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

Nhiệm vụ:
Từ đoạn văn bản luật dưới đây, tạo các instance của class đã khai báo, gán property phù hợp, và xuất ra Turtle hợp lệ (.ttl).  
- Tạo tên instance hợp lý dựa trên số điều luật và nội dung (ví dụ: Article13, Crime_DrunkOffense).  
- Chỉ trả kết quả Turtle, không giải thích.
- xoá ```turtle ở đầu và ``` ở cuối nếu có.

Văn bản luật:
\"\"\"{law_text}\"\"\"
"""

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        ttl_text = response.choices[0].message.content.strip()

        # Append vào file
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(ttl_text + "\n\n")

print(f"Đã tạo file {OUTPUT_FILE} với tất cả điều luật thành công!")
