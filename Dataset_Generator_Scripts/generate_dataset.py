"""
Placement Skill-Gap Hub - Demonstration Dataset Generator
HACKORBIT 2K26 | Team Codeavengers

Builds 3 related tables with deliberate logical relationships:
  - Readiness varies believably by branch (tech-focused skill set favors CSE/AIDS/IT)
  - Industry demand is DERIVED from how many sample companies actually require a skill
    (not an independently invented number) -> defensible under judge questioning
  - Placement likelihood and package correlate with a student's composite skill readiness
  - Everything is synthetic. No real institution, student, or company data is used.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

# ---------------------------------------------------------------- CONFIG
BRANCHES = ["CSE", "AIDS", "IT", "ECE", "MECH"]
BRANCH_COUNTS = {"CSE": 60, "AIDS": 50, "IT": 50, "ECE": 45, "MECH": 35}   # sums to 240
BATCHES = [2025, 2026]

SKILLS = ["Python", "SQL", "Power BI", "Machine Learning", "Java", "Communication"]

# Branch offset applied to TECH skills only (Python, SQL, Power BI, ML, Java).
# Communication is treated as largely branch-independent (soft skill).
TECH_BRANCH_OFFSET = {"CSE": 12, "AIDS": 16, "IT": 8, "ECE": -9, "MECH": -13}

# Base mean (before branch offset) and spread per skill, tuned so the overall
# weighted-average readiness lands close to the illustrative figures already
# quoted in report_HACKORBIT.pdf.
SKILL_BASE = {
    "Python":            {"mean": 47, "sd": 14},
    "SQL":               {"mean": 46, "sd": 13},
    "Power BI":          {"mean": 42, "sd": 13},
    "Machine Learning":  {"mean": 38, "sd": 13},
    "Java":              {"mean": 46, "sd": 14},
    "Communication":     {"mean": 68, "sd": 11},   # flat across branches, no tech offset
}

# Fictional companies (NOT real organizations) grouped by package tier.
COMPANIES = {
    "Tier1": ["Nexalytics Global", "Orbitrix Systems", "Quantera Labs"],
    "Tier2": ["BrightWave Technologies", "Verdant Software", "Ironpeak Analytics",
              "Solstice Data Works", "Meridian Cloud Co", "Cobalt Robotics",
              "Havenbyte Systems"],
    "Tier3": ["Lumen Field Systems", "Northstar Manufacturing", "Crestline Auto Components",
              "Pinegrove Electricals", "Union Foundry Works", "Anchor Logistics Tech",
              "Greenridge Utilities", "Falcon Precision Tools", "Amberline Textiles",
              "Copperleaf Industries", "Steadfast Engineering", "Millbrook Hydraulics"],
}
TIER_PACKAGE_RANGE = {"Tier1": (11.0, 18.0), "Tier2": (6.0, 10.0), "Tier3": (3.0, 6.0)}
TIER_HIRE_WEIGHT = {"Tier1": 0.10, "Tier2": 0.35, "Tier3": 0.55}   # who tends to hire more students

ALL_COMPANIES = COMPANIES["Tier1"] + COMPANIES["Tier2"] + COMPANIES["Tier3"]
COMPANY_TIER = {c: t for t, lst in COMPANIES.items() for c in lst}

# Probability a given company requires each skill (drives BOTH Demand_Level and
# Companies_Requiring_Count from the SAME underlying assignment, so the two
# numbers are never independently invented).
SKILL_REQUIRE_PROB = {
    "Python": 0.80, "SQL": 0.83, "Power BI": 0.76,
    "Machine Learning": 0.57, "Java": 0.58, "Communication": 0.46,
}

TARGET_PLACEMENT_RATE = 0.62

# ---------------------------------------------------------------- STUDENTS
rows = []
sid = 1
for branch in BRANCHES:
    n = BRANCH_COUNTS[branch]
    for i in range(n):
        batch = BATCHES[0] if i % 2 == 0 else BATCHES[1]
        rows.append({"Student_ID": f"STU{sid:04d}", "Branch": branch, "Batch": batch})
        sid += 1
students_df = pd.DataFrame(rows)

# ---------------------------------------------------------------- STUDENT_SKILLS
skill_rows = []
for _, s in students_df.iterrows():
    for skill in SKILLS:
        base = SKILL_BASE[skill]["mean"]
        sd = SKILL_BASE[skill]["sd"]
        offset = 0 if skill == "Communication" else TECH_BRANCH_OFFSET[s["Branch"]]
        score = rng.normal(base + offset, sd)
        score = int(np.clip(round(score), 2, 98))
        skill_rows.append({"Student_ID": s["Student_ID"], "Skill": skill, "Assessment_Score": score})
skills_df = pd.DataFrame(skill_rows)

# Composite tech-readiness per student (drives placement + package realism)
tech_skills = [s for s in SKILLS if s != "Communication"]
composite = (skills_df[skills_df["Skill"].isin(tech_skills)]
             .groupby("Student_ID")["Assessment_Score"].mean()
             .rename("Composite_Tech_Readiness"))
students_df = students_df.merge(composite, on="Student_ID")

# ---------------------------------------------------------------- INDUSTRY_SKILL_DEMAND
# Assign each company a set of required skills via the same probability that
# defines "demand" -> Demand_Level and Companies_Requiring_Count are DERIVED,
# not independently invented.
company_requirements = {c: [] for c in ALL_COMPANIES}
for company in ALL_COMPANIES:
    for skill in SKILLS:
        if rng.random() < SKILL_REQUIRE_PROB[skill]:
            company_requirements[company].append(skill)
    if not company_requirements[company]:            # guarantee every company needs >=1 skill
        company_requirements[company].append(rng.choice(SKILLS))

demand_rows = []
n_companies = len(ALL_COMPANIES)
for skill in SKILLS:
    count = sum(1 for c in ALL_COMPANIES if skill in company_requirements[c])
    demand_level = round(100 * count / n_companies)
    demand_rows.append({"Skill": skill, "Demand_Level": demand_level,
                         "Companies_Requiring_Count": count})
demand_df = pd.DataFrame(demand_rows)

# ---------------------------------------------------------------- PLACEMENT
# Placement probability: logistic-ish function of composite readiness, centered
# so the realized overall placement rate lands close to TARGET_PLACEMENT_RATE.
readiness = students_df["Composite_Tech_Readiness"].values
z = (readiness - readiness.mean()) / readiness.std()
prob = 1 / (1 + np.exp(-(z * 0.9 + 0.30)))     # shift tuned empirically below
placed = rng.random(len(students_df)) < prob

# Empirical calibration: nudge the logistic shift until overall rate is close to target
shift = 0.30
for _ in range(25):
    prob = 1 / (1 + np.exp(-(z * 0.9 + shift)))
    placed = rng.random(len(students_df)) < prob
    rate = placed.mean()
    if abs(rate - TARGET_PLACEMENT_RATE) < 0.01:
        break
    shift += 0.15 if rate < TARGET_PLACEMENT_RATE else -0.15

students_df["Placement_Status"] = np.where(placed, "Placed", "Not Placed")

def assign_company_and_package(row):
    if row["Placement_Status"] != "Placed":
        return pd.Series({"Company": "", "Package": np.nan})
    # Higher composite readiness -> better shot at a higher tier, via weighted choice
    r = row["Composite_Tech_Readiness"] / 100
    weights = np.array([
        TIER_HIRE_WEIGHT["Tier1"] * (0.4 + r),
        TIER_HIRE_WEIGHT["Tier2"] * (0.7 + 0.6 * r),
        TIER_HIRE_WEIGHT["Tier3"] * (1.3 - 0.5 * r),
    ])
    weights = weights / weights.sum()
    tier = rng.choice(["Tier1", "Tier2", "Tier3"], p=weights)
    company = rng.choice(COMPANIES[tier])
    lo, hi = TIER_PACKAGE_RANGE[tier]
    package = round(rng.uniform(lo, hi) + (r - 0.5) * 1.5, 2)
    package = round(float(np.clip(package, lo * 0.9, hi * 1.05)), 2)
    return pd.Series({"Company": company, "Package": package})

students_df[["Company", "Package"]] = students_df.apply(assign_company_and_package, axis=1)
students_placement_df = students_df[
    ["Student_ID", "Branch", "Batch", "Placement_Status", "Company", "Package"]
].copy()

# ---------------------------------------------------------------- SANITY REPORT
print("=== Sanity check (printed for review, not shipped to the workbook) ===")
print(f"Total students: {len(students_placement_df)}")
print(f"Placement rate: {(students_placement_df['Placement_Status']=='Placed').mean():.1%}")
placed_pkg = students_placement_df.loc[students_placement_df["Placement_Status"]=="Placed", "Package"]
print(f"Average package (placed): {placed_pkg.mean():.2f} LPA | Highest: {placed_pkg.max():.2f} LPA")
print(f"Distinct companies represented among placed students: {students_placement_df.loc[students_placement_df['Company']!='','Company'].nunique()}")
print()
print("Placement rate by branch:")
print(students_placement_df.groupby("Branch")["Placement_Status"].apply(lambda s: (s=="Placed").mean()).round(3))
print()
print("Readiness % and Demand % by skill (overall, unweighted by branch size):")
readiness_by_skill = skills_df.groupby("Skill")["Assessment_Score"].mean().round(1)
merged = demand_df.set_index("Skill").join(readiness_by_skill.rename("Readiness_%"))
merged["Gap"] = (merged["Demand_Level"] - merged["Readiness_%"]).round(1)
print(merged)

# ---------------------------------------------------------------- SAVE CSVs
students_placement_df.to_csv("Students_Placement.csv", index=False)
skills_df.to_csv("Student_Skills.csv", index=False)
demand_df.to_csv("Industry_Skill_Demand.csv", index=False)
print("\nCSV files written.")
