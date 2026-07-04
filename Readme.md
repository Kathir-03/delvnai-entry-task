# DelvnAI Internship Entry Task

## Overview

This repository contains my submission for the **DelvnAI Technologies Software Engineering Internship Entry Task**.

The project is divided into two parts:

- **Part A:** Answers to the conceptual questions on operating systems, SQL joins, version control, and API performance.
- **Part B:** A Python program that reads transaction data from a CSV file, calculates the total amount spent in each category, sorts the totals in descending order, and handles malformed data gracefully without terminating the program.

---

## Project Structure

```text
delvnai-entry-task/
│
├── README.md
├── transactions_summary.py
└── transactions.csv
```

- **README.md** – Documentation and answers to the conceptual questions.
- **transactions.csv** – Sample transaction dataset.
- **transactions_summary.py** – Python program that processes the transaction data.

---

## Part A – Fundamentals

### 1. Process vs Thread

A process is an independent program that is executed by the operating system. Each process has its own memory and system resources.

A thread is the smallest unit of execution within a process. Multiple threads inside the same process share memory and resources, allowing different tasks to run concurrently.

**Example:**

The operating system creates separate processes for applications like Chrome, Spotify, and VS Code. Each process runs independently, so if one application crashes, the others continue to work. Inside the Chrome process, multiple threads handle tasks such as downloading files, rendering web pages, and responding to user interactions simultaneously, making the browser more responsive.

---

### 2. LEFT JOIN vs INNER JOIN

A LEFT JOIN returns all the rows from the left table and only the matching rows from the right table. If there is no matching record in the right table, the corresponding columns are filled with **NULL**.

An INNER JOIN returns only the rows that have matching values in both tables.

**Example:**

Suppose the **Employee** table contains four employees, but only two of them have matching department IDs in the **Department** table.

- Using **INNER JOIN**, only those two matching employees are returned.
- Using **LEFT JOIN**, all four employees are returned, and the employees without matching departments will have **NULL** in the department column.

---

### 3. Version Control, Commit and Pull Request

**Version Control** – Version control is a system that tracks changes made to the source code over time. It helps maintain the history of a project, allowing developers to retrieve previous versions and collaborate without losing changes.

**Commit** – A commit is a snapshot of the project at a particular point in time. It records the code changes along with details such as the author, date and time, and a commit message describing what was changed.

**Pull Request** – A pull request is a request to merge changes from one branch into another. It allows team members to review the code, suggest improvements, and approve or reject the changes before they become part of the main codebase.

---

### 4. Causes for Slow API Response

#### 1. Slow Server Processing

The API response may be delayed due to complex database queries, high server load, or multiple users accessing the server simultaneously. As a result, the server takes longer to process the request.

**Steps to investigate:**

- Monitor the API response time.
- Check server logs for slow requests or errors.
- Monitor CPU and resource usage.

#### 2. Network Latency

The API response may also be delayed due to the time taken for data to travel between the client and the server. This can happen because of a slow internet connection, high network traffic, or long geographical distances.

**Steps to investigate:**

- Measure the total request time.
- Test the API from different networks or locations.
- Use network diagnostic tools such as `ping` and `traceroute` to identify network delays.

---

## Part B – Coding Task

### Objective

Develop a Python program that reads transaction data from a CSV file, calculates the total amount for each transaction category, sorts the totals in descending order, and handles malformed or invalid records gracefully without terminating the program.

---

### Features

- Reads transaction data from a CSV file.
- Calculates the total amount for each category.
- Sorts the categories in descending order based on the total amount.
- Handles invalid or malformed records using exception handling.
- Continues processing valid records even when invalid rows are encountered.
- Produces a clean and readable console output.

---

### Input Format

The program expects a CSV file named `transactions.csv` with the following structure:

```csv
date,category,amount
2026-06-04,Food,385
2026-06-05,Utilities,2378
2026-06-06,Food,511
```

---

### Sample Output

```text
Software : 17547
Utilities : 6614
Food : 1739
Groceries : 1694
Travel : 1627
Entertainment : 1119
```

---

### Error Handling

The program uses Python's `try-except` mechanism to handle malformed or invalid records gracefully instead of terminating execution.

The following scenarios are handled:

- Invalid numeric values (for example, `abc` instead of a number).
- Missing transaction category.
- Missing transaction amount.

Invalid rows are skipped, an appropriate error message is displayed, and the remaining valid records continue to be processed.

---

### How to Run

#### Prerequisites

- Python 3.x

#### Steps

1. Clone this repository.
2. Open a terminal in the project directory.
3. Ensure `transactions.csv` is present in the project folder.
4. Run the following command:

```bash
python transactions_summary.py
```

---

### Future Improvements

If I had more time, I would create a simple graphical interface so users could upload a CSV file and view the summarized results more easily.

---

## Part C – Reflection

Previously, while sorting a dictionary based on a specific value, I used the `lambda` function without fully understanding how it worked. So, I explored it further and gained a better understanding of its usage.

Apart from this, I used AI as my companion in my coding process that helped me work through each step with proper understanding.
