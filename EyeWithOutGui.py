from experta import *

class eyeDisease(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("")
        print("Welcom to Expert System ")
        print("for Diagnosing Eye Disease")
        print("")
        yield Fact(action="eyeDisease")

    @Rule(Fact(action='eyeDisease'), NOT(Fact(itching=W())))
    def symptom_0(self):
        # هل تعاني من حكة وحرقان في عينيك؟
        self.declare(
            Fact(itching=input("Do you experience itching and burning in your eyes? : ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(blurring=W())))
    def symptom_1(self):
        # "هل تعاني من رؤية ضبابية؟
        self.declare(
            Fact(blurring=input("Do you experience a blurring vision? : ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(redness=W())))
    def symptom_2(self):
        # هل تعانين من احمرار في لون عينيك؟
        self.declare(
            Fact(redness=input("Do you experience redness in your eye color?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(night=W())))
    def symptom_3(self):
        # هل تواجه صعوبة في الرؤية أثناء القيادة ليلاً؟
        self.declare(Fact(night=input(
            "Do you experience difficulty in seeing while driving at night?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(mucus=W())))
    def symptom_4(self):
        # هل تعاني من إفرازات مخاط لزجة في عينيك؟
        self.declare(Fact(mucus=input(
            "Do you experience a discharge of sticky mucus in your eyes?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(teare=W())))
    def symptom_5(self):
        # هل لديك دمعة في كلتا العينين؟
        self.declare(Fact(tear=input("Do you have a tear in both eyes?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(yellowing=W())))
    def symptom_6(self):
        # هل تعاني من اصفرار الألوان في عينيك؟
        self.declare(Fact(yellowing=input(
            "Do you experience yellowing of colors in your eyes?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(headache=W())))
    def symptom_7(self):
        # هل تعاني من صداع شديد؟
        self.declare(
            Fact(headache=input("Do you experience severe headache?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(cough=W())))
    def symptom_8(self):
        # هل تعاني من السعال وسيلان الأنف وحك الحلق؟
        self.declare(Fact(cough=input(
            "Do you experience cough, running nose and scratching throat?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(pain=W())))
    def symptom_9(self):
        # هل تعانين من ألم في العين وتورم في الجفن؟
        self.declare(
            Fact(pain=input("Do you experience eye pain and swollen eyelid?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(overstrain=W())))
    def symptom_10(self):
        # هل عيناك ترهقانك باستمرار؟
        self.declare(Fact(overstrain=input(
            "Does your eyes constantly overstrain you?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(sensitivity=W())))
    def symptom_11(self):
        # هل تعاني من زيادة الحساسية للضوء؟
        self.declare(Fact(sensitivity=input(
            "Do you experience an increased sensitivity to light? ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(rainbow=W())))
    def symptom_12(self):
        # هل ترى هالات أو دائرة بلون قوس قزح حول الضوء؟
        self.declare(Fact(rainbow=input(
            "Do you see halos or rainbow-colored circle around light?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(double=W())))
    def symptom_13(self):
        # هل تعاني من ازدواج الرؤية في عين واحدة؟
        self.declare(
            Fact(double=input("Do you experience double vision in a single eye?")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(sightedness=W())))
    def symptom_14(self):
        # هل تعاني من قصر النظر؟
        self.declare(Fact(sightedness=input(
            "Do you experience nearsightedness?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(sight=W())))
    def symptom_15(self):
        # هل تعاني من فقدان البصر المفاجئ؟
        self.declare(
            Fact(sight=input("Do you experience sudden loss of sight? ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(nausea=W())))
    def symptom_16(self):
        # هل تعاني من غثيان وقيء مستمرين؟
        self.declare(
            Fact(nausea=input("Do you constant nausea and vomiting?: ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(dilated=W())))
    def symptom_17(self):
        # هل لديك حدقة متوسعة؟
        self.declare(Fact(dilated=input("Do you have a dilated pupil? ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(eyelid=W())))
    def symptom_18(self):
        # هل تحتاج إلى إغلاق جفنك جزئيًا حتى ترى بوضوح؟
        self.declare(Fact(eyelid=input(
            "Do you need to partially close your eyelid to see clearly? ")))

    @Rule(Fact(action='eyeDisease'), NOT(Fact(vision=W())))
    def symptom_19(self):
        # هل أنت بحاجة إلى تجربة انخفاض مفاجئ في الرؤية؟
        self.declare(
            Fact(vision=input("Do you need experience a sudden decrease in vision? ")))

##########################################################################################################
##########################################################################################################


     # Myopia
    @Rule(AND(Fact(itching='no'), Fact(blurring='yes'), Fact(redness='no'), Fact(night='yes'),
              Fact(mucus='no'), Fact(tear='no'), Fact(
                  yellowing='no'), Fact(headache='yes'),
              Fact(cough='no'), Fact(pain='no'), Fact(
                  overstrain='yes'), Fact(sensitivity='no'),
              Fact(rainbow='no'), Fact(double='no'), Fact(
                  sightedness='yes'), Fact(sight='no'),
              Fact(nausea='no'), Fact(dilated='no'), Fact(eyelid='yes')))
    def disease_0(self):
        self.declare(Fact(disease="Myopia"))
# -----------------------------------------------------------------------
    # conjunctiva

    @Rule(AND(Fact(itching='yes'), Fact(blurring='yes'), Fact(redness='yes'), Fact(night='no'),
              Fact(mucus='yes'), Fact(tear='yes'), Fact(
                  yellowing='no'), Fact(headache='no'),
              Fact(cough='no'), Fact(pain='yes'), Fact(
                  overstrain='yes'), Fact(sensitivity='yes'),
              Fact(rainbow='no'), Fact(double='no'), Fact(
                  sightedness='no'), Fact(sight='no'),
              Fact(nausea='no'), Fact(dilated='no'), Fact(eyelid='no')))
    def disease_1(self):
        self.declare(Fact(disease="conjunctiva"))
# --------------------------------------------------------------------------

      # Ocular Allergy
    @Rule(AND(Fact(itching='yes'), Fact(blurring='no'), Fact(redness='yes'), Fact(night='yes'),
              Fact(mucus='yes'), Fact(tear='no'), Fact(
                  yellowing='no'), Fact(headache='no'), Fact(cough='no'),
              Fact(pain='yes'), Fact(overstrain='no'), Fact(
                  sensitivity='yes'), Fact(rainbow='no'), Fact(double='no'),
              Fact(sightedness='no'), Fact(sight='yes'), Fact(
                  nausea='no'), Fact(dilated='no'), Fact(eyelid='no'),
              ))
    def disease_2(self):
        self.declare(Fact(disease=" Ocular Allergy"))
# -------------------------------------------------------

      # Glaucoma
    @Rule(AND(Fact(itching='no'), Fact(blurring='yes'), Fact(redness='yes'), Fact(night='yes'),
              Fact(mucus='no'), Fact(tear='no'), Fact(
                  yellowing='yes'), Fact(headache='no'), Fact(cough='no'),
              Fact(pain='yes'), Fact(overstrain='no'), Fact(
                  sensitivity='no'), Fact(rainbow='yes'), Fact(double='no'),
              Fact(sightedness='no'), Fact(sight='yes'), Fact(
                  nausea='yes'), Fact(dilated='yes'), Fact(eyelid='no'),
              ))
    def disease_3(self):
        self.declare(Fact(disease="Glaucoma"))
# -------------------------------------------------------
    # Cataract

    @Rule(AND(Fact(itching='no'), Fact(blurring='yes'), Fact(redness='no'), Fact(night='yes'),
              Fact(mucus='no'), Fact(tear='no'), Fact(
                  yellowing='yes'), Fact(headache='no'), Fact(cough='no'),
              Fact(pain='no'), Fact(overstrain='no'), Fact(
                  sensitivity='yes'), Fact(rainbow='yes'), Fact(double='yes'),
              Fact(sightedness='yes'), Fact(sight='no'), Fact(
                  nausea='no'), Fact(dilated='no'), Fact(eyelid='no'),

              ))
    def disease_4(self):
        self.declare(Fact(disease="Cataract"))
# -----------------------------------------------------------------
   # night blindness

    @Rule(AND(Fact(itching='no'), Fact(blurring='yes'), Fact(redness='no'), Fact(night='yes'),
              Fact(mucus='no'), Fact(tear='no'), Fact(
                  yellowing='no'), Fact(headache='no'), Fact(cough='no'),
              Fact(pain='no'), Fact(overstrain='yes'), Fact(
                  sensitivity='yes'), Fact(rainbow='yes'), Fact(double='no'),
              Fact(sightedness='yes'), Fact(sight='yes'), Fact(
                  nausea='no'), Fact(dilated='no'), Fact(eyelid='no'),

              ))
    def disease_5(self):
        self.declare(Fact(disease="night blindness"))
# -------------------------------------------------------------------
     # Diabetic retinopathy

    @Rule(AND(Fact(itching='no'), Fact(blurring='yes'), Fact(redness='yes'), Fact(night='yes'),
              Fact(mucus='no'), Fact(tear='no'), Fact(
                  yellowing='no'), Fact(headache='no'), Fact(cough='no'),
              Fact(pain='no'), Fact(overstrain='yes'), Fact(
                  sensitivity='yes'), Fact(rainbow='yes'), Fact(double='no'),
              Fact(sightedness='yes'), Fact(sight='yes'), Fact(
                  nausea='no'), Fact(dilated='no'), Fact(eyelid='no'),

              ))
    def disease_6(self):
        self.declare(Fact(disease="Diabetic retinopathy"))
# -----------------------------------------------------------------------
     # Trachoma

    @Rule(AND(Fact(itching='yes'), Fact(blurring='no'), Fact(redness='yes'), Fact(night='no'),
              Fact(mucus='no'), Fact(tear='yes'), Fact(
                  yellowing='yes'), Fact(headache='no'), Fact(cough='no'),
              Fact(pain='no'), Fact(overstrain='yes'), Fact(
                  sensitivity='yes'), Fact(rainbow='yes'), Fact(double='no'),
              Fact(sightedness='no'), Fact(sight='no'), Fact(
                  nausea='no'), Fact(dilated='no'), Fact(eyelid='no'),

              ))
    def disease_7(self):
        self.declare(Fact(disease="Trachoma"))


# -----------------------------------------------------------

     # Refractive errors


    @Rule(AND(Fact(itching='no'), Fact(blurring='yes'), Fact(redness='no'), Fact(night='no'),
              Fact(mucus='no'), Fact(tear='no'), Fact(
                  yellowing='no'), Fact(headache='yes'), Fact(cough='no'),
              Fact(pain='no'), Fact(overstrain='yes'), Fact(
                  sensitivity='yes'), Fact(rainbow='yes'), Fact(double='no'),
              Fact(sightedness='yes'), Fact(sight='yes'), Fact(
                  nausea='no'), Fact(dilated='no'), Fact(eyelid='no'),

              ))
    def disease_8(self):
        self.declare(Fact(disease="Refractive errors"))


# -----------------------------------------------------------


    @Rule(Fact(action='eyeDisease'), Fact(disease=MATCH.disease))
    def disease(self, disease):
        print("")
        id_disease = disease
        print("")
        print("The most probable disease that you have is %s\n" % (id_disease))


# -----------------------------------------------------------
engine = eyeDisease()
while (1):
    engine.reset()  
    engine.run() 
    print("Would you like to diagnose some other symptoms?")
    if input() == "no":
        break
