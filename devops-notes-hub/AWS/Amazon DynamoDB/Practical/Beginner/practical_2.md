# 🧩 Practical 2 — Add, Update, and Delete Items in DynamoDB

### 🎯 Objective:

Perform **basic CRUD operations (Create, Read, Update, Delete)** manually using the **AWS Management Console**.

---

## 🪜 Step-by-Step Guide

---

### **Step 1: Open Your DynamoDB Table**

* Go to the **AWS Management Console** → search for **“DynamoDB”**.
* Click **Tables** on the left menu.
* Select the table you created earlier (e.g., `EmployeeTable`).

🖼️ *→ Add Screenshot 1 here (showing selected table page)*

---

### **Step 2: Navigate to the “Explore Table Items” Tab**

* Inside your table view, click the **“Explore table items”** tab (or “Explore items” in some UI versions).
* This is where you can add, view, and edit data directly.

🖼️ *→ Add Screenshot 2 here (Explore items tab page)*

---

### **Step 3: Add a New Item (Create Operation)**

1. Click on **“Create item”**.
2. In the form:

   * Enter **Partition key**: `EmployeeID` → for example: `"E101"`
   * Enter **Sort key**: `Department` → for example: `"HR"`
3. Add additional attributes:

   * Click **Add new attribute** → choose **String**
   * Add attributes like:

     * `Name`: `"John Doe"`
     * `Role`: `"HR Executive"`
     * `Salary`: `45000`
4. Click **“Create item”** to save.

🖼️ *→ Add Screenshot 3 here (filled item creation form)*

---

### **Step 4: Verify the Item (Read Operation)**

* After saving, you should see your newly added item listed in the **Items table**.
* You can expand the row to view its attributes and values.

🖼️ *→ Add Screenshot 4 here (item successfully added and visible)*

---

### **Step 5: Update an Existing Item (Update Operation)**

1. Select the item you want to edit.
2. Click the **“Edit”** button on the top.
3. Modify one or more fields — for example:

   * Change `Salary` from `45000` → `50000`
   * Change `Role` from `"HR Executive"` → `"Senior HR Executive"`
4. Click **“Save changes”**.

🖼️ *→ Add Screenshot 5 here (item edit form)*

---

### **Step 6: Confirm the Update**

* After saving, the table refreshes automatically.
* Verify that your updated fields are reflected correctly.

🖼️ *→ Add Screenshot 6 here (updated item details)*

---

### **Step 7: Delete an Item (Delete Operation)**

1. Select the item you want to delete.
2. Click on the **“Delete”** button at the top.
3. Confirm deletion when prompted.

🖼️ *→ Add Screenshot 7 here (delete confirmation popup)*

---

### **Step 8: Verify Deletion**

* The item should no longer appear in the **Items list**.
* This confirms the item was successfully deleted.

🖼️ *→ Add Screenshot 8 here (table showing no deleted item)*

---

✅ **Result:**
You have successfully performed all **CRUD operations** using the DynamoDB console:

| Operation  | Action        | Description               |
| ---------- | ------------- | ------------------------- |
| **Create** | Add new item  | Inserted employee data    |
| **Read**   | View item     | Verified item details     |
| **Update** | Modify fields | Updated salary and role   |
| **Delete** | Remove item   | Deleted record from table |

