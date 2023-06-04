import sys
from crytic_compile import CryticCompile
from join.compile.compilation_unit import SlitherCompilationUnit


def main():
    target = sys.argv[1]

    crytic_compile = CryticCompile(target)
    compilation_units= SlitherCompilationUnit(crytic_compile)
    
    print(compilation_units.custom_errors)


if __name__ == "__main__":
    main()