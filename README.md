# Higher-for-Longer Debt & Inflation Simulator

A Python-based financial simulation that demonstrates how debt, savings, and inflation can evolve over time under a higher-for-longer interest-rate environment.

## Project Overview

This project simulates the financial impact of:

- Rising debt at a fixed interest rate
- Savings growth at a fixed return
- Annual inflation fluctuations
- Inflation gradually moving toward an assumed target
- The effect of inflation on real purchasing power
- Nominal and inflation-adjusted net worth

The application is built as an interactive Streamlit web app, allowing users to enter their own financial values and simulate different time periods.

## Features

- Interactive debt and savings inputs
- Adjustable simulation period
- Annual inflation simulation
- Debt vs. savings visualization
- Inflation trend visualization
- Nominal net worth analysis
- Real net worth analysis
- Real purchasing power calculation
- Year-by-year simulation table

## Economic Assumptions

The current simulation uses:

- Starting inflation: 3.48%
- Target inflation: 4.00%
- Maximum assumed inflation: 6.00%
- Debt interest rate: 12.00%
- Savings return: 5.00%

Inflation includes randomized annual fluctuations and gradually moves toward the assumed target.

## Technologies Used

- Python
- Streamlit
- Pandas
- Random module
- Data visualization

## Project Structure

```text
higher-for-longer-inflation-simulator/
│
├── app.py
├── requirements.txt
└── README.md