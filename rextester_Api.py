import requests
#github.com/MystiqueShade | Channel : @MystiqueShade
languages = {
    "c#": 1,
    "csharp": "c#",
    "vb.net": 2,
    "vb": 2,
    "visual_basic_dotnet": 2,
    "f#": 3,
    "fsharp": 3,
    "java": 4,
    "python2": 5,
    "py2": 5,
    "c_gcc": 6,
    "gcc": 6,
    "c": ["gcc", "clang", "visual_c"],
    "cplusplus_gcc": 7,
    "cplusplus": "c++",
    "g++": 7,
    "c++": ["cplusplus_gcc", "cplusplus_clang", "visual_cplusplus"],
    "cpp_gcc": 7,
    "cpp": "c++",
    "php": 8,
    "pascal": 9,
    "pas": 9,
    "fpc": 9,
    "objective_c": 10,
    "objc": 10,
    "haskell": 11,
    "ruby": 12,
    "perl": 13,
    "lua": 14,
    "nasm": 15,
    "asm": 15,
    "sql_server": 16,
    "v8": 17,
    "common_lisp": 18,
    "clisp": 18,
    "lisp": ["common_lisp", "scheme"],
    "prolog": 19,
    "golang": 20,
    "go": 20,
    "scala": 21,
    "scheme": 22,
    "node": 23,
    "javascript": 23,
    "js": "javascript",
    "python3": 24,
    "py3": 24,
    "python": ["python3", "python2"],
    "c_clang": 26,
    "clang": 26,
    "cplusplus_clang": 27,
    "cpp_clang": 27,
    "clangplusplus": 27,
    "clang++": 27,
    "visual_cplusplus": 28,
    "visual_cpp": 28,
    "vc++": 28,
    "msvc": 28,
    "visual_c": 29,
    "d": 30,
    "r": 31,
    "tcl": 32,
    "mysql": 33,
    "postgresql": 34,
    "oracle": 35,
    "swift": 37,
    "bash": 38,
    "ada": 39,
    "erlang": 40,
    "elixir": 41,
    "ocaml": 42,
    "kotlin": 43,
    "brainfuck": 44,
    "fortran": 45,
}

class RextesterError(Exception):
    pass

class Rextester:
    def __init__(self, lang, code):
        self.URL = "https://rextester.com/rundotnet/Run"
        if lang not in languages:
            raise RextesterError("The entered language is incorrect!")

        data = {"LanguageChoiceWrapper": languages[lang], "Program": code}

        request = requests.post(self.URL, data=data)
        self.response = request.json()
        self.result = self.response["Result"]
        self.warnings = self.response["Warnings"]
        self.errors = self.response["Errors"]
        self.stats = self.response["Stats"]
        self.files = self.response["Files"]

        if not code:
            raise RextesterError("Your input will be incorrect!")

        elif not any([self.result, self.warnings, self.errors]):
            raise RextesterError("Your request is incomplete!")
