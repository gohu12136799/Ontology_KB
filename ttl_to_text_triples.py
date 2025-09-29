# file này dùng để lấy nội dung từ file ttl chuyển thành bộ 3, sau đó lưu vào triples_output.txt

from rdflib import Graph, Namespace, RDF, URIRef, Literal

# Load file TTL
g = Graph()
g.parse("triples.ttl", format="turtle")

ns1 = Namespace("http://example.org/criminal-law.owl#")

triples = []
for i, (s, p, o) in enumerate(g):
    # Chỉ lấy local name (không in full URI)
    def shorten(x):
        if isinstance(x, URIRef):
            return x.split("#")[-1]
        elif isinstance(x, Literal):
            return f"\"{x}\""
        else:
            return str(x)

    triples.append(f"T{i+1}: ({shorten(s)}, {shorten(p)}, {shorten(o)})")

# In ra console
for t in triples:
    print(t)

# Lưu ra file
with open("triples_output.txt", "w", encoding="utf-8") as f:
    for t in triples:
        f.write(t + "\n")

print("✅ Đã lưu kết quả vào triples_output.txt")
