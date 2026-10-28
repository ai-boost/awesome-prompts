# Prompt Library · 提示词库

Built by `scripts/build_library.py`. Rerun it to pull new upstream prompts; existing rows keep their category and titles.

## Columns

`id`, `category`, `lang` (`both`, `en` or `zh`), `title_en`, `title_zh`, `prompt_en`, `prompt_zh`, `for_devs`, `source`, `license`.

## Sources

- [prompts.chat](https://prompts.chat) (`prompts.csv`), CC0 1.0. English text of 2,586 prompts.
- [CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN](https://github.com/CHENJIAMIAN/awesome-chatgpt-prompts-zh-CN), CC0 1.0. Chinese text of 1,931 of them, kept only where the English is unchanged since the translation.
- [langgptai/wonderful-prompts](https://github.com/langgptai/wonderful-prompts), MIT, Copyright (c) 2023 yzfly. 18 original Chinese prompts. License: [LICENSE-wonderful-prompts-MIT.txt](LICENSE-wonderful-prompts-MIT.txt).

Categories and the missing-language titles were assigned by a model pass and spot-checked. 84 prompts were left out as sexual, jailbreak, spam or empty (ids in `skipped.json`).
