# SEC 8-K Filing Analysis System

A real-time monitoring and analysis system for SEC 8-K filings using Claude AI for sentiment analysis. The system specifically focuses on Item 1.01 filings and excludes penny stocks to improve signal quality.

## Features

- Real-time monitoring of SEC EDGAR 8-K filings
- Automatic filtering of penny stocks (share price < $5)
- Sentiment analysis of Item 1.01 content using Claude AI
- Local SQLite database for tracking analyzed filings
- Continuous monitoring with customizable intervals
- Historical analysis tracking and reporting

## Prerequisites

- Python 3.8+
- Claude API key
- SQLite3
- Internet connection for SEC EDGAR access

## Required Python Packages

```bash
pip install requests
pip install beautifulsoup4
pip install pandas
pip install yfinance
```

## Environment Setup

1. Set up your Claude API key as an environment variable:

```bash
export CLAUDE_API_SECRET_KEY="your-api-key-here"
```

2. Ensure your SEC EDGAR access is properly configured with your contact information in the headers:

```python
headers = {
    'User-Agent': 'Your Name your.email@domain.com',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.sec.gov'
}
```

## Usage

### Running the Program

```bash
python data_collection.py
```

### Main Menu Options

1. **View Filing History**
   - Displays all previously analyzed filings
   - Saves history to a timestamped file

2. **Start Continuous Monitoring**
   - Monitors for new 8-K filings in real-time
   - Customizable number of filings to check
   - Option to skip previously analyzed filings

3. **Exit**
   - Safely exits the program

### Analysis Format

The sentiment analysis results are formatted as:
```
[sentiment] [chance]% [confidence]%
```

Where:
- `sentiment`: extremely negative, negative, neutral, positive, or extremely positive
- `chance`: percentage likelihood of the predicted movement
- `confidence`: confidence level in the prediction

## Database Structure

The system uses SQLite to store analyzed filings with the following schema:

```sql
CREATE TABLE analyzed_filings (
    cik TEXT,
    filing_date TEXT,
    accession_number TEXT PRIMARY KEY,
    sentiment TEXT,
    analysis_date TEXT
)
```

## Error Handling

- Robust error handling for API calls and file operations
- Automatic retry mechanisms for SEC EDGAR rate limits
- Database connection error management
- Invalid filing format handling

## Limitations

- Limited to Item 1.01 content in 8-K filings
- Requires active internet connection
- Subject to SEC EDGAR access rate limits
- Excludes stocks trading under $5

## Best Practices

1. Respect SEC EDGAR rate limits
2. Regularly clean old database entries
3. Monitor API usage and costs
4. Keep environment variables secure
5. Regularly backup the SQLite database

## Contributing

Contributions are welcome! Please feel free to submit pull requests with improvements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.