# Aetheria Database & SQL Analytics

This project models a **fantasy RPG world** inside a **MySQL database** and demonstrates how SQL can be used for **game management, economy tracking, and player analytics**.  
It also includes a **Python-powered chat system** that interacts with the database in real time.

---

## 📌 Project Overview

The goal of this project is to design and analyze a complex game database that supports:

- **Relational Data Modeling**: Characters, Quests, NPCs, Items, Inventory, Guilds, and more.  
- **Game Economy Simulation**: Trades, transactions, and inflation/deflation tracking.  
- **Player Behavior Analysis**: Quest completion rates, item usage, social interactions.  
- **Application Layer**: A prototype chat interface that stores and retrieves messages via SQL.

This repository shows not only SQL query design but also **practical integration of Python with databases**.

---

## Database Design
- **17+ interconnected tables** (Character, Quest, Inventory, Item, Guild, NPC, Chat, Message, Transaction, etc.).  
- Foreign keys, logs (`QuestLog`, `GuildMembershipLog`), and synthetic data generation scripts.  

### Analytics & SQL Queries
- Player behavior analysis (inventory usage, quest completions, login activity).  
- Market & economy monitoring (inflation, hotspots, most-traded items).  
- Social graph insights (guild changes, friendships, mutual quests).  

### Chat System Prototype
- **Python terminal app (`chat.py`)**: send and retrieve messages directly from the database.  
- **Notebook interface**: live queries to inspect chat history and message activity.  

---

## 🛠️ Technologies Used
- **MySQL** – database engine  
- **Python (mysql-connector, ipython-sql)** – application & notebook queries  
- **Jupyter Notebooks** – analysis and visualization  
- **Neo4j (experimental)** – graph-based queries for quests and player interactions  

---

## 📊 Example Analyses

- Top 5 traded items in the in-game economy  
- Quests with the highest dropout vs. completion rates  
- Players with rapid item acquisitions (>1000 gold in a day)  
- Inflation/deflation detection over months  
- Peak playtime hours across all players  
- Social graph: mutual friends who completed quests together  

---

## 🤝 Future Improvements
- Integrate with a game engine for a live RPG prototype.  


