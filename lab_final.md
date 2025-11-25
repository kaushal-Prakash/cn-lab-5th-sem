
# **1. Detailed Report on Devices in Different Layers of Computer Network Architecture**

## **🔷 Introduction**

Computer networks are structured based on layered architectures.
The **OSI (Open Systems Interconnection) model** divides network functions into **7 layers**, where each layer has specific roles and devices that operate within that layer.

This layered approach ensures:

* Standardization
* Interoperability
* Troubleshooting
* Scalability

Below is a detailed layer-by-layer explanation of all devices in the OSI architecture.

---

# **🟦 OSI Model Layers & Devices**

---

# **1️⃣ Physical Layer Devices (Layer 1)**

### **📌 Role of Physical Layer**

* Transmits raw bits (0s and 1s)
* Deals with cables, connectors, signals
* Defines electrical, optical, mechanical characteristics

### **📡 Devices at Physical Layer**

#### **1. Cables**

* **Twisted Pair (UTP/STP)** – Used in Ethernet
* **Coaxial Cable** – Cable TV, older Ethernet
* **Optical Fiber** – High-speed data transmission

#### **2. Connectors**

* **RJ-45** – Ethernet
* **RJ-11** – Telephone lines

#### **3. Repeaters**

* Regenerate and strengthen weak signals

#### **4. Hubs (Multiport Repeaters)**

* Broadcasts to all ports
* No intelligence, no filtering

#### **5. NIC (Network Interface Card)**

* Converts data → signals
* Provides physical connectivity

---

# **2️⃣ Data Link Layer Devices (Layer 2)**

### **📌 Role**

* MAC addressing
* Error detection
* Framing
* Access control (CSMA/CD, CSMA/CA)

### **📡 Devices**

#### **1. Switches**

* Forwards frames using MAC table
* Each port = one collision domain

#### **2. Bridges**

* Connect LAN segments
* Filter based on MAC

#### **3. Access Points (Layer 2 APs)**

* Connect wireless devices

#### **4. Modems (work across Layer 1 & 2)**

* Convert digital ↔ analog

---

# **3️⃣ Network Layer Devices (Layer 3)**

### **📌 Role**

* Logical addressing (IP)
* Routing
* Best path selection

### **📡 Devices**

#### **1. Routers**

* Main layer 3 device
* Forwards packets using IP

#### **2. Layer 3 Switch**

* High-speed routing inside LAN

#### **3. Gateways**

* Connect dissimilar networks

#### **4. Firewalls (Partially Layer 3+)**

* Filter based on IP rules

---

# **4️⃣ Transport Layer Devices (Layer 4)**

### **📌 Role**

* End-to-end communication
* Segmentation
* Flow & error control
* Protocols: **TCP, UDP**

### **📡 Devices**

#### **1. Load Balancers**

* Distribute traffic
* Use TCP/UDP port numbers

#### **2. Layer 4 Firewalls**

* Block based on port numbers

#### **3. NAT Devices**

* Translate private ↔ public IP

---

# **5️⃣ Session Layer Devices (Layer 5)**

### **📌 Role**

* Establish, manage, terminate sessions

### **📡 Devices/Software**

* **Session Border Controllers (SBC)**
* **Remote Desktop Gateways**
* **NetBIOS / RPC Session Managers**

---

# **6️⃣ Presentation Layer Devices (Layer 6)**

### **📌 Role**

* Encryption
* Compression
* Data translation

### **📡 Devices/Software**

* **Hardware Security Modules (HSMs)**
* **SSL Accelerators**
* **Codecs (H.264, etc.)**

---

# **7️⃣ Application Layer Devices (Layer 7)**

### **📌 Role**

* Provides network services to applications

### **📡 Devices**

* **Application Layer Gateways (ALGs)**
* **Proxy Servers**
* **Web Servers**
* **Mail Servers**
* **DNS Servers**
* **FTP/SFTP Servers**

---

# **🧾 Summary Table (Layer-wise Devices)**

| **Layer**           | **Devices**                               |
| ------------------- | ----------------------------------------- |
| **1. Physical**     | Cables, Hubs, Repeaters, NIC, Connectors  |
| **2. Data Link**    | Switches, Bridges, APs, Modems            |
| **3. Network**      | Routers, L3 Switches, Gateways, Firewalls |
| **4. Transport**    | Load Balancers, NAT, L4 Firewalls         |
| **5. Session**      | SBCs, Session Managers                    |
| **6. Presentation** | HSMs, SSL Accelerators, Codecs            |
| **7. Application**  | Proxy, DNS, Web & Mail Servers            |

---

# **2. C Program: Separate Network & Host ID + Determine Class**

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

    if (a >= 1 && a <= 126) {
        printf("Class: A\n");
        printf("Network ID: %d.0.0.0\n", a);
        printf("Host  ID : 0.%d.%d.%d\n", b, c, d);
    }
    else if (a >= 128 && a <= 191) {
        printf("Class: B\n");
        printf("Network ID: %d.%d.0.0\n", a, b);
        printf("Host  ID : 0.0.%d.%d\n", c, d);
    }
    else if (a >= 192 && a <= 223) {
        printf("Class: C\n");
        printf("Network ID: %d.%d.%d.0\n", a, b, c);
        printf("Host  ID : 0.0.0.%d\n", d);
    }
    else if (a >= 224 && a <= 239) {
        printf("Class: D (Multicast)\n");
    }
    else if (a >= 240 && a <= 255) {
        printf("Class: E (Experimental)\n");
    }
    else {
        printf("Invalid IP Address\n");
    }

    return 0;
}
```

---

# **3. C Program for CRC Generation & Error Detection**

```c
#include <stdio.h>
#include <string.h>

void xor(char *a, char *b) {
    for (int i = 1; i < strlen(b); i++)
        a[i] = (a[i] == b[i]) ? '0' : '1';
}

void crc(char data[], char div[], char remainder[]) {
    int div_len = strlen(div);
    int data_len = strlen(data);

    char temp[200];
    strncpy(temp, data, div_len);
    temp[div_len] = '\0';

    for (int i = div_len; i <= data_len; i++) {
        if (temp[0] == '1')
            xor(temp, div);
        else
            xor(temp, "000000000");

        if (i < data_len) {
            memmove(temp, temp+1, div_len);
            temp[div_len-1] = data[i];
            temp[div_len] = '\0';
        }
    }
    strcpy(remainder, temp);
}

int main() {
    char data[200], div[] = "100000111", rem[200], recv[200];

    printf("Enter 40 bytes of data (320 bits):\n");
    scanf("%s", data);

    char appended[400];
    sprintf(appended, "%s%08d", data, 0);

    crc(appended, div, rem);
    printf("\nCRC: %s\n", rem);

    sprintf(recv, "%s%s", data, rem);
    printf("Transmitted Codeword: %s\n", recv);

    char check[200];
    crc(recv, div, check);

    if (strspn(check, "0") == strlen(check))
        printf("\nReceiver: No Error Detected.\n");
    else
        printf("\nReceiver: ERROR Detected!\n");

    return 0;
}
```

---

# **4. TCP Client–Server Program (Uppercase Conversion)**

### **📌 server.c**

```python
import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP and port
server_socket.bind(("0.0.0.0", 8080))

# Listen for connections
server_socket.listen(1)
print("Server is listening on port 8080...")

# Accept client
conn, addr = server_socket.accept()
print("Connected with:", addr)

# Receive data
data = conn.recv(1024).decode()
print("Received:", data)

# Convert to UPPERCASE
data = data.upper()

# Send back
conn.send(data.encode())

conn.close()
server_socket.close()
```

### **📌 client.c**

```python
import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server (localhost)
client_socket.connect(("127.0.0.1", 8080))

# Send message
msg = input("Enter message: ")
client_socket.send(msg.encode())

# Receive uppercase response
data = client_socket.recv(1024).decode()
print("From Server:", data)

client_socket.close()

```

---

# **5. Wireshark: Capture & Filter Packets**

## **a) Capture Ethernet / Wi-Fi Packets**

1. Open Wireshark
2. Select correct interface (**Ethernet / Wi-Fi**)
3. Click **Start Capture**
4. Generate traffic (open google.com)
5. Click **Stop**

---

## **b) Filter Packets**

### **TCP**

```
tcp
```

### **UDP**

```
udp
```

### **HTTP**

```
http
```

### **DNS**

```
dns
```

### **ARP**

```
arp
```

### **ICMP**

```
icmp
```

---

## **c) Capture Telnet Packets**

### **All Telnet packets**

```
tcp.port == 23
```

### **Telnet to a specific host**

```
tcp.port == 23 && ip.addr == <host_ip>
```

### **Telnet packets going TO host**

```
tcp.port == 23 && ip.dst == <host_ip>
```

### **Telnet packets FROM host**

```
tcp.port == 23 && ip.src == <host_ip>
```

---

