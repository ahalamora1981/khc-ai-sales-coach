# McKinsey Consulting Presentation Style Guide

> Reference document for generating PPTs in McKinsey's signature consulting aesthetic.

---

## 1. Design Philosophy

McKinsey presentations are **argument-driven, not decoration-driven**. Every element exists to advance a point. The style is defined by:

- **Ruthless clarity** — if it doesn't serve the argument, remove it
- **Data authority** — numbers speak, visuals support
- **Executive readability** — scannable in 30 seconds, deep on closer look

---

## 2. Color Palette

### Primary Palette (Use 90% of the time)

| Role | HEX | Usage |
|------|-----|-------|
| **McKinsey Blue** | `#003366` | Primary color — titles, key sections, headers |
| **White** | `#FFFFFF` | Page background, text on dark |
| **Light Gray** | `#F5F5F5` | Card backgrounds, subtle panels |
| **Medium Gray** | `#666666` | Body text, captions |
| **Dark Gray** | `#333333` | Secondary text, borders |

### Accent Palette (Use sparingly — max 1 per deck)

| Role | HEX | Usage |
|------|-----|-------|
| **Accent Blue** | `#0066CC` | Data highlights, call-to-action |
| **Accent Teal** | `#00857C` | Alternative accent (healthcare/sustainability) |
| **Accent Red** | `#CC0000` | Risk, warning, critical attention |

### Color Rules

- **60-30-10 rule**: 60% white/gray, 30% navy, 10% accent
- **Maximum 3 colors per page** (including neutrals)
- **No gradients** — flat color only
- **No decorative color** — color must have purpose

---

## 3. Typography

### Font Stack

| Role | Font | Weight | Fallback |
|------|------|--------|----------|
| **Title (Action Title)** | Georgia | Bold | Times New Roman, serif |
| **Subtitle** | Arial | SemiBold | Helvetica, sans-serif |
| **Body** | Arial | Regular | Helvetica, sans-serif |
| **Data/Numbers** | Arial | Bold | Helvetica, sans-serif |
| **Caption/Source** | Arial | Regular | Helvetica, sans-serif |

> **Note**: McKinsey uses custom typefaces (McKinsey Sans). For PPT-safe implementation, Georgia (titles) + Arial (body) captures the serif/sans contrast.

### Font Sizes (Baseline: 18px body)

| Level | Size | Weight | Usage |
|-------|------|--------|-------|
| **Action Title** | 28-32px | Bold | Top of slide — THE conclusion |
| **Section Title** | 22-24px | Bold | Sub-sections within slide |
| **Body** | 16-18px | Regular | Main content |
| **Data Labels** | 14-16px | Bold | Chart labels, KPI numbers |
| **Caption/Source** | 11-12px | Regular | Footnotes, source attribution |
| **Page Number** | 10px | Regular | Bottom right |

### Typography Rules

- **Action title IS the insight** — not a topic label
- **Sentence case** for titles (not ALL CAPS)
- **Bold key numbers** within body text
- **Source attribution** on every data slide (bottom left)

---

## 4. Layout Structure

### Page Template

```
┌─────────────────────────────────────────────────────────────┐
│  ACTION TITLE (the conclusion)                    [Page #] │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  [Content Area]                                             │
│  - Charts, data, frameworks                                 │
│  - 3-5 key points max                                       │
│  - Clear visual hierarchy                                   │
│                                                             │
│                                                             │
│                                                             │
│  Source: [attribution]                             [Page #] │
└─────────────────────────────────────────────────────────────┘
```

### Grid System

- **Margins**: 60px left/right, 50px top/bottom
- **Content width**: 1160px (on 1280px canvas)
- **Column gutters**: 24-32px
- **Vertical rhythm**: 20-24px between elements

### Layout Patterns

| Pattern | When to Use |
|---------|-------------|
| **Single column** | Data charts, key insight slides |
| **Two-column (50/50)** | Comparisons, before/after |
| **Two-column (40/60)** | Chart + commentary |
| **Three-column** | Feature comparisons, parallel points |
| **Matrix (2×2)** | Strategic frameworks, quadrants |
| **Full-bleed chart** | Data-dense analysis |

---

## 5. Visual Elements

### Lines & Borders

| Element | Style | Usage |
|---------|-------|-------|
| **Title underline** | 2px solid navy | Below action title |
| **Section divider** | 1px solid light gray | Between content sections |
| **Table borders** | 1px solid light gray | Horizontal only (no vertical) |
| **Card border** | None | Use background color instead |

### Charts (McKinsey Style)

- **Minimal gridlines** — horizontal only, light gray, dashed
- **No chart borders** — clean edges
- **Direct labeling** — labels on data points, not in legend
- **Source below** — "Source: [name], [year]"
- **Accent on key data** — highlight the insight color

### Icons (When Used)

- **Style**: Simple, geometric, single-weight
- **Color**: Navy or accent (never multi-color)
- **Size**: 24-32px
- **Usage**: Sparingly — only to reinforce a point

### Tables (McKinsey Style)

- **Header row**: Navy background, white text
- **Data rows**: White background, alternating light gray
- **Borders**: Horizontal only (top/bottom of header, bottom of last row)
- **Alignment**: Left-aligned text, right-aligned numbers
- **No vertical lines** — ever

---

## 6. Content Principles

### The Pyramid Principle

```
                    [CONCLUSION]
                         │
          ┌──────────────┼──────────────┐
          │              │              │
      [Argument 1]  [Argument 2]  [Argument 3]
          │              │              │
       [Data]         [Data]         [Data]
```

- **Conclusion first** — state the answer, then support it
- **MECE** — arguments are Mutually Exclusive, Collectively Exhaustive
- **Every number has a comparison** — "up 20% YoY" not just "20%"

### Action Titles

| ❌ Topic Title | ✅ Action Title |
|---------------|-----------------|
| "Market Overview" | "China market grows 7% YoY to ¥5T" |
| "Challenges" | "Three barriers block scaled deployment" |
| "Our Solution" | "AI coach reduces ramp-up time by 50%" |
| "Financials" | "NPV of ¥12M with 18-month payback" |

### Data Presentation

- **Always compare** — vs prior period, vs benchmark, vs target
- **Round smartly** — "¥4.98B" not "¥4,981,234,567"
- **Highlight the insight** — use accent color on the key data point
- **One chart = one message** — don't overload

---

## 7. Slide Types

### 1. Title Slide

- Company logo (top left or center)
- Project title (centered, large)
- Date, confidentiality notice
- Presenter name(s)

### 2. Section Divider

- Section number + title (centered)
- Minimal design — whitespace dominant
- Navy accent bar or rule

### 3. Insight Slide

- Action title = the conclusion
- 3-5 supporting arguments
- Data/evidence for each
- Source attribution

### 4. Data Slide

- Chart as primary visual
- Title states the insight
- Direct labels on data
- Source below chart

### 5. Framework Slide

- 2×2 matrix or process flow
- Clear labels
- Color-coded quadrants/steps
- Minimal decoration

### 6. Recommendation Slide

- Clear "We recommend..." statement
- 3-5 action items
- Owner/timeline for each
- Expected impact

---

## 8. What NOT to Do

### Avoid

- ❌ Gradients, shadows, 3D effects
- ❌ Decorative images or clip art
- ❌ More than 3 colors per slide
- ❌ Bullet points without insight
- ❌ Charts with legends (use direct labels)
- ❌ Vertical table borders
- ❌ ALL CAPS titles
- ❌ Emojis or informal icons
- ❌ "Slide title: Topic" format

### Red Flags

- Title doesn't state a conclusion
- Data without comparison
- More than 6 bullet points
- Chart without source
- Text-heavy slides (>50 words)

---

## 9. Example Color Application

### Slide with Data Chart

```
Background: #FFFFFF (white)
Title: #003366 (navy), 28px, Bold
Chart bars: #003366 (navy)
Highlight bar: #0066CC (accent blue)
Gridlines: #E0E0E0 (light gray), dashed
Axis labels: #666666 (medium gray)
Data labels: #333333 (dark gray), Bold
Source text: #999999 (light gray), 11px
Page number: #999999, 10px
```

### Slide with Framework

```
Background: #FFFFFF (white)
Title: #003366 (navy), 28px, Bold
Framework boxes: #F5F5F5 (light gray) background
Box borders: #E0E0E0 (light gray)
Box titles: #003366 (navy), Bold
Box body: #333333 (dark gray)
Accent elements: #0066CC (accent blue)
```

---

## 10. SVG Implementation Notes

### viewBox

Standard: `0 0 1280 720` (16:9)

### Common Elements

```xml
<!-- Title underline -->
<rect x="60" y="85" width="100" height="2" fill="#003366"/>

<!-- Section divider -->
<line x1="60" y1="120" x2="1220" y2="120" stroke="#E0E0E0" stroke-width="1"/>

<!-- Card background -->
<rect x="60" y="140" width="540" height="200" fill="#F5F5F5"/>

<!-- Chart gridline -->
<line x1="100" y1="300" x2="1100" y2="300" stroke="#E0E0E0" stroke-width="0.5" stroke-dasharray="4,4"/>

<!-- Source text -->
<text x="60" y="680" font-family="Arial, sans-serif" font-size="11" fill="#999996">Source: Industry Research, 2026</text>
```

---

## 11. Comparison: Generic vs McKinsey Style

| Element | Generic Corporate | McKinsey |
|---------|-------------------|----------|
| Title | "Q3 Performance Review" | "Q3 revenue exceeds target by 12%" |
| Colors | 4-5 colors + gradients | 2-3 flat colors |
| Charts | Gridlines, legends, borders | Minimal, direct labels, no borders |
| Tables | Vertical + horizontal borders | Horizontal only |
| Icons | Colorful, decorative | Simple, navy, purposeful |
| Text | Bullet-heavy, verbose | Insight-driven, concise |
| Decoration | Shadows, rounded corners | Flat, clean lines |

---

*Document version: 1.0 | Created: June 2026*
