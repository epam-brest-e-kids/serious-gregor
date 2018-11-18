import unittest
from unittest import TestCase
from unittest.mock import patch
import builtins

from main import Lesson7


class Test_Lesson7(TestCase):

    def test_01(self):
        self.assertTrue(hasattr(Lesson7, 'my_var'),
                        "Вы не создали переменнуюю")
        self.assertEqual(type(Lesson7.my_var), type(
            ""), "Тип вашей переменной не строкаю")

    def test_02(self):
        self.assertTrue(hasattr(Lesson7, 'MY_CONST'),
                        "Вы не создали константую")
        self.assertEqual(type(Lesson7.MY_CONST), type(
            5), "Тип вашей константы не целое числою")

    @patch("builtins.print", autospec=True)
    def test_03(self, mock):
        l = Lesson7()
        l.test_03()
        self.assertTrue(mock.called, "Вы не вызвали функцию печати в консоль")
        self.assertEqual(
            mock.call_args[0], ("Привет, мир, я Зомби!",), "Вы не напечатали нужную строку")

    @patch("builtins.input", autospec=True)
    def test_04(self, mock):
        l = Lesson7()
        l.test_04()
        self.assertTrue(mock.called, "Вы не вызвали функцию чтения из консоли")
        self.assertEqual(
            mock.call_args[0], ("Как твоё имя?: ", ), "Вы ничего не спросили у пользователя")


if __name__ == '__main__':
    unittest.main()
