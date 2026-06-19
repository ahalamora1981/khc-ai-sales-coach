# Solution Document

## AI-Powered Sales Coach Chatbot for KHC China

| Field | Value |
|-------|-------|
| **Document ID** | KHC-CN-AI-SOL-001 |
| **Version** | 0.1 (Draft) |
| **Date** | 18th June 2026 |
| **Author** | Infosys |
| **Status** | Draft - For Customer Review |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Understanding of Requirements](#2-understanding-of-requirements)
3. [Proposed Solution](#3-proposed-solution)
4. [Solution Architecture](#4-solution-architecture)
5. [Key Features & User Stories](#5-key-features--user-stories)
6. [Implementation Approach](#6-implementation-approach)
7. [Technology Stack](#7-technology-stack)
8. [Why Infosys](#8-why-infosys)
9. [Appendix](#9-appendix)

---

## 1. Executive Summary

Kraft Heinz China (KHC) seeks to develop an **AI-Powered Sales Coach Chatbot** to empower its field sales team in the foodservice sauce category. The solution will serve as an intelligent, always-available assistant that helps sales representatives learn product knowledge, receive personalized coaching, and make data-driven product recommendations based on restaurant menu analysis.

### Our Understanding

KHC China faces a strategic challenge: while being a global leader in ketchup, the company aims to become a leader in the Chinese sauce market. The field sales team needs better tools to:
- Learn product knowledge and sales techniques on-the-go
- Recommend appropriate KHC sauce products based on restaurant menus
- Access training materials via mobile devices rather than desktop computers

### Proposed Solution Overview

We propose an **AI-Powered Sales Coach** that functions as a personalized, mobile-first assistant. The solution differentiates through:

| Differentiator | Description |
|----------------|-------------|
| **Personal Memory** | Each user has a dedicated memory that records their experience, preferences, and learning outcomes, dynamically retrieved when needed |
| **Intelligent Menu Analysis** | Photo recognition of restaurant menus combined with taste profile analysis to recommend KHC products |
| **Contextual Learning** | Learning embedded in real sales scenarios, not passive content consumption |
| **Continuous Evolution** | The system learns and improves with each interaction |
| **Predictive Coaching** | AI proactively identifies knowledge gaps and pushes relevant content before sales visits |
| **Success Pattern Mining** | Extract and replicate successful sales patterns across the team |

### Business Outcomes

- **30%+ improvement** in sales team product knowledge
- **20%+ increase** in sauce category revenue per sales rep
- **50%+ reduction** in new hire ramp-up time
- **80%+ monthly active usage** among field sales team

---

## 2. Understanding of Requirements

### 2.1 Original Requirements

Based on the problem statement provided by KHC China Foodservice Sales team:

| # | Requirement | Original Statement |
|---|-------------|-------------------|
| 1 | Sales Coaching | "I want to have an AI chatbot to teach me how to sell KHC sauce to restaurants" |
| 2 | Self-Learning & Menu Recommendation | "AI chat robot has self-learning and recommend menu to me" |
| 3 | Product Recommendation | "I input the menu of this restaurant, and AI chat robot can recommend KHC sauce in the taste application and innovation recommendation for consumer taste" |
| 4 | Mobile Learning Coach | "I want to use my phone to learn... Just like a coach beside me" |

### 2.2 Our Interpretation

We interpret these requirements as four interconnected capabilities:

**Capability 1: AI Sales Coach**
- Real-time conversational AI that teaches sales techniques
- Product knowledge on-demand (features, benefits, applications, pricing)
- Objection handling and competitive positioning guidance
- Contextual advice based on customer type and situation

**Capability 2: Personal Memory System**
- Each user has a dedicated memory that accumulates over time
- Records: product preferences, successful recommendations, learning progress, frequently asked questions, customer feedback
- Memory is dynamically retrieved to personalize recommendations and coaching
- Memory evolves: old patterns are updated, new insights are incorporated

**Capability 3: Intelligent Menu Recommender**
- Photo-based menu recognition (primary) + text input (secondary)
- Taste profile analysis of existing menu items
- Recommendation of KHC sauce products that complement the menu
- Innovation suggestions for new menu items using KHC products
- Explanation of rationale for each recommendation

**Capability 4: Mobile Learning Hub**
- Conversational access to training materials
- Bite-sized learning modules (3-5 minute sessions)
- Scenario-based learning integrated with real sales situations
- Voice-enabled for hands-free interaction while in transit

### 2.3 Key Assumptions

| # | Assumption |
|---|------------|
| A1 | KHC Marketing team maintains three primary knowledge sources: (1) Marketing Knowledge Base with product materials and training content, (2) Sales Playbook with scripts and best practices, (3) Product Database with structured product information |
| A2 | The solution will be a standalone system without deep integration to SAP/CRM initially |
| A3 | Sales team members have company-issued smartphones or BYOD with reimbursement |
| A4 | Data residency requirements mandate deployment within mainland China |
| A5 | The solution will be delivered as a mobile application accessible via WeChat Work or Mini Program |

### 2.4 Business Context

**Market Opportunity**
- China's condiment market: ¥4,981 billion (2024), growing at 7.0% CAGR
- Foodservice channel accounts for 50% of consumption
- Compound seasonings (KHC's growth area) growing at 10.2% CAGR
- Restaurant chain penetration rate: 22% and rising

**Competitive Landscape**
- KHC is a leader in ketchup in Western markets but not in Chinese sauces
- Local competitors (Haitian, Lee Kum Kee) dominate domestic market
- AI-powered sales enablement is emerging as a differentiator in CPG industry

---

## 3. Proposed Solution

### 3.1 Solution Overview

The **KHC Sales Coach** is a mobile-first, AI-powered assistant that transforms how field sales representatives learn, prepare, and execute customer interactions. Unlike traditional training platforms that deliver static content, our solution provides **contextual, personalized, and evolving** guidance.

### 3.2 Core Innovation: Personal Memory Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      User Interaction                            │
│  (Question asked, menu analyzed, learning completed, etc.)       │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Memory Extraction Engine                       │
│  • What products did the user ask about?                         │
│  • What recommendations were accepted?                           │
│  • What learning modules were completed?                         │
│  • What customer feedback was received?                          │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Personal Memory Store                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  Product    │  │  Learning   │  │  Success    │              │
│  │  Preferences│  │  Progress   │  │  Patterns   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  Customer   │  │  Weakness   │  │  Context    │              │
│  │  Feedback   │  │  Areas      │  │  History    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Memory Update & Iteration                      │
│  • Old patterns are updated with new data                        │
│  • Confidence scores adjust based on outcomes                    │
│  • Irrelevant memories decay over time                           │
│  • New insights are incorporated continuously                    │
└─────────────────────────────────────────────────────────────────┘
```

**Memory Update Mechanism:**

| Event | Memory Action |
|-------|---------------|
| User asks about product X | Add to product interest profile |
| User accepts recommendation Y | Strengthen pattern: "Restaurant type Z → Product Y" |
| User completes learning module | Update learning progress, mark as proficient |
| Customer provides positive feedback | Reinforce recommendation approach |
| User consistently misses quiz questions | Flag as weakness area, trigger predictive coaching |
| Old recommendation pattern no longer works | Reduce confidence score, suggest alternative |

### 3.3 Innovation Highlights

#### Innovation 1: Personal Memory with Continuous Evolution

**What makes it different:**
- Not a generic AI chatbot — it's YOUR AI coach
- Learns your strengths, weaknesses, preferences, and successful patterns
- Provides increasingly personalized guidance over time
- Memory evolves: updates, strengthens, and sometimes forgets (like human memory)

**Example:**
> *A sales rep consistently struggles with objection handling for pricing. The Personal Memory detects this pattern and:*
> - *Prioritizes pricing objection training modules*
> - *Prepares tailored talking points before meetings with price-sensitive customers*
> - *Surfaces successful pricing conversations from other team members*

#### Innovation 2: Intelligent Menu Analysis

**What makes it different:**
- Photo recognition + OCR + taste profile analysis
- Not just "what products to use" but "why they fit this menu"
- Innovation suggestions for new menu items

**Workflow:**
```
Photo → OCR → Dish Recognition → Taste Analysis → KHC Product Match
                                                        ↓
                                              Innovation Suggestion
                                              (new dish ideas using KHC)
```

#### Innovation 3: Predictive Coaching

**What makes it different:**
- AI proactively identifies knowledge gaps before sales visits
- Pushes relevant content based on upcoming customer context
- Transforms reactive learning into proactive preparation

**Example:**
> *"You're visiting a Sichuan hotpot chain tomorrow. Based on your memory, you haven't worked with spicy sauce applications much. Here's a 5-minute briefing on our chili-based products and three successful case studies from similar restaurants."*

#### Innovation 4: Success Pattern Mining

**What makes it different:**
- Aggregates successful patterns across the sales team
- Identifies what works and replicates it
- Creates a living knowledge base of proven strategies

**Example:**
> *"Manager Zhang has exceeded targets for 3 consecutive months in the hotpot restaurant segment. His approach: always lead with cost-per-serving analysis, then demonstrate taste differentiation. Here's his playbook."*

#### Innovation 5: Contextual Learning

**What makes it different:**
- Learning happens in the flow of work, not in a classroom
- Content is triggered by real situations, not scheduled modules
- Knowledge is immediately applicable

**Example:**
> *A sales rep is at a restaurant and the owner mentions switching to a competitor. The AI coach instantly provides:*
> - *Competitive comparison talking points*
> - *Switching cost analysis framework*
> - *Relevant success stories from similar situations*

#### Innovation 6: Continuous Evolution

**What makes it different:**
- The system gets smarter with every interaction
- Recommendations improve based on acceptance/rejection data
- Knowledge gaps are automatically identified and addressed

### 3.4 Knowledge Sources (Assumed)

| Source | Content | Integration |
|--------|---------|-------------|
| **Marketing Knowledge Base** | Product materials, training content, brand guidelines, competitive analysis | Content ingestion pipeline |
| **Sales Playbook** | Sales scripts, objection handling, success stories, best practices | Structured content repository |
| **Product Database** | Product specs, taste profiles, applications, pricing, packaging | API or database connection |

*Note: These are assumed knowledge sources. Actual sources to be confirmed during detailed design phase.*

---

## 4. Solution Architecture

### 4.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              Mobile Client Layer                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐              │
│  │  WeChat Work    │  │  Mini Program   │  │  (Future:       │              │
│  │  Application    │  │  (Alternative)  │  │   Native App)   │              │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘              │
│           └────────────────────┼─────────────────────┘                       │
│                                │                                             │
└────────────────────────────────┼─────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              API Gateway Layer                                │
│  • Authentication (WeChat Work SSO)                                         │
│  • Rate limiting                                                            │
│  • Request routing                                                          │
│  • API versioning                                                           │
└────────────────────────────────┬────────────────────────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
        ▼                        ▼                        ▼
┌───────────────┐      ┌───────────────┐      ┌───────────────┐
│   AI/LLM      │      │   Knowledge   │      │   Memory      │
│   Service     │      │   Service     │      │   Service     │
│               │      │               │      │               │
│ • Chat engine │      │ • Content     │      │ • User memory │
│ • Menu        │      │   management  │      │ • Pattern     │
│   analysis    │      │ • Product     │      │   mining      │
│ • Predictive  │      │   lookup      │      │ • Learning    │
│   coaching    │      │ • Search      │      │   tracking    │
└───────┬───────┘      └───────┬───────┘      └───────┬───────┘
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              Data Layer                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   Vector    │  │   Relational│  │   Object    │  │   Cache     │         │
│  │   Database  │  │   Database  │  │   Storage   │  │   Layer     │         │
│  │ (Milvus)    │  │ (PostgreSQL)│  │   (OSS)     │  │  (Redis)    │         │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘         │
└─────────────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Cloud Infrastructure                               │
│                    AWS China / Alibaba Cloud (TBD)                            │
│  • Data residency within mainland China                                      │
│  • PIPL compliance                                                           │
│  • High availability (99.5% uptime)                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Component Descriptions

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Mobile Client** | WeChat Work Application / Mini Program | User interface, camera access, offline capability |
| **API Gateway** | Kong / AWS API Gateway | Authentication, routing, rate limiting |
| **AI/LLM Service** | DeepSeek (primary) / Qwen (backup) | Conversational AI, menu analysis, predictive coaching |
| **Knowledge Service** | Custom microservice | Content management, product lookup, semantic search |
| **Memory Service** | Custom microservice | User memory management, pattern mining, learning tracking |
| **Vector Database** | Milvus / Zilliz | Semantic search for knowledge base |
| **Relational Database** | PostgreSQL | User data, memory metadata, analytics |
| **Object Storage** | AWS S3 / Alibaba Cloud OSS | Training materials, images, documents |
| **Cache Layer** | Redis | Session management, frequently accessed data |

### 4.3 Data Flow

**Menu Analysis Flow:**
```
1. User captures menu photo
2. Image uploaded to API Gateway
3. OCR service extracts text
4. LLM identifies dishes and cuisine type
5. Taste profile analysis performed
6. Memory consulted for user preferences
7. KHC products matched based on taste + user history
8. Recommendations returned with rationale
```

**Predictive Coaching Flow:**
```
1. User's calendar/visit schedule checked
2. Memory analyzed for knowledge gaps related to upcoming visits
3. Relevant content identified from knowledge base
4. Personalized coaching brief generated
5. Push notification sent to user before visit
```

---

## 5. Key Features & User Stories

### 5.1 Phase 1 Features (MVP)

#### Feature 1.1: AI Sales Coach

**User Story:**
> As a field sales representative, I want to ask the AI about product details and sales techniques so that I can confidently handle customer conversations.

**Capabilities:**
- Ask questions about KHC sauce products (features, benefits, pricing, applications)
- Get sales scripts and talk tracks for different scenarios
- Receive objection handling guidance
- Access competitive comparison information

**Example Interaction:**
```
User: "The restaurant owner says Lee Kum Kee is cheaper. What should I say?"

AI Coach: "Here are three approaches:

1. Cost-per-serving analysis: 'While the upfront cost may seem lower, 
   our sauce requires 20% less per dish due to higher concentration...'

2. Taste differentiation: 'Our customers report that dishes made with 
   our sauce receive 15% better reviews on delivery platforms...'

3. Success story: 'Manager Wang faced similar objections at Golden 
   Dragon Restaurant. Here's how she handled it...'

Would you like me to elaborate on any of these approaches?"
```

#### Feature 1.2: Intelligent Menu Recommender

**User Story:**
> As a field sales representative, I want to analyze a restaurant's menu and receive KHC product recommendations so that I can propose value-added solutions.

**Capabilities:**
- Capture menu photo for automatic analysis
- Manual text input as alternative
- Dish recognition and categorization
- Taste profile analysis
- KHC product recommendations with rationale
- Innovation suggestions for new menu items

**Example Interaction:**
```
User: [Captures photo of restaurant menu]

AI Coach: "I've analyzed this Sichuan-style restaurant menu.

Current dishes: Mapo Tofu, Kung Pao Chicken, Dan Dan Noodles...

Taste Profile: Spicy (7/10), Numbing (8/10), Savory (6/10)

RECOMMENDATIONS:
1. KHC Chili Garlic Sauce - Perfect for enhancing Mapo Tofu's 
   heat profile while adding depth

2. KHC Sesame Oil - Would complement the Dan Dan Noodles with 
   authentic aroma

INNOVATION OPPORTUNITY:
Consider suggesting a 'Fusion Mapo Tofu' using our Chili Garlic 
Sauce + a touch of Italian herbs. This differentiation could 
attract younger diners while maintaining authenticity.

RATIONALE: Based on similar restaurants in this area that adopted 
fusion approaches, they saw 20% increase in average ticket size."
```

#### Feature 1.3: Voice-Enabled Interaction

**User Story:**
> As a field sales representative, I want to use voice commands so that I can interact with the AI while driving between customer visits.

**Capabilities:**
- Voice input for questions
- Voice output for responses
- Hands-free operation during transit

### 5.2 Phase 2 Features

#### Feature 2.1: Personal Memory System

**User Story:**
> As a field sales representative, I want the AI to remember my preferences, successful strategies, and learning progress so that it can provide increasingly personalized guidance.

**Capabilities:**
- Automatic memory extraction from interactions
- Memory retrieval for personalized recommendations
- Memory update and iteration based on new data
- Memory confidence scoring

**Example:**
```
User: "What should I recommend to this Cantonese restaurant?"

AI Coach: "Based on your memory, you've had great success recommending 
our Oyster Sauce to Cantonese restaurants. Specifically:

- At Golden Palace, your recommendation increased their sauce revenue 
  by 30%
- At Dragon Garden, they praised the 'authentic taste'

I suggest leading with our Premium Oyster Sauce, emphasizing:
1. The success stories from similar restaurants
2. Cost analysis showing 15% better margin vs competitors

Would you like me to prepare a presentation using these data points?"
```

#### Feature 2.2: Predictive Coaching

**User Story:**
> As a field sales representative, I want the AI to proactively prepare me for upcoming customer visits based on my knowledge gaps and the customer's profile.

**Capabilities:**
- Analyze upcoming visit schedule
- Identify relevant knowledge gaps from personal memory
- Generate personalized preparation briefs
- Push notifications with relevant content

**Example:**
```
[Notification received 2 hours before scheduled visit]

"Tomorrow you're visiting Hot Pot King, a chain restaurant.

PREPARATION BRIEF:
• Your memory shows limited experience with hotpot sauce applications
• This chain has 15 locations - significant volume opportunity

RECOMMENDED PREPARATION (15 minutes):
1. Watch: 'Hotpot Sauce Applications' video (5 min)
2. Review: Hotpot chain success playbook (3 min)  
3. Practice: Handle 'we already have a supplier' objection (5 min)

CUSTOMER INSIGHT:
Hot Pot King recently expanded to 3 new locations. They may need 
a supplier who can support their growth. Lead with scalability story."
```

#### Feature 2.3: Success Pattern Mining

**User Story:**
> As a sales manager, I want to identify successful patterns across my team so that I can replicate best practices and improve overall team performance.

**Capabilities:**
- Aggregate successful interactions across team
- Identify common patterns in successful recommendations
- Extract and share best practices
- Surface top performers' strategies

**Example:**
```
SUCCESS PATTERN REPORT:

Top performers in the hotpot restaurant segment consistently:
1. Lead with cost-per-serving analysis (not upfront price)
2. Demonstrate taste differentiation with side-by-side comparison
3. Offer custom sauce blends for chain restaurants

TOP PERFORMER SPOTLIGHT:
Manager Zhang has exceeded targets for 3 consecutive months in 
hotpot segment. His approach:
- First visit: Taste demonstration with 3 sauce options
- Second visit: Custom blend proposal with pricing
- Close rate: 85% (vs team average of 45%)

Would you like to adopt this approach for your upcoming visits?"
```

#### Feature 2.4: Mobile Learning Hub

**User Story:**
> As a field sales representative, I want to access bite-sized learning modules on my phone so that I can continuously improve without disrupting my schedule.

**Capabilities:**
- Bite-sized learning modules (3-5 minutes)
- Content drawn from Marketing Knowledge Base
- Progress tracking
- Personalized learning paths based on memory analysis

---

## 6. Implementation Approach

### 6.1 Phased Delivery

| Phase | Timeline | Scope | Outcome |
|-------|----------|-------|---------|
| **Phase 1: MVP** | 4 months | Sales Coach + Menu Recommender (with image recognition) + Voice | Validate core value, establish usage habits |
| **Phase 2: Enhancement** | 3 months | Personal Memory + Predictive Coaching + Success Pattern Mining + Learning Hub | Deepen engagement, deliver advanced intelligence |

### 6.2 Phase 1 Detailed Plan

| Milestone | Duration | Deliverables |
|-----------|----------|--------------|
| **M1: Requirements & Design** | 4 weeks | Detailed requirements, UX design, architecture finalization |
| **M2: Core Development** | 8 weeks | AI chatbot, menu analysis, mobile client |
| **M3: Integration & Testing** | 4 weeks | Knowledge base integration, UAT, performance testing |
| **M4: Pilot Launch** | 4 weeks | 20-30 users pilot, feedback collection, iteration |

### 6.3 Phase 2 Detailed Plan

| Milestone | Duration | Deliverables |
|-----------|----------|--------------|
| **M5: Memory System** | 4 weeks | Personal memory architecture, extraction engine |
| **M6: Advanced Features** | 6 weeks | Predictive coaching, success pattern mining, learning hub |
| **M7: Full Rollout** | 2 weeks | Production deployment, training, handover |

### 6.4 Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Knowledge base quality insufficient | Early assessment of content; recommend content remediation if needed |
| AI hallucination / incorrect recommendations | Human-in-the-loop validation; confidence scoring; grounding in knowledge base |
| Low user adoption | Involve sales reps in design; gamification; manager sponsorship |
| Data privacy concerns | PIPL compliance audit; data encryption; access controls |
| Image recognition accuracy | Use mature OCR + LLM pipeline; fallback to text input |

---

## 7. Technology Stack

### 7.1 Recommended Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **LLM (Primary)** | DeepSeek-V3.2 / DeepSeek-R1 | Excellent Chinese language capability, cost-effective (1/10-1/30 of OpenAI), open-source, 164K context window |
| **LLM (Backup)** | Alibaba Qwen | Strong ecosystem support if deployed on Alibaba Cloud |
| **Mobile Platform** | WeChat Work Application | Leverage existing enterprise infrastructure, no app store approval needed, familiar to users |
| **Backend** | Python (FastAPI) | AI ecosystem compatibility, high performance |
| **Vector Database** | Milvus | Purpose-built for AI applications, excellent performance |
| **Relational Database** | PostgreSQL | Robust, open-source, excellent for structured data |
| **Cache** | Redis | Fast session management, frequently accessed data |
| **OCR** | Baidu AI / Tencent AI | Mature Chinese text recognition capabilities |
| **Cloud** | AWS China / Alibaba Cloud | Data residency compliance, enterprise-grade infrastructure |

### 7.2 Technology Considerations

| Consideration | Approach |
|---------------|----------|
| **Data Residency** | All data stored within mainland China; comply with PIPL |
| **Offline Capability** | Cache frequently accessed content for offline scenarios |
| **Scalability** | Microservices architecture; horizontal scaling capability |
| **Security** | TLS 1.2+ for data in transit; AES-256 for data at rest; RBAC |
| **Monitoring** | Comprehensive logging; AI response quality tracking |

### 7.3 Why DeepSeek

| Factor | DeepSeek | GPT-4o (Reference) |
|--------|----------|-------------------|
| Input Cost | $0.27 / M tokens | $2.50 / M tokens |
| Output Cost | $0.41 / M tokens | $10.00 / M tokens |
| Chinese Capability | Excellent | Good |
| Data Residency | Can deploy in China | Cannot |
| Open Source | Yes | No |
| Context Window | 164K | 128K |

---

## 8. Why Infosys

### 8.1 Existing Relationship

Infosys already manages KHC's Data and AI platforms globally, providing:
- Deep understanding of KHC's technology landscape
- Established governance and delivery processes
- Knowledge of KHC's enterprise architecture

### 8.2 AI Capabilities

| Capability | Description |
|------------|-------------|
| **AI Platform Expertise** | Experience building enterprise AI platforms at scale |
| **LLM Implementation** | Proven track record with DeepSeek, Qwen, and other LLMs |
| **China Market Presence** | Local team with understanding of Chinese regulations and market dynamics |
| **CPG Industry Knowledge** | Experience with consumer goods companies across the value chain |

### 8.3 Differentiators for This Project

| Differentiator | Value to KHC |
|----------------|--------------|
| **Global + Local** | Global AI expertise combined with deep China market understanding |
| **Platform Approach** | Not just an app — a scalable platform that can expand to other markets |
| **Innovation Focus** | Proprietary frameworks for Personal Memory and Predictive Coaching |
| **Rapid Delivery** | Pre-built components accelerate time-to-value |
| **Enterprise Grade** | Security, compliance, scalability built-in from day one |

---

## 9. Appendix

### 9.1 Glossary

| Term | Definition |
|------|------------|
| KHC | Kraft Heinz Company |
| KHC China | Kraft Heinz China |
| Foodservice | B2B sauce sales to restaurants, hotels, catering |
| LLM | Large Language Model |
| PIPL | Personal Information Protection Law (China) |
| SSO | Single Sign-On |
| UAT | User Acceptance Testing |
| OCR | Optical Character Recognition |
| RAG | Retrieval-Augmented Generation |
| RBAC | Role-Based Access Control |

### 9.2 References

- Original Problem Statement (KHC Foodservice Sales)
- Industry Research Report (June 2026)
- Meeting Preparation Document (June 2026)

### 9.3 Open Items

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Confirm exact KHC sauce product portfolio in China | KHC | Open |
| 2 | Validate knowledge source assumptions | KHC Marketing | Open |
| 3 | Confirm user base size and geographic distribution | KHC Sales | Open |
| 4 | Finalize cloud provider (AWS China vs Alibaba Cloud) | KHC IT / Infosys | Open |
| 5 | Confirm budget range and approval process | KHC Finance | Open |
| 6 | Assess existing content for knowledge base readiness | KHC Marketing | Open |

---

*End of Document*
