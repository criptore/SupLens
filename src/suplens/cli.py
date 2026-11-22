"""Command line entry point for SupLens."""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Sequence
from dataclasses import dataclass

from suplens import __version__

# npm names: optional @scope/, then lowercase URL-safe characters.
_NAME_RE = re.compile(r"^(?:@[a-z0-9][a-z0-9._~-]*/)?[a-z0-9][a-z0-9._~-]*$")


@dataclass(frozen=True)
class PackageSpec:
    name: str
    version: str


def parse_spec(spec: str) -> PackageSpec:
    """Parse ``name@version`` (scoped names like ``@scope/pkg@1.2.3`` included)."""
    at = spec.rfind("@")
    if at <= 0:
        raise ValueError(f"expected <package>@<version>, got {spec!r}")
    name, version = spec[:at], spec[at + 1 :]
    if not version:
        raise ValueError(f"missing version in {spec!r}")
    if not _NAME_RE.match(name):
        raise ValueError(f"invalid npm package name: {name!r}")
    return PackageSpec(name=name, version=version)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="suplens",
        description="Compare a published npm release with its source repository.",
    )
    parser.add_argument("--version", action="version", version=f"suplens {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="check one release, e.g. suplens check axios@1.8.2")
    check.add_argument("spec", help="<package>@<version>")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "check":
        try:
            spec = parse_spec(args.spec)
        except ValueError as exc:
            parser.error(str(exc))
        print(
            f"suplens: checking {spec.name}@{spec.version} is not implemented yet "
            "(coming in the comparison engine milestone).",
            file=sys.stderr,
        )
        return 2

    return 1  # unreachable: argparse enforces a command
