# Estimation Workflow - Mineral Resource Estimation

## Category Legend

- **ACTION**: Tasks to execute (Calculate, Validate, Apply, Define)
- **VALIDATION**: Quality control checks and verification
- **PARAMETER**: Numerical values, thresholds, ranges
- **RATIONALE**: Explanations and justifications
- **WARNING**: Critical alerts and errors to avoid
- **DOCUMENTATION**: Recording and traceability requirements
- **FORMULA**: Mathematical and calculations
- **DELIVERABLE**: Expected outputs and final products
- **INPUT**: Required data and prerequisites
- **DECISION**: Decision points and choice criteria

---

## Workflow Overview & Proportional Time InvestmentF

**Total workflow time allocation:**
- Database Validation: **10%**
- Wireframe (Geological Modelling): **25%**
- Exploratory Data Analysis: **15%** (Capping, Compositing, Domains handling, Variography)
- Density: **5%**
- Estimation: **10%**
- Validation: **10%**
- Resource Classification: **6%**
- Depletion: **5%**
- Peer Review: **5%**
- Final Resource Tabulation and Reporting: **7%**
- Archive Results: **1%**
- Handover to Engineering: **1%**

*Note: This time allocation is dependent on the materiality of changes to the model (new data, different interpretation, internal vs public reporting)*

---

## Load Data

### Database Validation Checklist

**Status legend**: Green = Pass | Yellow = Warning | Red = Critical Issue

#### 1.01 - Collar coordinates
- Validate collar table has X, Y, Z coordinates
- Check for duplicate collar IDs
- Verify coordinate system is documented
- Survey table matches collar IDs
- No orphan records
- **Spatial clustering analysis**: identify drill patterns
- Generate collar location maps
- Check elevation consistency

#### Overlaps, missing intervals
- Check for overlapping FROM/TO intervals in assay table
- Identify gaps between sample intervals
- Flag intervals with FROM >= TO
- Validate sample depth vs survey depth
 Identify duplicate samples
- Validate negative/null values
- Convert units if necessary
- **Identify all chemical elements present**
- List all grade variables available
- Check detection limits and assay methods
- **Data completeness analysis**: % of samples with each element
- **Below detection limit (BDL) handling**: document treatment
- **Assay method documentation**: analytical methods used
- **Twin hole analysis**: if QAQC twin holes exist

#### "Suspicious" spikes of repeated grade values in histograms
- Detect repeated exact values (e.g., many samples = 0.5%)
- Histogram analysis for unnatural patterns
- Spike at detection limit values
- Investigate data entry errors
- Flag for review with geologist

#### Values set to lower detection limit (LDL) or ½ LDL
- Identify samples below detection limit
- Check if coded as ½ LDL or LDL
- Document treatment of BDL values
- Impact on statistics and estimation

#### Possible mixed units (g/t and oz)
- Check for unit inconsistencies
- Detect outliers that may be unit errors
- Au in g/t vs oz/t (factor of ~31x)
- Ag in g/t vs oz/t
- Base metals in % vs ppm
- Validate units are consistent across database

#### Check for bias between years and sample type (DD, RC, channel)
- Compare statistics by drilling campaign/year
- Compare DD (diamond drill) vs RC (reverse circulation)
- Channel samples vs drillhole samples
- T-test for statistical differences
- Document any systematic bias

#### Extract a list of errors and share with partner site
- Compile all validation errors in report
- Share with data source/geologist
- Request corrections at source
- Track error resolution
- Re-validate after corrections

#### Comparison with database from previous update
- Compare current vs previous database
- Identify new drillholes added
- Check for changed grade values
- Flag deletions or modifications
- Document reasons for changes

#### Number of assays by data type (drilling, RC, channels...)
- Count samples by method
- DD (diamond drilling): quantity and %
- RC (reverse circulation): quantity and %
- Channels/trenches: quantity and %
- Grab samples: quantity and %
- Document data source distribution

#### Comparison of pre-existing grade values in both databases
- Has any grade changed from previous database to current?
- Identify grade value changes for same sample ID
- Investigate reasons for changes
- Re-assays, lab corrections, data entry fixes
- Document and justify all changes
- Get sign-off from responsible geologist

### Reconnaissance of files and columns
####  Identify available data files (collar, survey, assay)
- use heuristics to determine cfiletype
#### Inspect column names and data types
- Map column names to standard nomenclature
- Identify key columns (hole_id, from, to, coordinates, grades)
- Document data schema and relationships
- Store column mappings in configuration file (JSON/YAML)
- Save as global variables for later reference
- Create data dictionary with column descriptions

#### Project characterization (knowledge building)
- **Identify drilling type**: Underground (UG) or surface drilling
- Analyze collar elevation patterns
- Check for vertical vs inclined holes
- Identify drill setup locations (single collar vs multiple)

#### Deposit characterization (knowledge building)
- **Analyze elemental suite** to identify deposit type
- Research geological setting and mineralization style
- Common deposit types: porphyry, VMS, IOCG, skarn, epithermal, sedimentary-hosted, etc.
- **Define PAY elements** (economic metals/minerals)
- Primary commodities (e.g., Cu, Au, Ag, Zn, Pb, Ni)
- By-product credits (e.g., Mo, Re, In)
- **Define penalty/deleterious elements** (contaminants)
- Elements affecting metallurgy (e.g., As, Sb, Hg, F)
- Elements with environmental concerns
- Penalty thresholds and impacts on NSR
- **Establish element correlations**
- Identify pathfinder elements
- Understand paragenesis and mineral associations
- Create element classification table
- **Mineralogical characterization**
- Key ore minerals identified
- Gangue mineralogy
- Alteration assemblages
- Metallurgical domains based on mineralogy
- **Lithological and structural framework**
- Stratigraphic sequence understanding
- Structural controls on mineralization
- Fault systems and their impact
- **Document deposit type hypothesis**
- Genetic model understanding
- Implications for continuity and grade distribution
- Store in configuration file for reference



### Density

#### Validate density data (if available)
- Check for outliers and errors
- Validate measurement methods
- Sufficient sample size for statistical validity
- Spatial distribution of density samples
- Compare with industry standards for rock types
- SG from core measurements (water displacement, pycnometer)
- Bulk density from metallurgical test work
- Default densities from literature (if no measurements)
- Check for outliers (typical range 2.0-5.0 g/cm³)
- Validate measurement method
- Verify sample representativeness

#### Use density weighting for compositing
- If SG varies significantly, use density weighting
- Tonnage-weighted composites more representative
- Formula: Composite grade = Σ(grade × length × SG) / Σ(length × SG)
- Document if density weighting applied

#### Define criteria for assigning density to block model
- If estimated by kriging: document parameters
- If assigned by domain: document values per domain
- If regression with grade: document formula
- Hybrid methods: document decision logic
- Validate density assignment results

#### Density by domain/lithology
- Calculate average SG per lithology
- Consider alteration impact on density
- Oxidation state effects (oxide vs fresh rock)
- Mineralization impact on density

#### Density-grade relationships
- Correlation analysis: SG vs grade
- High-grade zones often higher density (sulphides)
- Low-grade zones may be lower density (alteration)
- Establish regression relationships if correlation exists

#### Density estimation strategy
- If sufficient data: estimate SG by kriging
- If limited data: assign by domain/lithology
- If correlation with grade: use regression formula
- Hybrid approach: kriging with trend

#### Default density assignment
- Document density values used per domain
- Source of density values (measured, assumed, literature)
- Impact of density uncertainty on tonnage

#### Density validation
- Compare estimated vs measured densities
- Reconciliation with metallurgical test work
- Sensitivity analysis: ±0.1 g/cm³ impact on tonnage
- Document density confidence level

### Non-additive Variables

#### Review all available data and consider what is sufficiently populated for inclusion in model
- Identify all potential variables beyond grades
- Recovery, metallurgical parameters, geometallurgy
- Hardness, comminution indices
- Deleterious elements
- Check data population (>30% coverage minimum)

#### Discuss requirements with engineering
- What parameters does mining need?
- What parameters does processing need?
- Geometallurgical variables required?
- Environmental parameters?
- Align model outputs with downstream users

#### 9Examine relationship between non-additive variables and standard variables estimated
- **Non-additive variables**: recovery, density, metallurgical performance
- Cannot be averaged directly
- Must use inverse distance or special methods
- Correlation with grades (e.g., recovery vs Cu grade)

#### Estimation approach for non-additives**
- Direct estimation with appropriate method
- Regression models (e.g., recovery = f(grade))
- Classification into geomet domains
- Document estimation methodology

### Compositing
#### Composite length
- Define composite length
- Standard lengths: 1m, 2m, 5m, bench height
- Consider mining selectivity
- Downhole compositing: preserves vertical trends
- Bench compositing: matches mining method
- Apply compositing (downhole/bench)
- Handle partial intervals
- Options: include, exclude, or pro-rate partial intervals
#### Calculate weighted average grade
- Length-weighted averaging formula
- Density-weighted if SG data available
#### Validate compositing quality
- Check for bias introduction
- Verify no samples lost
- Account for all meters
- Document compositing method and parameters
#### Store composite database
- Retain original sample IDs for traceability
- Flag composite type (full/partial)
- Calculate composite quality metrics

#### Inside estimation domain
- Composite only within estimation domains
- Do not composite across domain boundaries
- Respect geological contacts
- Avoid mixing populations

#### Define compositing size based on:
- Drill spacing and sampling density
- Mining bench height
- Selectivity requirements (SMU)
- Variogram range (composites < 1/3 range)

#### Sample sizes
- Document original sample lengths
- Min, max, average sample length
- Distribution of sample lengths

#### Count before and after compositing
- Balance between number of assays subdivided into shorter composites
- And number of assays combined into longer composites
- Net count: should not change dramatically
- Document composite count per domain

#### Average of grades before and after compositing
- Calculate mean grade before compositing
- Calculate mean grade after compositing
- Should be nearly identical (length-weighted)
- Any difference indicates error
- Remain vigilant that sampling lengths are not "lost" to the compositing process
- Account for all sample meters
- Total meters before = total meters after
- No "missing" intervals
- Reconcile any discrepancies

#### Compare meters of assays in side domain and meters of composites (should be similar)
- Sum of assay lengths in domain
- Sum of composite lengths in domain
- Should match (within rounding)
- Flag large discrepancies for investigation

#### Ensure composites were created for all holes that cross wireframe
- Correct selection of minimum composite length
- All intersecting holes have composites
- No holes "missed" in compositing
- Validation query: holes with assays but no composites

### Absents Handling

#### Proportion of absents (especially inside mineralization domain)
- Calculate % missing values per element per domain
- Lower % expected in ore vs waste
- High absence in ore is suspicious
- Document and investigate

#### Replace by a nominal low value (detection limit)
- Option 1: Set to ½ detection limit
- Option 2: Set to detection limit
- Option 3: Set to zero (conservative)
- Document approach and rationale

#### Handle with special attention; can be very critical in resource estimation
- Missing data impacts statistics
- Affects variography
- Influences grade distribution
- Can introduce bias
- Document impact assessment

#### First step is to check with site why values are absent
- Data entry error?
- Analytical failure?
- Below detection limit?
- Never analyzed?
- Selective reporting?
- Contact lab/geologist for clarification

#### May be an interval assayed for one element but not another
- E.g., Zn not analyzed, but not Au
- Understand assay package differences
- Multi-element vs single-element analysis
- Document assay protocols

### Desurvey process
#### Desurvey method
- Select desurvey method (Minimum Curvature, Tangential, Balanced Tangential)
- Minimum Curvature: most accurate, industry standard
- Tangential: assumes straight line between survey points
- Balanced Tangential: average of tangent vectors
- Calculate 3D coordinates (X, Y, Z) for each sample interval
- Apply survey interpolation to sample depths
- Handle missing survey data (assume vertical if needed)
#### Desurvey validation
- Validate trajectory consistency
- Generate drillhole traces for visualization
- Export desurvey table with sample coordinates
- Store desurvey method in configuration file
- Validate azimuth and dip
- Check depths
- Calculate 3D drillhole trajectory
- Interpolate survey to samples
- **Calculate dogleg severity** (rate of change in deviation)
- Identify excessive doglegs (>3°/30m typically)
- **Generate "horsetail" plots** (fan diagram from collar)
- Visualize all holes from same setup point
- Assess deviation patterns and quality
- Document survey quality issues

---

## Geological Modeling

### Geological understanding and context

#### Gather understanding of geological setting and controls
- Research regional geology
- Understand tectonic setting
- Identify structural controls on mineralization
- Document geological history
- Consult published literature and reports

#### Deposit type (average size and grade)
- Classify deposit type (porphyry, VMS, IOCG, epithermal, etc.)
- Research typical size for this deposit type
- Compare grades with global averages for deposit type
- Benchmark against analogous deposits
- Document expected grade ranges

#### Mineralizing controls
- Identify geological controls on mineralization
- Structural controls (faults, shears, folds)
- Lithological controls (favorable host rocks)
- Alteration controls (alteration zoning)
- Stratigraphic controls
- Geochemical gradients

#### Analogous deposits
- Identify similar deposits globally
- Compare geological characteristics
- Compare grade distributions
- Learn from estimation approaches used
- Apply lessons learned

#### Define modelling criteria (lithology, grade, weathering...)
- Determine primary modelling criteria
- Lithological domains
- Grade shells (mineralized envelopes)
- Weathering/oxidation domains
- Alteration domains
- Combination criteria

#### Consider criteria from previous model
- Review previous model domains
- Is there justification for change?
- Document reasons for any changes
- Maintain consistency unless justified
- Avoid unnecessary re-interpretation

#### Consider geology and mining selectivity when selecting intervals to model
- Account for waste gaps within mineralization
- Minimum mining width (SMU)
- Maximum internal dilution
- Practical mining constraints
- Balance geology vs mining selectivity

#### Wireframe modelling
- Use appropriate modelling software
- Consistent interpretation rules
- Section spacing adequate for complexity
- Validation against drillholes

#### Modelling and validation of any subdomains (mineralization)
- Model mineralization subdomains
- High-grade cores vs lower-grade halos
- Multiple mineralization stages
- Statistical validation of subdomains
- Ensure adequate sample population

#### Modelling of any important known structures
- Model major faults with offsets
- Model shear zones
- Model fold geometries
- Structural impact on continuity
- Domain boundaries at structures

#### Modelling of host lithology, alteration and waste domains (dykes)
- Model host rock lithology
- Model alteration types and intensity
- Model waste domains (dykes, barren units)
- Unmineralized intrusions
- Structural waste (faults, shears)

### Wireframe validation

#### Limit wireframe extrapolation to reasonable distances
- Consider deposit type and geometric continuity
- Avoid over-extrapolation beyond data
- Typical limits: 25-50m from nearest drillhole
- Document extrapolation limits
- Conservative approach in poorly drilled areas

#### Volumetric and visual comparison with previous update
- Compare current vs previous wireframe volumes
- Identify areas of change
- Quantify volume differences
- Document reasons for changes
- Visual side-by-side comparison

#### When mine voids are available, validate shape and location against mineralization wireframes
- Overlay as-mined voids on wireframes
- Check agreement between mined shape and wireframe
- Identify areas of over/under prediction
- Reconciliation learnings
- Update wireframes if needed

#### Check polylines contours after geometry update
- Verify section strings after edits
- Check for crossed lines
- Validate digitizing errors
- Consistent pick points
- No orphan or duplicate polylines

#### Activate thickness legend with informative scale
- Display wireframe thickness maps
- Color-code by thickness ranges
- Review thicker zones (potential errors)
- Review very thin zones (below mining width)
- Document thickness statistics

#### Check manifold issues
- Identify non-manifold edges
- Fix self-intersecting triangles
- Repair open surfaces
- Validate closed volumes
- Software-specific validation tools

#### Confirm that new drillholes are correctly tagged and modeled
- All new holes incorporated in interpretation
- Holes tagged with correct domains (lith, domain, zone)
- Visual validation on sections
- Statistics include new data
- Update documentation with new hole count

#### Check proportion of NN values
- Nearest Neighbor (NN) proportion should be low
- Ideally <5% of blocks estimated by NN
- High NN% indicates sparse data or poor search
- Compare to previous model
- Flag areas with high NN for review

#### Check proportion of absent data inside ore
- Ideally expect lower proportion of absent data in ore
- Higher absence in ore than waste is suspicious
- May indicate preferential sampling bias
- Compare to previous model
- Investigate causes of high absence
- Impact on resource confidence

### Geological interpretation workflow
#### Data compilation for interpretation
- Drillhole logs (lithology, alteration, mineralization)
- Geochemical data patterns
- Structural measurements
- Geophysical data (if available)
- Surface mapping and outcrop data
#### Section interpretation
- Create cross-sections (typically 25-100m spacing)
- Interpret lithological contacts
- Interpret alteration zones
- Interpret mineralization envelopes
- Identify structural features (faults, folds)
- Consistent interpretation rules across sections
#### Plan view interpretation
- Interpret on benches/levels
- Validate against section interpretations
- Check for structural controls
- Identify plunge and trend

### Wireframe construction
#### Lithological wireframes
- Major lithological units
- Stratigraphic sequence
- Intrusive contacts
- Minimum thickness considerations
#### Alteration wireframes
- Alteration types and intensity
- Alteration zoning patterns
- Overprinting relationships
#### Mineralization wireframes/grade shells
- Define mineralization envelope
- Grade shell approach: use nominal grade threshold (e.g., 0.2% Cu)
- Multi-pass grade shells for different confidence levels
- Honor geological controls
- Minimum mining width (e.g., 3-5m)
- Maximum internal dilution (e.g., 2m)
#### Structural wireframes
- Major faults and offsets
- Fold geometries
- Shear zones
#### Wireframe quality control
- Check for self-intersections
- Validate closed volumes
- Edge matching between sections
- Smooth vs preserve detail balance
- Validate against drillholes (% intersections correct)

### Domain coding and hierarchy
#### Coding strategy
- Hierarchical system (e.g., 1000s = lithology, 100s = alteration, 10s = grade)
- Unique domain combinations
- Preserve geological hierarchy
#### Domain validation against drillholes
- % of samples correctly assigned
- Visual validation in sections and plans
- Check for misclassification
#### Hard vs soft boundary treatment
- Hard: faults, lithological contacts, sharp mineralization
- Soft: gradational alteration, diffuse mineralization
- Estimation strategy per boundary type
#### Minimum domain size for estimation
- Sufficient samples (30-50 minimum)
- Statistical viability
- Practical mining considerations
- Combine small domains if needed

### Metallurgical domain definition
#### Recovery domains
- Based on mineralogy and ore type
- Oxidation state (oxide, transition, sulphide)
- Deleterious element content
#### Geometallurgical characterization
- Hardness/grindability domains
- Comminution characteristics
- Processing method suitability
#### Link met domains to geological domains
- Correlation with lithology/alteration
- Spatial distribution
- Document met domain assumptions

---

## EDA (Exploratory Data Analysis)

**Note: EDA is an iterative process performed at three levels:**
1. **Full dataset**: Initial exploration of all data
2. **Geological domains**: Statistics by lithology, alteration, mineralization
3. **Stationary estimation domains**: Final domains used for kriging

### Descriptive statistics - Full dataset
#### Descriptive statistics - Full dataset

- Mean, median, mode
- Standard deviation, variance
- Minimum, maximum, quartiles
- Coefficient of variation
- Skewness and kurtosis

### Descriptive statistics - By geological domain
#### Descriptive statistics - By geological domain
- Repeat all statistics for each domain
- Compare domains to identify populations
- Validate domain boundaries
- Document statistical differences

### Descriptive statistics - By stationary estimation domain
#### Descriptive statistics - By stationary estimation domain
- Final statistics for kriging domains
- Verify stationarity assumptions
- Test for spatial trends
- Document domain parameters

### Outlier analysis and capping

#### Define capping values based on:
- **Multiple methods** (use at least 2-3)
- CV (Coefficient of Variation) method
- Statistical percentiles (P95, P98, P99)
- Geological judgment

#### Probability plots
- Normal probability plots
- Log-normal probability plots
- Identify inflection points
- Detect outlier populations
- Document distribution type

#### Histograms
- Frequency histograms by domain
- Identify grade populations
- Detect spikes or gaps
- Compare domains
- Log-scale histograms for skewed data

#### Boxplots
- Box-and-whisker plots by domain
- Identify outliers visually
- Compare domain variability
- Document outlier thresholds

#### Metal loss
- Calculate metal loss from capping
- Typically 1-5% acceptable
- >10% metal loss requires justification
- Document and report metal loss
- Balance bias reduction vs metal loss

#### High-level comparison with previous update
- Compare top cuts: current vs previous
- Justify any changes in capping strategy
- Consistency check
- Document reasons for differences

#### Check for dramatic differences
- Identify domains with major cap changes
- Investigate reasons (new data, re-interpretation)
- Validate with geologist
- Document justification

#### Analyze number of samples cut, mean grades after and before capping
- Count samples capped per domain
- % samples capped (target <5%)
- Mean grade before capping
- Mean grade after capping
- % reduction in mean (typically 5-15%)
- CV before and after (should decrease)

#### When possible, validate impacts of capping before and after compositing
- Apply capping to raw samples
- Composite, then check impact
- Or: composite first, then cap
- Compare both approaches
- Document selected approach and rationale

#### Capping implementation
- Identify extreme values (full dataset and by domain)
- Box plots by domain
- Percentiles (P95, P98, P99)

#### Top cut determination methods
- Coefficient of Variation (CV) method
- Probability plots (inflection points)
- Grade-tonnage impact analysis
- Expert geological judgment
- Define top cuts (capping values)
#### Different caps by domain** (important!)
- Each domain may have different top cut
- Document rationale per domain
- Apply capping to estimation domains
#### Capping validation**
- Compare statistics before vs after capping
- Impact on mean (typically reduces 5-15%)
- Impact on CV (should reduce significantly)
- % of samples capped (typically <5%)
- Metal loss from capping
#### Spatial capping considerations
- Check if high grades cluster or scatter
- Consider restricted search for high grades
- Evaluate need for indicator kriging
- Document capping rationale and impact
#### Store capped and uncapped databases
- Keep both for comparison
- Use capped for estimation
- Flag capped samples for traceability

### Compositing validation
#### Compare raw samples vs composited data
- Validate length-weighted averages
- Check for compositing bias
- Histogram comparison (before vs after)
- Document compositing impact on statistics

### Histograms and distributions
#### Histograms and distributions
- Frequency distribution
- Log-normal transformation
- Normality test
- Histograms by geological domain
- **Probability plots** (normal, log-normal)
- Test different distribution types

### Coefficient of Variation (CV) analysis
#### Coefficient of Variation (CV) analysis
- Calculate CV for each element and domain
- Identify high variability domains (CV > 1.0)
- Document variability patterns
- Consider impact on sample size requirements

### Declustering (if needed)
#### Declustering (if needed)
- Identify spatial clustering of samples
- Apply cell declustering or polygonal declustering
- Calculate declustered statistics
- Compare clustered vs declustered means
- Document declustering method and impact

#### Length-weighted vs equal-weighted statistics
- Compare statistics with and without length weighting
- Identify sampling bias (preferential sampling)
- Document impact on resource estimation
- Choose appropriate weighting for reporting

#### Basic spatial analysis
- Spatial distribution of samples
- Sampling density
- 3D scatter plots
- Sections and plans

### Domain analysis
#### Domain analysis
- Separate by lithology
- Separate by alteration
- Separate by mineralization
- Statistics by domain
#### Hard vs soft boundaries
- Hard boundaries: geological contacts, faults
- Soft boundaries: gradational zones, alteration halos
- 
#### Domain coding strategy
- Hierarchical coding system
- Lithology codes
- Alteration codes
- Mineralization codes
- Combined domain codes for estimation
- 
#### Statistical domain validation
- T-tests between domains
- ANOVA for multiple domains
- Non-parametric tests (Kruskal-Wallis)
- Confirm statistical separation
- 
#### Spatial domain continuity
- Check domain wireframe quality
- Validate against drill holes
- Review domain boundaries in sections
- Minimum domain thickness
- 
#### Estimation domain definition
- Combine or split domains based on:
  - Sample population size (minimum 30-50 composites)
  - Statistical similarity
  - Spatial continuity
  - Mining selectivity
- Create estimation domain map
- Document domain rationale

#### Contact plots
- Check continuity at contacts
- Identify population mixing

### Boundary Analysis 

#### Perform analysis to support decision on use of hard/soft/transitional boundaries
- **Hard boundaries**: geological faults, lithological contacts, sharp mineralization edges
- **Soft boundaries**: gradational alteration zones, diffuse mineralization
- **Transitional boundaries**: weathering profiles, gradual grade transitions
- Analyze grade behavior across boundaries
- Statistical tests for population differences
- Document boundary type selection

#### Demonstrate with contact plot, descriptive statistics
- **Contact plots**: plot grades on both sides of boundary
- Visualize grade continuity or discontinuity
- Calculate statistics for each side of contact
- T-tests or Mann-Whitney tests
- Variance ratio tests
- Document results supporting boundary decision
- Include contact plots in validation report

#### Anisotropy analysis
- Preferential directions
- Trend surfaces
- Mineralization orientation

#### Element correlation analysis
- **Calculate correlation matrix** for all elements
- Identify strong correlations (>0.7) and anti-correlations (<-0.7)
- Generate correlation heatmaps
- Scatter plots for correlated element pairs
- Document element associations
- **Store correlation coefficients** for validation later
- Identify co-kriging candidates

---

## Geostatistical Estimation

### Variography

#### 7.01 - Calculate the model variogram inside estimation domain and/or apply estimation domain masks
- Variogram calculated per estimation domain
- Do not mix domains in variogram calculation
- Apply domain masks to composites
- Separate variograms for each stationary domain

#### Consider how differences and similarities between multiple grade variables reflect geology
- Example: Zn and Pb should have similar variogram models in VMS deposit
- Anisotropy and ranges should reflect geology
- Check consistency across related elements
- Document geological rationale for variogram differences

#### High-level comparison with previous update
- Compare variogram ranges: current vs previous
- Compare nugget effect
- Compare anisotropy ratios
- Justify major changes
- Document reasons for differences

#### Check for substantial differences in anisotropy and ranges
- Investigate causes of major changes
- New data with different spacing?
- Re-interpretation of domains?
- Different compositing?
- Validate with geological team

### Variography
#### Calculate experimental variograms
- **Variogram parameters**
- Lag distance: typically 1/2 to 1/3 of drill spacing
- Number of lags: 10-20 lags
- Lag tolerance: 50% of lag distance
- Azimuth tolerance: 22.5° to 45°
- Dip tolerance: 15° to 30°
- Bandwidth: perpendicular search width
- Directional variograms (X, Y, Z)
- **Major, semi-major, and minor directions**
- Search orientations: 0°, 45°, 90°, 135° in plan
- Dip variations: horizontal, 45°, vertical
- Define lags and tolerances
- Identify anisotropy
- **Anisotropy types**
- Geometric anisotropy: different ranges, same sill
- Zonal anisotropy: different sills
- Combined anisotropy: both range and sill vary
- Model theoretical variograms (spherical, exponential, gaussian)
- **Variogram model selection**
- Spherical: most common, linear near origin
- Exponential: smoother, gradual approach to sill
- Gaussian: very smooth, parabolic near origin
- Power: for non-stationary data (avoid if possible)
- **Nested structures** (if applicable)
- Short-range structure (nugget effect + first structure)
- Long-range structure (geological continuity)
- Adjust nugget, sill, range
- **Nugget effect interpretation**
- Measurement error
- Micro-variability below sample spacing
- Nugget/Sill ratio: <0.3 good, 0.3-0.6 moderate, >0.6 poor
- Validate variogram model
- **Cross-validation**: leave-one-out test
- Calculate prediction errors
- Mean error (should be ~0, unbiased)
- Mean squared error
- Standardized mean squared error (should be ~1)
- Check for bias in cross-validation
- **Variogram quality metrics**
- Number of pairs per lag
- Minimum pairs threshold: 30-50 pairs
- Validate variogram quality
- **Anisotropy ellipsoid definition**
- Major range (longest continuity)
- Semi-major range (intermediate)
- Minor range (shortest, often vertical)
- Rotation angles: azimuth, dip, plunge
- Document in estimation parameters

### Block Model Setup

#### Block size
- Rule of thumb: ¼ to ½ of the nominal drillhole spacing
- Consider mining selectivity (SMU)
- Balance resolution vs estimation quality

#### Rule of thumb is ¼ to ½ of the nominal drillhole spacing
- Validate against drill spacing statistics
- Document block size rationale
- Compare with industry practice for deposit type

#### Subblocking generally required to honor wireframe volumes
- Minimum block size should be reasonable (e.g., 0.2m minimum)
- If done in Datamine: special attention on RESOL parameter of TRIFIL
- Sub-blocks for volume precision only

#### Consider mining method when deciding between subblocking or parent cell
- Underground vs open pit requirements
- Small-scale selective mining → sub-blocks may be useful
- Large-scale bulk mining → parent cells adequate

#### Rotation
- Align with orebody geometry if rotation improves efficiency
- Document rotation angles (azimuth, dip, plunge)

#### If required to honor geology, use only a single rotation around z axis
- Never more than 1 rotation to avoid complexity
- Validate with engineering if rotated model is acceptable
- Simple rotation preferred for mine planning integration

#### Validate with engineering if rotated model is acceptable
- Confirm mine planning software compatibility
- Check reporting requirements
- Document approval from engineering

#### Use only a single prototype/rotation to fit the entire model
- Consistency across entire deposit
- Avoid multiple rotation schemes
- Simplifies model management

#### Extents/Prototype
- Define model extents with appropriate buffer
- Cover all mineralization + buffer (50-100m typical)

#### Ensure the model extends above the topography
- Blocks above surface for future pit optimization
- Validate topography source and date

#### For open pit models, extents should cover roughly 200m past mineralized area
- Allow for pit optimization flexibility
- Waste blocks needed for pit shell generation
- Validate with engineering needs

#### Ensure the prototype is consistent with previous versions and with engineering
- Compare extents with previous model
- Validate origin, rotation, block size consistency
- Get engineering approval before estimation

### Define block model
#### Block size selection
- Rule of thumb: 1/4 to 1/3 of drill spacing
- Consider mining selectivity (SMU - Selective Mining Unit)
- Balance between resolution and estimation quality
- Block dimensions (X, Y, Z)
- Typical: 5m x 5m x 5m, 10m x 10m x 5m, 25m x 25m x 10m
- Z dimension often matches bench height
- Model origin
- SW corner or centroid of deposit
- Align with mine grid if applicable
- Model rotation
- Align with orebody orientation
- Align with geological strike
- May improve estimation efficiency
- Sub-blocks (if necessary)
- For detailed topography or wireframe conformance
- Minimum sub-block size (e.g., 1/8 parent block)
- **CRITICAL: Understanding sub-blocking risks**
- Sub-blocks created for volume precision (wireframe fitting)
- Must be properly aggregated back to parent cells
- Risk of grade weighting errors during reblocking
- **Parent cell discretization**
- Number of discretization points: 2x2x2 to 5x5x5
- Higher discretization for better volume precision
- Balance accuracy vs computation time

### Reblocking process (Sub-cell to Parent Cell)
#### Purpose of reblocking**
- Convert detailed sub-block model to parent cell grid
- Simplify model for mine planning and reporting
- Aggregate volumes and grades appropriately
- **CRITICAL REBLOCKING ISSUES TO AVOID**
- **Risk: Non-weighted grade averaging**
- If reblocking not done properly, grades may not be volume-weighted
- High-grade sub-blocks on edges may dominate parent cell incorrectly
- Example: Small high-grade sub-block + large low-grade sub-blocks → parent shows high grade (WRONG!)
- **Correct reblocking methodology**
- **Volume-weighted averaging** (essential!)
- Parent grade = Σ(sub-block grade × sub-block volume) / Σ(sub-block volume)
- **Density-weighted if SG varies**
- Parent grade = Σ(sub-block grade × sub-block tonnage) / Σ(sub-block tonnage)
- **Tonnage calculation**
- Parent tonnage = Σ(sub-block volume × sub-block density)
- Validate total tonnage matches
- **Metal conservation check (CRITICAL!)**
- Contained metal MUST be preserved during reblocking
- Metal before = Metal after reblocking
- Σ(sub-block grade × tonnage) = Parent grade × Parent tonnage
- **Any deviation indicates error in reblocking!**
- **Common reblocking errors**
- Simple arithmetic average (ignores volume) - WRONG!
- Maximum value selection (cherry-picking) - WRONG!
- Minimum value selection (over-conservative) - WRONG!
- Modal value (most common, ignores distribution) - WRONG!
- **Reblocking validation checklist**
- ✓ Compare total tonnage before/after (must match)
- ✓ Compare total metal before/after (must match exactly)
- ✓ Visual inspection: check edge artifacts
- ✓ Grade histograms: compare sub-block vs parent distributions
- ✓ Swath plots: validate grade trends preserved
- ✓ Statistics comparison: mean, variance should be similar
- **Edge effect management**
- High-grade sub-blocks on wireframe edges
- Ensure proper volume weighting
- Check for artificial high-grade halos at boundaries
- Validate against sample data in edge zones
- Review sections showing edge blocks
- **Software-specific considerations**
- Leapfrog: automatic volume-weighted reblocking (verify!)
- Surpac/Vulcan: manual reblock scripts (validate carefully!)
- Datamine: REBLOCR function (check parameters)
- Python/custom: verify weighting formula explicitly
- **Documentation**
- Document reblocking method used
- Archive validation statistics (tonnage/metal reconciliation)
- Include reblocking validation in technical report
- Flag if any anomalies detected and corrected

### Define attributes to estimate
#### Define attributes to estimate
- **Primary attributes**: grades for all PAY elements
- **Secondary attributes**: penalty elements, density
- **Derived attributes**: metal equivalents, NSR
- **Estimation metadata**: number of samples, average distance, kriging variance
- **Classification field**: Measured/Indicated/Inferred
- **MINED attribute**: track depletion status
- **Model extent definition**
- Buffer beyond drillhole envelope: 50-100m typical
- Constrain by geological limits
- Consider future drilling areas
- Avoid over-extrapolation

### Block Attributes

#### Estimated attributes
- All PAY elements estimated
- Penalty elements estimated
- Density estimated or assigned
- Document all estimated variables

#### Payable metals
- Economic metals for NSR calculation
- Recovery assumptions documented
- Price assumptions documented

#### Geomet attributes (magnetic susceptibility, hardness)
- Geometallurgical parameters if available
- Comminution indices (BWI, AI, etc.)
- Recovery domains
- Document data sources

#### Penalty elements (As, Bi...)
- Deleterious elements affecting metallurgy
- Environmental concerns (As, Hg, etc.)
- Penalty thresholds documented
- NSR impact calculated

#### Density – for open pits especially
- Flag waste blocks with density
- All blocks should have density assigned
- Even air blocks set to 0 for clarity

#### Flagged attributes
- Domain codes (lithology, oxidation, alteration)
- MINED status
- Classification category
- Special flags (sterilized, stockpile, etc.)

#### Domain and subdomain codes (lithology, oxidation, alteration...)
- Hierarchical coding system
- Consistent with wireframe tags
- Documented in data dictionary

#### Resource Classification
- Measured/Indicated/Inferred/Potential
- Classification criteria documented
- Stored as numeric and text

#### Depletion
- MINED attribute for production tracking
- Void volumes tagged
- Reconciliation-ready

#### For open pit scenarios: waste blocks are tagged with density information
- Can be a flat value (e.g., 2.7)
- Enables pit optimization
- Waste tonnage calculation

#### Calculated attributes
- NSR (Net Smelter Return)
- Metal equivalents (AuEq, CuEq, etc.)
- Payability flags
- Cut-off comparisons

#### Sulphide content
- If relevant for processing
- Acid generation potential
- Metallurgical domain indicator

#### Metal equivalent (ZnEq, AgEq, AuEq...)
- Formula documented with prices and recoveries
- Consistent with economic assumptions
- Used for reporting and optimization

#### Density
- All blocks have density assigned
- Method documented (estimated, assigned, default)
- Validation completed

### Depletion

#### Engineering department or mine site should provide voids and sterilization shapes
- As-mined surfaces from surveys
- Void wireframes or solids
- Sterilization zones (pillars, infrastructure, exclusion zones)
- Delivery format and schedule agreed

#### Some for underground mines are done by the engineering department
- UG voids more complex than open pit
- Stope surveys
- Development wireframes
- Non-valid voids (areas not truly mined)
- Coordinate with mine surveyors

#### If done by engineering department, geology department should validate depleted model
- Visual validation mandatory
- Check void shapes against actual mining
- Numeric reconciliation (tonnage, grade)
- Compare model vs production records
- Validate sterilized zones
- Sign-off process

#### Must be done on sub-blocks for precision (if block model is subblocked)
- Depletion applied to sub-blocks
- More accurate volume calculation
- Better void shape representation
- Then aggregate to parent cells for reporting

### MINED attribute implementation
#### Purpose of MINED flag**
- Track blocks already extracted
- Reconciliation with production
- Identify remaining resources
- **MINED coding system**
- 0 = Not mined (in-situ resource)
- 1 = Mined and extracted
- 2 = Mined but not processed (stockpiled)
- 3 = Sterilized (cannot be mined - infrastructure, pillars)
- 4 = Planned for mining (near-term)
- **MINED volume sources**
- Survey pickups (as-mined surfaces)
- Blast polygon records
- GPS dozer data
- LiDAR or photogrammetry
- Design vs actual comparison
- **Update frequency**
- Monthly updates typical for active mines
- Quarterly for slower operations
- Reconciliation cycle alignment
- **Depletion validation**
- Compare MINED volume vs production records
- Tonnage reconciliation
- Grade reconciliation
- Identify discrepancies (e.g., void spaces, overbreak)
- **Remnant resource calculation**
- Filter MINED = 0 for remaining resources
- Exclude sterilized areas
- Include stockpiles separately
- **Version control for MINED blocks**
- Date stamp for each update
- Historical tracking of depletion
- Archive previous states

#### Define search parameters
- Search ellipsoid (ranges X, Y, Z)
- Ellipsoid rotation
- Minimum number of samples
- Maximum number of samples
- Maximum per drillhole
- Number of octants
- Block discretization
- **Neighborhood analysis**: test different configurations
- Validate search radius adequacy
- Check sample distribution within search
- **Search ellipse optimization**: multiple pass strategy if needed

### Estimation

#### Define estimation method
- Ordinary Kriging (most common)
- Inverse Distance (ID2, ID3)
- Nearest Neighbor (for classification check)
- Multiple Indicator Kriging (if needed)
- Document method selection rationale

#### nverse Distance
- ID² or ID³ commonly used
- Compare with kriging as validation
- Simpler but less optimal
- Document power parameter

#### Ordinary kriging
- Industry standard for resource estimation
- Honors variogram model
- Provides estimation variance
- Unbiased estimates

#### Define estimation parameters
- Search ellipsoid dimensions (X, Y, Z)
- Rotation (match variogram anisotropy)
- Min/max samples
- Max samples per hole
- Octant requirements
- Discretization points

#### Comparison with previous update; check for substantial differences
- Compare estimation parameters
- Search radii changes
- Sample requirements changes
- Document reasons for any changes

#### Perform Kriging Neighborhood Analysis (KNA) to define the search parameters
- Analyze block estimation quality vs search parameters
- Test different search sizes
- Optimize min/max samples
- Balance between smoothing and local detail
- Document KNA results

#### Search ellipses should honor the anisotropy ratios from variography/geometry
- Major axis = variogram range (major direction)
- Semi-major axis = variogram range (semi-major)
- Minor axis = variogram range (minor)
- Rotation matches geological trends
- Document ellipsoid parameters

#### Search ellipse size should be standardized and use logical ranges
- Not necessarily full variogram range
- Often 50-75% of variogram range for tighter estimation
- Consistent across domains (unless justified)
- Document rationale

#### Check for substantial differences between multiple grade shells in polymetallic deposit
- How reflects geology (e.g., Zn vs Pb continuity in VMS)
- Correlated elements should have similar search parameters
- Document differences and geological basis

#### Look for "balance" in estimation passes (% of blocks estimated in each pass)
- First pass: majority of blocks (>70% ideal)
- Second pass: moderate (10-25%)
- Third pass: minimal (<10%)
- High % in later passes indicates problems

#### Always estimate in parent cell
- More stable estimates
- Avoid sub-block artifacts
- Classification also in parent cell

#### Use soft boundaries sparingly and with caution
- Ensure correct composites are used
- Risk of population mixing
- Hard boundaries preferred unless gradational
- Document soft boundary justification

#### Validate estimation parameters and results
- Check for estimation artifacts
- Validate against composites
- Swath plots for drift
- Statistical checks

#### Look for negative estimates and non-estimated blocks
- If proportions are too large, may require review of estimation parameters
- Negative values indicate issues (re-estimate)
- Non-estimated blocks: check search parameters
- Typical: <1% negative, <5% non-estimated

#### Basic statistics (raw assays vs composites vs declustered composites vs blocks)
- Compare mean, variance, CV at each stage
- Should be similar (within reason)
- Large changes indicate issues
- Document statistical progression

#### Swath plots (Nearest Neighbor estimates vs composites vs blocks)
- Trend analysis in X, Y, Z directions
- Check for conditional bias
- NN should match composites closely
- Kriging may smooth slightly
- Document acceptable deviations

#### Assays vs composites vs block histograms
- Should have similar shape and distribution
- Kriging smooths (reduces CV)
- Check for modes, skewness
- Especially around cutoff grade area
- Validate grade populations preserved

#### Ordinary Kriging (OK)
- Execute estimation
- Estimate average grade
- Estimate kriging variance
- Number of samples used
- Average distance of samples

### Estimation validation
#### Pareto Principle (80/20 Rule) for validation**
- Focus on what matters most first
- Validate high-grade/high-tonnage areas before low-grade periphery
- Prioritize domains with most contained metal
- Check critical zones (e.g., active mining areas) first
- 20% of blocks often contain 80% of metal - validate these first!
- 
#### Validation priority hierarchy**:
- High-grade core zones (most metal)
- Measured/Indicated resources (reportable)
- Active mining areas (immediate impact)
- Historical problem areas (known issues)
- Peripheral/low-grade areas (less critical)

### Visual Validation

#### Load each wireframe and the corresponding set of composites
- Visual check in 3D
- Composites align with wireframes
- No orphan composites outside wireframes
- Wireframe tag matches composite domain tag

#### Confirm the correct composites are used
- Correct composite length
- Correct domain filtering
- Capped composites (if applicable)
- No raw assays mixed in

#### Confirm the correct element is being used
- Element name correct (Au not Au_ppm)
- Units consistent (g/t, %, ppm)
- Check field names in software

#### Confirm there are no unsampled intervals inside wireframe without composites
- Unless absent for a known reason (lost core, etc.)
- Account for all drillhole intersections
- Flag anomalies for investigation

#### Look at the composite grades and block grades using the same color scale
- Visual comparison of grade distribution
- Block model should reflect composite patterns
- Identify smoothing effects
- Check for estimation artifacts

#### View data in 3D, plan and section (multiple different slices)
- **Minimum 5 sections per direction** (N-S, E-W, vertical)
- Multiple plan views at different elevations
- 3D rotation for spatial understanding
- Document section locations

#### Compare that block grades for all estimation methods are similar
- OK vs ID vs NN comparison
- Should have similar patterns
- Document differences and reasons
- Use for method validation

#### Look at blocks and composites together using various cutoffs
- Example at right above 5% Zn
- Check grade continuity
- Validate high-grade zones captured
- Edge effects assessment

#### Look for artefacts
- Geometric artifacts from search ellipse
- Edge effects at domain boundaries
- Unexpected grade patterns
- Isolated high/low grade blocks

#### Ensure there are no abrupt, unintended changes in grade
- Gradual transitions expected
- Abrupt changes should match geology
- Check for estimation errors
- Validate against composites

#### Ensure all blocks are estimated (even if not part of resource statement)
- All blocks inside model extents
- Air blocks can be set to zero
- Waste blocks estimated or flagged
- Document non-estimated blocks (if any)

### Statistical validation
#### Statistical validation
- Swath plots (X, Y, Z)
- Compare composites vs blocks
- Visual validation (sections)
- Variance check
- Slope of regression
- Q-Q plots
#### Scatter plot: block grade vs mean of samples inside block**
- Calculate average of composites within each block
- Plot block estimate vs composite mean (1:1 line)
- Check for conditional bias
- Analyze regression statistics (R², slope, intercept)
#### Validate element correlations** (samples vs blocks)
- Compare correlation matrix: composites vs block model
- Ensure block estimates honor sample correlations
- Check correlation preservation for all element pairs
- Document correlation validation results
#### Delta script: compare current model vs previous model**
- Calculate grade differences (current - previous)
- Generate difference maps and sections
- Identify areas of significant change
- Quantify tonnage and grade reconciliation
- Document reasons for changes

### Complementary analysis
#### Complementary analysis
- Multiple Indicator Kriging (if applicable)
- Conditional simulation (for uncertainty)
- Nearest neighbour (for comparison)
#### Co-kriging**: for correlated elements (if applicable)
- Use primary and secondary variables
- Leverage element correlations
#### Block support adjustment**: if clustering exists
- Apply change of support models if needed

---

## Resource Classification

### Define mathematical criteria, Consider multi-factor criteria
#### Listed earlier in this document:
- Data quality
- Availability of density information
- Geological continuity
- Search neighborhood
- Number of samples and/or DDH
- Drillhole spacing and extrapolation
- Variogram range
- Kriging variance
- Geometallurgy penalty
- Quantitative criteria based on estimation metadata
- Distance to samples
- Document all criteria mathematically


#### Data quality
- Sample recovery
- QAQC results
- Drilling accuracy
- Geological logging quality

#### Availability of density information
- Measured density preferred
- Assumed density acceptable for lower categories
- Impact on tonnage confidence

#### Geological continuity
- Well-understood geology = higher confidence
- Complex geology = downgrade
- Structural disruption impact

#### Search neighborhood
- Samples within search ellipse
- Distribution around block
- Octant requirements

#### Number of samples and/or DDH used to estimate a block
- Minimum thresholds per category
- Independent drillholes (not just samples)

#### Drillhole spacing and extrapolation
- Measured: tight spacing, minimal extrapolation
- Indicated: moderate spacing
- Inferred: wide spacing or extrapolation

#### Variogram range
- Blocks within variogram range = higher confidence
- Beyond range = lower confidence

#### Kriging variance
- Low variance = higher confidence
- Relative kriging variance thresholds

#### Geometallurgy penalty
- Metallurgical data availability
- Recovery confidence
- Processing risk

#### Blocks should be classified in parent cell
- Not in sub-blocks
- More stable classification
- Consistent with reporting

#### Inferred/Mineral Potential blocks should not be in contact with Measured blocks
- Logical spatial progression
- Measured → Indicated → Inferred
- Avoid "spotted dog" pattern

#### Criteria should be documented and reproducible
- All formulas documented
- Thresholds justified
- Independent verification possible

#### Smoothing with manually drawn wireframes
- Review mathematical classification
- Apply geological judgment
- Smooth transitions
- Downgrade where needed
- Validate tonnage impact (<10% change)

#### Downgrade of blocks with uncertainty around mining voids, data quality, etc.
- Wholesale downgrade for critical issues
- Areas near old workings
- Poor data quality zones
- High geological complexity
- Document downgrade areas and rationale

#### Geometric criteria
- Distance to samples
- Typical thresholds: <50m Measured, 50-150m Indicated, >150m Inferred
- Adjust based on drill spacing and confidence
- Number of samples
- Minimum samples: 12-16 for Measured, 8-12 for Indicated, 4+ for Inferred
- Number of drillholes
- Minimum holes: 3+ for Measured, 2+ for Indicated, 1+ for Inferred
- Ensures data from independent sources
- Spatial distribution (octants)
- Octant requirements: 3+ octants for higher categories
- Minimum samples per octant: 1-2
- Ensures geometric distribution around block
- Sampling density
- Samples per unit volume or per block
- Drill spacing analysis: closer spacing = higher confidence
- **Drill hole spacing thresholds**
- Measured: tight spacing (25-50m typical)
- Indicated: moderate spacing (50-100m)
- Inferred: wide spacing (>100m)
- Adjust for deposit continuity and complexity

#### Geostatistical criteria
- Kriging variance
- Thresholds: low variance = higher confidence
- Normalize by data variance for comparison
- Slope of regression
- From swath plots or QQ plots
- Ideal = 1.0, acceptable >0.7 for Measured, >0.5 for Indicated
- Indicates conditional bias
- Kriging efficiency
- KE = 1 - (kriging variance / data variance)
- Higher KE = better estimation quality
- Typical: >0.5 for Measured, >0.3 for Indicated
- Coefficient of variation
- Local CV vs global CV
- Lower local CV = more confidence
- **Relative kriging variance** (important!)
- RKV = kriging variance / block variance
- Thresholds: <0.15 Measured, 0.15-0.30 Indicated, >0.30 Inferred
- **Kriging Neighborhood Analysis (KNA)**
- Number of samples used per block
- Distribution of samples around blocks
- Search pass analysis (1st pass vs 2nd pass blocks)

#### Geological criteria
- Geological continuity
- Well-defined geological boundaries
- Consistent mineralization style
- Predictable geometry
- Structural complexity
- Simple structures = higher confidence
- Faulting and folding impact
- Discontinuities and offsets
- Domain confidence
- Quality of geological interpretation
- Density of geological logging
- Consistency between geologists
- Data quality
- Sample recovery (>90% good, 80-90% acceptable, <80% poor)
- Drilling accuracy and deviation
- Analytical quality (QAQC results)
- **Geological model confidence levels**
- High confidence: well-drilled, understood geology
- Moderate confidence: adequate data, some interpretation
- Low confidence: sparse data, complex geology
- Document confidence by area/domain

#### Apply classification
- Define thresholds for Measured
- Define thresholds for Indicated
- Define thresholds for Inferred
- Apply combined rules
- Validate spatial coherence
- **Alternative: 15% uncertainty rule**
- Measured: <15% uncertainty over 3 months production
- Indicated: <15% uncertainty over 1 year production
- Inferred: remainder (>15% uncertainty)
- Calculate uncertainty metrics for time-based classification
- **Multi-factor criteria approach**
- Data quality
- Availability of density information
- Geological continuity
- Search neighborhood
- Number of samples and/or DDH used to estimate a block
- Drillhole spacing and extrapolation
- Variogram range
- Kriging variance
- Geometallurgy penalty (if applicable)
#### STEP 1: RESCAT MATH (Mathematical Classification)**
- Perform manipulations in macro or LF Edge calculations
- Combine different confidence criteria with AND logic
#### Example classification formula:**
- **Criteria 1**: Distance to drillhole <=40m
- **Criteria 2**: Number of samples >=8
- **Criteria 3**: Number of drillholes >=4
- **Criteria 4**: Number of DDH within search area (40m-80m) = specific range
- **Measured (3)**: If [Distance <=40] AND [Samples >=8] AND [DDH >=4] AND [DDH in 40-80m] <= 3
- **Indicated (2)**: If [Distance <=75] AND [Samples >=14] AND [DDH >=3] AND [DDH in 40-80m] <= 2
- **Inferred (1)**: If [Distance <=125] AND [Samples >=8] AND [DDH >=2] AND [DDH in 40-80m] <= 3
- **Non-resource (0)**: Otherwise (blocks not meeting minimum criteria)
#### more items
- Maximum drillhole distance is critical (e.g., max/hole is 5)
- Non-resource domains assigned to 0
- Document all threshold values and rationale
- **Pass/fail analysis**: blocks passing each criterion
- Generate criterion compliance maps
- Quantify % of blocks per category per criterion
- **Classification in parent cell**
- Classify at parent block level (not sub-blocks)
- More stable and representative
- **Spatial separation rules**
- Inferred/Mineral Potential blocks should NOT be in contact with Measured blocks
- Ensure logical spatial progression: Measured → Indicated → Inferred
- Avoid "spotted dog" classification pattern
- **Criteria documentation**
- All criteria must be documented and reproducible
- Mathematical formulas for each criterion
- Threshold justification

### STEP 2: Convert to categorical
#### Convert RESCAT MATH output to categorical values**
- [RESCAT MATH (2)] = 1 → 'Measured'
- [RESCAT MATH (2)] = 2 → 'Indicated'
- [RESCAT MATH (2)] = 3 → 'Inferred'
- [RESCAT MATH (2)] = 4 → 'Potential' (or 'Mineral Potential')
- Otherwise → '0' (Non-resource)
- **Create discrete color code using standard RESCAT colors**
#### Standard color scheme*
- 🟥 **Red**: Measured (highest confidence)
- 🟨 **Yellow**: Indicated (moderate confidence)
- 🟩 **Green**: Inferred (lower confidence)
- 🟦 **Blue**: Mineral Potential (exploration target)
- Apply consistent color coding across all visualizations
- Use for plans, sections, and 3D views
#### Add contour lines if necessary
- Boundary lines between classification categories
- Highlight transitions between Measured/Indicated/Inferred
- Useful for presentations and reporting clarity
- Black or white contour lines depending on background
- Document color scheme in reporting

#### Review and adjustments
- Check isolated enclaves
- **Visual validation with multiple sections**
- Create **minimum 5 sections per direction** (N-S, E-W, vertical)
- Review mathematical classification BEFORE smoothing
- Review classification AFTER smoothing
- **Always compare both side-by-side**
- Plot drillholes on sections
- Validate classification adherence to drill spacing
- Check for artifacts and isolated blocks
- Document section locations for reproducibility
- **Manual smoothing with wireframes**
- Draw classification wireframes manually
- Review distribution of blocks estimated by each search pass
- Refine estimation parameters (search ellipse size, octants, etc.)
- Apply common sense to the output
- **Why smooth?**
- Relying solely on estimation passes produces artifacts
- Single block of Measured in "sea" of Indicated (not representative)
- Measured between two drillholes, but not along actual data
- Forces geologist to review block distribution and refine parameters
#### Allows downgrade based on:
- Historical mining uncertainty
- Interpretation uncertainty  
- Extrapolation beyond reasonable limits
#### Common practice widespread in mining industry
- Avoids "spotted dog" classification pattern
- Smooth transitions
- **Visual inspection**: review sections showing categories
- Display drillhole traces and collar locations
- Overlay category boundaries
- Check spatial logic of classifications
- **Transition analysis**: verify smooth category boundaries
- Validate tonnages before smoothing
- Validate tonnages after smoothing
- Calculate difference in % (before vs after)
- **Typical smoothing impact**: should be <10% tonnage change
- Document all smoothing adjustments and rationale
- **Downgrade considerations**
- Mining voids and data quality issues
- Areas with high uncertainty
- Structural complexity zones
- Extrapolation areas
- **PUNISHMENT: Wholesale downgrade for critical shortcomings**
- Apply wholesale downgrade to blocks with fatal data quality flaws
#### *Critical shortcomings requiring downgrade:**
- No downhole surveys (assume vertical may be incorrect)
- No QAQC data (no quality assurance/quality control)
- Data digitized from paper maps (high uncertainty)
- Drill hole inclination digitized from paper material
- High geological complexity (e.g., due to folds, faults)
- Low sample recovery (<80%)
- Inconsistent geological logging between geologists
- Missing density information
- Legacy data with unknown reliability
#### Example: East Zhairem deposit
- No Indicated or Measured resources declared because:
- Database digitized from papers by Kazzinc Exploration geologists
- Drill holes inclination also digitized from paper material
- No Qa/Qc data available
- High complexity due to folds
- Result: All material classified as Inferred or Mineral Potential only
#### Downgrade documentation
- Document specific reason for each downgrade area
- Quantify impact on tonnage and grade
- Create downgrade area wireframes/polygons
- Include in assumptions register
- **Sensitivity analysis**: test different threshold values
- Document impact of threshold changes
- Validate with geological team
- Document criteria

### Final comments and workflow notes
#### Use at least 2 criteria for RESCAT determination
- Examples: DH spacing + geological continuity + data quality
- Multiple criteria provide robustness
- Avoid relying on single metric
- **Avoid radical changes without justification**
- If a previous model exists, do not produce radical changes in the distribution between classes without proper justification
- Document reasons for any significant category shifts
- Reconcile differences with previous estimates
- Stakeholder communication for material changes
- **Consistency and reproducibility**
- Maintain consistent methodology across updates
- Document all assumptions and decisions
- Enable independent verification
- Archive all supporting data and calculations

---

## Report

### Cut-off grade determination and RPEEE
#### Reasonable Prospects for Eventual Economic Extraction (RPEEE)**
- Define what constitutes reportable resource
- Establish economic viability criteria
- Document extraction method assumptions (open pit/underground)
- **Cut-off grade derivation**
- Cost assumptions: mining, processing, G&A
- Metal prices: current, 3-year average, long-term consensus
- Metallurgical recovery assumptions
- By-product credits (if applicable)
- **Cut-off grade formula documentation**
- Breakeven grade calculation
- Formula: COG = (Mining cost + Processing cost + G&A) / (Price × Recovery)
- Sensitivity to price and cost changes
- **Cut-off justification and defense**
- Comparison with industry benchmarks
- Historical performance (if production exists)
- Peer deposit comparison
- External consultant validation (if available)
- **Reportability criteria**
- Minimum mining width/thickness
- Maximum internal dilution
- Maximum depth/elevation constraints
- Geotechnical limitations
- Environmental/regulatory constraints
- Infrastructure access requirements
- **What is NOT considered resource**
- Material below cut-off grade
- Material outside RPEEE envelope
- Isolated blocks not meeting continuity
- Areas with fatal flaws (sterilized ground)
- Document exclusion rationale
- **Economic assumptions register**
- All cost inputs with sources
- Metal price sources and justification
- Recovery assumptions and test work basis
- Discount rates (if NPV-based COG)
- Exchange rates
- Date of assumptions

### Final Resource Tabulation

#### Decision on cut-off grade for resource calculation
- Formulae used (ZnEq, density, NSR)
- Economic parameters documented
- Breakeven calculation shown
- Sensitivity analysis performed
- Document rationale

#### Comparison with previous update
- Tonnage comparison by category
- Grade comparison by element
- Metal comparison
- Explain material differences (>10%)

#### Reconciliation (for Year End or considerable differences in resources)
- If major changes: detailed reconciliation required
- Waterfall chart showing changes
- Attribution of changes (drilling, depletion, re-interp, etc.)
- Management presentation

#### PowerPoint presentation with main criteria and parameters used
- Executive summary slides
- Methodology overview
- Key parameters table
- Resource statement
- Comparison with previous
- Recommendations

#### Written report for Year End update
- Full technical report
- Table 1 (JORC/NI 43-101) compliance
- Audit-ready documentation
- All sections complete

#### Any major deviations from Year End expectations should be documented and explained
- Major changes flagged early
- E.g., major change in interpretation
- Downgrade for QAQC errors
- Depletion reconciliation issues
- Stakeholder communication

#### Report should include dates for database closure and depletion solids
- Database freeze date
- Depletion update date (as-mined survey date)
- Model completion date
- Report issue date
- Version control

#### Prepare resource tables
- Tonnage by category (Measured, Indicated, Inferred)
- Average grade by category
- Contained metal by category
- Apply cut-off grades
- Report by geological domain
- Cut-off sensitivity analysis
- **Breakdown by oxidation state**: oxide/transition/fresh (if applicable)
- **Metal equivalents**: if multiple PAY elements
- Calculate metal equivalent formulas
- Document metal prices and recoveries used

#### Graphics and visualizations
- Grade-tonnage curves
- Location maps
- Representative sections
- Plans by level
- 3D model visualization
- **Drill hole spacing analysis**: density maps
- Heat maps showing sample density
- **Strip ratio analysis**: waste-to-ore ratio (if open pit)

#### Quality metrics
- Total number of samples
- Sampling density (m/ton)
- Validation statistics
- Drift analysis
- **Drill hole spacing statistics**: average, min, max

#### Comparisons
- Current vs previous resources
- Reconciliation (if production exists)
- Method comparison
- **Comparison with global benchmarks**: for deposit type
- Industry averages for similar deposits
- Typical grade ranges and tonnages
- **Waterfall chart: current vs previous model**
- Start with previous model total (tonnage/metal)
#### Show changes step-by-step:
- (+/-) New drilling added
- (+/-) Depletion (MINED blocks removed)
- (+/-) Re-interpretation (domain changes)
- (+/-) Grade re-estimation (methodology changes)
- (+/-) Classification changes
- (+/-) Cut-off grade changes
- (+/-) RPEEE envelope changes
- End with current model total
- Quantify each component's impact
- Visualize as waterfall/bridge chart
- **Tonnage reconciliation breakdown**
- By category (Measured/Indicated/Inferred)
- By domain/lithology
- By area/zone
- **Grade reconciliation breakdown**
- Average grade changes per element
- Identify areas of significant change
- Statistical significance testing
- **Metal reconciliation**
- Contained metal comparison
- % change analysis
- Variance attribution
- **Change attribution matrix**
- Table showing impact of each change driver
- Rank changes by magnitude
- Document reasons for each change

#### Technical documentation
- Methodology used
- Estimation parameters
- Assumptions and limitations
- Classification criteria
- Uncertainties and risks
- Code compliance (JORC, NI 43-101, SAMREC)
- **Assumptions register**: document all key assumptions
- **Risk and uncertainty section**: identify sources
- Data quality risks
- Geological interpretation risks
- Estimation parameter uncertainty
- Classification confidence levels

#### Versioning and change log
- Version control for model updates
- Document all changes from previous version
- Rationale for parameter changes
- Impact assessment of modifications
- Sign-off and approval tracking

### Software and tools documentation
#### Software used and versions**
- Database management: Accula, DataShed, SQL, etc.
- Geological modelling: Leapfrog, Vulcan, Surpac, Micromine
- Geostatistics: Supervisor, Isatis, SGeMS, GS3M
- Visualization: Paraview, Leapfrog Viewer
- Custom scripts: Python, R versions and libraries
- **Data traceability**
- Original data sources and dates
- Data transformations applied
- Intermediate file formats
- Final output formats
- **Reproducibility**
- Parameter files archived
- Script version control (Git repositories)
- Seed values for stochastic processes
- Computation environment documentation
- **Quality assurance checks**
- Independent verification of calculations
- Peer review process
- External audit trail
- **File naming conventions**
- Consistent naming scheme
- Version numbers in filenames
- Date stamps
- Descriptive tags

### Audit compliance documentation
#### Table 1 (JORC/NI 43-101 checklist)**: complete all sections
- Section 1: Sampling Techniques and Data
- Section 2: Reporting of Exploration Results
- Section 3: Estimation and Reporting of Mineral Resources
- Section 4: Estimation and Reporting of Ore Reserves (if applicable)
- Cross-reference to report sections for each item
- **Audit ruler/scorecard**: compliance tracking
- Rate compliance level for each criterion
- Identify gaps and areas for improvement
- Action items for non-compliant areas
- Timeline for addressing deficiencies
- **Audit trail documentation**
- Data lineage and transformations
- Decision rationale for all key parameters
- Peer review sign-offs
- External audit readiness

### Archive Relevant Files

#### Composites
- Final composite database
- Composite validation report
- Before/after capping comparisons
- File format: CSV, database export

#### Wireframes (in Datamine/Surpac/.dxf formats)
- Leapfrog format is NOT accepted in other software
- Export to standard formats: .dxf, .00t, .dm
- All domain wireframes
- Validation wireframes
- Version control

#### Leapfrog, Datamine, Supervisor and/or Isatis projects
- Complete project files
- All intermediate steps preserved
- Parameter files
- Scripts and macros
- Version documented

#### Block model (in Datamine/.csv formats)
- Leapfrog format is NOT accepted in other software
- Export to: .dm (Datamine), .csv, .txt
- All attributes included
- Metadata documented

#### Archive scripts, macros, journal files (required for reproducibility)
- All Python/R scripts
- Datamine macros
- Leapfrog Edge calculations
- Parameter files
- Version control (Git commits if applicable)
- README documentation

#### **Refer to document collection ID1867 for naming convention and adding guide**
- Follow corporate naming standards
- Version numbering scheme
- Date stamps
- Project codes
- Consistent file structure

### Transfer to Engineering

#### Desirable format
- Discuss format requirements with engineering
- Software compatibility
- Preferred coordinate system
- Block size requirements

#### Required attributes
- Engineering specifies what they need
- Minimum: grades, density, classification, domains
- Optional: geomet, recovery, NSR
- MINED status (if operating mine)

#### "Clean" version
- Single grade column for each grade variable
- RESCAT (classification)
- MINED status
- Density
- **Do not keep kriging passes, number of samples used, kriging variance, etc.**
- Simplified for mine planning use

#### Models used for possible open pit extraction require reblocking to the SMU
- Selective Mining Unit size
- Discuss with mining engineer
- Reblock from detailed model to SMU
- Validate reblocking (metal conservation!)


### Deliverables
#### Technical report** (audit style format)
- Executive summary
- Data quality assessment
- Methodology and parameters
- Validation results
- Resource statement
- Compliance sections
- Use provided audit report template
- **PowerPoint presentation** (findings summary)
- Key findings and highlights
- Resource statement summary
- Comparison with previous estimates
- Risk assessment
- Recommendations
- Use provided presentation template
- Management-level summary (non-technical)

#### Annexes
- Complete descriptive statistics
- Modeled variograms
- Kriging parameters
- Cross-validation
- Listing of drillholes used
#### Project knowledge summary:
- Drilling type (UG/Surface)
- Deposit type characterization
- PAY elements identified
- Penalty elements identified
- Horsetail plots and deviation analysis
- Dogleg severity statistics
- Spatial clustering patterns
- Element correlations and associations
