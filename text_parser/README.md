Optional file text searcher
_______________________________

Pre-Requirements:
1) In case of usage python version lower than 2.7 need to install argparse module
  - pip install -r requirments.txt

Run:
./parse_runner.py -f <file-path> -u <reg ex pattern> -c<reg ex pattern> -m <reg ex pattern>
 file-path - should be absolute in case if it out of file_storage dir in another case you can indicate just file name from dir
 -u -c -m params are mutually exclusive

Example for running:
 (e.g ./parse-runner.py -f file1.txt -m \d+)

 Multiple files:
 (e.g ./parse-runner.py -f file1.txt file2.txt -m \d+)
