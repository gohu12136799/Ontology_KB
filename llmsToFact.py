# import os
# from openai import OpenAI
# from owlready2 import get_ontology
# from dotenv import load_dotenv

# # Load biến môi trường từ file .env
# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=api_key)
# model = os.getenv('MODEL')

# # Load ontology schema từ file criminal_law.owl
# onto = get_ontology("criminal_law.owl").load()

# # Hàm gọi LLM để trích xuất facts
# def extract_facts_from_text(text: str) -> str:
#     prompt = f"""
#     Bạn là chuyên gia pháp lý và chuyên gia ontology.
#     Hãy phân tích đoạn văn bản sau và sinh code Python (owlready2)
#     để thêm dữ liệu (individuals và quan hệ) vào ontology pháp luật hình sự.

#     Lưu ý quan trọng:
#     - Ontology đã được load vào biến 'onto'.
#     - KHÔNG tạo ontology mới.
#     - Chỉ tạo cá thể và quan hệ bằng các lớp/thuộc tính đã có trong ontology.
#     - Các lớp có sẵn: Offender, Victim, Court, PenalCodeArticle, Murder, Imprisonment.
#     - Các quan hệ có sẵn: commits, isVictimOf, definedIn, judgedBy, isPunishedBy.
#     - Các cá thể phải được thêm trực tiếp vào 'onto'.

#     Văn bản: "{text}"

#     Trả về code Python thô, KHÔNG bao gồm ```python hoặc ``` trong câu trả lời.
#     """

#     response = client.chat.completions.create(
#         # model="gpt-4o-mini", 
#         model = model,
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0
#     )

#     return response.choices[0].message.content


# if __name__ == "__main__":
#     # Ví dụ chạy thử
#     text = "Nguyễn Văn A giết Trần Thị B. Vụ án được xét xử tại Tòa án Nhân dân Hà Nội theo Điều 123 Bộ luật Hình sự 2015. Nguyễn Văn A bị phạt tù 20 năm."
    
#     facts_code = extract_facts_from_text(text)
    
#     print("=== Code sinh ra từ LLM ===")
#     print(facts_code)
    
#     # Thực thi code sinh ra để thêm facts vào ontology
#     try:
#         # Làm sạch code (bỏ các ký hiệu ```python ... ```)
#         facts_code = facts_code.strip()
#         if facts_code.startswith("```"):
#             facts_code = facts_code.split("```")[1]
#             if "```" in facts_code:
#                 facts_code = facts_code.split("```")[0]
#             facts_code = facts_code.strip()
#         exec(facts_code, {"onto": onto, **globals()}, locals())
#     except Exception as e:
#         print(" Lỗi khi chạy code sinh ra:", e)
    
#     # In ra các cá thể hiện có để kiểm tra
#     print("\n=== Các cá thể trong ontology sau khi thêm facts ===")
#     for ind in onto.individuals():
#         print(ind)

#     # Lưu ontology schema + facts ra file mới
#     # onto.save(file="criminal_law_with_facts.owl", format="rdfxml")
#     # print("\n Đã lưu ontology với facts mới vào criminal_law_with_facts.owl")
