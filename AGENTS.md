# AGENTS.md

## Purpose

This repository is Danilo Díaz Tarascó's public GitHub profile. Its primary
artifact is `README.md`, which GitHub renders at
[`github.com/ddtdanilo`](https://github.com/ddtdanilo).

Keep every contribution accurate, respectful, accessible, and consistent with
the public portfolio at
[`ddtdanilo.github.io`](https://ddtdanilo.github.io).

## Non-negotiable rules

1. Use **Danilo Díaz Tarascó** or **Danilo Díaz**. Never substitute another
   surname.
2. Write all repository content in English.
3. Do not add private email addresses, phone numbers, street addresses,
   government identifiers, citizenship or residency details, client secrets,
   credentials, or confidential project information.
4. Link only to public, verifiable work. Do not invent metrics, titles,
   affiliations, awards, dates, or project outcomes.
5. Keep the profile intentionally simple. Avoid banners, badge walls, vanity
   counters, contribution streaks, animations, autoplaying media, complex
   tables, and unreliable dynamic cards.
6. Preserve accessibility: meaningful alternative text, readable contrast,
   semantic headings, descriptive links, and no information conveyed by color
   alone.
7. Prefer plain Markdown, short sections, and restrained prose.

## Repository map

| Path | Responsibility |
| --- | --- |
| `README.md` | Public GitHub profile content |
| `scripts/validate_profile.py` | Dependency-free repository checks |
| `.github/workflows/profile.yml` | Continuous validation |
| `.github/` | Contribution, ownership, and automation policy |
| `CONTRIBUTING.md` | Contribution workflow |
| `SECURITY.md` | Private vulnerability reporting policy |
| `CLAUDE.md` | Guidance for Claude-based contributors |

## Working agreement

Before editing:

1. Read `README.md`, this file, and the file being changed.
2. Treat the live portfolio and linked public repositories as the sources of
   truth for biographical and project claims.
3. Verify time-sensitive facts at their primary source.
4. Make the smallest coherent change that fully solves the issue.

After editing:

```bash
python3 scripts/validate_profile.py
git diff --check
```

Review rendered Markdown whenever its structure changes. Confirm that links are
HTTPS, headings remain in order, and the result is easy to scan in both light
and dark GitHub themes.

## Commit and pull-request conventions

- Branch from `main`.
- Use focused, imperative Conventional Commit messages such as
  `docs: refine selected work`.
- Do not push directly to `main`.
- Explain user-visible changes and validation in the pull request.
- Keep commits signed when the local environment supports signing.
- Never bypass required reviews or status checks.

## Content maintenance

Review the profile when Danilo's role, selected work, portfolio, or public
contact links change. Prefer durable statements over quickly aging numbers.
When removing a project, remove its associated prose and links in the same
change.
