# file dùng để query, test câu hỏi: "Tội say rượu bị xử lý thế nào?"
from rdflib import Graph, Namespace, URIRef
import re

# 1. Load ontology
g = Graph()
g.parse("triples.ttl", format="turtle")


ns1 = Namespace("http://example.org/criminal-law.owl#")

# 2. Simple keyword mapping (có thể mở rộng)
keywords_to_crime = {
    "say rượu": "Crime_DrunkOffense",
    "rượu bia": "Crime_DrunkOffense",
    "trộm": "Theft",
    "giết người": "Murder",
    "lừa đảo": "Fraud",
    "tham nhũng": "Corruption",
    "thiệt hại nghiêm trọng": "Crime_VoI_GayThietHai",
    "mất khả năng nhận thức": "Condition_LossOfControl",
    "mất khả năng điều khiển hành vi": "Condition_LossOfControl",
}

# 3. Hàm nhận câu hỏi và tìm crime instance
def find_crime_instance(question):
    question = question.lower()
    for keyword, crime in keywords_to_crime.items():
        if re.search(r"\b" + re.escape(keyword) + r"\b", question):
            return crime
    return None

# 4. Hàm truy vấn SPARQL cho crime đã tìm được
def query_crime(crime_name):
    crime_uri = f"ns1:{crime_name}"
    query = f"""
    PREFIX ns1: <http://example.org/criminal-law.owl#>
    SELECT ?lawText ?condition ?punishment
    WHERE {{
        {crime_uri} a ns1:Crime ;
            ns1:definedIn ?law ;
            ns1:hasCondition ?condition ;
            ns1:isPunishedBy ?punishment .
        ?law ns1:hasText ?lawText .
    }}
    """
    results = []
    for row in g.query(query):
        results.append({
            "lawText": str(row.lawText),
            "condition": str(row.condition),
            "punishment": str(row.punishment)
        })
    return results

# 5. Nhận input từ user
user_question = input("Nhập câu hỏi của bạn về tội phạm: ")

crime_instance = find_crime_instance(user_question)
if crime_instance:
    results = query_crime(crime_instance)
    if results:
        for r in results:
            print("\n--- Kết quả ---")
            print("Nội dung luật:\n", r["lawText"])
            print("Điều kiện:", r["condition"])
            print("Hình phạt:", r["punishment"])
    else:
        print("Không tìm thấy thông tin trong ontology.")
else:
    print("Không nhận diện được tội nào phù hợp với câu hỏi.")
