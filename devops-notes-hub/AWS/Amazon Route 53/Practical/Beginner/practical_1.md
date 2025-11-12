# 🌐 Practical 1: Register a Domain (Optional)

**Goal:**
Register a new domain using **Amazon Route 53** (or use an existing one) to manage DNS records for your web applications.

---

## 🧠 Objective

You will learn how to:

* Register a domain using AWS Route 53
* Understand the concept of Hosted Zones
* Identify key DNS records (A, CNAME, NS, SOA)

---

## 🪜 Step-by-Step Procedure

### **Step 1: Open Route 53 Console**

1. Go to the [AWS Management Console](https://console.aws.amazon.com/).
2. In the **search bar**, type **Route 53** and open it.
3. You’ll land on the **Route 53 Dashboard**.

🖼️ *Add Screenshot Here: Route 53 Dashboard*

---

### **Step 2: Start Domain Registration**

1. Click on **“Registered domains”** in the left navigation panel.
2. Choose **“Register Domain”**.
3. In the **Search domain** field, type your desired domain name (e.g., `myproject-demo.com`).
4. Click **Check** to see if it’s available.

🖼️ *Add Screenshot Here: Domain Search Page*

---

### **Step 3: Choose Domain and TLD**

* If the domain is available, select it.
* Choose your preferred **TLD** (e.g., `.com`, `.org`, `.dev`, `.in`).
* Click **Add to cart** → **Continue**.

🖼️ *Add Screenshot Here: Domain Selection*

---

### **Step 4: Provide Contact Details**

1. Enter the **Registrant contact information** (name, email, address).
2. You can use AWS’s **privacy protection** to hide your personal info from WHOIS.
3. Click **Continue**.

🖼️ *Add Screenshot Here: Contact Details Form*

---

### **Step 5: Review and Purchase**

1. Review your order summary.
2. Accept the **Terms and Conditions**.
3. Click **Complete Order**.
4. You’ll receive a confirmation email from **Amazon Registrar** to verify your email address.

🖼️ *Add Screenshot Here: Order Summary Page*

---

### **Step 6: Verify Domain Registration**

* Wait a few minutes for AWS to complete registration.
* Once verified, go to **“Registered domains”** → your domain will appear in the list.
* AWS automatically creates a **Hosted Zone** for this domain in Route 53.

🖼️ *Add Screenshot Here: Registered Domain List*

---

## 🧩 Key Notes

| Concept          | Description                                              |
| ---------------- | -------------------------------------------------------- |
| **Hosted Zone**  | A container that holds DNS records for your domain.      |
| **A Record**     | Maps a domain name to an IP address (IPv4).              |
| **CNAME Record** | Maps one domain name to another (useful for subdomains). |
| **NS Record**    | Lists the nameservers responsible for your domain.       |
| **SOA Record**   | Contains administrative information about your zone.     |

---

## ✅ Practical Validation

* [ ] Domain successfully registered (or existing domain used)
* [ ] Hosted Zone automatically created in Route 53
* [ ] Email verification completed
* [ ] Can view DNS records (A, CNAME, NS, SOA)

---

## 💡 Pro Tip

> If you already own a domain from **GoDaddy**, **Namecheap**, or another registrar,
> you can still use **Route 53** by **migrating the domain’s name servers** to AWS.
