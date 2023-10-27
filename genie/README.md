## Commands to execute test cases
| Command | Usage |
| ------ | ------ |
| pytest | Execute all tests |
| pytest .\pangea | Execute test cases unders a specific project module|
| pytest .\pangea\test_sectors.py | Execute all test cases in a file |
| pytest .\test_sectors.py::test_fetch_sectors_api | Execute a specific test case in the file |
| pytest -vs | v-Verbose and s-displays the print statements  |
| pytest -m "TRISQUARE_1" | m-select all test cases with the marker TRISQUARE_1 |
| pytest -k "TRISQUARE_12" | k-select 1 test cse with the marker TRISQUARE_12 |
