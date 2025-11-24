# 🌐 **9. DNS & DHCP Options in VPC**

This section helps you understand:

* How DNS resolution works inside a VPC
* How to **enable/disable DNS** for instances
* How to customize **DHCP Options Sets** (domain name, DNS servers)

---

# 🚀 **Step-by-Step Guide**

---

# 🧩 **Part 1: Enable DNS Resolution in Your VPC**

## **1️⃣ Open VPC Settings**

1. Go to **AWS Console → VPC Dashboard**
2. Select **Your Custom VPC**

---

## **2️⃣ Check DNS Settings**

Inside the VPC settings:

1. Go to the **“DNS Resolution”** setting

   * Ensure: **DNS resolution = Yes**
2. Go to the **“DNS Hostnames”** setting

   * Enable: **DNS hostnames = Yes**
     (Only works if VPC has a public subnet + IGW)

👉 *Add Screenshot Here*

---

# 🧪 **Test DNS Resolution**

Login to your **public EC2**:

```bash
ping google.com
```

Expected: ✔ DNS resolution should work.

Now test internal DNS:

```bash
ping ip-10-0-2-45.ec2.internal
```

(if ping is allowed)

👉 *Add Screenshot Here*

---

# 🧩 **Part 2: Create & Customize DHCP Options Set**

## **3️⃣ Open DHCP Options Section**

1. Go to **VPC Console**
2. From left menu, click **DHCP Options Sets**

👉 *Add Screenshot Here*

---

## **4️⃣ Create a New DHCP Options Set**

Click **Create DHCP options set**
Fill details:

| Field                   | Example Value                       |
| ----------------------- | ----------------------------------- |
| **Name**                | `custom-dhcp-options`               |
| **Domain name**         | `example.local` *(optional)*        |
| **Domain name servers** | `AmazonProvidedDNS` *(default)*     |
| (Optional)              | Custom DNS server IP (like 8.8.8.8) |

Click **Create DHCP Options Set**

👉 *Add Screenshot Here*

---

## **5️⃣ Associate DHCP Options Set with the VPC**

1. Select your DHCP options set
2. Click **Associations → Edit**
3. Select **Your VPC**
4. Save

👉 *Add Screenshot Here*

---

# 🧪 **Part 3: Test the Effect of DHCP Options**

## **6️⃣ Reboot EC2 Instances**

For new DHCP settings to take effect:

* Select your EC2
* **Instance → Reboot**

👉 *Add Screenshot Here*

---

## **7️⃣ Verify DNS Server Used by EC2**

On Linux EC2:

```bash
cat /etc/resolv.conf
```

You should see either:

* Amazon DNS → `169.254.169.253`
* Custom DNS (like 8.8.8.8) if you configured it

👉 *Add Screenshot Here*

---

# 📘 **Understanding DNS & DHCP in VPC**

### ✔ **DNS Resolution**

* Converts domain names → IPs
* Used for both internal VPC DNS and internet DNS
* Must enable:

  * DNS Resolution
  * DNS Hostnames

---

### ✔ **DHCP Options Set**

DHCP Options controls:

* Domain Name
* DNS Servers
* NTP (time servers)
* NetBIOS servers (legacy Windows)

Default = **AmazonProvidedDNS**

Custom DHCP is useful when:

* Using custom domain (e.g., example.company.internal)
* Using internal DNS servers
* Hybrid Cloud setups (VPN + On-Prem)

---

# 🎉 **DNS & DHCP Setup Complete**

You have successfully:
✔ Enabled DNS resolution in VPC
✔ Created a custom DHCP options set
✔ Associated it with your VPC
✔ Tested DNS behavior inside EC2 instances

