from owlready2 import *

# Tạo ontology mới
onto = get_ontology("http://example.org/criminal-law.owl")


# tất cả các lớp (classes) và quan hệ (properties) được khai báo bên trong khối "with onto" này sẽ thuộc về ontology
with onto:
     # ===================== CLASSES =====================
    class Person(Thing): pass# thing (lớp gốc - root class trong owl, các khái niệm class đều kế thừa từ thing)     
    
    class Offender(Person): pass# lớp phạm tội
    class Victim(Person): pass # Lớp nạn nhân
    class Judge(Person):pass  # Lớp thẩm phán
    class Prosecutor(Person): pass # Lớp công tố viên
    class PoliceOfficer(Person): pass # Lớp cảnh sát
    class Witness(Person): pass # Lớp nhân chứng
    class Lawyer(Person): pass # Lớp luật sư

    class DefenseAttorney(Lawyer): pass # Lớp luật sư bào chữa

    class Court(Thing): pass # Lớp toà án
    class Trial(Thing): pass # Lớp phiên toà
    class CriminalCase(Thing): pass # Lớp vụ án hình sự
    class Evidence(Thing): pass # Lớp chứng cứ
    class Location(Thing):  pass # Lớp địa điểm
    class Time(Thing): pass # Lớp thời gian
    class Date(Thing): pass # Lớp ngày
    class TimePeriod(Thing): pass # Lớp khoảng thời gian

    class LegalProvision(Thing): pass # Lớp điều luật
    class PenalCodeArticle(LegalProvision): pass # Lớp bộ luật hình sự

    class Crime(Thing): pass  # lớp tội danh

    class ViolentCrime(Crime): pass # lớp tội phạm bạo lực
    class Murder(ViolentCrime): pass # lớp tội phạm giết người
    class Assault(ViolentCrime): pass # lớp tội xâm hại

    class PropertyCrime(Crime): pass # lớp tội tài sản
    class Theft(PropertyCrime): pass # trộm
    class Robbery(PropertyCrime): pass # cướp

    class EconomicCrime(Crime): pass # lớp tội phạm kinh tế
    class Fraud(EconomicCrime): pass # lớp tội phạm gian lận
    class Corruption(EconomicCrime): pass # lớp tội phạm tham nhũng

    class CrimeSeverity(Thing): pass # lớp mức độ tội phạm
    class Intent(Thing): pass # lớp tâm lý phạm tội (cố ý, vô ý, mưu mô, hoặc lừa đảo.)
    class Organized(Intent):pass # có tổ chức

    class Punishment(Thing): pass # lớp hình phạt
    class Imprisonment(Punishment): pass # tù giam
    class Fine(Punishment): pass # phạt tiền
    class DeathPenalty(Punishment): pass # tử hình
    class Probation(Punishment): pass #  cải tạo không giam giữ
    class Sentence(Punishment): pass # bản án (gồm số năm tù, số tiền phạt, thời gian cải tạo)

 # ===================== OBJECT PROPERTIES =====================
    class commits(ObjectProperty): # người phạm tội thực hiện một tội danh nào.
        domain = [Offender]
        range = [Crime]

    class isVictimOf(ObjectProperty): # ai là nạn nhân của tội phạm nào
        domain = [Victim]
        range = [Crime]

    class isPunishedBy(ObjectProperty): # người phạm tội bị xử lý bằng hình phạt nào
        domain = [Offender]
        range = [Punishment]

    class definedIn(ObjectProperty): # tội danh này được quy định trong điều luật nào
        domain = [Crime]
        range = [LegalProvision]

    class judgedBy(ObjectProperty): # tội phạm được xét xử ở toà nào
        domain = [Crime]
        range = [Court]

    class partOfCase(ObjectProperty): # tội phạm là một phần của vụ án hình sự nào
        domain = [Crime]
        range = [CriminalCase]

    class hasEvidence(ObjectProperty): # tội phạm có những chứng cứ nào
        domain = [Crime]
        range = [Evidence]

    class witnessedBy(ObjectProperty): # tội phạm được chứng kiến bởi nhân chứng nào
        domain = [Crime]
        range = [Witness]

    class representedBy(ObjectProperty): # người phạm tội được đại diện bởi luật sư nào
        domain = [Offender]
        range = [Lawyer]

    class prosecutedBy(ObjectProperty): # tội phạm được truy tố bởi công tố viên nào
        domain = [Crime]
        range = [Prosecutor]

    class investigatedBy(ObjectProperty): # tội phạm được điều tra bởi cảnh sát nào
        domain = [Crime]
        range = [PoliceOfficer]

    class judgedInTrial(ObjectProperty): # tội phạm được xét xử trong phiên toà nào
        domain = [Crime]
        range = [Trial]

    class occurredAt(ObjectProperty): # tội phạm xảy ra tại địa điểm nào
        domain = [Crime]
        range = [Location]

    class hasSentence(ObjectProperty): # người phạm tội nhận bản án nào
        domain = [Offender]
        range = [Sentence]

    class hasSeverity(ObjectProperty): # tội phạm có mức độ nghiêm trọng nào
        domain = [Crime]
        range = [CrimeSeverity]

    class hasIntent(ObjectProperty): # tội phạm có ý định gì
        domain = [Crime]
        range = [Intent]

# ===================== DATA PROPERTIES =====================
    class hasName(DataProperty, FunctionalProperty): # tên của người, toà án, tội phạm, chứng cứ, điều luật, phiên toà, địa điểm, bản án
        domain = [Person, Court, Crime, Evidence, LegalProvision, Trial, Location, Sentence]
        range = [str]

    class hasAge(DataProperty): # tuổi của người
        domain = [Person]
        range = [int]

    class hasGender(DataProperty): # giới tính của người
        domain = [Person]
        range = [str]

    class sentenceLength(DataProperty): # độ dài bản án (số năm tù)
        domain = [Imprisonment]
        range = [int]  # số năm

    class fineAmount(DataProperty): # số tiền phạt
        domain = [Fine]
        range = [float]

    class occurredOnDate(DataProperty): # ngày xảy ra tội phạm
        domain = [Crime, Trial]
        range = [str]  # định dạng ISO yyyy-mm-dd

# # Thêm dữ liệu thật: thêm ở 1 file khác


# ===================== LƯU ONTOLOGY ra file owl =====================
onto.save(file = "criminal_law.owl", format = "rdfxml")
onto.save(file = "criminal_law_updated.owl", format = "rdfxml")
print("Ontology đã được lưu thành công!")
