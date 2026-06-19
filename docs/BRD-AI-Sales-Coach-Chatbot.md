# Business Requirements Document

## AI-Powered Sales Coach Chatbot for KHC China Foodservice Team

| Field | Value |
|-------|-------|
| **Document ID** | KHC-CN-AI-BRD-001 |
| **Version** | 1.0 (Draft) |
| **Date** | June 2026 |
| **Author** | [Internal Team] |
| **Status** | Draft - For Internal Review |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Business Context](#2-business-context)
3. [Problem Statement](#3-problem-statement)
4. [Business Objectives](#4-business-objectives)
5. [User Personas](#5-user-personas)
6. [Functional Requirements](#6-functional-requirements)
7. [Non-Functional Requirements](#7-non-functional-requirements)
8. [Technical Architecture Overview](#8-technical-architecture-overview)
9. [Integration Points](#9-integration-points)
10. [Success Metrics & KPIs](#10-success-metrics--kpis)
11. [Constraints & Assumptions](#11-constraints--assumptions)
12. [Risks & Mitigations](#12-risks--mitigations)
13. [High-Level Timeline](#13-high-level-timeline)
14. [Appendix](#14-appendix)

---

## 1. Executive Summary

Kraft Heinz China (KHC China) seeks to develop an **AI-powered Sales Coach Chatbot** to empower its field sales team in the foodservice sauce category. The solution will serve as an intelligent, always-available assistant that helps sales representatives:

- **Learn** product knowledge and sales techniques through mobile-first, conversational AI
- **Recommend** appropriate KHC sauce products based on restaurant menu analysis
- **Coach** sales behaviors through scenario-based training and real-time guidance

This initiative aligns with KHC China's strategic goal to become a market leader in the Chinese sauce market, leveraging advanced AI capabilities (including domestic LLMs such as DeepSeek) to create a competitive advantage.

**Proposed Solution:** A mobile application (App) powered by AI/LLM technology that functions as a personalized sales coach, product recommender, and learning platform — accessible anytime, anywhere via smartphone.

---

## 2. Business Context

### 2.1 Market Landscape

- KHC is a global leader in ketchup in Western markets but **not yet a leader in the Chinese sauce market**
- China's sauce market is highly competitive with strong local players (Lee Kum Kee, Hai Tian, etc.)
- Chinese consumers have diverse and sophisticated taste preferences across regional cuisines

### 2.2 Strategic Imperative

- KHC China aims to **accelerate growth in the foodservice sauce segment**
- Field sales team effectiveness is a critical driver of revenue growth
- Digital transformation of sales operations is a company priority post-SAP implementation

### 2.3 Competitive Intelligence

- Competitors in China are already leveraging AI chatbots for sales enablement
- China has advanced AI ecosystem (DeepSeek, Qwen, etc.) that can be leveraged
- KHC China wants a **differentiated, locally-optimized solution** — not a replica of US tools

---

## 3. Problem Statement

### 3.1 Current Challenges

| Challenge | Impact |
|-----------|--------|
| Sales reps lack product knowledge to effectively position KHC sauces | Lost sales opportunities |
| Current e-learning materials require desktop access | Low engagement, poor adoption |
| No intelligent tool to match KHC products to restaurant needs | Missed recommendation opportunities |
| Training is not personalized or on-demand | Slow onboarding for new hires |
| Sales team doesn't carry laptops | Mobile-first solution required |

### 3.2 User Pain Points (Direct Quotes)

> *"I want to have an AI chatbot to teach me how to sell KHC sauce to restaurants."*

> *"I want to use my phone to learn, not sit down with a computer."*

> *"I see my friend in China competitors can use the AI chatbot for learning. It is very convenient and effective."*

> *"Just like a coach beside me."*

---

## 4. Business Objectives

### 4.1 Primary Objectives

| ID | Objective | Priority |
|----|-----------|----------|
| OBJ-01 | Increase field sales team product knowledge and selling confidence | High |
| OBJ-02 | Enable intelligent, menu-based product recommendations | High |
| OBJ-03 | Provide mobile-first, on-demand learning experience | High |
| OBJ-04 | Create a competitive differentiator in sales enablement | Medium |
| OBJ-05 | Build a self-learning system that improves over time | Medium |

### 4.2 Target Outcomes (12 months post-launch)

- **30%+ improvement** in sales team product knowledge assessment scores
- **20%+ increase** in sauce category revenue per sales rep
- **80%+ monthly active usage** among field sales team
- **50%+ reduction** in new hire ramp-up time

---

## 5. User Personas

### Persona 1: Field Sales Representative (一线销售)

| Attribute | Description |
|-----------|-------------|
| **Role** | Visits restaurants daily to promote and sell KHC sauce products |
| **Tech Comfort** | Moderate; comfortable with smartphone apps, limited desktop usage |
| **Primary Need** | Quick answers on which KHC product fits a specific restaurant's menu |
| **Pain Point** | Cannot remember all product details; lacks confidence in recommendations |
| **Usage Context** | On-site at restaurants, in transit, between meetings |

### Persona 2: Sales Team Lead (销售主管)

| Attribute | Description |
|-----------|-------------|
| **Role** | Manages a team of field sales reps; responsible for team performance |
| **Tech Comfort** | Moderate to High |
| **Primary Need** | Ensure team is well-trained and equipped to sell effectively |
| **Pain Point** | Difficulty tracking team knowledge gaps; limited training resources |
| **Usage Context** | Office, team meetings, field visits |

### Persona 3: Marketing / Category Manager (市场/品类经理)

| Attribute | Description |
|-----------|-------------|
| **Role** | Owns product knowledge base, training content, and go-to-market strategy |
| **Tech Comfort** | High |
| **Primary Need** | Ensure sales team has access to latest product info and selling strategies |
| **Pain Point** | Content is static; hard to know what's being used or effective |
| **Usage Context** | Office, content creation and management |

---

## 6. Functional Requirements

### 6.1 Module Overview

| Module | Description | Priority |
|--------|-------------|----------|
| **M1: AI Sales Coach** | Conversational AI that teaches sales techniques and product knowledge | P0 |
| **M2: Menu Analyzer & Recommender** | Analyze restaurant menus and recommend KHC products | P0 |
| **M3: Mobile Learning Hub** | On-demand access to training materials in conversational format | P0 |
| **M4: Product Knowledge Base** | Comprehensive, searchable product database | P1 |
| **M5: Scenario Training** | Role-play simulations for sales conversations | P1 |
| **M6: Analytics Dashboard** | Usage metrics and knowledge gap insights | P2 |

---

### 6.2 M1: AI Sales Coach

| Req ID | Requirement | Priority |
|--------|-------------|----------|
| M1-R01 | Provide conversational interface for sales questions | P0 |
| M1-R02 | Answer questions about KHC sauce products (features, benefits, pricing, applications) | P0 |
| M1-R03 | Provide sales scripts and talk tracks for different scenarios | P0 |
| M1-R04 | Handle objections and suggest responses (e.g., "too expensive", "already have supplier") | P0 |
| M1-R05 | Support Chinese language (Mandarin) as primary language | P0 |
| M1-R06 | Support voice input for hands-free interaction | P1 |
| M1-R07 | Remember conversation context within a session | P0 |
| M1-R08 | Escalate to human support when unable to answer | P1 |

---

### 6.3 M2: Menu Analyzer & Recommender

| Req ID | Requirement | Priority |
|--------|-------------|----------|
| M2-R01 | Accept restaurant menu input (text, photo, or manual entry) | P0 |
| M2-R02 | Identify dishes and categorize by cuisine type | P0 |
| M2-R03 | Analyze flavor profiles of menu items | P0 |
| M2-R04 | Recommend KHC sauce products that complement existing menu | P0 |
| M2-R05 | Provide innovation suggestions for new menu items using KHC products | P1 |
| M2-R06 | Explain rationale for each recommendation | P0 |
| M2-R07 | Highlight menu gaps where KHC products could add value | P1 |
| M2-R08 | Support multiple Chinese cuisine types (Cantonese, Sichuan, etc.) | P0 |

---

### 6.4 M3: Mobile Learning Hub

| Req ID | Requirement | Priority |
|--------|-------------|----------|
| M3-R01 | Convert existing e-learning content into conversational format | P0 |
| M3-R02 | Provide bite-sized learning modules (3-5 min sessions) | P0 |
| M3-R03 | Track learning progress per user | P1 |
| M3-R04 | Offer quizzes and knowledge checks | P1 |
| M3-R05 | Provide daily tips or "knowledge of the day" notifications | P2 |
| M3-R06 | Support offline access to cached content | P1 |
| M3-R07 | Deliver personalized learning paths based on role and knowledge gaps | P2 |

---

### 6.5 M4: Product Knowledge Base

| Req ID | Requirement | Priority |
|--------|-------------|----------|
| M4-R01 | Maintain structured database of all KHC sauce products | P0 |
| M4-R02 | Include product attributes: ingredients, flavor profile, usage scenarios, shelf life | P0 |
| M4-R03 | Include competitive comparison information | P1 |
| M4-R04 | Include pricing and packaging information | P1 |
| M4-R05 | Support search by product name, category, cuisine, or use case | P0 |
| M4-R06 | Update mechanism for marketing team to manage content | P0 |

---

### 6.6 M5: Scenario Training

| Req ID | Requirement | Priority |
|--------|-------------|----------|
| M5-R01 | Provide role-play simulations for common sales scenarios | P1 |
| M5-R02 | Simulate different restaurant owner personas | P1 |
| M5-R03 | Provide feedback and scoring on user responses | P2 |
| M5-R04 | Cover scenarios: new customer pitch, upsell, objection handling, menu consultation | P1 |
| M5-R05 | Allow practice in Chinese language | P1 |

---

### 6.7 M6: Analytics Dashboard

| Req ID | Requirement | Priority |
|--------|-------------|----------|
| M6-R01 | Track daily/weekly/monthly active users | P2 |
| M6-R02 | Track most common questions and topics | P2 |
| M6-R03 | Identify knowledge gaps across the sales team | P2 |
| M6-R04 | Track recommendation acceptance rate | P2 |
| M6-R05 | Provide dashboard for sales managers | P2 |
| M6-R06 | Feed data back to improve AI model | P2 |

---

## 7. Non-Functional Requirements

### 7.1 Performance

| Req ID | Requirement |
|--------|-------------|
| NFR-01 | Chatbot response time < 3 seconds for text queries |
| NFR-02 | Menu image recognition < 5 seconds |
| NFR-03 | App launch time < 2 seconds |
| NFR-04 | Support 500+ concurrent users |

### 7.2 Availability & Reliability

| Req ID | Requirement |
|--------|-------------|
| NFR-05 | System availability: 99.5% uptime during business hours (8AM-8PM CST) |
| NFR-06 | Graceful degradation when AI service is unavailable (cached responses) |

### 7.3 Security & Compliance

| Req ID | Requirement |
|--------|-------------|
| NFR-07 | All data must be stored within mainland China (data residency) |
| NFR-08 | Comply with China's Personal Information Protection Law (PIPL) |
| NFR-09 | User authentication via corporate SSO or WeChat Work login |
| NFR-10 | Encryption of data in transit (TLS 1.2+) and at rest |
| NFR-11 | Role-based access control (RBAC) for different user types |

### 7.4 Usability

| Req ID | Requirement |
|--------|-------------|
| NFR-12 | Mobile-first UI design (iOS and Android) |
| NFR-13 | Chinese (Simplified) as primary language |
| NFR-14 | Intuitive interface requiring minimal training |
| NFR-15 | Support for voice input and output |

### 7.5 Scalability

| Req ID | Requirement |
|--------|-------------|
| NFR-16 | Architecture must support expansion to other KHC markets |
| NFR-17 | Knowledge base must be extensible to other product categories |

---

## 8. Technical Architecture Overview

### 8.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Mobile App (iOS/Android)                │
│                   ┌───────────────────────┐                 │
│                   │   Chat Interface       │                 │
│                   │   Menu Upload          │                 │
│                   │   Learning Modules     │                 │
│                   └───────────┬───────────┘                 │
└───────────────────────────────┼─────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                      API Gateway                             │
│              (Authentication, Rate Limiting)                 │
└───────────────────────────────┼─────────────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│  AI/LLM       │     │  Knowledge    │     │  Analytics    │
│  Service      │     │  Base         │     │  Service      │
│  (DeepSeek/   │     │  Service      │     │               │
│   Qwen)       │     │               │     │               │
└───────┬───────┘     └───────┬───────┘     └───────┬───────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
                    ┌───────────────┐
                    │  Data Layer   │
                    │  (China Cloud)│
                    └───────────────┘
```

### 8.2 Technology Recommendations

| Component | Recommendation | Rationale |
|-----------|----------------|-----------|
| **LLM** | DeepSeek / Qwen / GLM | China-based, Mandarin-optimized, compliance |
| **Mobile Framework** | React Native / Flutter | Cross-platform, cost-effective |
| **Backend** | Python (FastAPI) / Node.js | AI ecosystem compatibility |
| **Cloud** | Alibaba Cloud / Tencent Cloud | Data residency, China presence |
| **Image Recognition** | Baidu AI / Tencent AI | Chinese menu recognition |
| **Vector Database** | Milvus / Zilliz | Knowledge base semantic search |

---

## 9. Integration Points

| System | Integration Type | Purpose | Priority |
|--------|------------------|---------|----------|
| **Corporate SSO / WeChat Work** | Authentication | User login and identity | P0 |
| **Marketing Knowledge Base** | API / Data Sync | Training content and product info | P0 |
| **CRM System** | API (future) | Customer interaction data | P2 |
| **SAP** | API (future) | Product and pricing data | P2 |
| **WeChat Mini Program** (optional) | Distribution | Alternative delivery channel | P2 |

---

## 10. Success Metrics & KPIs

### 10.1 Adoption Metrics

| Metric | Target (6 months) | Target (12 months) |
|--------|-------------------|-------------------|
| Monthly Active Users (MAU) | 70% of sales team | 85% of sales team |
| Daily Active Users (DAU) | 40% of sales team | 60% of sales team |
| Average sessions per user per week | 3+ | 5+ |
| Average session duration | 5+ minutes | 8+ minutes |

### 10.2 Business Impact Metrics

| Metric | Target (12 months) |
|--------|-------------------|
| Sauce category revenue growth per rep | +20% |
| Product knowledge assessment scores | +30% |
| New hire ramp-up time | -50% |
| Recommendation-to-sale conversion | 25%+ |

### 10.3 Quality Metrics

| Metric | Target |
|--------|--------|
| AI response accuracy (user-rated) | 85%+ helpful |
| Menu recommendation relevance | 80%+ user satisfaction |
| System uptime | 99.5% |
| Average response time | < 3 seconds |

---

## 11. Constraints & Assumptions

### 11.1 Constraints

| ID | Constraint |
|----|------------|
| C-01 | Solution must be deployed within mainland China for data residency |
| C-02 | Must use China-approved AI models (no OpenAI/ChatGPT direct usage) |
| C-03 | Must be delivered as native/hybrid mobile app (not web-only) |
| C-04 | Must support offline/low-connectivity scenarios for field use |
| C-05 | Integration with existing marketing knowledge base content |

### 11.2 Assumptions

| ID | Assumption |
|----|------------|
| A-01 | Marketing team will provide product knowledge base content |
| A-02 | Sales team has company-issued smartphones or BYOD with reimbursement |
| A-03 | Corporate IT will support SSO/WeChat Work integration |
| A-04 | Budget is approved for cloud infrastructure and AI API costs |
| A-05 | Stakeholders will be available for UAT and feedback cycles |

---

## 12. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| AI hallucination / incorrect product recommendations | Medium | High | Implement human-in-the-loop validation; confidence scoring; knowledge base grounding |
| Low user adoption | Medium | High | Involve sales reps in design; gamification; manager buy-in |
| Content maintenance burden | Medium | Medium | Automated content sync; clear ownership; content management workflow |
| Data privacy concerns | Low | High | PIPL compliance audit; data encryption; access controls |
| AI model cost overrun | Medium | Medium | Usage quotas; caching; model optimization |
| Integration complexity with legacy systems | Medium | Medium | Phased integration; API-first design |

---

## 13. High-Level Timeline

### Phase 1: MVP (3-4 months)

| Milestone | Duration |
|-----------|----------|
| Requirements finalization & design | 4 weeks |
| Core AI chatbot (Sales Coach) | 6 weeks |
| Menu input & basic recommendation | 4 weeks |
| Mobile app development (iOS + Android) | 6 weeks |
| UAT & pilot launch (20-30 users) | 4 weeks |

### Phase 2: Enhancement (2-3 months)

| Milestone | Duration |
|-----------|----------|
| Scenario training module | 4 weeks |
| Advanced menu analysis (image recognition) | 3 weeks |
| Analytics dashboard | 3 weeks |
| Full rollout to sales team | 2 weeks |

### Phase 3: Optimization (Ongoing)

| Activity |
|----------|
| AI model fine-tuning based on usage data |
| Knowledge base expansion |
| Integration with CRM/SAP |
| Feature enhancements based on user feedback |

---

## 14. Appendix

### 14.1 Glossary

| Term | Definition |
|------|------------|
| KHC | Kraft Heinz Company |
| KHC China | Kraft Heinz China |
| Foodservice | B2B sauce sales to restaurants, hotels, catering |
| LLM | Large Language Model |
| PIPL | Personal Information Protection Law (China) |
| SSO | Single Sign-On |
| UAT | User Acceptance Testing |
| MAU/DAU | Monthly/Daily Active Users |

### 14.2 Reference Documents

- Original Problem Statement (internal email)
- KHC China IT Capability Assessment
- Competitor AI Chatbot Analysis (TBD)

### 14.3 Open Questions

| # | Question | Owner | Status |
|---|----------|-------|--------|
| 1 | Confirm user base size and geographic distribution | Business | Open |
| 2 | Confirm budget range and approval process | Finance | Open |
| 3 | Determine preferred cloud vendor (Alibaba vs Tencent) | IT | Open |
| 4 | Assess existing marketing knowledge base format and volume | Marketing | Open |
| 5 | Confirm integration requirements with SAP/CRM | IT | Open |

---

*End of Document*
