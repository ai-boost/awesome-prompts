# For GPT3.5
```
# Instruction

"""
YOUR INSTRUCTION HERE
"""

# Requirements

- Your answer should consist of ten sections, with at least 2000 words in each section.

- Use Markdown with dividing lines between each section.

- Strictly follow user instructions while providing in-depth and detailed answers.
```

# For GPT-4/GPTs
Unstable Now😭 I am working hard to optimize. GPT4 seems to easily overlook your detailed instructions now. See: https://www.reddit.com/r/ChatGPT/comments/17mp9b7/gpt4_is_responding_faster_but_the_quality_is/

Since the prompt is not stable, before improving the prompt, I will first provide the basic principles.

There are two principles behind AutoGPT, segmented output and interface invocation.

Segmented output: A good example is the chatgpt 3.5 prompt just given, which forces the chatgpt reply to be divided into 10 sections, each requiring n words. In this way, chatgpt can generate content that is longer than normal. (That's not enough, of course)

Interface Invocation: Interface invocation is necessary, whether it is dalle3, you actions, or code interpreter, they can all serve two purposes. Purposes: Assist in segmentation (similar to the function of dividing lines) Provide the goals required for the next step and guide the model to continue generating. Due to its strong comprehension ability, GPT4 will faithfully follow instructions and continuously generate content.
