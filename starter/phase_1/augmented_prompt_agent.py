import os
# TODO: 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
agent = AugmentedPromptAgent(openai_api_key, persona)

# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = agent.respond(prompt)
# Print the agent's response
print(augmented_agent_response)

# TODO: 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt.
# - How the system prompt specifying the persona affected the agent's response.
#
# Response:
# In this example, the agent thinks its a collage professor and it starts its response with "Dear students,".
# This is because the system prompt specifies the persona of a college professor, which influences how the agent structures its response.
# The knowledge used by the agent is based on the training data of the OpenAI model, which includes general knowledge about world capitals.
# Temparature is set to 0, meaning the response will be deterministic and consistent across calls.
# Extra findings:
# When system promt set to  {"role": "system", "content": self.persona + " Forget all previous context."}
# The agent responds with `Dear students, the capital of France is Paris.`
#
# However, when the system prompt is set to `{"role": "system", "content": "Forget all previous context." + self.persona}`,
# It thinks its an email and responds like below
#
# Dear students,

# The capital of France is Paris.

# Sincerely,
# Your college professor


### In either case answer is consistent
