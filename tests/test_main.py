import unittest

from llmconf import LLMConf, OpenAIConf


class TestConf(unittest.TestCase):
    def test_init_with_nothing(self):
        self.assertEqual(str(LLMConf()), "LLMConf {}")

    def test_init_with_query(self):
        self.assertEqual(str(LLMConf(query="Hi")), "LLMConf {'query': 'Hi'}")

    def test_to_openai(self):
        conf1 = LLMConf(pretrained_model_name_or_path="gpt-3.5-turbo")
        conf2 = conf1.to(OpenAIConf)
        self.assertEqual(str(conf2), "OpenAIConf {}")


if __name__ == "__main__":
    unittest.main()
