# ⚖️ AWS Referee: EC2 vs Lambda

A lightweight decision-support tool that helps users choose between **AWS EC2** and **AWS Lambda** by explaining **trade-offs** instead of giving a single “winner.”

---

## 📝 Problem Statement

Developers are often told which AWS service is “better” without understanding *why*.  
This can lead to poor architectural decisions when constraints like cost, scalability, latency, and operational overhead are ignored.

The AWS Referee tool solves this by providing **context-aware recommendations**, helping users make informed decisions instead of consuming generic advice.

---

## 💡 Solution Overview

The Referee tool:

- Accepts user inputs about workload constraints:
  - Cost sensitivity
  - Traffic patterns
  - Latency requirements
  - Operational overhead tolerance
- Compares EC2 and Lambda side-by-side
- Shows pros, cons, and trade-offs
- Provides a recommendation based on constraints
- Offers a visual, intuitive, and interactive UI

---

## 🛠️ Tech Stack

- **Python**  
- **Streamlit** for interactive UI

---

## 🤖 How Kiro Accelerated Development

Kiro AI was used to generate structured trade-off reasoning between EC2 and Lambda.  
This allowed rapid generation of:

- Clear pros and cons for each service
- Key trade-offs for different workload types
- Recommendation logic that adapts to user constraints

All Kiro outputs are included in the `/.kiro` directory, demonstrating how AI helped speed up decision analysis and informed the final application logic.

---

## 🖥️ Demo

The app displays:

- Comparison cards for **EC2** and **Lambda**
- Sidebar for workload inputs
- Verdict banner with recommendations
- Deep-dive tabs showing pricing, scalability, and maintenance considerations

Screenshots of the UI and Kiro outputs are included in the blog and repository.

---

## 📦 Setup & Run

1. Clone the repository:

git clone <your-repo-url>
cd aws-referee-ec2-vs-lambda

2. Install dependencies:

pip install -r requirements.txt

3. Run the app:

streamlit run app.py

