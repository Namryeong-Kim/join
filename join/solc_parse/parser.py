import join.solc_parse.parser_function as ps
import join.solc_parse.parser_env as env

def parser():
    env.halt_incompatible_system()
    version_list = ps.get_version_list()
    solidity_file = ps.get_solidity_source()
    sign, version = ps.parse_solidity_version(solidity_file)
    #print("[Input]", sign, version)
    check = ps.check_version(version_list, version)
    if check == False:
        print("incorrect version")
        return
    if len(version) != 1:
        sign, version = ps.compare_version(sign, version)
    sign = sign[0]
    version = version[0]
    
    index = ps.find_matching_index(version, version_list)

    if sign == '<':
        version = version_list[index - 1]
        #print("[Output]", version)
        ps.install_solc(version)
    elif sign == '>':
        version = version_list[index + 1]
        #print("[Output]", version)
        ps.install_solc(version)
    elif (sign == '^' or sign == '~'):
        version = ps.get_highest_version(version_list, version)
        #print("[Output]", version)
        ps.install_solc(version)
    elif (sign == '=' or sign == '>=' or sign == '<=') or (not sign and version):
        #print("[Output]", version)
        ps.install_solc(version)
    else:
        print("incorrect sign")
        return

if __name__ == "__main__":
    parser()