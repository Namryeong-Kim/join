import sys
from crytic_compile import CryticCompile, InvalidCompilation
# from slither.core.compilation_unit import SlitherCompilationUnit
# from slither.solc_parsing.slither_compilation_unit_solc import SlitherCompilationUnitSolc
from join.solc_parse.parser import parser

def main():
    target = sys.argv[1]
    print("solc parsing...")
    parser()

    target = CryticCompile(sys.argv[1]) # compile

    try:
        if isinstance(target, CryticCompile):
            crytic_compile = target
            print("1",crytic_compile)
        else:
            crytic_compile = CryticCompile(target)
            print("2",crytic_compile)
            #_crytic_compile = crytic_compile
    except InvalidCompilation as e:
        # pylint: disable=raise-missing-from
        raise print(f"Invalid compilation: \n{str(e)}")
    
if __name__ == "__main__":
    main()