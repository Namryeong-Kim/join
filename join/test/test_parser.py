
from join.compile.solc_parse.parser import parse
from solc_select.solc_select import installed_versions, install_artifacts

def main():
    print(installed_versions())
    # install_artifacts([])
    # print(installed_versions())
    parse()

if __name__ == "__main__":
    main()