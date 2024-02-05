"""
Introduction to writing classes
"""
import unittest


# TODO Create a class called student with the member variables and
#  methods used in the test class below to make all the tests pass
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.homework_done = False

    def do_homework(self):
        self.homework_done = True

    def go_to_school(self, time='7 am'):
        leave_str = self.name + ' is leaving for school at ' + time
        return leave_str

# ================== DO NOT MODIFY THE CODE BELOW ============================

class TestWriteClassesTests(unittest.TestCase):
    student_1 = Student(name='Zeeshan', grade=7)
    student_2 = Student(name='Amelia', grade=8)
    student_3 = Student(name='Penelope', grade=9)

    def test_student_objects_created(self):
        self.assertIsNotNone(TestWriteClassesTests.student_1, msg='student 1 not created!')
        self.assertIsNotNone(TestWriteClassesTests.student_2, msg='student 2 not created!')
        self.assertIsNotNone(TestWriteClassesTests.student_3, msg='student 3 not created!')

    def test_names(self):
        self.assertTrue(TestWriteClassesTests.student_1.name == 'Zeeshan')
        self.assertTrue(TestWriteClassesTests.student_2.name == 'Amelia')
        self.assertTrue(TestWriteClassesTests.student_3.name == 'Penelope')

    def test_grades(self):
        self.assertTrue(TestWriteClassesTests.student_1.grade == 7)
        self.assertTrue(TestWriteClassesTests.student_2.grade == 8)
        self.assertTrue(TestWriteClassesTests.student_3.grade == 9)

    def test_student_methods(self):
        self.assertEquals(False, TestWriteClassesTests.student_1.homework_done)
        self.assertEquals(False, TestWriteClassesTests.student_2.homework_done)
        self.assertEquals(False, TestWriteClassesTests.student_3.homework_done)

        TestWriteClassesTests.student_1.do_homework()
        TestWriteClassesTests.student_2.do_homework()
        TestWriteClassesTests.student_3.do_homework()

        self.assertEquals(True, TestWriteClassesTests.student_1.homework_done)
        self.assertEquals(True, TestWriteClassesTests.student_2.homework_done)
        self.assertEquals(True, TestWriteClassesTests.student_3.homework_done)

    def test_going_to_school(self):
        leave_str = TestWriteClassesTests.student_1.go_to_school(start='6 am')
        self.assertEqual('Zeeshan is leaving for school at 6 am', leave_str)

        leave_str = TestWriteClassesTests.student_2.go_to_school(start='6:30 am')
        self.assertEqual('Amelia is leaving for school at 6:30 am', leave_str)

        leave_str = TestWriteClassesTests.student_3.go_to_school()
        self.assertEqual('Penelope is leaving for school at 7 am', leave_str)



unittest.main()
