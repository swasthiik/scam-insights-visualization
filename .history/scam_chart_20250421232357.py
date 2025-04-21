vimport pandas as pd
import matplotlib.pyplot as plt

# Simulated data
data = {
    'message': [
        "Please share OTP to proceed",
        "Get a job with 10LPA, click now",
        "You've won $10,000 lottery",
        "Your bank account is blocked, login now",
        "OTP required to verify account",
        "Urgent job offer without interview",
        "Claim your lottery prize now!",
        "Verify your bank account immediately",
        "Your OTP is 482918, do not share",
        "Congratulations! You are selected for a job"
    ],
    'label': [
        'OTP Scam', 'Job Fraud', 'Fake Lottery', 'Bank Fraud',
        'OTP Scam', 'Job Fraud', 'Fake Lottery', 'Bank Fraud',
        'OTP Scam', 'Job Fraud'
    ]
}

df = pd.DataFrame(data)

grouped = df['label'].value_counts().reset_index()
grouped.columns = ['Scam Type', 'Count']

# Plot
plt.figure(figsize=(8, 8))
plt.pie(
    grouped['Count'],
    labels=grouped['Scam Type'],
    autopct='%1.1f%%',
    startangle=90,
    explode=[0.1 if i == 0 else 0 for i in range(len(grouped))],
    shadow=True,
    colors=['#f87171','#60a5fa','#facc15','#34d399']
)

plt.title("📊 Scam Message Categories (Simulated Data)")
plt.show()