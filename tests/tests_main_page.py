import allure
import pytest
from pages.main_page import MainPage
from data import AnswerText
from conftest import driver


class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, AnswerText.ANSWER_TEXT_PRICE),
            (1, AnswerText.ANSWER_TEXT_COUNT),
            (2, AnswerText.ANSWER_TEXT_TIME),
            (3, AnswerText.ANSWER_TEXT_ORDER_TODAY),
            (4, AnswerText.ANSWER_TEXT_EXTEND_RETURN),
            (5, AnswerText.ANSWER_TEXT_CHARGE),
            (6, AnswerText.ANSWER_TEXT_CANCEL),
            (7, AnswerText.ANSWER_TEXT_MKAD),
        ],
        ids=[
            "Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5",
            "Question 6",
            "Question 7",
            "Question 8",
        ]
    )
    @allure.title(f'Проверка вопроса и получения текста ответа на главной в блоке FAQ')
    def test_question_and_answer(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.find_logo_with_wait()
        main_page.allow_cookie()
        main_page.scroll_to_last_element_in_page()
        assert main_page.click_question_get_answer(num) == result
