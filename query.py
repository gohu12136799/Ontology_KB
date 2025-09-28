# truy vấn viết ở đây
from owlready2 import *

# Load ontology đã tạo trước đó
onto = get_ontology("health.owl").load()

# --- 1. Truy vấn trực tiếp bằng Python API ---
# --- 1.1 Truy vấn individuals ---
print("Danh sách Person:")
for person in onto.Person.instances():
    print("-", person)


