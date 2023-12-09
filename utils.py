import vertexai, os
from vertexai.language_models import CodeGenerationModel

class VertexAI(object):
    def __init__(self):
        self.client = vertexai.init(project=os.environ["PROJECT"], location="us-central1")
        self.model = CodeGenerationModel.from_pretrained("code-bison")
        self.parameters = {
            "candidate_count": 1,
            "max_output_tokens": 1024,
            "temperature": 0.2
        }
        self.result = str()

    def predict(self, prefix) -> str:
        response = self.model.predict(prefix=prefix, **self.parameters)
        return response.text

    def ask(self, prefix):
        self.result = self.predict(prefix)
        return self.result
    def display(self):
        print(self.result)
