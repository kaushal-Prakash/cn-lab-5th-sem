Great — I’ll upgrade everything with:

### ✔ **Inline comments for every important line**

### ✔ **More explanatory notes for each question**

### ✔ **Still keeping code short, simple, and clean**

To avoid hitting message limits, **I will send answers in multiple parts**.

---

# ✅ **PART 1 — Q1 & Q2 (Updated Notes + C Code with Inline Comments)**

I will send Q3–Q11 after this.
Let me know if you want them all in one file afterwards.

---

# 🌐 **1. Report: Devices in Each Layer of Network Architecture**

### ✔ More Detailed Notes

### **OSI Model (7 Layers) — Devices & Functions**

---

## **Layer 1 → Physical Layer**

### Devices:

* **Hubs**
* **Repeaters**
* **Cables** (Coaxial, Fiber, Ethernet)
* **Network Interface Cards (NIC)** (partly works here)

### Notes:

* Transmits **BITS (0s and 1s)**
* No understanding of frames or packets
* Amplifies / forwards raw signals
* No addressing takes place

---

## **Layer 2 → Data Link Layer**

### Devices:

* **Switches**
* **Bridges**
* **NIC (upper half)**

### Notes:

* Works with **MAC addresses**
* Performs:

  * **Framing**
  * **Error detection (CRC)**
  * **Flow control**
* Switches build **MAC tables** for forwarding

---

## **Layer 3 → Network Layer**

### Devices:

* **Routers**
* **Layer-3 Switches**

### Notes:

* Works with **IP addresses**
* Responsible for:

  * Routing
  * Subnetting
  * Packet forwarding
  * Path selection (DV, LS algorithms)

---

## **Layer 4 → Transport Layer**

### Devices:

* **Firewalls**
* **Load Balancers**

### Notes:

* Provides **reliable (TCP)** or **unreliable (UDP)** delivery
* Implements:

  * Segmentation
  * Acknowledgments
  * Port numbers

---

## **Layer 5 → Session Layer**

### Devices:

* **Gateways**

### Notes:

* Manages sessions between hosts
* Controls:

  * Dialog maintenance
  * Checkpointing

---

## **Layer 6 → Presentation Layer**

### Devices:

* **Gateways** (for encryption, compression)

### Notes:

* Encrypts/Decrypts
* Compresses data
* Converts between formats (JPEG, MP3, ASCII, Unicode)

---

## **Layer 7 → Application Layer**

### Devices:

* **Proxies**
* **Application Gateways (e.g., mail gateway)**
* **Web servers / DNS servers**

### Notes:

* Provides high-level services:

  * HTTP
  * FTP
  * SMTP
  * DNS
* Closest to the user

---

# 🟩 Done with Q1.

Moving to Q2.

---

# 🖥 **2. C Program — Determine IPv4 Class + Network ID + Host ID**

### ✔ More Notes

* IPv4 divided into **Class A, B, C, D, E**
* Class determined by **first octet** (value before first dot):

  * 0–127 → Class A
  * 128–191 → Class B
  * 192–223 → Class C
  * 224–239 → Class D (Multicast)
  * 240–255 → Class E (Experimental)

### Why split Network / Host?

* Network ID identifies the network
* Host ID identifies the device inside the network
* Helps routers forward packets

---

# ✔ **C Code with Detailed Inline Comments**

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char ip[20];

    printf("Enter IPv4 address: ");
    scanf("%s", ip);                  // Read IP as string (e.g., 192.168.1.5)

    int a, b, c, d;

    // Parse the four octets from the IP address string
    // %d.%d.%d.%d reads four integers separated by dots
    sscanf(ip, "%d.%d.%d.%d", &a, &b, &c, &d);

    printf("Class: ");

    // CLASS A CHECK
    if (a >= 0 && a <= 127) {
        printf("A\n");

        // Network ID → first octet only (A = N.H.H.H)
        printf("Network ID: %d.0.0.0\n", a);

        // Host ID → remaining three octets
        printf("Host ID: 0.%d.%d.%d\n", b, c, d);
    }

    // CLASS B CHECK
    else if (a <= 191) {
        printf("B\n");

        // Network ID = first two octets
        printf("Network ID: %d.%d.0.0\n", a, b);

        // Host ID = last two octets
        printf("Host ID: 0.0.%d.%d\n", c, d);
    }

    // CLASS C CHECK
    else if (a <= 223) {
        printf("C\n");

        // Network ID = first 3 octets
        printf("Network ID: %d.%d.%d.0\n", a, b, c);

        // Host ID = last octet only
        printf("Host ID: 0.0.0.%d\n", d);
    }

    // CLASS D (Multicast)
    else if (a <= 239) {
        printf("D (Multicast)\nNo Network/Host concept.\n");
    }

    // CLASS E (Reserved)
    else {
        printf("E (Reserved)\nNo Network/Host concept.\n");
    }

    return 0;
}
```

---

### ✔ **Time Complexity (TC)**

```
O(1) → constant time operations (simple parsing)
```

### ✔ **Space Complexity (SC)**

```
O(1) → only fixed variables used
```

---

### If you want, I can also provide:

✔ Flowchart
✔ Output screenshots (ASCII example)
✔ Combined single PDF

---

# ✅ **3. CRC Code Generation & Error Detection**

### **Notes**

* CRC = Cyclic Redundancy Check
* Used for **error detection** in frames
* Generator polynomial (example here): **1101**
* Append zeros equal to degree of generator
* Compute remainder using XOR
* At receiver:

  * Recompute remainder
  * If remainder = 0 → No error
  * Else → Error

---

## ✔ **C Program with Inline Comments**

```c
#include <stdio.h>
#include <string.h>

// XOR operation on two strings (skipping the first bit)
void xor(char *a, char *b) {
    for (int i = 1; i < strlen(b); i++)
        a[i] = (a[i] == b[i]) ? '0' : '1';  // XOR logic
}

// Function to calculate CRC remainder
void crc(char data[], char gen[], char rem[]) {
    int l_gen = strlen(gen);
    char temp[50];

    strcpy(temp, data);  // temp contains data + zeros

    // Division process
    for (int i = 0; i <= strlen(data) - l_gen; i++) {
        if (temp[i] == '1')        // divide only when bit is 1
            xor(temp + i, gen);    // XOR generator with temp
    }

    // Copy remainder from the end
    strcpy(rem, temp + strlen(data) - (l_gen - 1));
}

int main() {
    char data[50] = "10101010";   // Your 40-byte data simplified
    char gen[10] = "1101";        // Generator polynomial
    char appended[60], rem[10];

    // Append zeros equal to generator degree (3 zeros for 1101)
    strcpy(appended, data);
    strcat(appended, "000");

    // Compute remainder
    crc(appended, gen, rem);
    printf("CRC Remainder: %s\n", rem);

    // Prepare transmitted frame = data + remainder
    char tx[60];
    strcpy(tx, data);
    strcat(tx, rem);

    printf("Transmitted Frame: %s\n", tx);

    // Receiver recomputes CRC to check for errors
    char rem2[10];
    crc(tx, gen, rem2);

    printf("Receiver Remainder: %s\n", rem2);

    // If remainder is all zeros → No error
    if (strcmp(rem2, "000") == 0)
        printf("No Error Detected\n");
    else
        printf("Error Detected!\n");

    return 0;
}
```

### ✔ TC & SC

* **TC = O(n × m)** (n = data length, m = generator length)
* **SC = O(n)**

---

# ✅ **4. Distance Vector Routing Using Bellman–Ford Algorithm**

### **Notes**

* Distance Vector routing uses:

  * Each router knows **distance to neighbors**
  * Periodically exchanges routing tables
* Bellman-Ford principle:

  ```
  dist[v] = min(dist[v], dist[u] + cost[u][v])
  ```

---

## ✔ **C Code with Inline Comments**

```c
#include <stdio.h>
#define INF 999  // Infinity constant

int main() {
    int n;

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    int cost[10][10];

    printf("Enter cost matrix (use 999 for no link):\n");

    // Read cost adjacency matrix
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &cost[i][j]);

    int dist[10];

    // Initialize distance vector from node 0
    for (int i = 0; i < n; i++)
        dist[i] = cost[0][i];

    // Bellman-Ford relaxation for (n−1) iterations
    for (int k = 0; k < n - 1; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[j] > dist[i] + cost[i][j]) // Relax edge
                    dist[j] = dist[i] + cost[i][j];

    printf("Distance vector from node 0:\n");

    // Print result
    for (int i = 0; i < n; i++)
        printf("%d ", dist[i]);

    return 0;
}
```

### ✔ TC & SC

* **TC = O(n³)**
* **SC = O(n²)**

---

# ✅ **5. TCP Client–Server (Uppercase Conversion)**

### **Notes**

* TCP uses:

  * Connection-oriented communication
  * Reliable byte stream
* Server:

  1. Create socket
  2. Bind port
  3. Listen
  4. Accept client
  5. Read → Convert to uppercase → Send

---

## 🔹 **TCP Server (C Code)**

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
    int s = socket(AF_INET, SOCK_STREAM, 0);  // Create TCP socket

    // Server address
    struct sockaddr_in serv = {AF_INET, htons(8000), INADDR_ANY};

    bind(s, (struct sockaddr *)&serv, sizeof(serv));  // Bind to port 8000
    listen(s, 1);                                     // Listen for connections

    int c = accept(s, NULL, NULL);    // Accept client connection

    char buf[100];
    read(c, buf, sizeof(buf));        // Read client's message

    // Convert to uppercase
    for (int i = 0; buf[i]; i++)
        buf[i] = toupper(buf[i]);

    write(c, buf, strlen(buf));       // Send back

    close(c);
    close(s);
}
```

---

## 🔹 **TCP Client (C Code)**

```c
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int s = socket(AF_INET, SOCK_STREAM, 0);     // Create socket

    struct sockaddr_in serv = {AF_INET, htons(8000)};
    serv.sin_addr.s_addr = inet_addr("127.0.0.1"); // Connect to localhost

    connect(s, (struct sockaddr *)&serv, sizeof(serv));

    char msg[100];
    printf("Enter message: ");
    scanf("%s", msg);

    write(s, msg, strlen(msg));    // Send message to server
    read(s, msg, sizeof(msg));     // Read server response

    printf("Server Reply: %s\n", msg);

    close(s);
}
```

---

# 📡 **6. Wireshark Capture — Notes Only**

### **(a) Capture Ethernet / Wi-Fi Packets**

* Open Wireshark
* Select interface: `Ethernet0` or `Wi-Fi`
* Click **Start**
* Observe:

  * Frames
  * Source MAC
  * Destination MAC
  * Protocol

### **(b) Filters**

```
tcp
udp
dns
http
```

### **(c) Telnet traffic for a specific host**

```
telnet && ip.addr == 192.168.1.10
```

---

# ✅ **7. Sliding Window Protocol**

### **Notes**

* Flow control protocol
* Sender sends a group of frames (window)
* Receiver acknowledges
* Sender shifts window forward

---

## ✔ **C Code with Inline Comments**

```c
#include <stdio.h>

int main() {
    int frames, window;

    printf("Enter number of frames: ");
    scanf("%d", &frames);

    printf("Enter window size: ");
    scanf("%d", &window);

    int i = 1;  // Starting frame

    while (i <= frames) {
        printf("\nSending frames: ");

        // Send frames within window
        for (int j = i; j < i + window && j <= frames; j++)
            printf("%d ", j);

        printf("\nAcknowledged frames: ");

        // Assume all frames acknowledged for simplicity
        for (int j = i; j < i + window && j <= frames; j++)
            printf("%d ", j);

        i += window;  // Slide window
    }

    return 0;
}
```

### ✔ TC = O(n), SC = O(1)

---

# 🖧 **8. Simulator Tasks (Notes Only)**

No C program needed.

---

# 📦 **10. Analyze Packet Headers (Notes)**

Use Wireshark "Packet Details View".

* **Ethernet Header**

  * Destination MAC
  * Source MAC
  * EtherType

* **IP Header**

  * Version
  * Header length
  * TTL
  * Source IP
  * Destination IP

* **TCP Header**

  * Source port
  * Destination port
  * Sequence number
  * ACK number

---

# ✉ **11. Spam Detection (Simple C Program)**

### Notes

* Very basic keyword-based
* Detects common spam words

---

## ✔ **C Code with Inline Comments**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char email[500];

    printf("Enter email text:\n");
    fgets(email, 500, stdin);   // Read full email text

    // Simple keyword check
    if (strstr(email, "win") || strstr(email, "free") ||
        strstr(email, "click") || strstr(email, "prize"))
    {
        printf("Spam Email Detected\n");
    }
    else {
        printf("Not Spam\n");
    }

    return 0;
}
```

### ✔ TC = O(n), SC = O(1)

---

# 🎉 Done!

Just tell me!
