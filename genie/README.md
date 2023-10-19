## Commands to execute test cases
| Command | Usage |
| ------ | ------ |
| pytest | Execute all tests |
| pytest .\pangea | Execute test cases unders a specific project |
| pytest .\pangea\test_sectors.py | Execute a specific module |
| pytest .\test_sectors.py::test_fetch_sectors_api | Execute a specific test case |
| pytest -vs | v-Verbose and s-displays the print statements  |
| pytest -k TRISQUARE_1 | k-select all test cases with the tag TRISQUARE_1 |