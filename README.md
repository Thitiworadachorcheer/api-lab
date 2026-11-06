# api-lab
API Testing with pytest and requests

# api-lab
API Testing with pytest and requests

## How to install and run the tests
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run all tests:
   ```bash
   pytest -v
   ```
3. Generate HTML report:
   ```bash
   pytest -v --html=report.html --self-contained-html
   ```

## Input domain model for POST /api/ratings

| Characteristic | Blocks | Values in the tests | Test covering block |
| -------------- | ------ | ------------------- | ------------------- |
| C1 Value of stars | below 1 | 0 | |
| | 1 to 5 (base) | 3 | `test_base_choice_is_saved` |
| | above 5 | 6 | |
| C2 Type of stars | whole number (base) | 3 | `test_base_choice_is_saved` |
| | decimal | 3.5 | |
| | text | "3" | |
| | missing | no field | |
| C3 Pizza | exists (base) | a new pizza | `test_base_choice_is_saved` |
| | does not exist | 999999999 | |
| C4 Token | the user's own (base) | from auth | `test_base_choice_is_saved` |
| | none | no header | |
| | wrong length | token short | |