# multiple inheritance 

class knowledge:

    def education(self):

        print('To get knowledge')

    def school(self):

        print ( 'children go to school to gain knowledge')

class college : 

    def undergraduate(self):

        print ('To get knowledge and skill development')

    def postgraduate (self):

        print ('To get extra knowledge and skill development')


class learning(knowledge,college):

    def company(self):

        print ('Work place')

ob=learning()

print ('----- learning Features----')

ob.education()

ob.school()

ob.undergraduate()

ob.postgraduate()

ob.company()