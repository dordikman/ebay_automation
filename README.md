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
    - Running in default browser: 
        ```
        pytest tests/test_search.py
        ```
    - Running in headed mode: 
        ```
        pytest tests/test_search.py --headed
        ```
    - Running in other browsers: 
        ```
        pytest tests/test_search.py --browser chromium
        pytest tests/test_search.py --browser firefox
        ```
    - Running in WebKit:
        ```
        pytest tests/test_search.py --browser webkit
        ```
    - Running in parallel:
        ```
        pytest tests/test_search.py --browser chromium --browser firefox --browser webkit
        ```




