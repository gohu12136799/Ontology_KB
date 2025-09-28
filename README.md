## Hướng dẫn cài đặt Ontology

### 1. Tạo môi trường ảo (virtualenv)

python3 -m venv venv
source venv/bin/activate # Mac/Linux

### 2. Cài thư viện RDFLib và Owlready2 (dùng thư viện này khi code python),openai

pip install rdflib owlready2 <!--nếu chưa cài -->
pip install openai python-dotenv <!--nếu chưa cài -->

### 3. Sau khi tạo các quan hệ, thuộc tính, class như định nghĩa ở dưới, chạy lệnh sau

python3 tên_file.py // lệnh này sẽ tạo ra file owl, dùng file owl để vào potege để xem trực quan, truy vấn và suy luận.

#### 1. Các khái niệm của Ontology

Classes: mô hình hóa khái niệm (Person, Disease, Doctor, Hospital, …).

ObjectProperty: mô hình hóa quan hệ giữa các thực thể (ví dụ: Person --has_disease--> Disease).

DataProperty: gán thuộc tính dữ liệu (ví dụ: tuổi, tên, độ nặng).

Individuals: John, Flu, Fever, Tamiflu… là các cá thể cụ thể.

#### 2. Truy vấn: khi có file owl. tạo file query.py để truy vấn và file reasoner.py để suy luận

chạy: python3 file_name.py,

có 2 cách để viết truy vấn trong python: 1. Truy vấn trực tiếp bằng Python API 2. Truy vấn bằng SPARQL
Owlready2 tích hợp một SPARQL engine đơn giản để có thể viết câu query giống như trong RDF/OWL chuẩn.

#### 3. Owlready2 đúng là thư viện Python, được viết bằng Python

#### 4. khi gọi tới reasoner (sync_reasoner_pellet) Owlready2 không tự viết engine suy luận bằng Python, Nó chỉ là wrapper để gọi Pellet Reasoner (Java) chạy ở dưới.

do đó cần cài thêm Java Runtime: brew install openjdk@17
kiểm tra: java -version
