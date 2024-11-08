import os
import unittest

from llmconf import LLMConf


os.environ.clear()


class TestBasics(unittest.TestCase):
    def test_init_with_nothing(self):
        self.assertEqual(str(LLMConf(backend="openai")), "LLMConf {'backend': 'openai'}")

    def test_init_with_query(self):
        self.assertEqual(
            str(LLMConf(backend="openai", query="Hi")),
            "LLMConf {'backend': 'openai', 'query': 'Hi'}",
        )

    def test_attribute_error(self):
        conf = LLMConf(backend="openai")
        with self.assertRaises(AttributeError):
            conf.load_params  # noqa: B018
        with self.assertRaises(AttributeError):
            conf.gene_params  # noqa: B018


class TestOpenAI(unittest.TestCase):
    def test_to_openai(self):
        conf1 = LLMConf(backend="openai", pretrained_model_name_or_path="gpt-3.5-turbo")
        conf2 = conf1.openai
        self.assertEqual(str(conf2), "OpenAIConf {'backend': 'openai', 'model': 'gpt-3.5-turbo'}")

    def test_to_openai2(self):
        conf1 = LLMConf(backend="openai", model="tmp", max_completion_tokens=24, max_new_tokens=8)
        conf2 = conf1.openai
        self.assertEqual(
            str(conf2),
            "OpenAIConf {'backend': 'openai', 'model': 'tmp', 'max_completion_tokens': 24}",
        )

    def test_to_specific_cases(self):
        conf = LLMConf(
            backend="openai",
            api_key="key",
            base_url="url",
            model="model_a",
            max_new_tokens=100,
            query="Hi",
        ).openai
        self.assertEqual(str(conf.load_params), "{'api_key': 'key', 'base_url': 'url'}")
        self.assertEqual(
            str(conf.gene_params),
            "{'messages': [{'role': 'user', 'content': 'Hi'}], 'model': 'model_a', 'max_completion_tokens': 100}",
        )


class TestTransformers(unittest.TestCase):
    def test_to_transformers(self):
        conf1 = LLMConf(backend="transformers", model="gpt-3.5-turbo", max_completion_tokens=100)
        conf2 = conf1.transformers
        self.assertEqual(
            str(conf2),
            "TransformersConf {'backend': 'transformers', 'pretrained_model_name_or_path': 'gpt-3.5-turbo', 'max_new_tokens': 100}",
        )

    def test_to_transformers2(self):
        conf1 = LLMConf(
            backend="transformers", model="tmp", max_completion_tokens=24, max_new_tokens=8
        )
        conf2 = conf1.transformers
        self.assertEqual(
            str(conf2),
            "TransformersConf {'backend': 'transformers', 'pretrained_model_name_or_path': 'tmp', 'max_new_tokens': 8}",
        )

    def test_to_specific_cases(self):
        conf = LLMConf(backend="transformers", model="model_a", max_tokens=100, query="Hi")
        self.assertEqual(
            str(conf.transformers.load_params),
            "{'pretrained_model_name_or_path': 'model_a'}",
        )
        self.assertEqual(
            str(conf.transformers.gene_params),
            "{'max_new_tokens': 100}",
        )


if __name__ == "__main__":
    unittest.main()
