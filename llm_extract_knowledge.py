# # file này sử dụng llms để trích xuất tri thức từ văn bản luật, chưa dùng tới
# """
# Step1: Gọi LLM để tự động trích xuất Entities & Relations từ đoạn văn bản luật.
# Tên file gợi ý: step1_llm_extract_law.py
# """

# import os
# import json
# import re
# from typing import Dict, Any
# from dotenv import load_dotenv

# from openai import OpenAI

# # # ======= CẤU HÌNH ========
# # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  
# # MODEL = "gpt-4o-mini"  
# # openai.api_key = OPENAI_API_KEY
# # # =========================


# # Load biến môi trường từ file .env
# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")
# model = os.getenv('MODEL')

# client = OpenAI(api_key=api_key)


# # đầu vào: đoạn luật
# law_text = """
# Người nào giết người thì bị phạt tù từ 12 năm đến 20 năm, tù chung thân hoặc tử hình.
# Phạm tội trong các trường hợp: giết nhiều người, giết phụ nữ có thai, giết trẻ em...
# """

# # Prompt thiết kế để LLM tự phát hiện Entities & Relations
# PROMPT_TEMPLATE = """
# Bạn là một hệ thống trích xuất tri thức pháp luật. 
# Nhiệm vụ: đọc đoạn văn bản luật dưới đây và **tự động phát hiện** tất cả các
# thực thể (Entities) và quan hệ (Relations) giữa chúng. 

# Yêu cầu bắt buộc:
# 1. Chỉ trả về **một** JSON hợp lệ (KHÔNG kèm giải thích).
# 2. JSON phải theo schema sau:
# {{
#   "Entities": {{
#       "<EntityType1>": ["EntityA", "EntityB", ...],
#       "<EntityType2>": [...]
#   }},
#   "Relations": [
#       {{ "subject": "<EntityName>", "predicate": "<relation>", "object": "<EntityName>" }},
#       ...
#   ],
#   "Notes": "optional text (short) about ambiguities"  // not required, may omit
# }}
# 3. Các thực thể và mối quan hệ **PHẢI bằng tiếng Anh**. Entity names nên là dạng token ngắn, CamelCase hoặc snake_case (không chứa dấu phẩy).
# 4. Nếu phát hiện điều luật / khoản / điều, thì tạo entity type "LegalProvision" với mã (vd: Article123_PenalCode2015).
# 5. Nếu không chắc, ghi vào "Notes" (không bắt buộc).

# Đoạn văn bản luật:
# \"\"\"{law_text}\"\"\"
# """

# def call_llm_and_get_json(law_text: str, max_retries: int = 2) -> Dict[str, Any]:
#     prompt = PROMPT_TEMPLATE.format(law_text=law_text)
#     for attempt in range(max_retries + 1):
#         resp = client.chat.completions.create(
#             model=model,
#             messages=[
#                 {"role": "system", "content": "Bạn là trợ lý AI chuyên trích xuất tri thức từ văn bản pháp luật."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0,
#             max_tokens=1000
#         )
#         # text = resp.choices[0].message["content"].strip()
#         text = resp.choices[0].message.content

#         # Thử tách JSON từ text (phòng trường hợp LLM kèm chú thích)
#         json_text = extract_json_text(text)
#         if not json_text:
#             # Nếu không có JSON, thử next attempt
#             if attempt < max_retries:
#                 continue
#             else:
#                 raise ValueError("LLM không trả về JSON hợp lệ. Output:\n" + text)

#         try:
#             data = json.loads(json_text)
#             # basic validation
#             if "Entities" in data and "Relations" in data:
#                 return data
#             else:
#                 # nếu thiếu key, thử tiếp
#                 if attempt < max_retries:
#                     continue
#                 else:
#                     raise ValueError("JSON trả về thiếu key 'Entities' hoặc 'Relations'.\n" + json_text)
#         except json.JSONDecodeError:
#             if attempt < max_retries:
#                 continue
#             else:
#                 raise

# def extract_json_text(text: str) -> str:
#     """
#     Cố gắng trích JSON từ text bằng regex tìm dấu ngoặc nhọn lớn nhất.
#     """
#     # tìm block bắt đầu bằng { và kết thúc bằng }, lấy block dài nhất hợp lệ
#     matches = re.findall(r"\{(?:.|\n)*\}", text)
#     if not matches:
#         return None
#     # chọn block dài nhất, sau đó kiểm tra parse được không
#     matches_sorted = sorted(matches, key=len, reverse=True)
#     for candidate in matches_sorted:
#         try:
#             json.loads(candidate)
#             return candidate
#         except Exception:
#             continue
#     return None

# def normalize_entities(data: Dict[str, Any]) -> Dict[str, Any]:
#     """
#     Một bước hậu xử lý: chuyển tên entity về dạng phù hợp (loại bỏ ký tự lạ, chuẩn hoá khoảng trắng).
#     """
#     entities = data.get("Entities", {})
#     norm = {}
#     for etype, elist in entities.items():
#         clean_list = []
#         for e in elist:
#             e_clean = re.sub(r"[^\w\s\-]", "", e).strip().replace(" ", "_")  # simple cleanup
#             clean_list.append(e_clean)
#         norm[etype] = list(dict.fromkeys(clean_list))  # remove duplicates, giữ thứ tự
#     data["Entities"] = norm
#     return data

# def main():
#     data = call_llm_and_get_json(law_text)
#     data = normalize_entities(data)
#     print("=== Extracted knowledge ===")
#     print(json.dumps(data, indent=2, ensure_ascii=False))

#     # Ghi ra file để bước sau dùng
#     with open("extracted_knowledge_article123.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)

# if __name__ == "__main__":
#     main()
