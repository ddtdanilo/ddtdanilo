# Contributing

Thank you for helping improve this profile. Corrections to public facts, broken
links, accessibility, wording, and repository automation are welcome.

## Before opening a change

- Read [`AGENTS.md`](AGENTS.md).
- Open an issue for a factual correction or substantial redesign.
- Do not include private contact details, confidential work, or unverified
  biographical claims.

## Development

Create a branch from `main`, make a focused change, then run:

```bash
python3 scripts/validate_profile.py
git diff --check
```

Inspect `README.md` in a GitHub-compatible preview. If `assets/header.svg`
changes, render it and check its legibility at desktop and mobile widths.

## Pull requests

Use an imperative Conventional Commit title, explain why the profile improves,
and list the checks you ran. A pull request must pass the `Profile checks`
status check and review before merge.

By contributing, you agree that your contribution may be distributed under
this repository's [MIT License](LICENSE).
