# Online Workshop on Longchain & Open-source LLMs

## Workshop Description

Hey everyone,

I've got an idea for an engaging online workshop! We'll be diving into Langchain, a framework for developing applications powered by language models, and exploring its potential with the latest open-source Language Models (LLMs).
see <https://python.langchain.com/docs/get_started/introduction>.

**Here's the plan:**
The workshop will give participants hands-on experience with Longchain - how it works, storing data, and making the most out of it. Plus, we'll blend in the power of open-source LLMs to see how they can supercharge Longchain for some really awesome applications.

### Objectives

- Langchain basics.
- Show how LLMs can level up Longchain's capabilities.
- Encourage participants to brainstorm and build cool stuff using Langchain and LLMs.

### What's in it?

- Sessions will cover Langchain and LLM integration.
- Many interactive activities and group discussions.
- Resources and support materials to help participants create their own projects.

### Why it matters?

We're aiming to create a community of folks excited about Langchain and recent LLMs (such as Llama and Mixtral).
This workshop could spark some fantastic ideas and collaborations in this space!

In a nutshell, this workshop could be a game-changer in how we use Longchain and LLMs.
I'm thrilled about the potential and would love your thoughts on making this happen.

## `Hello_world` example

- Some conceptual: <https://python.langchain.com/docs/use_cases/chatbots/>

### Using paying OpenAI API key

- applicable also for any proprietary large language model

- Basic Langchain (using OpenAI API key): <https://www.youtube.com/watch?v=mrjq3lFz23s>

### Using local LLMs

#### `LLAMA2-chat`

#### Quantization and model format

<<https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGU>

## RAG chains

### What ?

RAG (Retrieval-Augmented Generation) chain refers to a specific architecture that combines elements of retrieval-based methods and generative models in natural language processing tasks. In this context, a RAG chain typically consists of two main components:

1. **Retriever**: This component is responsible for retrieving relevant information from a large repository or knowledge base. It uses search or **retrieval mechanisms** to find contextually relevant documents or passages related to the input query or prompt.

2. **Generator**: The generator, often based on generative models like transformers and is responsible for generating coherent and contextually relevant responses or outputs based on the retrieved information and the input query or context.

The RAG model operates by first retrieving relevant information using the retriever component. Then, it uses this retrieved information along with the input query to generate a response or output using the generator component. This fusion of retrieval and generation enables the model to leverage both the specificity of retrieved information and the creativity and coherence of generative models.

RAG models have been used in various natural language understanding and generation tasks, including question answering, summarization, conversational systems, and more. They aim to enhance the capabilities of traditional language models by incorporating retrieved information to improve the relevance and quality of generated responses.

### Why?

### Tools

- `Thebloke` quantized version of llama2-7B-chat (medium 4Go): <https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf>

### How?

- RAG pipelines: <https://medium.com/@madhur.prashant7/demo-langchain-rag-demo-on-llama-2-7b-embeddings-model-using-chainlit-559c10ce3fbf>

## Some references

<!-- TODO -->

- Calling Llama2 using LangChain: <https://python.langchain.com/docs/integrations/chat/llama_api>
