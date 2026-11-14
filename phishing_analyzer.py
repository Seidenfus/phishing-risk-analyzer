# AI DEVELOPMENT LOG
#
# Copilot Prompt 1: We are going to create a beginner-friendly Python program that asks a user questions about a suspicious email and gives it a low, medium, or high phishing risk rating.
#
# Copilot Prompt 2:
#
# Copilot Prompt 3:
#
# One problem or bug I encountered: Program didn't ask if user wants to analyze another message.
#
# How I fixed it: Added return to function "aks_yes_no" at the end of the program and goodbye message if user says no. 
#
# One change I made myself without Copilot: Improved wording. Risk rating displayed Low level while scoring 2 warning signs; Was modified to display Medium risk rating when scoring 2 signs.
#
##1. How does your program calculate the phishing risk?
#-Represents "yes" as 1 and "no" as 0, sums all the answers for a final value that represents a rating on the risk level.  
##2. Why does your program use a list to store warning signs?
#-This makes it easier to count and validate the questions, modify the program in the future and use a loop to ask questions.
##3. Why can a suspicious link be a sign of phishing?
#-An untrusted link could mean that it leads to a malicious websites that will try to retrieve your sensitive information.

"""A simple, beginner-friendly phishing risk analyzer."""


def ask_yes_no(question):
    """Ask a question until the user enters yes or no."""
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer in {"yes", "y"}:
            return True
        if answer in {"no", "n"}:
            return False
        print("Please answer with yes or no.")


def get_risk_rating(score):
    """Return a risk rating for a phishing warning score."""
    if score >= 4:
        return "High"
    if score >= 2:
        return "Medium"
    return "Low"


def analyze_email():
    """Ask about an email and display its phishing risk rating."""
    print("Phishing Risk Analyzer")
    print("Answer a few questions about the suspicious email.\n")

    warning_signs = [
        "Is the sender unknown or unexpected?",
        "Does the email create urgency or pressure you to act quickly?",
        "Does it ask for a password, payment, or other personal information?",
        "Does it include a link that looks unusual or does not match the claimed website?",
        "Does it contain an unexpected attachment?",
        "Does it promise a prize, refund, or other offer that seems too good to be true?",
    ]

    score = sum(ask_yes_no(question) for question in warning_signs)
    rating = get_risk_rating(score)

    print(f"\nRisk rating: {rating}")
    print(f"Warning signs found: {score} out of {len(warning_signs)}")

    if rating == "High":
        print("Avoid clicking links, opening attachments, or replying.")
    elif rating == "Medium":
        print("You should verify sender by trusted methods. Check the sender email address for suspicious signs, check if links match real trusted websites or have suspicious behavior before acting.")
    else:
        print("Few warning signs were found, but stay cautious and verify unexpected requests.")

    return ask_yes_no("\nWould you like to analyze another message?")



if __name__ == "__main__":
    while True:
        if not analyze_email():
            print("Goodbye!")
            break