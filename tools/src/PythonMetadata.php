<?php

namespace PhpyTool;

class PythonMetadata
{
    public static function isStdLibrary(string $module)
    {
        static $stdLibrary = null;
        if (!$stdLibrary) {
            $stdLibrary = array_flip(self::getStdLibrary());
        }
        return isset($stdLibrary[$module]);
    }

    private static function getStdLibrary(): array
    {
        return [
            "os",
            "sys",
            "re",
            "math",
            "random",
            "dataclasses",
            "json",
            "datetime",
            "time",
            "calendar",
            "collections",
            "heapq",
            "bisect",
            "array",
            "weakref",
            "types",
            "copy",
            "pprint",
            "reprlib",
            "enum",
            "numbers",
            "textwrap",
            "this",
            "cmath",
            "decimal",
            "fractions",
            "statistics",
            "itertools",
            "functools",
            "operator",
            "pathlib",
            "fileinput",
            "stat",
            "filecmp",
            "tempfile",
            "glob",
            "fnmatch",
            "linecache",
            "shutil",
            "macpath",
            "pickle",
            "copyreg",
            "shelve",
            "marshal",
            "dbm",
            "sqlite3",
            "zlib",
            "gzip",
            "bz2",
            "lzma",
            "zipfile",
            "tarfile",
            "csv",
            "configparser",
            "netrc",
            "xdrlib",
            "plistlib",
            "hashlib",
            "hmac",
            "secrets",
            "builtins",
            "platform",
            "asyncio",
            "socket",
            "turtle",
            "typing",
            "tkinter",
        ];
    }

    static function getPipPackage(string $module): ?string
    {
        static $map = array(
            "torch" => "torch",
            "transformers" => "transformers",
            "accelerate" => "accelerate",
            "TermTk" => "pytermtk",
            "paddlenlp" => "paddlenlp",
            "cefpython3" => "cefpython3",
            "dearpygui" => "dearpygui",
            "pygame" => "pygame",
            "gi" => "PyGObject",
            "gradio_client" => "gradio_client",
            "gradio" => "gradio",
            "openai" => "openai",
            "webview" => "pywebview",
            "numpy" => "numpy",
            "magicgui" => "magicgui",
            "modelscope" => "modelscope",
            "tqdm" => "tqdm",
            "llama_index" => "llama-index",
            "wx" => "wxPython",
            "pyqt5" => "PyQt5",
        );

        [$root] = explode('.', $module);
        return $map[$root] ?? null;
    }
}