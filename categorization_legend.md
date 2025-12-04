# Categorization Legend - Resource Estimation Workflow

## 📋 Category Tags

### 🔧 ACTION
- Tasks to be performed
- Verbs: Execute, Calculate, Validate, Apply, Define, Create
- Example: "Calculate experimental variograms"

### VALIDATION
- Quality control checks
- Verification steps
- Example: "Check for outliers"

### 📊 PARAMETER
- Numerical values, thresholds, ranges
- Configuration settings
- Example: "Typical: 5m x 5m x 5m"

### RATIONALE
- Explanations of "why"
- Justifications
- Example: "Ensures geometric distribution around block"

### ⚠️ WARNING
- Critical alerts
- Common errors to avoid
- Example: "CRITICAL: Non-weighted grade averaging"

### DOCUMENTATION
- Recording requirements
- Traceability needs
- Example: "Document rationale per domain"

### 🧮 FORMULA
- Mathematical equations
- Calculations
- Example: "Grade = Σ(grade × volume) / Σ(volume)"

### 📦 DELIVERABLE
- Expected outputs
- Final products
- Example: "PowerPoint presentation"

### 📥 INPUT
- Required data
- Prerequisites
- Example: "SG from core measurements"

### 🎯 DECISION
- Decision points
- Choice criteria
- Example: "Consider mining method when deciding"

---

## Hierarchical Structure

```
Level 1: ## MAJOR SECTION
  Level 2: ### Subsection
    Level 3: #### Checklist Item (X.XX)
      Level 4: - 🔧 ACTION / VALIDATION / etc.
        Level 5: - Additional detail
```

## Example with Categories:

### Compositing Checklist (5.01-5.08)

#### 5.01 - Inside estimation domain
- 🔧 Composite only within estimation domains
- ⚠️ Do not composite across domain boundaries
- Respect geological contacts
- Avoid mixing populations

#### 5.02 - Define compositing size based on:
- 📊 Drill spacing and sampling density
- 📊 Mining bench height
- 🎯 Selectivity requirements (SMU)
- 📊 Variogram range (composites < 1/3 range)

#### 5.03 - Sample sizes
- Document original sample lengths
- 📊 Min, max, average sample length
- Distribution of sample lengths

#### 5.04 - Count before and after compositing
- Balance between number of assays subdivided into shorter composites
- And number of assays combined into longer composites
- 📊 Net count: should not change dramatically
- Document composite count per domain

#### 5.05 - Average of grades before and after compositing
- 🧮 Calculate mean grade before compositing
- 🧮 Calculate mean grade after compositing
- Should be nearly identical (length-weighted)
- ⚠️ Any difference indicates error
