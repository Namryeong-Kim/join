import sys
from pathlib import Path

from crytic_compile import CryticCompile, CompilationUnit
from join.compile.compilation_unit import SlitherCompilationUnit
from join.compile.solc_parse.parser import parse
from typing import Union, List, ValuesView, Type, Dict, Optional

from join.core.scope.scope import FileScope
from join.core.declarations import Import


def main():
    target = sys.argv[1]
    target_path = Path(target)
    crytic_compile = CryticCompile(target)
    compilation_units = SlitherCompilationUnit(crytic_compile)
    print(compilation_units.import_directives)

    file_scope = FileScope(target_path)
    import_obj = Import(target_path, file_scope)
    print(import_obj.filename_path)
    print(import_obj.filename)
    print(import_obj.alias)
    import_obj.alias = "my_alias"
    print(import_obj.alias)


if __name__ == "__main__":
    main()



