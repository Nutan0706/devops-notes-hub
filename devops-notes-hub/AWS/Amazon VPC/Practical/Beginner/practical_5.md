# 🚀 Launch EC2 Instances in Public & Private Subnets

Test connectivity using SSH (public only).

---

# ✅ **Overview**

You will:

* Launch **1 Public EC2**
* Launch **1 Private EC2**
* SSH into Public EC2 using Key Pair
* Test connectivity between Public → Private

---

# 🧩 **Prerequisites**

* Custom VPC with:

  * Public Subnet (with IGW and Public Route Table)
  * Private Subnet (with NAT Gateway or no internet)
* Security Groups created (optional)

---

# 🖥️ **1️⃣ Create a Key Pair**

1. Go to **AWS Console → EC2 → Key Pairs**
2. Click **Create key pair**
3. Name: `my-keypair`
4. Key type: **RSA**
5. File format:

   * `.pem` (Linux/Mac)
   * `.ppk` (Windows Putty)
6. Download the key file

<img width="929" height="450" alt="image" src="https://github.com/user-attachments/assets/e72c75a6-d126-42f5-b905-6586573933ec" />


---

# 🖥️ **2️⃣ Launch EC2 in Public Subnet**

1. Go to **EC2 → Instances → Launch Instance**
2. Name: `public-ec2`
3. Choose AMI: **Amazon Linux 2** or **Ubuntu**
4. Instance type: `t2.micro`
5. Key pair: **Select `my-keypair`**
6. Network settings:

   * VPC: **Your Custom VPC**
   * Subnet: **Public Subnet (example: ap-south-1a)**
   * Auto-assign Public IP: **ENABLED**
7. Security Group:

   * Allow **SSH (22)** from your IP
8. Storage: default
9. Launch Instance

<img width="908" height="677" alt="image" src="https://github.com/user-attachments/assets/d7e721c7-3598-485a-95b3-c66f115ecc78" />


---

# 🖥️ **3️⃣ Launch EC2 in Private Subnet**

1. Go to **Launch Instance** again
2. Name: `private-ec2`
3. AMI: same as before
4. Instance type: `t2.micro`
5. Key pair: **same key (my-keypair)**
6. Network settings:

   * VPC: **Your Custom VPC**
   * Subnet: **Private Subnet (example: ap-south-1b)**
   * Auto-assign Public IP: **DISABLED**
7. Security Group:

   * Allow SSH **only from Public EC2 security group**
8. Launch Instance

<img width="881" height="623" alt="image" src="https://github.com/user-attachments/assets/d5d7f5bd-99b4-4e32-ba88-c999aaad0476" />


---

# 🔐 **4️⃣ SSH into Public EC2**

Use the command (Linux/Mac):

```bash
chmod 400 my-keypair.pem

ssh -i my-keypair.pem ec2-user@<PUBLIC_EC2_PUBLIC_IP>
```

For Ubuntu AMI:

```bash
ssh -i my-keypair.pem ubuntu@<PUBLIC_EC2_PUBLIC_IP>
```


---

# 🔗 **5️⃣ Test Connectivity From Public → Private EC2**

### **5.1 Get Private IP of private-ec2**

1. Go to EC2 → Instances
2. Copy the **Private IP** of `private-ec2`

👉 *Add Screenshot Here*

### **5.2 From the public EC2 terminal**

Run:

```bash
ping <PRIVATE_EC2_PRIVATE_IP>
```

and then try SSH:

```bash
ssh ec2-user@<PRIVATE_EC2_PRIVATE_IP>
```

Ubuntu EC2:

```bash
ssh ubuntu@<PRIVATE_EC2_PRIVATE_IP>
```
<img width="506" height="135" alt="image" src="https://github.com/user-attachments/assets/e6742826-1e5e-4f94-a539-f4d0b0502649" />


---

# 🧪 **6️⃣ Verify Results**

| Test                                      | Expected Result                 |
| ----------------------------------------- | ------------------------------- |
| SSH into public EC2                       | ✔️ Works (public IP + key pair) |
| SSH into private EC2 directly from laptop | ❌ Not allowed                   |
| SSH public → private within VPC           | ✔️ Should work                  |
| Ping private EC2                          | ✔️ Works if ICMP allowed        |

---

# 🎉 **EC2 Setup Complete!**

You have successfully:
✔️ Launched EC2 in Public & Private Subnets
✔️ Connected to Public EC2 via SSH
✔️ Verified VPC internal connectivity

