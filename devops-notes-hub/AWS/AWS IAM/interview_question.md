# AWS IAM Interview Questions

## 🟢 Beginner Level (1–10)

1. **What is AWS IAM and why is it important?**  
   🔹 *Hint:* Think **"who can access what"** in AWS.

2. **What are IAM Users in AWS?**  
   🔹 *Hint:* Long-term identities for individuals or applications.

3. **What are IAM Groups used for?**  
   🔹 *Hint:* Used to apply the same permissions to multiple users.

4. **What is an IAM Role?**  
   🔹 *Hint:* Temporary credentials for AWS services or cross-account access.

5. **What are IAM Policies?**  
   🔹 *Hint:* JSON documents defining permissions for AWS actions.

6. **What are the two types of IAM policies?**  
   🔹 *Hint:* Managed and Inline.

7. **What is the Root User in AWS?**  
   🔹 *Hint:* The account owner with full privileges — avoid daily use.

8. **What is the difference between IAM User and IAM Role?**  
   🔹 *Hint:* User = permanent, Role = temporary.

9. **How does IAM provide security for AWS resources?**  
   🔹 *Hint:* By controlling access through authentication and authorization.

10. **What are IAM Access Keys used for?**  
    🔹 *Hint:* For CLI and SDK programmatic access.

## 🟡 Moderate Level IAM Questions (11–20)

11. **What is a Managed Policy vs Inline Policy?**  
    - **Hint:** Managed is reusable, Inline is attached directly to an identity.

12. **What are Identity-based and Resource-based policies?**  
    - **Hint:** Identity = user/group/role; Resource = directly on AWS resource.

13. **How can you enforce MFA (Multi-Factor Authentication) for IAM Users?**  
    - **Hint:** Use IAM policy condition `aws:MultiFactorAuthPresent`.

14. **How can you check which user made a change in IAM?**  
    - **Hint:** Use AWS CloudTrail logs.

15. **What is IAM Policy Simulator used for?**  
    - **Hint:** To test and debug policy permissions.

16. **How do you attach a policy to a user using AWS CLI?**  
    - **Hint:** Use `aws iam attach-user-policy`.

17. **What are the key elements of an IAM Policy?**  
    - **Hint:** Effect, Action, Resource, Condition.

18. **How to restrict access to a specific IP using IAM Policy?**  
    - **Hint:** Use Condition with `aws:SourceIp`.

19. **What is the maximum number of groups a user can belong to?**  
    - **Hint:** The limit is **10**.

20. **How to give an EC2 instance permission to access S3 securely?**  
    - **Hint:** Attach IAM Role to the EC2 instance.
   
## 🔵 Advanced Level IAM Questions (21–30)

21. **What is AWS STS and how does it work with IAM Roles?**  
    - **Hint:** STS issues temporary credentials for roles and federated users.

22. **What is AssumeRole and when do you use it?**  
    - **Hint:** Used for cross-account or temporary access via STS.

23. **How does policy evaluation logic work in IAM?**  
    - **Hint:** Explicit Deny > Allow > Default Deny.

24. **How to manage secrets or sensitive data in IAM policies?**  
    - **Hint:** Avoid hardcoding; use Secrets Manager or Parameter Store.

25. **What are IAM Permission Boundaries?**  
    - **Hint:** Define the maximum permissions an identity can have.

26. **What are IAM Access Analyzer findings?**  
    - **Hint:** Detect unintended resource sharing.

27. **What are Service Control Policies (SCPs) in AWS Organizations?**  
    - **Hint:** Set limits on IAM permissions across accounts.

28. **What is a Policy Version in IAM?**  
    - **Hint:** Up to 5 versions per policy; only one can be active.

29. **How to automate IAM policy deployment?**  
    - **Hint:** Use Terraform, CloudFormation, or AWS CLI scripts.

30. **How to audit unused IAM users or access keys?**  
    - **Hint:** Use IAM Credential Report or Access Analyzer.

## 🔴 Expert & Scenario-Based IAM Questions (31–40)

31. **You need to give a developer temporary access to EC2 only. What will you do?**  
    - **Hint:** Create an IAM Role and use STS temporary credentials.

32. **You have multiple AWS accounts — how will you manage centralized IAM?**  
    - **Hint:** Use AWS Organizations with SCPs and cross-account roles.

33. **An IAM user accidentally deleted a policy. How do you recover?**  
    - **Hint:** Recreate using CloudTrail logs or policy version history.

34. **How do you provide S3 bucket access to an external vendor securely?**  
    - **Hint:** Use a resource-based S3 bucket policy with external account role.

35. **You have hundreds of users — how will you enforce password rotation?**  
    - **Hint:** Configure an IAM Password Policy.

36. **How to allow Lambda to write logs to CloudWatch?**  
    - **Hint:** Attach the `AWSLambdaBasicExecutionRole` policy.

37. **You want to allow EC2 to run SSM commands — what will you configure?**  
    - **Hint:** Attach the `AmazonSSMManagedInstanceCore` role to EC2.

38. **A user can list but not delete S3 objects — why?**  
    - **Hint:** Policy allows `s3:ListBucket` but missing `s3:DeleteObject`.

39. **How to share IAM roles between AWS accounts?**  
    - **Hint:** Configure `AssumeRole` with a trust policy referencing another account.

40. **What will happen if you delete a policy that’s attached to a user?**  
    - **Hint:** The permissions granted by that policy are immediately revoked.
## 🟣 Commonly Asked IAM Questions (41–50)

41. **What is the difference between AWS IAM and AWS Cognito?**  
    - **Hint:** IAM = internal AWS users; Cognito = external app users.

42. **What’s the purpose of the `.aws/credentials` file?**  
    - **Hint:** Stores CLI access keys and profiles.

43. **How do IAM policies differ from S3 bucket policies?**  
    - **Hint:** IAM = identity-based, S3 = resource-based.

44. **How to give read-only access to all AWS services?**  
    - **Hint:** Attach the `ReadOnlyAccess` managed policy.

45. **What is the default policy behavior if no “Allow” is defined?**  
    - **Hint:** Deny by default.

46. **How to detect unused IAM roles?**  
    - **Hint:** Check `lastUsed` metric from IAM APIs.

47. **How to revoke compromised IAM credentials immediately?**  
    - **Hint:** Delete access keys or deactivate credentials.

48. **How can you list all IAM users from CLI?**  
    - **Hint:** Use `aws iam list-users`.

49. **How to enable MFA Delete for S3 using IAM?**  
    - **Hint:** Enable MFA Delete in S3 bucket versioning settings.

50. **What is the max number of IAM roles per AWS account?**  
    - **Hint:** Default 1,000 (can be increased via AWS support).
    
