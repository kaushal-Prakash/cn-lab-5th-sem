Here are **clean, concise, and well-structured notes** based on your transcript.

# **📘 Notes: Components of a Computer Network (Introduction)**

This lecture introduces the basic components required to perform experiments in a Computer Networks Lab.

---

## **1️⃣ Components of a Computer Network**

A computer network mainly consists of **three categories of components**:

### **A. Nodes**

### **B. Transmission Media**

### **C. Services**

---

# **A. NODES**

Nodes are the devices **present in the network**.
They are classified into two types:

---

## **1. End Nodes (End Devices)**

These devices **generate or receive** data.

### **Examples:**

* PCs / Desktops
* Laptops
* Printers
* Smartphones
* Tablets
* PDAs
* Cameras
* Any device **sending or accepting data**

### **Function:**

* Sender → sending data
* Receiver → accepting data

---

## **2. Intermediate Nodes (Intermediate Devices)**

These devices **forward data** from the sender to the receiver.

### **Examples:**

* Hub
* Repeater
* Bridge
* Switch
* Router
* Firewall
* Wireless Access Point (WAP)
* Gateway
* Cell phone towers
* NIC (Network Interface Card)

### **Function:**

* Ensure packets reach the correct destination
* Perform routing, switching, filtering, etc.

---

# **B. TRANSMISSION MEDIA**

Medium through which data travels between nodes.
It can be **wired** or **wireless**.

---

## **1. Wired Transmission Media**

Uses physical cables to transmit data (as electrical signals).

### **Types of Wired Cables**

* **Ethernet Cable**

  * Straight-through
  * Crossover
* **Coaxial Cable**
* **Fiber Optic Cable**

### **Characteristics**

* High reliability
* Less interference
* Faster data rate compared to wireless (generally)

---

## **2. Wireless Transmission Media**

Uses **air** as the medium.
Data is transmitted as **electromagnetic waves**.

### **Types of Wireless Media**

* **Infrared waves**
* **Radio waves**
* **Microwaves**
* **Satellite communication**

### **Usage Based on Distance**

* Short distance → Infrared
* Medium distance → Radio waves
* Long distance → Microwave / Satellite

---

# **C. NETWORK SERVICES**

Services offered within a network to support communication or data sharing.

### **Common Network Services**

* **Email Service**

  * Provided by Email servers (e.g., Gmail, Outlook)
* **World Wide Web (WWW)**

  * Provides websites, apps like Amazon, Flipkart, etc.
* **Instant Messaging Services**

  * WhatsApp, Messenger, etc.
* **Telnet Service**

  * Used for remote login
* **DNS Service**

  * Converts domain names → IP addresses
* **FTP Service**

  * File sharing and file transfer

*(More services can be added depending on the network environment.)*

---

# **📍 Example Diagram (Explained Conceptually)**

A sample network includes:

### **End Devices**

* PCs
* Laptops
* Printers
* Mobile Phones

### **Intermediate Devices**

* Routers
* Switches
* Cell phone towers (wireless connection)

### **How Communication Happens**

* When a PC in one network sends data to a PC in another network:

  * The **two PCs** → End nodes
  * The **routers and switches** forwarding data → Intermediate nodes

* If a user needs a service:

  * They communicate with the appropriate **server** (e.g., DNS server, Email server).

---

# **📌 Summary**

* **Nodes**: End devices (send/receive data) & Intermediate devices (forward data).
* **Media**: Wired (Ethernet, Fiber, Coaxial) & Wireless (IR, Radio, Microwave).
* **Services**: Email, WWW, DNS, FTP, Telnet, Instant Messaging, etc.

This understanding forms the base for all **Computer Network Lab experiments**.
---

# **📘 Networking Device: HUB — Notes**

## **1️⃣ Introduction**

A **Hub** is the **simplest networking device** used in LANs to connect multiple devices.
It works at the **Physical Layer (Layer 1)** of the OSI Model.

---

# **2️⃣ Why do we need a Hub?**

* When only **two PCs** are used, they can be connected **directly** using an Ethernet cable.
* When more than two systems (PC1, PC2, PC3…) need to be connected:

  * A single Ethernet port on a PC can connect to **only one device**.
  * So, direct connections become impossible.
  * Hence, we use a **Hub** to interconnect multiple devices.

---

# **3️⃣ Function of a Hub (How it Works)**

### ✔ Receives data from one port

### ✔ Broadcasts it to **all other ports**

* If PC2 sends data to PC6:

  * Hub does **not** send only to PC6.
  * It sends the data **to every device** connected.

This behaviour is called **broadcasting**.

---

# **4️⃣ Why Hubs are Inefficient?**

Because of broadcast behavior:

### ❌ Creates **unnecessary network traffic**

### ❌ Wastes **bandwidth**

### ❌ Not intelligent

### ❌ Cannot identify MAC addresses

* Hub knows **only port numbers**, not the devices connected.
* It has **no buffer or memory**, so it cannot store MAC addresses.

---

# **5️⃣ Ports in a Hub**

* Usually available in **8-port** or **16-port** versions
* 4-port hubs also exist

Each port can connect one device.

---

# **6️⃣ Detailed Example**

If an 8-port hub is connected to 8 PCs (PC1…PC8):

* Suppose **PC2 → PC6** data transfer is needed.
* Expected behaviour: **Unicast** (PC2 → PC6 only)
* Hub behaviour: **Broadcast** (PC2 → all PCs)

This confirms that the hub:

* Has no MAC–learning capability
* Treats every packet as if all devices should receive it

---

# **7️⃣ Types of Hubs**

## **A. Passive Hub**

* Simply receives data.
* Broadcasts to all ports.
* **Does not** amplify or regenerate signals.
* Works only as a basic connector.

## **B. Active Hub**

* Has all features of a passive hub **plus repeater functionality**.
* Amplifies/regenerates weak signals.
* Useful when data travels long distances or signals degrade.

---

# **8️⃣ Important Characteristics**

### **🔹 Layer:** Physical Layer (Layer 1)

### **🔹 Network type:** Used only in **LAN**

### **🔹 Behaviour:** Broadcasts to all ports

### **🔹 Intelligence:** No intelligence (does not read MAC addresses)

### **🔹 Memory:** No buffer or lookup table

### **🔹 Traffic:** Causes unnecessary traffic due to broadcasting

### **🔹 Speed:** Slow and outdated compared to switches

---

# **9️⃣ Quick Summary (Perfect for Exams)**

* Hub operates at **Layer 1 (Physical Layer)**.
* No MAC learning, no routing, no filtering.
* Simple device used to connect multiple systems in a LAN.
* Data received on one port is **broadcast** to all other ports.
* Leads to **traffic congestion** and **wasted bandwidth**.
* Available in 4, 8, 16-port configurations.
* **Passive Hub:** Only broadcasts
* **Active Hub:** Broadcasts + amplifies signals (acts as a repeater)

---

# **📘 Networking Device: REPEATER — Notes**

## **1️⃣ Introduction**

A **Repeater** is a networking device used to **regenerate weak signals** in a network.
It works at the **Physical Layer (Layer 1)** of the OSI Model.

---

# **2️⃣ Why Do We Need a Repeater?**

* Signals weaken as they travel over long distances in a network.
* This weakening is called **signal attenuation**.
* If a signal becomes too weak, it cannot be understood by the receiver.
* A Repeater is placed **between two parts of a network** to refresh the signal.

### **Example**

* Node A sends a signal to node B.
* As the signal travels, its strength reduces.
* A repeater placed in between **restores the original strength** of the signal before forwarding it.

---

# **3️⃣ How a Repeater Works (Functioning)**

* It receives a **weak / distorted signal**.
* Regenerates the signal to its **original strength**.
* Forwards the regenerated signal to the next device/network segment.

✔ Keeps the original shape and strength
✔ Removes noise/distortion
✔ Does not modify data
✔ Does not make the signal stronger than original — only restores

---

# **4️⃣ Repeater vs Amplifier (Important Difference)**

| Feature | Repeater                    | Amplifier                            |
| ------- | --------------------------- | ------------------------------------ |
| Purpose | Regenerates original signal | Increases magnitude                  |
| Output  | Same as original (X → X)    | Stronger than original (X → 2X, 4X…) |
| Noise   | Removes noise               | Amplifies noise also                 |
| Layer   | Works at Physical Layer     | Not a network device                 |

**Key Point:**

> Repeater is NOT an amplifier. Repeater restores signal; amplifier increases magnitude.

---

# **5️⃣ Important Characteristics of a Repeater**

* Works at **Physical Layer (Layer 1)**
* **Cannot read MAC addresses**

  * Hence, like a hub, it forwards the signal blindly
* Used to **extend network distance**
* Used only in **homogeneous networks** (same type of network segments)

---

# **6️⃣ Does a Repeater Forward Signals to All Devices?**

Yes.
Because the repeater:

* **Cannot recognize destination MAC addresses**
* Simply forwards any signal it receives to the next network segment
* So if the destination device is on the same side, the repeater still forwards the signal unnecessarily

This is why a repeater is **not an intelligent device**.

---

# **7️⃣ Placement of Repeaters**

Repeater placement depends on:

* Type of transmission medium
* Maximum supported cable length
* Distance between nodes

### Typical Distances:

* **Copper/Ethernet**: 100–200 meters
* **Fiber Optic Cable**: signal can travel **up to ~60 km** without requiring a repeater

If the distance is very long, **multiple repeaters** can be placed.

---

# **8️⃣ Uses of a Repeater**

* To extend LAN segments
* To maintain signal quality across long distances
* Used in wired networks (Ethernet, coaxial, fiber)
* Used in wireless networks (Wi-Fi repeaters boost range)

---

# **9️⃣ Quick Summary (Exam-Friendly)**

* Repeater works at **Layer 1 (Physical Layer)**.
* Used to **regenerate and retransmit** weak signals.
* Works on **bit-level**, no MAC address checking.
* Helps extend network distance.
* Not intelligent → cannot identify source/destination.
* **Repeater ≠ Amplifier.**
* Fibre cables require repeaters only after very long distances (up to 60 km).

---

# **📘 Networking Device: BRIDGE — Notes**

## **1️⃣ Introduction**

A **Bridge** is a networking device used to **divide a LAN into smaller segments** and reduce network traffic.
It works at the **Data Link Layer (Layer 2)** of the OSI model.

---

# **2️⃣ What Does a Bridge Do?**

A Bridge:

* Connects **one LAN to another LAN**
* Divides a large network into **smaller parts**
* Forwards data based on **MAC addresses**
* Reduces unnecessary network traffic
* Uses the **same protocol** on both connected LANs

**Layer:** Data Link Layer (Layer 2)

---

# **3️⃣ Why Do We Need a Bridge? (Problem with Hubs)**

Recall Hub behavior:

* Hub **broadcasts** every incoming frame to all connected devices
* This causes:

  * ❌ High bandwidth consumption
  * ❌ Unnecessary traffic
  * ❌ No MAC learning
  * ❌ No filtering

A solution is to **split** the large network (8 PCs) into two smaller networks (4 PCs each) using a **Bridge**.

---

# **4️⃣ How Bridge Works (Functioning)**

### **Bridge divides network into two segments**

Example:

* LAN 1 → Port 1 → PC1, PC2, PC3, PC4
* LAN 2 → Port 2 → PC5, PC6, PC7, PC8

### **Bridge maintains a MAC Address Table**

It stores:

* **MAC Address**
* **Port number** (Port 1 or Port 2)

Example Table:

| MAC Address | Port |
| ----------- | ---- |
| PC1         | 1    |
| PC2         | 1    |
| PC3         | 1    |
| PC4         | 1    |
| PC5         | 2    |
| PC6         | 2    |
| PC7         | 2    |
| PC8         | 2    |

---

# **5️⃣ Data Forwarding Rules (Very Important)**

### **Case 1: Source & Destination in the SAME LAN**

Example: PC1 → PC4

* Both are on **Port 1**
* Bridge **does not forward** the frame to port 2
* Sends only within Port 1
* Avoids unnecessary traffic

### **Case 2: Source & Destination in DIFFERENT LANs**

Example: PC1 → PC8

* PC1 → Port 1
* PC8 → Port 2
* Bridge **forwards** the frame from Port 1 to Port 2
* Hub on that side broadcasts (Hub always broadcasts)
* But fewer devices = lower bandwidth usage

---

# **6️⃣ Why Does Bridge Reduce Traffic?**

Because:

* It **filters** frames based on MAC addresses
* It forwards frames **only where needed**
* Each side has fewer devices → **less broadcast domain collision**

Compared to a big single hub network:

* Old case: 8 devices received every frame
* Bridge case: only 4 devices in each segment receive broadcast
  → Less bandwidth consumption

---

# **7️⃣ Important Characteristics of a Bridge**

* Works at **Data Link Layer (Layer 2)**
* Uses **MAC addresses** for forwarding
* Connects **two LANs** using the same protocol
* Performs **filtering + forwarding**
* Maintains **MAC address table**
* Reduces network congestion
* Still uses hubs on each side, so **local broadcasts** still happen
* Bridge has **two ports** (typically)

  * Port 1 → LAN 1
  * Port 2 → LAN 2

---

# **8️⃣ Comparison (Hub vs Bridge)**

| Feature      | Hub             | Bridge                 |
| ------------ | --------------- | ---------------------- |
| Layer        | Physical (L1)   | Data Link (L2)         |
| Forwarding   | Broadcast only  | Filtering + forwarding |
| Intelligence | Not intelligent | Learns MAC addresses   |
| Traffic      | High            | Reduced                |
| Table        | No table        | MAC table              |

---

# **9️⃣ Quick Summary (Perfect for Exams)**

* Bridge works at **Layer 2**.
* Connects two LANs using the **same protocol**.
* Uses **MAC address table** to decide forwarding.
* **Filters** frames within same LAN and **forwards** across LANs only when needed.
* Reduces bandwidth wastage compared to hubs.
* Splits one large LAN into smaller, more efficient segments.

---


