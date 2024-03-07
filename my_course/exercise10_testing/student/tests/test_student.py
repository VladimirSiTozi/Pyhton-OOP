from unittest import TestCase, main

from project.student import Student


class TestHero(TestCase):
    def setUp(self) -> None:
        self.student = Student('Goshko', {'Programing Basics': ['note1', 'note2', 'note3']})

    def test_correct_init(self):
        name = 'Goshko'
        courses = {'Programing Basics': ['note1', 'note2', 'note3']}
        self.assertEqual(name, self.student.name)
        self.assertEqual(courses, self.student.courses)

    def test_correct_init_courses_are_none(self):
        self.student = Student('Goshko', None)
        name = 'Goshko'
        courses = {}

        self.assertEqual(name, self.student.name)
        self.assertEqual(courses, self.student.courses)

    def test_enroll_should_enroll_course_and_add_notes(self):
        expected_result = "Course already added. Notes have been updated."
        actual_result = self.student.enroll('Programing Basics', ['note4'])

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(['note1', 'note2', 'note3', 'note4'], self.student.courses['Programing Basics'])

    def test_enroll_not_existing_course_add_new_course_and_new_notes(self):
        expected_result = "Course and course notes have been added."
        actual_result = self.student.enroll('JS', ['n1', 'n2'], 'Y')

        self.assertEqual(expected_result, actual_result)
        self.assertEqual({'Programing Basics': ['note1', 'note2', 'note3'], 'JS': ['n1', 'n2']}, self.student.courses)

    def test_enroll_not_existing_course_with_empty_string(self):
        expected_result = "Course and course notes have been added."
        actual_result = self.student.enroll('JS', ['n1', 'n2'], '')

        self.assertEqual(expected_result, actual_result)
        self.assertEqual({'Programing Basics': ['note1', 'note2', 'note3'], 'JS': ['n1', 'n2']}, self.student.courses)

    def test_enroll_not_existing_course_not_adding_note(self):
        expected_result = "Course has been added."
        actual_result = self.student.enroll('JS', ['n1', 'n2'], 'asd')

        self.assertEqual(expected_result, actual_result)
        self.assertEqual([], self.student.courses['JS'])

    def test_add_notes_to_existing_course(self):
        actual_result = self.student.add_notes('Programing Basics', 'n99')
        expected_result = 'Notes have been updated'

        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.student.courses['Programing Basics'], ['note1', 'note2', 'note3', 'n99'])

    def test_add_notes_to_not_existing_course_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('JS', 'n99')

        expected_result = 'Cannot add notes. Course not found.'
        self.assertEqual(expected_result, str(ex.exception))

    def test_leave_course_should_remove_existing_course(self):
        actual_result = self.student.leave_course('Programing Basics')
        expected_result = "Course has been removed"

        self.assertEqual(actual_result, expected_result)
        self.assertEqual({}, self.student.courses)

    def test_leave_not_existing_course_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('JS')

        expected_result = 'Cannot remove course. Course not found.'
        self.assertEqual(expected_result, str(ex.exception))











if __name__ == '__main__':
    main()