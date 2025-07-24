import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyAw7kAeeBcVV1ut57KllxzPcj0W0a1934s"))

models = genai.list_models()
for model in models:
    print(model.name, "→", model.supported_generation_methods)
