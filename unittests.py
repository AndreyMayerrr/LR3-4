import unittest
from resh import solution

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass
    def test_1(self):
        result = solution(0, 0, 0)
        self.assertEqual(result, "Уравнение верно для любого значения x (x ∈ R)")

    def test_2(self):
        result = solution(0, 0, -2)
        self.assertEqual(result, "Уравнение ложно для любого значения x (x ∈ Ø)")

    def test_3(self):
        result = solution(0, 2, 0)
        self.assertEqual(result, "Уравнение имеет 1 корень x = 0")

    def test_4(self):
        result = solution(0, -4, 4)
        self.assertEqual(result, f"Уравнение имеет 1 корень x = {1.0}")

    def test_5(self):
        result = solution(10, 0, 0)
        self.assertEqual(result, "Уравнение имеет 2 равных корня x = 0")

    def test_6(self):
        result = solution(10, 0, 10)
        self.assertEqual(result, "Действительных корней нет (x ∉ R)")

    def test_7(self):
        result = solution(10, 0, -10)
        self.assertEqual(result, f"Данное уравение имеет 2 корня x1 = {-1.0}, x2 = {1.0}")

    def test_8(self):
        result = solution(10, 10, 0)
        self.assertEqual(result, f"Данное уравение имеет 2 корня x1 = {0.0}, x2 = {-1.0}")

    def test_9(self):
        result = solution(1, -5, 4)
        self.assertEqual(result, f"Данное уравение имеет 2 корня x1 = {1.0}, x2 = {4.0}")

    def test_10(self):
        result = solution(2, 4, 2)
        self.assertEqual(result, f"Данное уравение имеет 1 корень x1 = {-1.0}")

    def test_11(self):
        result = solution(10, 10, 20)
        self.assertEqual(result, "Действительных корней нет (x ∉ R)")



if __name__ == '__main__':
    unittest.main()