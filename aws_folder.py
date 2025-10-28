import os

# Path to your existing AWS folder (adjust if needed)
aws_folder = "devops-notes-hub/AWS"

# List of AWS services and their folder names
aws_subtopics = [
    "Amazon EC2",
    "Amazon S3",
    "AWS Lambda",
    "Amazon RDS",
    "Amazon VPC",
    "Amazon CloudFront",
    "AWS IAM",
    "Amazon DynamoDB",
    "AWS Elastic Beanstalk",
    "Amazon Route 53"
]

# Ensure AWS folder exists
if not os.path.exists(aws_folder):
    print("❌ AWS folder not found! Please check the path.")
else:
    # Loop through each subtopic
    for service in aws_subtopics:
        service_path = os.path.join(aws_folder, service)
        os.makedirs(service_path, exist_ok=True)

        # Create concept.md
        concept_file = os.path.join(service_path, "concept.md")
        if not os.path.exists(concept_file):
            with open(concept_file, "w") as f:
                f.write(f"# {service} Concepts\n\n")
                f.write("> Write down the key concepts, architecture, and use cases here.\n")

        # Create interview_question.md
        interview_file = os.path.join(service_path, "interview_question.md")
        if not os.path.exists(interview_file):
            with open(interview_file, "w") as f:
                f.write(f"# {service} Interview Questions\n\n")
                f.write("> Add commonly asked interview questions and answers here.\n")

    print(f"✅ AWS subfolder structure created successfully inside '{aws_folder}'!")
