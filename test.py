from pathlib import Path
from slither import Slither
from crytic_compile import CryticCompile, InvalidCompilation
from slither.core.compilation_unit import SlitherCompilationUnit
from slither.solc_parsing.slither_compilation_unit_solc import SlitherCompilationUnitSolc
from slither.detectors import all_detectors
from argparse import Namespace
from slither.tools.similarity.test import test

compiled_sol = CryticCompile('./reentrancy.sol') # compile
slither = Slither(compiled_sol) # slither
slither.register_detector(all_detectors.ReentrancyEth)

args = Namespace()
args.model = "etherscan_verified_contracts.bin"
args.filename = compiled_sol.filename 
args.contract = slither.contracts[0].name
args.fname = "EtherStore.withdraw" 
args.input = "cache.npz"  
args.ntop = 10  

test(args)


# results = slither.run_detectors()
# for detector_result in results:
#     for result in detector_result:
#         print(result['description'])


# print(compiled_sol.src_content)
# for compilation_unit in compiled_sol.compilation_units.values():
#     compilation_unit_slither = SlitherCompilationUnit("SlitherCore", compilation_unit)
#     parser = SlitherCompilationUnitSolc(compilation_unit_slither)


# for contract in slither.contracts:
#     for function in contract.functions:
#         for node in function.nodes:
#             print(node.add_inline_asm)
#             print(node.can_reenter)
#             print(node.can_send_eth)
#             for inner_node in node.sons:
#                 print(inner_node)
#                 for ir in inner_node.irs:
#                     print(ir)
