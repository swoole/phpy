from __future__ import annotations

import os
import re
import shlex
import subprocess
from pathlib import Path

from setuptools import Extension, setup


ROOT = Path(__file__).parent.resolve()


def php_config(*arguments: str) -> str:
    executable = os.environ.get("PHP_CONFIG", "php-config")
    try:
        return subprocess.check_output(
            [executable, *arguments],
            cwd=ROOT,
            text=True,
        ).strip()
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        raise RuntimeError(
            f"Unable to run {executable!r}. Install PHP with embed support, "
            "or set PHP_CONFIG to the matching php-config executable."
        ) from error


def compiler_options() -> tuple[list[str], list[str], list[str]]:
    include_dirs: list[str] = [str(ROOT), str(ROOT / "include")]
    for option in shlex.split(php_config("--includes")):
        if option.startswith("-I"):
            include_dirs.append(option[2:])

    prefix = Path(php_config("--prefix"))
    library_dirs = [str(prefix / "lib")]
    runtime_library_dirs = [] if os.name == "nt" else library_dirs.copy()
    return include_dirs, library_dirs, runtime_library_dirs


def package_version() -> str:
    header = (ROOT / "php_phpy.h").read_text(encoding="utf-8")
    match = re.search(r'PHP_PHPY_VERSION\s+"([^"]+)"', header)
    if match is None:
        raise RuntimeError("PHP_PHPY_VERSION is missing from php_phpy.h")
    return match.group(1)


include_dirs, library_dirs, runtime_library_dirs = compiler_options()
sources = [str(ROOT / "phpy.cc")]
sources.extend(str(source) for source in sorted((ROOT / "src").rglob("*.cc")))

setup(
    name="phpy",
    version=package_version(),
    description="Use PHP libraries from Python and Python libraries from PHP",
    license="Apache-2.0",
    python_requires=">=3.8",
    ext_modules=[
        Extension(
            "phpy",
            sources=sources,
            include_dirs=include_dirs,
            library_dirs=library_dirs,
            runtime_library_dirs=runtime_library_dirs,
            libraries=["php"],
            define_macros=[("HAVE_PHP_EMBED", "1"), ("PHPY_EXPORTS", "1")],
            extra_compile_args=["-std=c++14", "-Wall"],
            language="c++",
        )
    ],
)
