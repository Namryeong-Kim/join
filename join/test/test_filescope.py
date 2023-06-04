import sys
from crytic_compile import CryticCompile, CompilationUnit
from join.compile.compilation_unit import SlitherCompilationUnit
from join.compile.solc_parse.parser import parse
from typing import Union, List, ValuesView, Type, Dict, Optional
from pathlib import Path
from join.core.scope.scope import FileScope


def get_scope_test(target):
    
    crytic_compile = CryticCompile(target)
    filename = "./reentrancy.sol"
    compilation_uint = CompilationUnit(crytic_compile, filename)
    compilation_units = SlitherCompilationUnit(compilation_uint)
    file_scope = compilation_units.get_scope("reentrancy.sol")
    print(file_scope)

def file_scope_test(target):
    crytic_compile = CryticCompile(target)
    target_path = Path(target)
    compilation_units = SlitherCompilationUnit(crytic_compile)
    print(compilation_units.import_directives)

    file_scope = FileScope(target_path)
    print(file_scope)
    #file_scope = FileScope("./reentrancy.sol")

    # accessible_scopes에 다른 FileScope 객체 추가
    accessible_scope_1 = FileScope("../reentrancy.sol")
    file_scope.accessible_scopes.append(accessible_scope_1)

    print(file_scope.add_accesible_scopes())
    #print(file_scope.srcmap_runtime(compilation_units, "EtherStore"))


def main():
    target = sys.argv[1]
    #get_scope_test(target)
    file_scope_test(target)



if __name__ == "__main__":
    main()



