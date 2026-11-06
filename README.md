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
| C1 Value of stars | below 1 | 0 | `test_stars_out_of_range[0]` |
| | 1 to 5 (base) | 3 | `test_base_choice_is_saved` |
| | above 5 | 6 | `test_stars_out_of_range[6]` |
| C2 Type of stars | whole number (base) | 3 | `test_base_choice_is_saved` |
| | decimal | 3.5 | `test_stars_decimal` |
| | text | "3" | `test_stars_text` |
| | missing | no field | `test_stars_missing` |
| C3 Pizza | exists (base) | a new pizza | `test_base_choice_is_saved` |
| | does not exist | 999999999 | `test_pizza_does_not_exist` |
| C4 Token | the user's own (base) | from auth | `test_base_choice_is_saved` |
| | none | no header | `test_rating_without_token` |
| | wrong length | token short | `test_rating_with_short_token` |