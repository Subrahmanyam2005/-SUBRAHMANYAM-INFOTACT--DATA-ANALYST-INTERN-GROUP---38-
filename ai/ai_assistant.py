import os
from .prompt_templates import SYSTEM_PROMPT,insights_prompt
def explain_with_openai(metrics,bottlenecks,model="gpt-4.1-mini"):
 if not os.getenv("OPENAI_API_KEY"): raise RuntimeError("Configure OPENAI_API_KEY in secrets")
 from openai import OpenAI
 r=OpenAI().responses.create(model=model,instructions=SYSTEM_PROMPT,input=insights_prompt(metrics,bottlenecks))
 return r.output_text
