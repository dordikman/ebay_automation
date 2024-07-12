# eBay Automation Test Suite

## Setup Instructions

1. Clone the repository:
    ```
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```
    cd ebay_automation
    ```

3. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

5. Use the terminal to run the tests:
   ...
   running in default browser: pytest tests/test_search.py 
   running in headed mode: pytest tests/test_search.py --headed
   running in other browser: pytest tests/test_search.py --browser chromium/firefox....
   running in webkit: pytest tests/test_search.py --browser webkit
   running in parallel: pytest tests/test_search.py --browser chromium --browser firefox --browser webkit 