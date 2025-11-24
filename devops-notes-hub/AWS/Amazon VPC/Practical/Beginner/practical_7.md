# 🔒 **7. Use Network ACLs (NACLs)**

Configure a Network ACL to restrict traffic to/from specific IPs and test by modifying rules.

---

# 🧩 **What Are NACLs?**

Network ACLs are **stateless** firewalls that control **inbound & outbound traffic** for subnets.

* Applied at **Subnet level**
* Rules are evaluated in **order** (rule number → lowest first)
* Must create **both Inbound & Outbound** rules

---

# 🚀 **Step-by-Step Guide for GitHub**

---

## **1️⃣ Open the NACL Console**

1. Go to **AWS Console → VPC → Network ACLs**
2. You will see:

   * Default NACL
   * Custom NACLs (if any)

<img width="1455" height="237" alt="image" src="https://github.com/user-attachments/assets/7a8af402-dc37-4bbc-a359-8e05668b92d3" />


---

## **2️⃣ Create a Custom Network ACL**

1. Click **Create Network ACL**
2. Name: `public-subnet-nacl`
3. Select your **custom VPC**
4. Click **Create Network ACL**

<img width="1334" height="423" alt="image" src="https://github.com/user-attachments/assets/816546fb-0e4d-477c-a277-bfcb68e180c3" />


---

## **3️⃣ Associate the NACL with Public Subnet**

1. Select the newly created NACL
2. Go to **Subnet associations** tab
3. Click **Edit**
4. Select your **public-subnet-1**
5. Click **Save**

<img width="1338" height="334" alt="image" src="https://github.com/user-attachments/assets/946258f1-7c29-47a7-8c36-01c47fd2dda4" />


---

## **4️⃣ Add Inbound Rules (Allow SSH Only From Your IP)**

1. Select the NACL
2. Go to **Inbound Rules → Edit Inbound Rules**
3. Add these rules:

| Rule # | Type            | Protocol | Port       | Source         | Allow/Deny |
| ------ | --------------- | -------- | ---------- | -------------- | ---------- |
| 100    | SSH             | TCP      | 22         | `<YOUR_IP>/32` | ALLOW      |
| 110    | HTTP            | TCP      | 80         | 0.0.0.0/0      | ALLOW      |
| 120    | Ephemeral Ports | TCP      | 1024-65535 | 0.0.0.0/0      | ALLOW      |
| 200    | ALL Traffic     | ALL      | ALL        | 0.0.0.0/0      | DENY       |

4. Save rules

<img width="1311" height="193" alt="image" src="https://github.com/user-attachments/assets/b9b27283-acba-4287-bcb3-ac370268f94e" />


---

## **5️⃣ Add Outbound Rules**

1. Go to **Outbound Rules → Edit**
2. Add:

| Rule # | Type        | Protocol | Port Range | Destination | Allow/Deny |
| ------ | ----------- | -------- | ---------- | ----------- | ---------- |
| 100    | ALL Traffic | ALL      | ALL        | 0.0.0.0/0   | ALLOW      |
| 200    | ALL Traffic | ALL      | ALL        | 0.0.0.0/0   | DENY       |

<img width="1334" height="264" alt="image" src="https://github.com/user-attachments/assets/612fd4c9-9485-414a-b5e1-bba431fd3b8f" />


---

## **6️⃣ Test Connectivity (SSH Allowed From Your IP)**

From your laptop run:

```bash
ssh -i my-keypair.pem ec2-user@<PUBLIC_EC2_PUBLIC_IP>
```

Expected:
✔️ SSH should work **only from your IP**
❌ Other IPs → SSH fails

---

## **7️⃣ Modify Rule to Block SSH**

Now test restrictions:

1. Go to **Inbound rules**
2. Change the SSH rule from **ALLOW → DENY**
   OR delete the allow rule
3. Try SSH again

Expected:
❌ You should NOT be able to SSH into the public EC2


---

## **8️⃣ Re-Allow SSH**

1. Re-add the inbound rule allowing your IP
2. SSH should work again


---

# 🎉 Summary

You successfully:

* Created a custom NACL
* Associated it with a subnet
* Allowed specific IP traffic
* Denied all other traffic
* Tested by modifying rules

A perfect demonstration of **stateless filtering** in AWS.


