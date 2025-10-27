import os

base_folder = "devops-notes-hub"

topic = [
    "Docker",
    "Kubernetes",
    "Jenkins",
    "Terraform",
    "AWS",
    "Linux",
    "Bash",
    "Python",
    "Git",
    "Prometheus",
    "Grafana"
]

os.makedirs(base_folder, exist_ok=True)

for topic in topic:
    topic_path = os.path.join(base_folder, topic)
    os.makedirs(topic_path, exist_ok=True)
    file_path = os.path.join(topic_path, "interview_questions.md")

    with open(file_path, "w") as file:
        file.write(f"# {topic} Interview Questions\n\n")

print(f"DevOps notes structure created in '{base_folder}' folder.")
