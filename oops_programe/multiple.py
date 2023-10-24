class Father:
    def __init__(self, f_name):
        self.f_name = f_name
    # def father_name(self):
    #     print('father name=', self.f_name)
class Mother:
    def __init__(self, m_name):
        self.m_name = m_name

    # def mother_name(self):
    #     print('mother name =', self.m_name)

class Son(Father,Mother):
    def __init__(self, f_name, m_name, s_name):
        Father.__init__(self, f_name)
        Mother.__init__(self, m_name)
        self.s_name = s_name

    def family_detalis(self):
        # super().father_name()
        # super().mother_name()
        print('FAMILY DETALIS :', 'FATHER_NAME =', self.f_name, 'MOTHER_NAME =', self.m_name,' SON_NAME =', self.s_name)



kid = Son('XXX','YYY','XYX')

kid.family_detalis()


