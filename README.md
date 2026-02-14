<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [Campus-Lost-And-Found] 🎯

## Basic Details

### Team Name: [SHEcodes]

### Team Members
- Member 1: [Diya Anzar] - [Lbs institute of technology for women]
- Member 2: [Shafna S Rawther] - [Lbs institute of technology for women]

### Hosted Project Link
[]
### Project Description
[Campus Lost & Found is a web-based platform designed to help students easily report, find, and recover lost items within the college campus. Students can post details of items they have lost or found, along with contact information, making it easier to reconnect items with their rightful owners. The platform organizes items into Lost, Found, and Recovered categories, ensuring clarity and reducing confusion in the recovery process.]

### The Problem statement
[In a college campus, students frequently misplace personal belongings such as ID cards, books, bottles, and electronic accessories. Currently, there is no centralized and reliable system to report or track these lost items. Information is usually shared through word of mouth or informal social media messages, which often leads to confusion, delayed recovery, or items remaining unclaimed. This lack of an organized system makes the process of finding lost items inefficient and stressful for students.]

### The Solution
[The Campus Lost & Found system provides a centralized web-based platform where students can easily report lost and found items within the college campus. Users can add item details such as name, description, and contact information, allowing others to quickly identify and respond to relevant posts. The system categorizes items into Lost, Found, and Recovered sections, ensuring clear tracking of each item’s status. This structured approach reduces confusion, improves communication between students, and makes the recovery process faster and more efficient.]

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: [Python, HTML, CSS]
- Frameworks used: [Flask, Bootstrap]
- Libraries used: [SQLite3]
- Tools used: [VS Code, Git, GitHub]

**For Hardware:**
-- Not applicable (This is a software-based web application)

---

## Features

List the key features of your project:
- Feature 1: [Student login system using college register number and password format]
- Feature 2: [- Option to report lost items with item name, description, and contact details]]
- Feature 3: [Ability to post found items separately when the owner is unknown]
- Feature 4: [Automatic categorization of items into Lost, Found, and Recovered sections]
- Feature 5: [Status update functionality to move items from Lost → Found → Recovered]
- Feature 6: [Clean dashboard displaying all items with clear status labels]
- Feature 7: [Secure logout functionality for student accounts]


---

## Implementation

### For Software:

#### Installation
```bash
[pip install flask]
```

#### Run
```bash
[python app.py]
```

### For Hardware:

#### Components Required
[not applicable]
#### Circuit Setup
[This project is a software-based web application and does not involve any electronic circuits or hardware connections.]

---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

<img width="1900" height="1036" alt="login" src="https://github.com/user-attachments/assets/4624b6fb-713d-40b4-a839-9f0778f8909a" />
*The Student Login page allows registered students to securely access the Campus Lost & Found system using their register number and password. After successful login, users are redirected to the dashboard to view and manage lost, found, and recovered items.*

<img width="1914" height="1077" alt="dashboard" src="https://github.com/user-attachments/assets/131eb881-9b01-46ff-bac5-813a4651bdc4" />

*The dashboard displays the Campus Lost & Found system where users can add new items and view all reported lost items in a structured table. It allows users to mark items as found, view contact details, and manage item status efficiently after login.*


<img width="1895" height="1058" alt="recovereditems" src="https://github.com/user-attachments/assets/9092d656-c004-40f0-a99b-8be3a7776bfe" />
*Displays all items that have been successfully returned to their owners, along with item details and contact information, confirming completion of the recovery process.*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
* The system follows a simple client–server architecture.  
Users interact with the frontend built using HTML, CSS, and Bootstrap.  
Requests are handled by a Flask backend, which processes login, item posting, and status updates.  
All data is stored and retrieved from an SQLite database.*

**Application Workflow:**

![Workflow](docs/workflow.png)
*1. Student logs in using their register number and password  
2. Dashboard loads with lost items list  
3. User can add lost or found items  
4. Items can be marked as found or recovered  
5. Database updates reflect in real time on the dashboard*

---

### For Hardware:

#### Schematic & Circuit

not applicable

#### Build Photos

not applicable
---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

not applicable

#### Installation Guide

**For Android (APK):**
not applicable

**For iOS (IPA) - TestFlight:**
not applicable

**Building from Source:**
```bash
# For Android
not applicable
# or
./gradlew assembleDebug

# For iOS
not applicable
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

not applicable

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
1. Ensure Python is installed on your system.
2. Install required dependencies:
   ```bash
   pip install flask
## Run Instructions
python app.py

## Application Demo

### Login Page
Users can log in using their college register number and password to access the system securely.

### Dashboard
After login, users can:
- Add lost items with description and contact details
- View all reported lost items
- Mark items as recovered
- View recovered items separately
**Output:**
  
After successful login, users are redirected to the dashboard where they can:
- Add lost or found items with description and contact details
- View items categorized as Lost, Found, and Recovered
- Mark items as recovered once returned to the owner
- Log out securely from the system

##


 Project Demo

### Video
https://github.com/user-attachments/assets/6f601df4-1af9-465c-b77b-6338300246cc
*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [ Diya Anzar]: [Backend development using Flask, database design with SQLite, login authentication logic, item status management (lost/found/recovered), and overall project integration.]
- [Shafna S Rawther]: [Frontend design using HTML, CSS, and Bootstrap, UI/UX layout for login and dashboard pages, form validation support, and documentation assistance.]


---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
