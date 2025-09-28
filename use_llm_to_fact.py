# file này để import các đoạn văn bản luật thành code Python owlready2 (fact.py)

# # file moi
# import os
# from openai import OpenAI
# from owlready2 import get_ontology
# from dotenv import load_dotenv
# from law_texts import law_158
# # Load biến môi trường từ file .env
# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=api_key)
# model = os.getenv('MODEL')
# onto = get_ontology("criminal_law_updated.owl").load()

# # Đoạn văn bản pháp luật cần chuyển thành cá thể và quan hệ trong ontology
# law_text = law_158

# prompt = f"""
# Bạn là chuyên gia lập trình Python và ontology pháp luật.  
# Nhiệm vụ: Chuyển văn bản pháp luật sau thành code Python sử dụng owlready2.  

# Yêu cầu:
# 1. Chỉ trả về code Python, không giải thích gì.
# 2. Tất cả comment phải ở dạng: # ===================== <Tên phần> =====================, gồm đầy đủ nội dung như: Điều luật, tội danh, hình phạt, Mức độ nghiêm trọng và ý định,Tình tiết tăng nặng
# 3. Sử dụng ontology đã có sẵn trong "criminal_law_updated.owl".
# 4. Tạo cá thể cho: Điều luật, Tội danh, Hình phạt, Mức độ nghiêm trọng, Ý định, Tình tiết tăng nặng.
# 5. Gán tên cho các cá thể bằng .hasName.
# 6. Sử dụng .append() cho các thuộc tính không phải FunctionalProperty.
# 7. Code phải sẵn sàng chèn vào file fact.py, bỏ chữ python, from, import hay lưu các thay đổi.
# 8. thêm tiền tố onto. trước mỗi lớp để tham chiếu đúng đến ontology đã load.
# 9.xoá ```python và ``` nếu có trong câu trả lời.

# **Văn bản pháp luật:**

# {law_text}
# """

# response = client.chat.completions.create(
#     model=model,
#     messages=[{"role":"user","content":prompt}],
#     temperature=1
# )

# print(response.choices[0].message.content)
# code_python = response.choices[0].message.content

# with open("fact.py", "a", encoding="utf-8") as f:
#     f.write("\n\n")  # thêm khoảng trống trước khi chèn
#     f.write(code_python)

# print("Đã append code Python vào file fact.py thành công!")
import os
from openai import OpenAI
from owlready2 import get_ontology
from dotenv import load_dotenv
import law_texts  # import cả module
# Load biến môi trường từ file .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
model = os.getenv('MODEL')
onto = get_ontology("criminal_law_updated.owl").load()

# Lặp qua tất cả biến bắt đầu bằng "law_" trong module law_texts
for attr in dir(law_texts):
    if attr.startswith("law_"):
        law_text = getattr(law_texts, attr)  # lấy nội dung điều luật

        prompt = f"""
Bạn là chuyên gia lập trình Python và ontology pháp luật.  
Nhiệm vụ: Chuyển văn bản pháp luật sau thành code Python sử dụng owlready2.  

Yêu cầu:
1. Chỉ trả về code Python, không giải thích gì.
2. Tất cả comment phải ở dạng: # ===================== <Tên phần> =====================, gồm đầy đủ nội dung như: Điều luật, tội danh, hình phạt, Mức độ nghiêm trọng và ý định,Tình tiết tăng nặng
3. Sử dụng ontology đã có sẵn trong "criminal_law_updated.owl". các lớp ontology hiện có như onto.Person : Người

onto.Offender : Người phạm tội (kế thừa Person)

onto.Victim : Nạn nhân (kế thừa Person)

onto.Judge : Thẩm phán (kế thừa Person)

onto.Prosecutor : Công tố viên (kế thừa Person)

onto.PoliceOfficer : Cảnh sát (kế thừa Person)

onto.Witness : Nhân chứng (kế thừa Person)

onto.Lawyer : Luật sư (kế thừa Person)

onto.DefenseAttorney : Luật sư bào chữa (kế thừa Lawyer)

onto.Court : Tòa án

onto.Trial : Phiên tòa

onto.CriminalCase : Vụ án hình sự

onto.Evidence : Bằng chứng

onto.Location : Địa điểm

onto.Time : Thời gian

onto.Date : Ngày

onto.TimePeriod : Khoảng thời gian

onto.LegalProvision : Điều khoản pháp luật

onto.PenalCodeArticle : Điều luật (kế thừa LegalProvision)

onto.Crime : Tội danh

onto.ViolentCrime : Tội bạo lực (kế thừa Crime)

onto.Murder : Giết người (kế thừa ViolentCrime)

onto.Assault : Tấn công (kế thừa ViolentCrime)

onto.PropertyCrime : Tội phạm về tài sản (kế thừa Crime)

onto.Theft : Trộm cắp (kế thừa PropertyCrime)

onto.Robbery : Cướp (kế thừa PropertyCrime)

onto.EconomicCrime : Tội phạm kinh tế (kế thừa Crime)

onto.Fraud : Gian lận (kế thừa EconomicCrime)

onto.Corruption : Tham nhũng (kế thừa EconomicCrime)

onto.CrimeSeverity : Mức độ nghiêm trọng

onto.Intent : Ý định / tình tiết tăng nặng

onto.Punishment : Hình phạt

onto.Imprisonment : Hình phạt tù (kế thừa Punishment)

onto.Fine : Phạt tiền (kế thừa Punishment)

onto.DeathPenalty : Tử hình (kế thừa Punishment)

onto.Probation : Cải tạo / treo (kế thừa Punishment)

onto.Sentence : Bản án (kế thừa Punishment)
4. Tạo cá thể cho: Điều luật, Tội danh, Hình phạt, Mức độ nghiêm trọng, Ý định, Tình tiết tăng nặng.
5. Gán tên cho các cá thể bằng .hasName.
6. Sử dụng .append() cho các thuộc tính không phải FunctionalProperty.
7. Code phải sẵn sàng chèn vào file fact.py, bỏ chữ python, from, import hay lưu các thay đổi.
8. thêm tiền tố onto. trước mỗi lớp để tham chiếu đúng đến ontology đã load.
9. Xoá ```python và ``` nếu có trong câu trả lời.

**Văn bản pháp luật:**

{law_text}
"""
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=1
        )

        code_python = response.choices[0].message.content
        print(code_python)
        # Append vào fact.py
        with open("fact.py", "a", encoding="utf-8") as f:
            f.write("\n\n")  # thêm khoảng trống trước khi chèn
            f.write(code_python)

        print(f"Đã append code Python cho {attr} vào file fact.py")
