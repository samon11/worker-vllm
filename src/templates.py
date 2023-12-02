class Template():
    def __init__(self, template_method):
        self.template_method = template_method

    def __call__(self, prompt):
        return self.template_method(prompt)
    
    def __call__(self, prompt, system):
        if system is None:
            return self.template_method(prompt)

        return self.template_method(prompt, system)

LLAMA2_TEMPLATE = Template(
    lambda prompt: """SYSTEM: You are a helpful assistant.
USER: {}
ASSISTANT: """.format(prompt)
)

SELF_RAG_TEMPLATE = Template(
    lambda prompt, system: """### Instruction:
{instruction}

### Input:
{input}

### Response:
""".format_map({"instruction": system, "input": prompt}))

DEFAULT_TEMPLATE = Template(
    lambda prompt: prompt
)
