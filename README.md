# Data Development Pathway with Python and SQL
This is an example project for the Code Louisville Python Data Development Course.

## Project Requirements
1. Project is uploaded to your GitHub repository and shows at minimum 5 separate commits
   * **Using GitHub’s file uploader does not count as a check-in**. You must upload via Git
1. Project includes a README file that explains the following:
   * A one paragraph or longer description of what your project is about.
   * **Relevant packages that need installed to run the project**.
   * Which 3+ features you have included from the below lists to meet the requirements
   * Any special instructions required for the reviewer to run your project. (For example: **“run python main.py” from the command line**)
   * Guide to use markdown for README.md files (https://guides.github.com/features/mastering-markdown/)
1. Choose at least 3 items on the Features List below and implement them in your project
   * We recommend you pick a 4th item (or more!) to add, just in case something goes wrong with one of your other items - 3 is only the minimum requirement

### FEATURE LIST
  * Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.
  * Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code.
  * Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
  * Implement a log that records errors, invalid inputs, or other important events and writes them to a text file.
  * Read data from an external file, such as text, JSON, CSV, etc and use that data in your application.
  * Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code. For example, you could create a function that reads how many items there are in a text file, returns that value, and later uses that value to execute a loop a certain number of times.
  * Implement a regular expression (regex) to ensure a field either a phone number or an email address is always stored and displayed in the same format.
  * Connect to an external/3rd party API and read data into your app
  * Create 3 or more unit tests for your application.
  * Build a conversion tool that converts user input to another type and displays it (ex: converts cups to grams).
  * Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event).
  * Analyze text and display information about it (ex: how many words in a paragraph).
  * Visualize data in a graph, chart, or other visual representation of data.
  * Other features can be added to this list with mentor or staff permission, but we want to see you stretch your skills, so you’ll want to pick something challenging.

### "STRETCH” FEATURE LIST
These count too! But they will require going outside of the base curriculum to learn about and may be more challenging.
  * Implement a “scraper” that can be fed a type of file or URL and pull information off of it. For example, a web scraper that lets you provide any website URL and it will find certain keywords on the page.
  * Implement optical character recognition (OCR) that you can upload PDFs to and it will generate the text.

Project Requirements doc:  https://docs.google.com/document/d/1ynpHplwh_JajXUkICg0RQ-kquZt7K8KqxcC1YHSYxrc/edit#heading=h.yo1u3nm5kgy


# My Project
Using Google's BigQuery DataSet from the Ethereum blockchain this package will query for the top 10 most popular collectibles (ERC-721 contracts), by number of transactions.  The results will be inspected, and a project confidence score will be returned for each project.

## Requirements
* a working Python environment using Python 3.9.6 or newer
* a Google account for BigQuery
* Google Cloud CLI installed https://cloud.google.com/sdk/docs/quickstart
  * create a new project
  * enter project name of your choice
* Enable BigQuery API for the project
  * https://console.developers.google.com/apis/library/bigquery.googleapis.com?project=$PROJECT_ID

## Instructions
1. Pull the code down:  `git clone git@github.com:white8785/codelouisvillepython2022.git`
1. Enter project folder:  `cd codelouisvillepython2022`
1. Install required Python packages:  `pip install -r requirements`
1. Setup Authentication for BigQuery: https://github.com/googleapis/python-bigquery-sqlalchemy#authentication
    ```
    gcloud auth application-default login
    gcloud auth login
    # if ^^^ is unsupported, update
    # gcloud components update
    ```
1. Execute:  `python ./main.py`

## Expectations
Data will be pulled from [BigQuery](https://console.cloud.google.com/marketplace/product/ethereum/crypto-ethereum-blockchain?pli=1&project=unifi-254402), the Ethereum Blockchain will be inspected, and a chart for visualization will be displayed.

## Features Implemented
1. Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code.
1. Calculate and display data based on an external factor.
1. Connect to an external/3rd party API and read data into your app
1. Visualize data in a graph, chart, or other visual represenation of data.


# Core Python Documentation References
  * Setting up a proper Python package: https://packaging.python.org/tutorials/packaging-projects/
  * [python.org](python.org)
  * [PEP8](python.org/dev/peps)