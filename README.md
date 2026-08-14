# Placement Skill-Gap Hub

> **From Placement Statistics to Skill-Gap Intelligence.**

A data-driven placement analytics and decision-support solution built for **HACKORBIT 2K26 – Track A: DataDrishti** by **Team Codeavengers, BANNARI AMMAN INSTITUTE OF TECHNOLOGY**.

---

## 🏆 Hackathon

| Field | Details |
|---|---|
| Hackathon | HACKORBIT 2K26 |
| Team | **Codeavengers** |
| Institute | **BANNARI AMMAN INSTITUTE OF TECHNOLOGY** |
| Track | **Track A — DataDrishti** |
| Project | **Placement Skill-Gap Hub** |
| Official Problem | **Placement Skill-Gap Hub — Model placement stats across branches.** |

---

## 🎯 Problem

Traditional placement reports mainly answer:

> **“What happened?”**

They show metrics such as:

- Placement rate
- Students placed
- Average package
- Highest package
- Recruiting companies
- Branch-wise placement performance

But these reports often do not make it easy to answer:

- Which skills are most demanded by industry?
- Are students sufficiently prepared in those skills?
- Which branches have the largest readiness gaps?
- Which skills should training teams prioritize?
- How can placement analytics support better training decisions?

### Our insight

> **Placement statistics tell us what happened. Skill-gap intelligence reveals where readiness gaps exist and what should be improved.**

---

## 💡 Solution

**Placement Skill-Gap Hub** connects three analytical dimensions:

```text
Placement Outcomes
        +
Industry Skill Demand
        +
Student Skill Readiness
        ↓
     Skill Gap
        ↓
 Training Priority
        ↓
 Actionable Recommendation
```

The solution uses analytics and interactive visualization to transform placement data into a decision-support workflow for:

- Students
- Placement Cells
- Faculty / Training Teams
- Institution Management

---

## 🔎 Core Analytical Model

The central metric is:

```text
Skill Gap = Industry Demand − Student Readiness
```

Example using the demonstration dataset:

```text
SQL Industry Demand      = 86.0%
SQL Student Readiness    = 49.8%

Skill Gap                = 36.2 percentage points
Priority                 = CRITICAL
```

### Important

A positive gap indicates a readiness shortfall relative to the demonstration demand level.

The project uses **percentage-point difference**, not percentage growth.

---

# 📊 Analytics Story

The project follows a simple decision journey:

### 01 — Measure
**What is happening?**

Placement performance by branch, batch and company.

### 02 — Compare
**What does industry need, and are students ready?**

Industry demand vs. student readiness.

### 03 — Diagnose
**Where are the largest gaps?**

Skill-gap analysis and branch-level comparisons.

### 04 — Prioritize
**What should be addressed first?**

Rule-based priority classification.

### 05 — Act
**What should we do next?**

Training recommendations based on the identified gap.

---

# 🧠 Analytics Types Used

| Analytics Type | How it appears in the project |
|---|---|
| **Descriptive** | Placement rates, packages, companies, branch comparisons |
| **Diagnostic** | Demand vs. readiness and skill-gap analysis |
| **Prescriptive** | Rule-based training priority recommendations |
| **Predictive** | Future scope |
| **AI** | Future scope |

The current MVP is primarily **descriptive + diagnostic + prescriptive analytics**.

---

# 🖥️ Dashboard

The showcase dashboard is organized into three major sections.

## 1. Placement Command Center

Answers:

> **“What is happening?”**

### KPIs

- Total Students
- Students Placed
- Placement Rate
- Average Package
- Highest Package
- Company Count

### Visuals

- Placement Rate by Branch
- Students Placed by Company
- Package Distribution
- Branch and Batch slicers

---

## 2. Skill Demand vs. Readiness

Answers:

> **“What does industry need, and are we ready?”**

### Visuals

- Industry Demand % by Skill
- Industry Demand vs. Student Readiness
- Skill Gap Table
- Skill-gap formula
- Highest-priority skill insight

### Current demonstration skills

- Python
- SQL
- Power BI
- Machine Learning
- Java
- Communication

---

## 3. Action Center

Answers:

> **“What should we do next?”**

### Skill Gap Priority Matrix

Axes:

- **X:** Student Readiness %
- **Y:** Industry Demand %

Interpretation:

```text
High Demand + Low Readiness
            ↓
Critical Training Priority
```

### Rule-Based Training Recommendation Engine

Priority thresholds:

```text
Gap ≥ 25 points     → CRITICAL
Gap ≥ 15 points     → HIGH
Gap ≥ 5 points      → MEDIUM
Gap < 5 points      → LOW
```

These thresholds are part of the current demonstration workflow and can be tuned when validated against real institutional requirements.

---

# 🧩 Key Showcase Features

The latest showcase UI includes:

### Animated Intro
A polished entry screen communicates the project story as:

```text
Placement → Demand → Readiness → Gap → Action
```

### Interactive Slicer Buttons
Users can interactively filter by:

- Branch
- Batch
- Skill

The active selection is visually highlighted.

### Dynamic Filter Feedback
The UI shows the current filter context, for example:

```text
CSE · 2026
```

### Sticky Filter Bar
Filters remain available while navigating the dashboard.

### Scroll Progress
A subtle top progress indicator shows navigation position.

### Section Reveal Animations
Dashboard sections progressively animate into view.

### Hover Micro-interactions
Cards, KPIs and controls use subtle elevation and motion for better feedback.

### Toast Feedback
Filter changes and demo actions provide immediate UI feedback.

### Quick Demo Path
A dedicated evaluator action can load a predefined demonstration path and move directly into the skill-gap story.

### Accessibility
The showcase includes:
- Keyboard-accessible controls
- Visible focus states
- `aria-pressed` state for slicers
- Reduced-motion support

---

# 📍 Branch Skill-Gap Heatmap

The showcase includes a branch-level view that helps answer:

> **“Which skills show the largest readiness gap for each branch?”**

Rows represent branches.

Columns represent skills.

Cells show the skill-gap value in percentage points.

Color intensity communicates severity:

- Low
- Medium
- High

This makes the project more actionable than a dashboard that only compares overall placement percentages.

---

# 🧭 Evaluator Demo Flow

A recommended 2-minute live demo:

```text
1. Placement Command Center
        ↓
2. Select a branch / batch
        ↓
3. Show placement KPIs
        ↓
4. Open Skill Demand vs. Readiness
        ↓
5. Focus on SQL
        ↓
6. Show 86.0% demand
        ↓
7. Show 49.8% readiness
        ↓
8. Show 36.2 percentage-point gap
        ↓
9. Open Action Center
        ↓
10. Show SQL = CRITICAL
        ↓
11. Show training recommendation
```

### The key message

> **“We don't just show placement numbers. We show what skills need to improve.”**

---

# 🏗️ Solution Architecture

```text
                    DATA SOURCES
                         │
              ┌──────────┴──────────┐
              │                     │
        Placement Data        Skill Data
              │                     │
              └──────────┬──────────┘
                         ↓
                  DATA PREPARATION
                    Power Query
                         ↓
                    DATA MODEL
              Students / Placements
              Companies / Skills
                         ↓
                 ANALYTICAL LAYER
                  DAX Measures
                         ↓
              ┌──────────┴──────────┐
              │                     │
       Placement Analytics    Skill-Gap Analytics
              │                     │
              └──────────┬──────────┘
                         ↓
                   POWER BI
                 Interactive BI
                         ↓
              Decision-Support Story
                         ↓
        Training Priorities / Insights
```

The HTML showcase is a lightweight companion to the Power BI analytical workflow.

---

# 🛠️ Technology Stack

## Analytics

- **Microsoft Power BI**
- **Power Query**
- **DAX**
- Semantic / Data Modeling

## Data

- Excel / CSV-style structured data
- Demonstration placement data
- Demonstration student skill data
- Demonstration industry skill-demand data

## Showcase UI

- HTML5
- CSS3
- Vanilla JavaScript
- Inline SVG visual components

## Design Approach

- Responsive layout
- Modern card-based UI
- Interactive slicers
- Accessible controls
- Motion with reduced-motion support
- No external JavaScript dependency for the showcase

---

# 🗃️ Data Model

A simplified analytical model contains three logical data areas:

### Students

```text
Student ID
Branch
Batch
Placement Status
Company
Package
```

### Skills

```text
Student ID
Skill
Skill Score / Readiness
```

### Industry Demand

```text
Skill
Demand Level
```

These are combined to derive:

```text
Industry Demand
Student Readiness
Skill Gap
Priority
Recommendation
```

---

# 🧹 Data Preparation

The data workflow follows the standard analytics lifecycle:

```text
Identify
   ↓
Prepare
   ↓
Clean
   ↓
Transform
   ↓
Model
   ↓
Visualize
   ↓
Analyze
   ↓
Decide
```

### Preparation tasks

- Data profiling
- Cleaning inconsistent values
- Handling missing values
- Standardizing categories
- Correcting data types
- Connecting related tables
- Ensuring model consistency
- Protecting unnecessary personal information

---

# 📐 Power BI Workflow

The current analytics implementation is designed around:

```text
Excel / CSV
    ↓
Power Query
    ↓
Clean Data
    ↓
Semantic Model
    ↓
DAX Measures
    ↓
Power BI Visuals
    ↓
Interactive Dashboard
```

### Typical measures include

- Total Students
- Students Placed
- Placement Rate
- Average Package
- Highest Package
- Company Count
- Industry Demand
- Student Readiness
- Skill Gap
- Priority

---

# ⚠️ Data Transparency

## Sample / Demonstration Dataset

**No real Bannari Amman Institute of Technology student, placement, or recruiter data is used in the current showcase.**

The figures are synthetic demonstration values created to validate:

- Dashboard interaction
- Analytical calculations
- Skill-gap logic
- Priority classification
- Recommendation workflow

When real institutional data becomes available, the same analytical workflow can be applied after appropriate validation, governance, privacy review and access controls.

---

# 🚫 What the Current MVP Does Not Claim

The current MVP does **not** claim:

- AI-powered recommendations
- Machine-learning prediction
- Guaranteed placement improvement
- Real-time recruiter ingestion
- Causal proof that a skill gap causes placement outcomes
- Authentic institutional placement statistics

### Current recommendation engine

The Training Recommendation Engine is explicitly:

> **Rule-Based**

It uses gap thresholds to classify priorities.

This keeps the MVP technically transparent and explainable.

---

# 🚀 Future Scope

The architecture can be extended with:

### 1. Resume Skill Extraction
Automatically extract skills from student resumes.

### 2. Job Description Skill Extraction
Automatically identify required skills from recruiter job descriptions.

### 3. Automated Industry Demand
Refresh skill demand using updated recruiter/job-market information.

### 4. ML-Based Placement Prediction
Estimate placement readiness or probability using validated historical data.

### 5. Personalized Learning Recommendations
Suggest skill-specific learning plans based on student readiness.

### 6. Training Impact Simulation
Allow placement teams to explore “what-if” scenarios for improving readiness.

### 7. Institutional Integration
Connect the workflow to placement, assessment and academic systems.

---

# 🎨 Design Principles

The project follows a **judge-first UX philosophy**:

### Clarity over complexity
Every visual should answer a question.

### Insight over decoration
Charts exist to support decisions, not simply to look attractive.

### Actionability
The dashboard should move from observation to action.

### Transparency
Synthetic data and rule-based logic are explicitly disclosed.

### Consistency
Metrics, colors, labels and interaction patterns remain consistent across the experience.

### Accessibility
Keyboard navigation, focus states and reduced-motion support are considered from the start.

---

# 👨‍⚖️ Why This Is Different

A traditional placement dashboard may stop at:

```text
Placement Rate
Average Package
Companies
Branch Comparison
```

Placement Skill-Gap Hub continues:

```text
Placement Outcomes
        ↓
Industry Demand
        ↓
Student Readiness
        ↓
Skill Gap
        ↓
Priority
        ↓
Training Recommendation
```

### Our differentiator

> **We connect placement outcomes, recruiter skill demand and student readiness into one actionable skill-gap workflow.**

---

# 🗣️ 30-Second Pitch

> “Placement Skill-Gap Hub is a Power BI-based decision-support solution that goes beyond traditional placement reporting. We combine placement outcomes, industry skill demand and student skill readiness to calculate skill gaps branch-wise. When demand is high and readiness is low, the system identifies that skill as a training priority and provides a rule-based recommendation. Our goal is to move from simply reporting placement statistics to providing actionable skill intelligence.”

---

# 🎤 Judge Q&A

### Why is this different from a normal dashboard?

Because the dashboard does not stop at placement outcomes. It compares industry demand with student readiness and converts the gap into a training priority.

### Why Power BI?

Because the problem is fundamentally an analytics and decision-support problem. Power BI supports data preparation, semantic modeling, calculations, visualization and interactive exploration in one workflow.

### Is this AI?

Not in the current MVP. The recommendation engine is rule-based and intentionally transparent. AI/ML is part of the future roadmap.

### Where did the data come from?

The current showcase uses a synthetic demonstration dataset. We intentionally do not present synthetic figures as real institutional statistics.

### How is skill gap calculated?

```text
Skill Gap = Industry Demand − Student Readiness
```

A positive result indicates a readiness shortfall relative to the demonstration demand level.

### Can this scale?

Yes. The model is designed so that the demonstration dataset can later be replaced by validated institutional data and integrated with real placement and assessment systems.

### Does the project prove that skill gaps cause lower placement?

No. The dashboard identifies gaps and relationships for decision support. It does not claim causal proof.

---

# 📂 Suggested Repository Structure

```text
placement-skill-gap-hub/
│
├── README.md
│
├── dashboard/
│   ├── placement_skill_gap_hub_modern_ui.html
│   └── assets/
│
├── powerbi/
│   ├── Placement_Skill_Gap_Hub.pbix
│   └── screenshots/
│
├── data/
│   ├── students.csv
│   ├── skills.csv
│   └── industry_demand.csv
│
├── docs/
│   ├── architecture/
│   ├── methodology/
│   └── presentation/
│
└── LICENSE
```

---

# ▶️ Running the Showcase

The showcase is a standalone HTML page.

### Option 1 — Open directly

Open:

```text
placement_skill_gap_hub_modern_ui.html
```

in a modern browser.

### Option 2 — Run a local server

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

The showcase uses client-side data and does not require a backend server or external runtime dependency.

---

# ✅ Hackathon Readiness Checklist

- [x] Problem clearly defined
- [x] Placement overview dashboard
- [x] Branch-wise analytics
- [x] Industry skill demand
- [x] Student skill readiness
- [x] Skill-gap calculation
- [x] Priority classification
- [x] Rule-based recommendations
- [x] Interactive slicers
- [x] Branch skill-gap heatmap
- [x] Animated intro
- [x] Modern responsive UI
- [x] Filter feedback
- [x] Quick evaluator demo path
- [x] Accessibility considerations
- [x] Synthetic-data disclosure
- [x] Power BI alignment
- [x] Future scope clearly separated from MVP

---

# 👥 Team

## Codeavengers

**BANNARI AMMAN INSTITUTE OF TECHNOLOGY**

**HACKORBIT 2K26 — Track A: DataDrishti**

---

# 🌟 Closing

> **Placement data should not end as a report.  
> It should become a strategy.**

### Placement Skill-Gap Hub

**From Placement Statistics to Skill-Gap Intelligence.**

