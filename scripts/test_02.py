import allure
import pytest


class Test_02:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试步骤01")
    def test_001(self):
        print("我是一个测试方法1")
        allure.attach("标题", "具体内容")
        assert True

    def test_add_png(self):
        with open("\\Users\\deen\\Desktop\\app_po_02\\scripts\\abc.PNG", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
            assert True
