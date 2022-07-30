from torch import Tensor
from transformers import AutoModelForCausalLM, AutoTokenizer


class Model:
    TOKENIZER = "Salesforce/codegen-350M-multi"
    MODEL = "Salesforce/codegen-350M-multi"

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.TOKENIZER)
        self.model = AutoModelForCausalLM.from_pretrained(self.MODEL)

    def __call__(self, prompt: str, language: str) -> str:
        processed = self.__preprocess(prompt, language)
        generated_code = self.__generate(processed)
        postprocessed = self.__postprocess(generated_code)
        return postprocessed

    def __preprocess(self, prompt: str, language: str) -> Tensor:
        """
        Tokenize the prompt.

        :param prompt: The prompt to tokenize
        :return: The tokenized prompt
        """
        prompt = f"# {language}\n{prompt}\n"
        return self.tokenizer.encode(prompt, return_tensors="pt")

    def __generate(self, prompt: Tensor) -> str:
        """
        Generate code from a Huggingface model.

        :param prompt: The tokenized prompt
        :return: The generated code
        """
        return self.model.generate(
            prompt,
            do_sample=True,
            num_return_sequences=1,
            max_length=128,
            pad_token_id=self.tokenizer.eos_token_id,
        )[0]

    def __postprocess(self, code: Tensor) -> str:
        """
        Postprocess the generated code.

        :param code: The generated code
        :return: The postprocessed code
        """
        return self.tokenizer.decode(code, skip_special_tokens=True)
