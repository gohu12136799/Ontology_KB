
# file này được generate tự động từ use_llm_to_fact.py
from owlready2 import *

# Load ontology đã có
onto = get_ontology("criminal_law_updated.owl").load()

with onto:
    # ===================== Điều luật =====================
    article152 = onto.PenalCodeArticle("Article152")
    article152.hasName = "Điều 152. Tội đánh tráo người dưới 01 tuổi"

    # ===================== Tội danh =====================
    baby_swap = onto.Crime("BabySwap")
    baby_swap.hasName = "Đánh tráo người dưới 01 tuổi"
    baby_swap.definedIn.append(article152)

    # ===================== Hình phạt =====================
    # Khoản 1: 2-5 năm tù
    imprison_2_5 = onto.Imprisonment("Imprisonment_2_5")
    imprison_2_5.hasName = "Phạt tù 2-5 năm"
    imprison_2_5.sentenceLength.append(2) 
    baby_swap.isPunishedBy.append(imprison_2_5)

    # Khoản 2: 3-7 năm tù, với tình tiết tăng nặng
    imprison_3_7 = onto.Imprisonment("Imprisonment_3_7")
    imprison_3_7.hasName = "Phạt tù 3-7 năm (có tình tiết tăng nặng)"
    imprison_3_7.sentenceLength.append(3)
    baby_swap.isPunishedBy.append(imprison_3_7)

    # Khoản 3: 7-12 năm tù, với tình tiết nghiêm trọng hơn
    imprison_7_12 = onto.Imprisonment("Imprisonment_7_12")
    imprison_7_12.hasName = "Phạt tù 7-12 năm (tái phạm nguy hiểm hoặc tính chất chuyên nghiệp)"
    imprison_7_12.sentenceLength.append(7)
    baby_swap.isPunishedBy.append(imprison_7_12)

    # Khoản 4: phạt tiền 10-50 triệu
    fine_10_50 = onto.Fine("Fine_10_50")
    fine_10_50.hasName = "Phạt tiền 10-50 triệu"
    fine_10_50.fineAmount.append(10000000)
    baby_swap.isPunishedBy.append(fine_10_50)

    # ===================== Mức độ nghiêm trọng và ý định =====================
    severe = onto.CrimeSeverity("Severe")
    severe.hasName = "Nghiêm trọng"
    baby_swap.hasSeverity.append(severe)

    intent_deliberate = onto.Intent("DeliberateIntent")
    intent_deliberate.hasName = "Cố ý"
    baby_swap.hasIntent.append(intent_deliberate)

    # ===================== Tình tiết tăng nặng =====================
    # Tạo subclasses của Intent nếu muốn chi tiết
    organized = onto.Intent("Organized")
    organized.hasName = "Có tổ chức"
    baby_swap.hasIntent.append(organized)

    abuse_trust = onto.Intent("AbuseTrust")
    abuse_trust.hasName = "Lợi dụng chức vụ, quyền hạn, nghề nghiệp hoặc chăm sóc người dưới 1 tuổi"
    baby_swap.hasIntent.append(abuse_trust)

    repeat_offense = onto.Intent("RepeatOffense")
    repeat_offense.hasName = "Phạm tội 2 lần trở lên"
    baby_swap.hasIntent.append(repeat_offense)

# điều 153
# ===================== Điều luật =====================
    article153 = onto.PenalCodeArticle("Article153")
    article153.hasName = "Điều 153. Tội chiếm đoạt người dưới 16 tuổi"

    # ===================== Tội danh =====================
    child_abduction = onto.Crime("ChildAbduction")
    child_abduction.hasName = "Chiếm đoạt người dưới 16 tuổi"
    child_abduction.definedIn.append(article153)

    # ===================== Hình phạt =====================
    # Khoản 1: 3-7 năm tù
    imprison_3_7 = onto.Imprisonment("Imprisonment_3_7")
    imprison_3_7.hasName = "Phạt tù 3-7 năm"
    imprison_3_7.sentenceLength.append(3)
    child_abduction.isPunishedBy.append(imprison_3_7)

    # Khoản 2: 5-10 năm tù, với tình tiết tăng nặng
    imprison_5_10 = onto.Imprisonment("Imprisonment_5_10")
    imprison_5_10.hasName = "Phạt tù 5-10 năm (tình tiết tăng nặng)"
    imprison_5_10.sentenceLength.append(5)
    child_abduction.isPunishedBy.append(imprison_5_10)

    # Khoản 3: 10-15 năm tù, với tình tiết nghiêm trọng
    imprison_10_15 = onto.Imprisonment("Imprisonment_10_15")
    imprison_10_15.hasName = "Phạt tù 10-15 năm (tình tiết nghiêm trọng)"
    imprison_10_15.sentenceLength.append(10)
    child_abduction.isPunishedBy.append(imprison_10_15)

    # Khoản 4: phạt tiền 10-50 triệu
    fine_10_50 = onto.Fine("Fine_10_50_Article153")
    fine_10_50.hasName = "Phạt tiền 10-50 triệu"
    fine_10_50.fineAmount.append(10000000)
    child_abduction.isPunishedBy.append(fine_10_50)

    # ===================== Mức độ nghiêm trọng và ý định =====================
    severe = onto.CrimeSeverity("Severe")
    severe.hasName = "Nghiêm trọng"
    child_abduction.hasSeverity.append(severe)

    deliberate_intent = onto.Intent("DeliberateIntent")
    deliberate_intent.hasName = "Cố ý"
    child_abduction.hasIntent.append(deliberate_intent)

    # ===================== Tình tiết tăng nặng =====================
    organized = onto.Intent("Organized")
    organized.hasName = "Có tổ chức"
    child_abduction.hasIntent.append(organized)

    abuse_trust = onto.Intent("AbuseTrust")
    abuse_trust.hasName = "Lợi dụng chức vụ, quyền hạn, nghề nghiệp"
    child_abduction.hasIntent.append(abuse_trust)

    care_responsibility = onto.Intent("CareResponsibility")
    care_responsibility.hasName = "Đối với người mà mình có trách nhiệm chăm sóc, nuôi dưỡng"
    child_abduction.hasIntent.append(care_responsibility)

    multiple_victims = onto.Intent("MultipleVictims")
    multiple_victims.hasName = "Đối với từ 02 người đến 05 người"
    child_abduction.hasIntent.append(multiple_victims)

    repeat_offense = onto.Intent("RepeatOffense")
    repeat_offense.hasName = "Phạm tội 02 lần trở lên"
    child_abduction.hasIntent.append(repeat_offense)

    mental_disorder_11_45 = onto.Intent("MentalDisorder11_45")
    mental_disorder_11_45.hasName = "Gây rối loạn tâm thần và hành vi 11%-45%"
    child_abduction.hasIntent.append(mental_disorder_11_45)

    serious_injury_31 = onto.Intent("SeriousInjury31")
    serious_injury_31.hasName = "Gây thương tích >= 31%"
    child_abduction.hasIntent.append(serious_injury_31)

    professional = onto.Intent("Professional")
    professional.hasName = "Có tính chất chuyên nghiệp"
    child_abduction.hasIntent.append(professional)

    multiple_victims_6 = onto.Intent("MultipleVictims6")
    multiple_victims_6.hasName = "Đối với 06 người trở lên"
    child_abduction.hasIntent.append(multiple_victims_6)

    mental_disorder_46 = onto.Intent("MentalDisorder46")
    mental_disorder_46.hasName = "Gây rối loạn tâm thần và hành vi >= 46%"
    child_abduction.hasIntent.append(mental_disorder_46)

    victim_death = onto.Intent("VictimDeath")
    victim_death.hasName = "Làm nạn nhân chết"
    child_abduction.hasIntent.append(victim_death)

    dangerous_repeat = onto.Intent("DangerousRepeat")
    dangerous_repeat.hasName = "Tái phạm nguy hiểm"
    child_abduction.hasIntent.append(dangerous_repeat)


# ===================== Điều luật =====================
onto.penal_code_article_157 = onto.PenalCodeArticle(hasName="Điều 157. Tội bắt, giữ hoặc giam người trái pháp luật")

# ===================== Tội danh =====================
onto.crime_illegal_detention = onto.Crime(hasName="Tội bắt, giữ hoặc giam người trái pháp luật")

# ===================== Hình phạt =====================
onto.punishment_probation = onto.Probation(hasName="Cải tạo không giam giữ đến 03 năm")
onto.punishment_imprisonment1 = onto.Imprisonment(hasName="Phạt tù từ 06 tháng đến 03 năm")
onto.punishment_imprisonment2 = onto.Imprisonment(hasName="Phạt tù từ 02 năm đến 07 năm")
onto.punishment_imprisonment3 = onto.Imprisonment(hasName="Phạt tù từ 05 năm đến 12 năm")

# ===================== Mức độ nghiêm trọng =====================
onto.crime_severity1 = onto.CrimeSeverity(hasName="Mức độ nghiêm trọng từ 06 tháng đến 03 năm")
onto.crime_severity2 = onto.CrimeSeverity(hasName="Mức độ nghiêm trọng từ 02 năm đến 07 năm")
onto.crime_severity3 = onto.CrimeSeverity(hasName="Mức độ nghiêm trọng từ 05 năm đến 12 năm")

# ===================== Ý định =====================
onto.intent_organization = onto.Intent(hasName="Phạm tội có tổ chức")
onto.intent_abuse_power = onto.Intent(hasName="Lợi dụng chức vụ, quyền hạn")
onto.intent_public_official = onto.Intent(hasName="Đối với người thi hành công vụ")
onto.intent_repeat_offense = onto.Intent(hasName="Phạm tội 02 lần trở lên")
onto.intent_multiple_victims = onto.Intent(hasName="Đối với 02 người trở lên")
onto.intent_vulnerable_persons = onto.Intent(hasName="Đối với người dưới 18 tuổi, phụ nữ mà biết là có thai, người già yếu hoặc người không có khả năng tự vệ")
onto.intent_family_hardship = onto.Intent(hasName="Làm gia đình người bị giam lâm vào tình trạng khó khăn, quẫn bách")
onto.intent_mental_disturbance1 = onto.Intent(hasName="Gây rối loạn tâm thần từ 11% đến 45%")
onto.intent_mental_disturbance2 = onto.Intent(hasName="Gây rối loạn tâm thần 46% trở lên")
onto.intent_cruel_treatment = onto.Intent(hasName="Tra tấn, đối xử tàn bạo, vô nhân đạo hoặc hạ nhục phẩm giá nạn nhân")

# ===================== Tình tiết tăng nặng =====================
onto.aggravating_circumstance_death = onto.Intent(hasName="Làm người bị bắt chết hoặc tự sát")
onto.aggravating_circumstance_certain_positions = onto.Intent(hasName="Cấm đảm nhiệm chức vụ nhất định từ 01 năm đến 05 năm")


# ===================== Điều luật =====================
onto.penal_code_article_158 = onto.PenalCodeArticle(hasName="Điều 158. Tội xâm phạm chỗ ở của người khác")

# ===================== Tội danh =====================
onto.crime_intrusion = onto.PropertyCrime(hasName="Tội xâm phạm chỗ ở của người khác")

# ===================== Hình phạt =====================
onto.punishment_reform = onto.Probation(hasName="Cải tạo không giam giữ đến 02 năm")
onto.punishment_imprisonment = onto.Imprisonment(hasName="Phạt tù từ 03 tháng đến 02 năm")

# ===================== Mức độ nghiêm trọng =====================
onto.severity_case = onto.CrimeSeverity(hasName="Mức độ nghiêm trọng thông thường")

# ===================== Ý định =====================
onto.intent_case = onto.Intent(hasName="Ý định phạm tội xâm phạm chỗ ở")

# ===================== Tình tiết tăng nặng =====================
onto.aggravating_factor = onto.Intent(hasName="Tình tiết tăng nặng trong tội xâm phạm chỗ ở")  # Sử dụng lại lớp Intent cho tình tiết tăng nặng



# ===================== Điều luật =====================
onto.article159 = onto.PenalCodeArticle(hasName='Điều 159. Tội xâm phạm bí mật hoặc an toàn thư tín, điện thoại, điện tín hoặc hình thức trao đổi thông tin riêng tư khác của người khác')

# ===================== Tội danh =====================
onto.offense = onto.Crime(hasName="Xâm phạm bí mật hoặc an toàn thư tín, điện thoại, điện tín hoặc hình thức trao đổi thông tin riêng tư khác")

# ===================== Hình phạt =====================
onto.punishment_warning = onto.Imprisonment(hasName="Phạt cảnh cáo")
onto.punishment_fine_low = onto.Fine(hasName="Phạt tiền từ 20.000.000 đồng đến 50.000.000 đồng")
onto.punishment_probation = onto.Probation(hasName="Phạt cải tạo không giam giữ đến 03 năm")

# ===================== Mức độ nghiêm trọng =====================
onto.severity = onto.CrimeSeverity(hasName="Mức độ nghiêm trọng của tội xâm phạm bí mật")

# ===================== Ý định =====================
onto.intent = onto.Intent(hasName="Ý định phạm tội xâm phạm bí mật")

# ===================== Tình tiết tăng nặng =====================
onto.aggravating_factor = onto.Intent(hasName="Tình tiết tăng nặng: Có tổ chức; Lợi dụng chức vụ, quyền hạn; Phạm tội 02 lần trở lên; Tiết lộ thông tin làm ảnh hưởng đến danh dự, uy tín, nhân phẩm; Làm nạn nhân tự sát.")



# ===================== Điều luật =====================
onto.PenalCodeArticle168 = onto.PenalCodeArticle(hasName="Điều 168. Tội cướp tài sản")

# ===================== Tội danh =====================
onto.Robbery = onto.Robbery(hasName="Cướp tài sản")

# ===================== Hình phạt =====================
onto.Imprisonment3To10Years = onto.Imprisonment(hasName="Phạt tù từ 03 năm đến 10 năm")
onto.Imprisonment7To15Years = onto.Imprisonment(hasName="Phạt tù từ 07 năm đến 15 năm")
onto.Imprisonment12To20Years = onto.Imprisonment(hasName="Phạt tù từ 12 năm đến 20 năm")
onto.Imprisonment18ToLife = onto.Imprisonment(hasName="Phạt tù từ 18 năm đến 20 năm hoặc tù chung thân")
onto.Imprisonment1To5Years = onto.Imprisonment(hasName="Phạt tù từ 01 năm đến 05 năm")
onto.Fine10To100Million = onto.Fine(hasName="Phạt tiền từ 10.000.000 đồng đến 100.000.000 đồng")

# ===================== Mức độ nghiêm trọng =====================
onto.CrimeSeverityHigh = onto.CrimeSeverity(hasName="Mức độ nghiêm trọng cao")

# ===================== Ý định =====================
onto.Intent = onto.Intent(hasName="Ý định phạm tội")

# ===================== Tình tiết tăng nặng =====================
# onto.AggravatingCircumstances = onto.Intent(hasName="Tình tiết tăng nặng")



# ===================== Điều luật =====================
rule = onto.PenalCodeArticle(hasName="Điều 161. Tội làm sai lệch kết quả bầu cử, kết quả trưng cầu ý dân")

# ===================== Tội danh =====================
crime = onto.Crime(hasName="Tội làm sai lệch kết quả bầu cử, kết quả trưng cầu ý dân")

# ===================== Hình phạt =====================
punishment_1 = onto.Probation(hasName="Phạt cải tạo không giam giữ đến 02 năm")
punishment_2 = onto.Imprisonment(hasName="Phạt tù từ 03 tháng đến 02 năm")
punishment_3 = onto.Imprisonment(hasName="Phạt tù từ 01 năm đến 03 năm")
punishment_4 = onto.Imprisonment(hasName="Phạt tù từ 01 năm đến 05 năm - cấm đảm nhiệm chức vụ")

# ===================== Mức độ nghiêm trọng =====================
severity_1 = onto.CrimeSeverity(hasName="Tội phạm nhẹ")
severity_2 = onto.CrimeSeverity(hasName="Tội phạm vừa")




# ===================== Lưu ontology =====================
onto.save(file="fact_criminal_law.owl", format="rdfxml")
print("Đã lưu ontology với các điều khoản thành công!")