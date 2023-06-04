import sys
from crytic_compile import CryticCompile
from join.compile.compilation_unit import SlitherCompilationUnit
from join.compile.solc_parse.parser import parse
from typing import Union, List, ValuesView, Type, Dict, Optional

from join.core.scope.scope import FileScope


def main():
    target = sys.argv[1]

    crytic_compile = CryticCompile(target)
    compilation_units= SlitherCompilationUnit(crytic_compile)


    # FileScope 객체 생성
    file_scope = FileScope("./reentrancy.sol")

    # accessible_scopes에 다른 FileScope 객체를 추가
    accessible_scope_1 = FileScope("../reentrancy.sol")
    file_scope.accessible_scopes.append(accessible_scope_1)

    print(file_scope.add_accesible_scopes())
    print(file_scope.srcmap_runtime(compilation_units, "EtherStore"))


if __name__ == "__main__":
    main()



