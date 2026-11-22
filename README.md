# SupLens

**Know when a release of your package doesn't match your code.**

> ⚠️ Pre-alpha. Nothing works yet: this repository is being set up in the open.

## Why

Since 2025, worms like Shai-Hulud have turned one stolen npm token into hundreds of poisoned
packages. In May 2026, Mini Shai-Hulud shipped malicious versions with *valid* SLSA provenance:
a signature tells you where a package was built, not what it does.

The people best placed to spot a fake release are the maintainers themselves, yet most security
tools are built for the companies that *consume* packages. If your account is hijacked tonight, who
tells you that a version you never wrote just went out under your name?

## What SupLens will do

For every new version of a package you maintain, SupLens compares:

1. **The published tarball vs. your Git tag.** A file present in the package but absent from your
   repository is a strong signal.
2. **Version N vs. version N-1.** New install scripts, new network calls, reads of `~/.npmrc`, SSH
   keys or environment variables, obfuscated code, unexpected binaries.

If something looks off, it opens an issue in your repository, so you hear about it in minutes,
not from a blog post a week later.

It runs as a **scheduled GitHub Action inside your own repo**: no account, no server, no data
leaves GitHub.

## Roadmap

- [x] Project skeleton, license, CI
- [ ] `suplens check <package>@<version>`: tarball vs. Git tag diff, plus static rules
- [ ] Replays of real attacks (axios, Shai-Hulud, Mini Shai-Hulud) as test cases
- [ ] Maintainer mode: scheduled GitHub Action that watches your packages and opens issues
- [ ] Later: PyPI, an LLM second opinion on suspicious diffs, consumer-side checks on Dependabot PRs

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
ruff check . && ruff format --check .
```

## Safety rules

SupLens only does **static analysis**: it reads package files, it never runs them. It never
collects or stores credentials leaked by malware, even when they are public.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). To report a vulnerability in SupLens itself, see
[SECURITY.md](SECURITY.md).

## License

[Apache-2.0](LICENSE)
