import unittest

from llmconf import LLMConf


class TestBasics(unittest.TestCase):
    def test_init_with_nothing(self):
        self.assertEqual(str(LLMConf()), "LLMConf {}")

    def test_init_with_query(self):
        self.assertEqual(str(LLMConf(query="Hi")), "LLMConf {'query': 'Hi'}")


class TestOpenAI(unittest.TestCase):
    def test_to_openai(self):
        conf1 = LLMConf(pretrained_model_name_or_path="gpt-3.5-turbo")
        conf2 = conf1.openai
        self.assertEqual(str(conf2), "OpenAIConf {'model': 'gpt-3.5-turbo'}")

    def test_to_openai2(self):
        conf1 = LLMConf(model="tmp", max_completion_tokens=24, max_new_tokens=8)
        conf2 = conf1.openai
        self.assertEqual(str(conf2), "OpenAIConf {'model': 'tmp', 'max_completion_tokens': 24}")

    def test_to_specific_cases(self):
        conf = LLMConf(
            api_key="key", base_url="url", model="model_a", max_new_tokens=100, query="Hi"
        )
        self.assertEqual(str(conf.openai.openai_init), "{'api_key': 'key', 'base_url': 'url'}")
        self.assertEqual(
            str(conf.openai.chat_completions), "{'model': 'model_a', 'max_completion_tokens': 100}"
        )


class TestTransformers(unittest.TestCase):
    def test_to_transformers(self):
        conf1 = LLMConf(model="gpt-3.5-turbo", max_completion_tokens=100)
        conf2 = conf1.transformers
        self.assertEqual(
            str(conf2),
            "TransformersConf {'pretrained_model_name_or_path': 'gpt-3.5-turbo', 'max_new_tokens': 100}",
        )

    def test_to_transformers2(self):
        conf1 = LLMConf(model="tmp", max_completion_tokens=24, max_new_tokens=8)
        conf2 = conf1.transformers
        self.assertEqual(
            str(conf2),
            "TransformersConf {'pretrained_model_name_or_path': 'tmp', 'max_new_tokens': 8}",
        )

    def test_to_specific_cases(self):
        conf = LLMConf(model="model_a", max_tokens=100, query="Hi")
        self.assertEqual(
            str(conf.transformers.from_pretrained),
            "{'pretrained_model_name_or_path': 'model_a'}",
        )
        self.assertEqual(
            str(conf.transformers.generation_config),
            "{'max_new_tokens': 100}",
        )


if __name__ == "__main__":
    unittest.main()
