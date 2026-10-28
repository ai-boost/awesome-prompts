# Prompt Library · 提示词库

Built by `scripts/build_library.py`. Rerun it to pull new upstream prompts; existing rows keep their category and titles.

## Columns

`id`, `category`, `lang` (`both`, `en` or `zh`), `title_en`, `title_zh`, `prompt_en`, `prompt_zh`, `for_devs`, `source`, `license`.

## Sources

- [prompts.chat](https://prompts.chat) (`prompts.csv`), CC0 1.0. English text of 2,586 prompts.
- [CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN](https://github.com/CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN), CC0 1.0. Chinese text of 1,931 of them, kept only where the English is unchanged since the translation.
- [rockbenben/ChatGPT-Shortcut](https://github.com/rockbenben/ChatGPT-Shortcut), MIT, Copyright (c) 2023 rockbenben. The author's Chinese versions for 0 prompts.chat prompts and 122 prompts of its own. License: [LICENSE-ChatGPT-Shortcut-MIT.txt](LICENSE-ChatGPT-Shortcut-MIT.txt).
- [langgptai/wonderful-prompts](https://github.com/langgptai/wonderful-prompts), MIT, Copyright (c) 2023 yzfly. 36 original Chinese prompts. License: [LICENSE-wonderful-prompts-MIT.txt](LICENSE-wonderful-prompts-MIT.txt).
- [langgptai/awesome-doubao-prompts](https://github.com/langgptai/awesome-doubao-prompts), Apache-2.0. 27 original Chinese prompts. License: [LICENSE-awesome-doubao-prompts-Apache-2.0.txt](LICENSE-awesome-doubao-prompts-Apache-2.0.txt).
- [langgptai/awesome-gemini-prompts](https://github.com/langgptai/awesome-gemini-prompts), CC0 1.0. 6 original Chinese prompts.
- [DeepSeek prompt library](https://api-docs.deepseek.com/zh-cn/prompt-library/), Copyright DeepSeek, Inc. 13 official example prompts, quoted with attribution (`sources/deepseek-prompt-library.json`).

## Machine translation

655 prompts got a Chinese version and 83 got an English version from a model. The `translated` column names that language, and the Markdown pages mark those entries. A human translation from any source replaces the machine one on the next build.

Categories and the missing-language titles were assigned by a model pass and spot-checked. 105 prompts were left out as sexual, jailbreak, spam or empty (ids in `skipped.json`).
