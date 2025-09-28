import os
from openai import OpenAI
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Khởi tạo client OpenAI
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Câu hỏi từ người dùng
user_question = """
Nếu như có một người bắt giữ trái pháp luật hai nạn nhân, trong đó có một người dưới 18 tuổi,
thì liệu mức hình phạt áp dụng sẽ là gì và có bị cấm đảm nhiệm chức vụ không nhỉ?
"""

# Prompt chuẩn hóa câu hỏi
prompt = f"""
Bạn là chuyên gia pháp luật và lập trình Python.
Nhiệm vụ: Viết lại câu hỏi pháp luật dưới dạng chuẩn, rõ ràng, dễ hiểu,
giữ nguyên ý nghĩa, loại bỏ từ ngữ thừa hoặc không chính thức.

Trả về duy nhất câu hỏi đã chuẩn hóa, KHÔNG trả về JSON hay code Python.

Câu hỏi cần chuẩn hóa:
{user_question}
"""

# Gọi OpenAI API
response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)

# Lấy câu hỏi đã chuẩn hóa
normalized_question = response.choices[0].message.content.strip()

# In ra màn hình
print("Câu hỏi đã chuẩn hóa:")
print(normalized_question)

# Lưu vào file text nếu muốn
# with open("normalized_question.txt", "w", encoding="utf-8") as f:
#     f.write(normalized_question)

# print("Đã lưu câu hỏi chuẩn hóa vào normalized_question.txt")
