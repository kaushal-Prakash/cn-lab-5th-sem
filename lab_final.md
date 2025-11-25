


# **1. Detailed Report on Devices in Different Layers of Computer Network Architecture**

## **🔷 Introduction**

Computer networks are structured based on layered architectures.
The **OSI (Open Systems Interconnection) model** divides the network functions into **7 layers**, where each layer has specific roles and devices that operate within that layer.

This layered structure helps in:

* Standardization
* Interoperability
* Troubleshooting
* Scalability

Below is a layer-by-layer explanation of all devices associated with the OSI architecture.

---

# **🟦 OSI Model Layers & Devices**

---

# **1️⃣ Physical Layer Devices (Layer 1)**

### **📌 Role of Physical Layer**

* Transmits raw bits (0s and 1s)
* Defines physical media, voltage levels, cables, connectors
* Deals with the physical aspects of network communication

### **📡 Devices Operating at Physical Layer**

## **1. Cables**

### **a. Twisted Pair Cable (UTP/STP)**

* Most commonly used in LAN
* Used in Ethernet cabling
* UTP (Unshielded) used in homes and offices
* STP (Shielded) avoids electromagnetic interference

### **b. Coaxial Cable**

* Used in cable TV networks, early Ethernet (10BASE2, 10BASE5)
* Provides better shielding

### **c. Optical Fiber**

* Uses light signals
* Very high speed (Gbps to Tbps)
* Used in backbone networks, ISPs, long-distance communication

---

## **2. Connectors**

### **a. RJ-45**

* Used with twisted pair cables for Ethernet

### **b. RJ-11**

* Used in telephone lines, DSL connections

---

## **3. Repeaters**

* Regenerate and re-amplify weak signals
* Extend the distance of communication
* Used in LAN, WAN, early Wi-Fi extenders

---

## **4. Hubs (Multiport Repeaters)**

* Operate purely at layer 1
* Broadcast received signal to **all** ports
* No filtering, no intelligence
* Causes network collisions → rarely used today

---

## **5. Network Interface Card (NIC) – Hardware Layer**

* Provides physical access to the network
* Converts data into electrical/light signals
* Wireless NICs use antennas
* Ethernet NICs use RJ-45 ports

---

# **2️⃣ Data Link Layer Devices (Layer 2)**

### **📌 Role of Data Link Layer**

* Error detection/correction
* MAC addressing
* Controls access to media (CSMA/CD, CSMA/CA)

### **📡 Devices Operating at Layer 2**

## **1. Switches**

* Most important Layer 2 device
* Uses **MAC address table** to forward frames
* Reduces collision domains (each port = one collision domain)
* Faster, efficient, widely used in LANs

---

## **2. Bridges**

* Used to divide large LANs into smaller segments
* Operates on MAC addresses
* Controls traffic between segments
* Switch = multiport bridge

---

## **3. Layer 2 Wireless Access Point (AP)**

* Connects wireless devices to wired network
* Uses Wi-Fi standards (802.11a/b/g/n/ac/ax)
* Provides MAC-level filtering and authentication

---

## **4. Modems (Partially Layer 2)**

* Convert digital ↔ analog signals
* Used in DSL, cable internet
* Technically work across Physical + Data Link

---

# **3️⃣ Network Layer Devices (Layer 3)**

### **📌 Role of Network Layer**

* Logical addressing (IP addresses)
* Routing of packets
* Best path selection
* Packet fragmentation

### **📡 Devices Operating at Network Layer**

## **1. Routers**

* Main Layer 3 device
* Uses IP addresses to forward packets
* Connects different networks (LAN ↔ WAN)
* Maintains routing tables (RIP, OSPF, BGP)

---

## **2. Layer 3 Switch**

* High-speed switch performing routing
* Used in enterprise networks
* Supports VLAN routing (Inter-VLAN routing)

---

## **3. Gateways (Layer 3 and above)**

* Connect networks with **different architectures/protocols**
* Example: VoIP gateway, IoT gateways
* More intelligent than routers

---

## **4. Firewalls (Partly Layer 3)**

* Filter traffic using IP rules
* Block/allow packets
* Used for network security
* Many modern firewalls work on layers 3–7

---

# **4️⃣ Transport Layer Devices (Layer 4)**

### **📌 Role of Transport Layer**

* End-to-end communication
* Segmentation
* Flow control
* Error control
* Protocols: **TCP, UDP**

### **📡 Devices Operating at Transport Layer**

Transport layer mostly involves software-level devices, but some hardware exists.

## **1. Load Balancers**

* Distribute network traffic across multiple servers
* Use TCP/UDP port numbers
* Used in data centers, cloud scaling

---

## **2. Advanced Firewalls (Layer 4)**

* Can block traffic based on **TCP/UDP ports**
* Example: Block port 80 (HTTP) or 443 (HTTPS)

---

## **3. NAT Devices**

* Translate private ↔ public IPs
* Work at Layer 3 + Layer 4 (port translation)
* Found in home routers

---

# **5️⃣ Session Layer Devices (Layer 5)**

### **📌 Role of Session Layer**

* Manages connections between devices
* Establish, maintain, terminate sessions
* Example: Login sessions, remote desktop sessions

### **📡 Devices/Software at Layer 5**

Session layer is mostly software-based:

## **1. Session Border Controllers (SBC)**

* Used in VoIP and SIP networks
* Manage media + signaling sessions
* Provide security, NAT traversal, session control

---

## **2. Remote Desktop Gateways**

* Manage user sessions in remote access
* Example: RDP Gateway

---

## **3. NetBIOS / RPC Session Managers**

* Allow session establishment between computers in LAN

---

# **6️⃣ Presentation Layer Devices (Layer 6)**

### **📌 Role of Presentation Layer**

* Data translation
* Encryption/decryption
* Compression
* Ensures data is readable on both sides

### **📡 Devices/Software at Layer 6**

Almost fully software-level:

## **1. Encryption Devices**

* SSL accelerators
* Hardware Security Modules (HSMs)
* Perform fast data encryption/decryption

---

## **2. Data Compression Devices**

* WAN optimization appliances
* Reduce bandwidth usage by compressing data

---

## **3. Codecs (Encoder/Decoder Devices)**

* Used for audio and video streaming
* Convert analog ↔ digital formats
* Example: H.264 codec hardware

---

# **7️⃣ Application Layer Devices (Layer 7)**

### **📌 Role of Application Layer**

* Interface between users and the network
* Supports network applications such as email, browsing, file transfer

### **📡 Devices Operating at Layer 7**

## **1. Application Layer Gateways (ALGs)**

* Understand application protocols (HTTP, FTP, DNS)
* Provide deep packet inspection (DPI)
* Used in enterprise firewalls

---

## **2. Proxy Servers**

* Operate at application layer
* Provide caching, filtering, logging
* Examples:

  * HTTP Proxy
  * Forward/Reverse Proxy
  * Content filtering proxy

---

## **3. Web Servers**

* Host websites and applications
* Use HTTP/HTTPS
* Examples: Apache, NGINX, IIS

---

## **4. Mail Servers**

* Handle email communication
* Protocols: SMTP, POP3, IMAP

---

## **5. DNS Servers**

* Resolve domain names to IP addresses
* Critical for routing and browsing

---

## **6. FTP/SFTP Servers**

* File transfer
* Backup storage
* Remote file management

---

# **🧾 Summary Table (Layer-wise Devices)**

| **Layer**           | **Devices**                                   |
| ------------------- | --------------------------------------------- |
| **1. Physical**     | Cables, Hubs, Repeaters, NIC, Connectors      |
| **2. Data Link**    | Switches, Bridges, APs, Modems                |
| **3. Network**      | Routers, L3 Switch, Gateways, Firewalls       |
| **4. Transport**    | Load Balancers, NAT Devices, L4 Firewalls     |
| **5. Session**      | SBCs, Session Managers                        |
| **6. Presentation** | HSMs, SSL accelerators, Codecs                |
| **7. Application**  | Proxy Servers, DNS, Mail Servers, Web Servers |

---

# **2. C Program: Separate Network & Host ID + Find Class**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    char ip[20];
    int a, b, c, d;

    printf("Enter IPv4 address (example: 192.168.1.5): ");
    scanf("%s", ip);

    // Split the IP into 4 integers
    sscanf(ip, "%d.%d.%d.%d", &a, &b, &c, &d);

    printf("\nGiven IP: %s\n", ip);

    // Determine the class using the first octet
    if (a >= 1 && a <= 126) {
        printf("Class: A\n");
        printf("Network ID: %d.0.0.0\n", a);
        printf("Host ID: 0.%d.%d.%d\n", b, c, d);
    }
    else if (a >= 128 && a <= 191) {
        printf("Class: B\n");
        printf("Network ID: %d.%d.0.0\n", a, b);
        printf("Host ID: 0.0.%d.%d\n", c, d);
    }
    else if (a >= 192 && a <= 223) {
        printf("Class: C\n");
        printf("Network ID: %d.%d.%d.0\n", a, b, c);
        printf("Host ID: 0.0.0.%d\n", d);
    }
    else if (a >= 224 && a <= 239) {
        printf("Class: D (Multicast)\n");
        printf("No Network/Host ID for Class D\n");
    }
    else if (a >= 240 && a <= 255) {
        printf("Class: E (Experimental)\n");
        printf("No Network/Host ID for Class E\n");
    }
    else {
        printf("Invalid IP Address\n");
    }

    return 0;
}
```

---

# ✅ **Sample Output**

```
Enter IPv4 address (example: 192.168.1.5): 192.168.1.5

Given IP: 192.168.1.5
Class: C
Network ID: 192.168.1.0
Host ID: 0.0.0.5
```

---

# **3. Simple C Program for CRC Generation & Error Detection**

```c
#include <stdio.h>
#include <string.h>

// Function to perform XOR except the first bit
void xor(char *a, char *b) {
    for (int i = 1; i < strlen(b); i++)
        a[i] = (a[i] == b[i]) ? '0' : '1';
}

// CRC Division
void crc(char data[], char div[], char remainder[]) {
    int div_len = strlen(div);
    int data_len = strlen(data);

    char temp[200];
    strncpy(temp, data, div_len);         // Take first divisor length bits
    temp[div_len] = '\0';

    for (int i = div_len; i <= data_len; i++) {
        if (temp[0] == '1')               // If leading bit is 1 → XOR
            xor(temp, div);
        else                              // Else XOR with zeros
            xor(temp, "000000000");

        if (i < data_len) {               // Bring down next bit
            memmove(temp, temp+1, div_len);
            temp[div_len-1] = data[i];
            temp[div_len] = '\0';
        }
    }
    strcpy(remainder, temp);              // CRC remainder
}

int main() {
    char data[200], div[] = "100000111", rem[200], recv[200];

    printf("Enter 40 bytes of data in binary (320 bits):\n");
    scanf("%s", data);

    // Append zeros for division
    char appended[400];
    sprintf(appended, "%s%08d", data, 0);   // Append 8 zeros for CRC-8

    crc(appended, div, rem);               // Generate CRC
    printf("\nCRC: %s\n", rem);

    // Transmitted codeword = data + CRC
    sprintf(recv, "%s%s", data, rem);
    printf("Transmitted Codeword: %s\n", recv);

    // Receiver side — check for error
    char check[200];
    crc(recv, div, check);

    if (strspn(check, "0") == strlen(check))
        printf("\nReceiver: No Error Detected.\n");
    else
        printf("\nReceiver: ERROR Detected in Data!\n");

    return 0;
}
```

---

# ✅ **How This Works (Very Simple)**

1. User inputs **40 bytes (converted to binary = 320 bits)**
2. Append 8 zeros
3. Perform CRC division using the polynomial **100000111**
4. Generate remainder (CRC)
5. Send: `data + crc`
6. Receiver divides again

   * All zeros → no error
   * Non-zero → error detected

---

## 🧩 **What Exactly is CRC?**

### **CRC (Cyclic Redundancy Check)** is:

👉 **An error-detection technique** used in digital networks and storage systems.
👉 It detects accidental changes (noise, bit flips) in the transmitted data.
👉 It uses **binary division** and polynomial arithmetic to generate a short code called **CRC remainder**.

CRC is **not encryption**, **not compression** —
It is simply a powerful **error detection mechanism**.

---

# 🔍 **Why do we need CRC?**

During data transmission:

* Noise
* Interference
* Dropped signals
* Cable faults

can **flip 1 or more bits**.

CRC helps the receiver check:
✔ Did the data arrive correctly?
✔ Did any bit get corrupted?

If corrupted → **receiver detects error**.

---

# 🧠 **How CRC Works (Concept)**

CRC treats:

* The **data** as a large binary number
* The **generator polynomial** as another binary number

Then it performs:

```
DATA BITS  ÷  GENERATOR POLYNOMIAL  →  REMAINDER (CRC)
```

This remainder is attached to data and sent to the receiver.

---

# 📌 **Sender Side**

1. Take the data bits
2. Append `n` zeros (where n = degree of generator polynomial)
3. Perform binary division
4. Get remainder = **CRC**
5. Transmit: `Data + CRC`

---

# 📌 **Receiver Side**

1. Perform the **same division** on received bits
2. If remainder = 0 → ✔ Data correct
3. Else → ❌ Error in transmission

---

# 📐 **Important: CRC Uses Polynomial Math**

Example generator polynomial:

```
x⁸ + x² + x + 1
```

This becomes binary:

```
100000111
```

Each bit = coefficient of polynomial.

CRC performs **polynomial long division** where coefficients are modulo-2.

---

# ⚙ **CRC Operations Are Simpler Than Normal Math**

**In CRC:**

| Operation      | Meaning                  |
| -------------- | ------------------------ |
| Addition       | XOR                      |
| Subtraction    | XOR                      |
| Multiplication | Left shift               |
| Division       | Polynomial long division |

CRC uses **XOR** because there is **no carry**.

Example:

```
1 XOR 1 = 0  
1 XOR 0 = 1  
0 XOR 0 = 0
```

---

# 📘 **Why XOR Starts from Index 1?**

Because the **leading bit decides the division** (choose divisor or zeros).
It is not XORed; it's only used to choose the divisor.

---

# 🧪 **What Types of Errors Can CRC Detect?**

CRC is very powerful:

✔ Single-bit errors
✔ Double-bit errors
✔ Odd number of bit errors
✔ Burst errors (up to length of generator polynomial)

That’s why CRC is used in:

* Ethernet
* Wi-Fi
* USB
* Modems
* Storage disks
* MPEG, PNG, ZIP

---

# 🎯 **CRC vs Other Methods**

| Method   | Strength                          |
| -------- | --------------------------------- |
| Parity   | Detects single-bit errors only    |
| Checksum | Weaker, may miss patterns         |
| **CRC**  | Very strong, detects burst errors |

CRC is the **industry standard** for reliable data transmission.

---

# 💡 Example (Very Simple)

Data:

```
1101
```

Generator (divisor):

```
1011
```

After division, remainder (CRC) might be:

```
011
```

Transmitted → `1101 011`

Receiver divides and checks if remainder = 0.

---





