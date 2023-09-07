import openai

class GPT3Agent:
    """
    A class to represent a GPT3Agent.

    ...

    Attributes
    ----------
    api_key : str
        API key for GPT-3

    Methods
    -------
    generate_content(prompt: str, max_tokens: int = 1000):
        Generates content using GPT-3 based on the given prompt and max tokens.
    """

    def __init__(self, api_key: str):
        """
        Constructs all the necessary attributes for the GPT3Agent object.

        Parameters
        ----------
            api_key : str
                API key for GPT-3
        """

        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_content(self, prompt: str, max_tokens: int = 1000) -> str:
        """
        Generates content using GPT-3 based on the given prompt and max tokens.

        Parameters
        ----------
            prompt : str
                The prompt to generate content from.
            max_tokens : int, optional
                The maximum number of tokens to generate (default is 1000).

        Returns
        -------
        str
            Generated content.
        """

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=max_tokens
        )

        return response.choices[0].text.strip()
