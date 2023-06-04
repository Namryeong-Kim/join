import sys
from crytic_compile import CryticCompile
from join.compile.compilation_unit import SlitherCompilationUnit
from join.compile.solc_parse.parser import parse
from typing import Union, List, ValuesView, Type, Dict, Optional
from join.core.declarations import Pragma


def main():
    target = sys.argv[1]

    # parsing solc verison in solidity file automatically
    #parse()

    crytic_compile = CryticCompile(target)
    compilation_units= SlitherCompilationUnit(crytic_compile)
    
    compilation_units.pragma_directives.append(Pragma(["solidity", "^0.8.0;"], "./reentrancy.sol"))
    print(compilation_units.pragma_directives[0])

    for pragma in compilation_units.pragma_directives:
        print(pragma.name)
        print(pragma.version)
        print(pragma.is_solidity_version)
        print(pragma.is_abi_encoder_v2)
        print(pragma.directive)
        print(pragma.scope)
        print(pragma.__str__())


if __name__ == "__main__":
    main()