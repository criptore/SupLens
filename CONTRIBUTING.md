# Contributing to SupLens

Thanks for your interest! SupLens is early, so the most useful contributions right now are:

- **Real-world cases:** links to malicious npm releases (with the clean version before them) that
  SupLens should catch.
- **False alarm reports:** legitimate releases that SupLens flags.
- **Code** for the items on the roadmap in the README.

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Before opening a pull request, make sure `ruff check .`, `ruff format --check .` and `pytest`
pass. Keep pull requests focused on one change and add a test for it.

## Ground rules

- **Never commit live malware.** Test fixtures describe malicious behavior with minimal, inert
  snippets, or reference packages by name and version.
- **Static analysis only.** Code in this project must never install, import or execute the
  packages it analyzes.
- **Never collect leaked secrets.** Counting victims of a campaign is fine; retrieving their
  credentials is not.
- **Be careful with accusations.** A suspicious release is reported privately to the registry
  and the maintainer first. Never name a package as malicious in a public issue before it has
  been confirmed.

## Code of conduct

Be kind and assume good faith. Harassment of any kind is not tolerated.
