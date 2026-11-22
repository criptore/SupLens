import pytest

from suplens import __version__
from suplens.cli import PackageSpec, main, parse_spec


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("axios@1.8.2", PackageSpec("axios", "1.8.2")),
        ("@tanstack/query-core@5.0.0", PackageSpec("@tanstack/query-core", "5.0.0")),
        ("left-pad@1.3.0-beta.1", PackageSpec("left-pad", "1.3.0-beta.1")),
    ],
)
def test_parse_spec_valid(raw, expected):
    assert parse_spec(raw) == expected


@pytest.mark.parametrize("raw", ["axios", "axios@", "@scope/pkg", "@1.0.0", "Bad Name@1.0.0"])
def test_parse_spec_invalid(raw):
    with pytest.raises(ValueError):
        parse_spec(raw)


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    assert __version__ in capsys.readouterr().out


def test_check_is_a_stub_for_now(capsys):
    assert main(["check", "axios@1.8.2"]) == 2
    assert "not implemented yet" in capsys.readouterr().err


def test_check_rejects_bad_spec():
    with pytest.raises(SystemExit) as exc:
        main(["check", "axios"])
    assert exc.value.code == 2
