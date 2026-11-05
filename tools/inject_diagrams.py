"""
Injects self-contained, exam-ready ASCII Box-and-Arrow diagrams into
Units 5, 6, 7, and 9 so students never have to refer to external slides during revision.
"""

from pathlib import Path

# --- UNIT 5 DIAGRAMS ---
U5_DIAG_1 = '''
```
                   INDIAN FINANCIAL MARKET ARCHITECTURE
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
   MONEY MARKET (T <= 1 Year)                              CAPITAL MARKET (T > 1 Year)
   (Regulated by RBI)                                      (Regulated by SEBI)
         │                                                       │
   ┌─────┴─────────────────────┐                           ┌─────┴─────────────────────┐
   ▼                           ▼                           ▼                           ▼
[ Wholesale / Interbank ]  [ Retail / Corporate ]     [ Primary Market (NIM) ]     [ Secondary Market ]
• Call/Notice Money        • Treasury Bills (T-Bills) • Public Issue (IPO / FPO)   • Stock Exchanges (BSE/NSE)
• Term Money               • Commercial Paper (CP)    • Rights Issue               • Demat Trading (T+1)
• Repos & Reverse Repos    • Certificates of Dep (CD) • Private Placement / QIP    • Clearing Corp (NSCCL)
```
'''

U5_DIAG_2 = '''
```
               PRIMARY MARKET CAPITAL MOBILIZATION WORKFLOW
                                     │
           [ Corporate Issuer / Deficit Unit Needs Capital ]
                                     │
                                     ▼
           [ Appoints Book Running Lead Manager (BRLM) ]
                                     │
                                     ▼
           [ Prepares Draft Red Herring Prospectus (DRHP) ]
                                     │
                                     ▼
           [ SEBI Review & Regulatory In-Principle Approval ]
                                     │
                                     ▼
           [ Marketing, Roadshows & Price Band Announcement ]
                                     │
                                     ▼
           [ ASBA Public Bidding (Retail, HNI, QIB Pools) ]
                                     │
                                     ▼
           [ Basis of Allotment Finalization & Demat Credit ]
                                     │
                                     ▼
           [ Capital Transferred to Issuer & Stock Listed on Exchange ]
```
'''

U5_DIAG_3 = '''
```
                 IPO BOOK BUILDING & PRICE DISCOVERY ARCHITECTURE
                                     │
           [ Issuer & Merchant Banker Fix Price Band ]
           (Cap Price <= 1.20 x Floor Price, e.g., Rs 100 - Rs 120)
                                     │
                                     ▼
           [ Bidding Window Opens (3 to 5 Working Days) ]
           (Investors submit bids at varying price points via ASBA)
                                     │
            ┌────────────────────────┼────────────────────────┐
            ▼                        ▼                        ▼
      [ Bid @ Rs 100 ]         [ Bid @ Rs 110 ]         [ Bid @ Rs 120 ]
      (50,000 Shares)          (1,20,000 Shares)        (2,50,000 Shares)
                                     │
                                     ▼
           [ Book Runner Consolidates Cumulative Demand Curve ]
                                     │
                                     ▼
           [ Cut-Off Price Determined where Total Demand = Total Supply ]
                                     │
                                     ▼
           [ All Successful Bidders Pay Cut-Off Price; Balance Unblocked ]
```
'''

U5_DIAG_4 = '''
```
           SECONDARY MARKET TRADING & T+1 ROLLING SETTLEMENT
                                     │
     [ Investor / Buyer ] ──(Enters Order)──► [ Trading Member / Broker ]
                                                        │
                                                        ▼
                                             [ Automated Screen (BOLT/NEAT) ]
                                             (Matches Order by Price-Time Priority)
                                                        │
                                                        ▼ (Trade Executed: Day T)
                                             [ Clearing Corporation (NSCCL/ICCL) ]
                                             (Acts as Central Counterparty via Novation)
                                                        │
                                     ┌──────────────────┴──────────────────┐
                                     ▼ (Day T+1 Pay-in)                    ▼ (Day T+1 Pay-out)
                            [ Clearing Member Bank ]              [ Depositories (NSDL/CDSL) ]
                            (Debits Buyer / Credits Seller)       (Transfers Demat Shares to Buyer)
```
'''

U5_DIAG_5 = '''
```
                 DUAL FINANCIAL REGULATORY ARCHITECTURE (INDIA)
                                     │
                       [ Ministry of Finance (MoF) ]
                                     │
            ┌────────────────────────┴────────────────────────┐
            ▼                                                 ▼
[ RESERVE BANK OF INDIA (RBI) ]                [ SECURITIES & EXCHANGE BOARD (SEBI) ]
  • Statutory Act: RBI Act, 1934                 • Statutory Act: SEBI Act, 1992
  • Mandate: Monetary Policy & Liquidity         • Mandate: Investor Protection & Market Integrity
  • Regulated Domain:                            • Regulated Domain:
    - Commercial & Regional Rural Banks            - Stock Exchanges (BSE, NSE, MCX)
    - Non-Banking Financial Companies (NBFCs)      - Merchant Bankers & Underwriters
    - Money Markets (Call, T-Bills, CPs, Repos)    - Mutual Funds & Asset Management Cos (AMCs)
    - Foreign Exchange (Forex) & G-Secs            - Depositories (NSDL, CDSL) & Brokers
```
'''

U5_DIAG_6 = '''
```
               LIFECYCLE MECHANICS OF A FINANCIAL SPECULATIVE BUBBLE
                                     │
  [ Phase 1: DISPLACEMENT ] ──► Technological shock or macro shift introduces new profit narrative
            │
            ▼
  [ Phase 2: BOOM & CREDIT ]──► Abundant cheap liquidity accelerates buying; asset prices climb
            │
            ▼
  [ Phase 3: EUPHORIA ]    ──► "New Era" narrative; retail FOMO; irrational valuation multiples
            │
            ▼
  [ Phase 4: PROFIT-TAKING]──► Sophisticated smart-money begins quietly liquidating positions
            │
            ▼
  [ Phase 5: PANIC & CRASH ]─► Credit dries up, margin calls trigger forced selling, asset prices crash
```
'''

# --- UNIT 6 DIAGRAMS ---
U6_DIAG_1 = '''
```
              RBI LIQUIDITY ADJUSTMENT FACILITY (LAF) MECHANISM
                                     │
               ┌─────────────────────┴─────────────────────┐
               ▼                                           ▼
      [ REPO TRANSACTION ]                       [ REVERSE REPO TRANSACTION ]
    (RBI Injects Cash Liquidity)                 (RBI Absorbs Excess Liquidity)
               │                                           │
  Commercial Bank ──(G-Sec Collateral)──► RBI    Commercial Bank ◄──(G-Sec Collateral)── RBI
  Commercial Bank ◄────(Cash Funds)───── RBI    Commercial Bank ────(Cash Surplus)────► RBI
               │                                           │
   [ Bank Repurchases G-Sec at                 [ RBI Repurchases G-Sec at
     Repo Rate (e.g., 6.50%) ]                   Reverse Repo Rate (e.g., 3.35%) ]
```
'''

U6_DIAG_2 = '''
```
           CONVERTIBLE DEBENTURE PAYOFF & CONVERSION LIFECYCLE
                                     │
           [ Issuer Issues Fully/Partly Convertible Debenture (FCD/PCD) ]
                                     │
                                     ▼
           [ Investor Receives Fixed Coupon Interest (Years 1 to n) ]
                                     │
                                     ▼
           [ Conversion Window Reached: Evaluate Conversion Parity ]
                                     │
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
         Market Price > Conversion Price    Market Price < Conversion Price
         [ Option IN-THE-MONEY ]            [ Option OUT-OF-THE-MONEY ]
                    │                                 │
                    ▼                                 ▼
         Convert into Equity Shares         Hold for Fixed Redemption
         (Capture Capital Gains Growth)     (Receive Principal Repayment)
```
'''

U6_DIAG_3 = '''
```
             CAPITAL STRUCTURE PRIORITY OF CLAIMS (LIQUIDATION HIERARCHY)
                                     │
                       ┌───────────────────────────┐
                       │   SENIOR SECURED DEBT     │  ◄── Highest Priority / Lowest Risk
                       │   (Bank Loans, Mortgages) │      (Secured by Fixed Assets)
                       ├───────────────────────────┤
                       │  SENIOR UNSECURED DEBT    │  ◄── Commercial Paper, Unsecured Debentures
                       ├───────────────────────────┤
                       │    SUBORDINATED DEBT      │  ◄── Tier-II Capital, Mezzanine Finance
                       ├───────────────────────────┤
                       │    PREFERENCE SHARES      │  ◄── Fixed Dividend Claim Before Equity
                       ├───────────────────────────┤
                       │      COMMON EQUITY        │  ◄── Lowest Priority / Highest Risk
                       │   (Ordinary Shareholders) │      (Residual Claimants of Assets)
                       └───────────────────────────┘
```
'''

U6_DIAG_4 = '''
```
                 RIGHTS ISSUE EXECUTION & DILUTION WORKFLOW
                                     │
           [ Board Approves Rights Ratio & Subscription Price ]
           (e.g., 1 Rights Share for every 4 Shares held @ Rs 80; CMP = Rs 100)
                                     │
                                     ▼
           [ Record Date: Eligible Shareholders Credited with RE in Demat ]
                                     │
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
           [ EXERCISE RIGHTS ]               [ RENOUNCE RIGHTS ]
           Subscribe @ Discounted Price      Sell Rights Entitlement (RE) on Exchange
           (Retains Percentage Ownership)    (Receives Cash; Ownership Percentage Diluted)
                                     │
                                     ▼
           [ Theoretical Ex-Rights Price (TERP) Established ]
           $$TERP = \\frac{(N \\times CMP) + (S \\times Issue Price)}{N + S}$$
```
'''

U6_DIAG_5 = '''
```
                 FINANCIAL DERIVATIVES RISK TRANSFER TAXONOMY
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
   [ OVER-THE-COUNTER (OTC) ]                              [ EXCHANGE-TRADED ]
   • Custom Bilateral Contracts                            • Standardized Contracts
   • High Counterparty / Default Risk                      • Guaranteed by Clearing Corporation
   • Non-liquid / Flexible Settlement                      • High Liquidity / T+1 Daily MTM Settlement
         │                                                       │
   ┌─────┴──────────────┐                                  ┌─────┴──────────────┐
   ▼                    ▼                                  ▼                    ▼
[ Forward Contracts ] [ Currency / IR Swaps ]           [ Financial Futures ] [ Financial Options ]
```
'''

U6_DIAG_6 = '''
```
           SYMMETRIC (FUTURES) VS. ASYMMETRIC (OPTIONS) PAYOFF
                                     │
           FUTURES PAYOFF                           CALL OPTION PAYOFF
       (Symmetric / Linear)                       (Asymmetric / Non-Linear)
               Profit                                       Profit
                 ▲                                            ▲
                 │     / Payoff                               │          / Payoff
                 │    /                                       │         /
          ───────┼───/──────► Price                    ───────┼────────/─────► Price
                /│                                       -Prem│_______/ Strike
               / │                                            │
                 ▼                                            ▼
               Loss                                         Loss
  (Unlimited Upside & Downside)              (Unlimited Upside; Max Loss = Premium Paid)
```
'''

U6_DIAG_7 = '''
```
          PLAIN VANILLA FIXED-FOR-FLOATING INTEREST RATE SWAP (IRS)
                                     │
                       ┌───────────────────────────┐
                       │   SWAP BANK / DEALER      │
                       │   (Market Intermediary)   │
                       └───────────────────────────┘
                         ▲                       ▲
     Pays Fixed (7.00%)  │                       │  Pays Floating (SOFR + 1.20%)
    Receives SOFR + 0.80%│                       │  Receives Fixed (7.20%)
                         ▼                       ▼
            ┌────────────────────────┐       ┌────────────────────────┐
            │       COMPANY A        │       │       COMPANY B        │
            │ (Seeks Floating Debt)  │       │   (Seeks Fixed Debt)   │
            └────────────────────────┘       └────────────────────────┘
```
'''

# --- UNIT 7 DIAGRAMS ---
U7_DIAG_1 = '''
```
              FINANCIAL SERVICES CORE INTERMEDIARY TAXONOMY
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
   [ FUND-BASED FINANCIAL SERVICES ]                       [ FEE-BASED FINANCIAL SERVICES ]
   (Asset & Capital Balance Sheet Deployment)              (Advisory & Intermediary Services)
         │                                                       │
   ┌─────┴─────────────────────┐                           ┌─────┴─────────────────────┐
   ▼                           ▼                           ▼                           ▼
[ Short-Term / Working Cap ] [ Long-Term Capital Pres ]  [ Capital Market Advisory ] [ Asset Administration ]
• Factoring & Forfaiting     • Equipment Leasing         • Merchant Banking (IPOs)   • Credit Rating (CRISIL)
• Consumer Credit            • Hire Purchase (HP)        • Underwriting              • Portfolio Mgmt (PMS)
• Trade Credit Bills         • Housing Finance / VC      • Stock Broking             • Custodial Services
```
'''

U7_DIAG_2 = '''
```
                EQUIPMENT LEASE VS. HIRE PURCHASE CONTRACTUAL FLOW
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
   [ EQUIPMENT LEASE ]                                     [ HIRE PURCHASE (HP) ]
   • Legal Structure: Bailment (Indian Contract Act)       • Legal Structure: Sale Agreement (HP Act)
   • Title / Ownership: REMAINS WITH LESSOR                • Title: TRANSFERS ON FINAL INSTALLMENT
   • Down Payment: Typically NIL                           • Down Payment: 15% to 25% Mandatory
   • Tax Deduction: Full Lease Rental is Tax Deductible    • Tax Deduction: Double Shield (Interest + Deprec)
   • Balance Sheet: Capitalized under Ind AS 116           • Balance Sheet: Hirer Capitalizes Full Asset Value
```
'''

U7_DIAG_3 = '''
```
             FACTORING VS. FORFAITING TRADE FINANCE WORKFLOW
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
   [ FACTORING (Short-Term Trade) ]                        [ FORFAITING (Medium/Long-Term Export) ]
   • Tenor: 30 to 180 Days                                 • Tenor: 1 to 7 Years
   • Underlying: Consumer Goods & Receivables Ledger       • Underlying: Capital Goods & Plant Machinery
   • Recourse: Recourse OR Non-Recourse                    • Recourse: STRICTLY 100% WITHOUT RECOURSE
   • Financing: 80% to 90% Advance                         • Financing: 100% Cash Financed Upfront
   • Debt Instrument: Sales Invoices & Debt Assignment     • Debt Instrument: Avalised Promissory Notes / Bills
```
'''

U7_DIAG_4 = '''
```
                 VENTURE CAPITAL 5-STAGE INVESTMENT LIFECYCLE
                                     │
  [ Phase 1: SEED / ANGEL ]    ──► Concept validation, prototype proof, founders' bootstrapping
            │
            ▼
  [ Phase 2: EARLY STAGE ]     ──► Series A/B funding; product launch, market fit, revenue traction
            │
            ▼
  [ Phase 3: GROWTH CAPITAL ]  ──► Series C+ expansion, scaling operations, market penetration
            │
            ▼
  [ Phase 4: BRIDGE / PRE-IPO ]──► Mezzanine financing, restructuring balance sheet for public market
            │
            ▼
  [ Phase 5: STRATEGIC EXIT ]  ──► Liquidity event via Initial Public Offering (IPO) or M&A Buyout
```
'''

U7_DIAG_5 = '''
```
           MERCHANT BANKING 3-PHASE ISSUE MANAGEMENT ARCHITECTURE
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
[ 1. PRE-ISSUE MANAGEMENT ]   [ 2. ISSUE EXECUTION ]      [ 3. POST-ISSUE MONITORING ]
• Due diligence & audit       • Price Band fixation       • ASBA escrow reconciliation
• Prospectus drafting (DRHP)  • Bidding window management • Basis of allotment with SEBI
• SEBI regulatory filing      • Marketing & roadshows     • Demat share credit via DPs
• Underwriting syndication    • Collecting Banker liaison • Final listing on BSE/NSE
```
'''

U7_DIAG_6 = '''
```
                 CREDIT RATING AGENCY (CRA) 6-STEP RATING FLOW
                                     │
           [ Issuer Submits Rating Request & Signed Agreement ]
                                     │
                                     ▼
           [ Rating Team Gathers Financial, Operational & Management Data ]
                                     │
                                     ▼
           [ Factory / Plant Inspection & Management Interview ]
                                     │
                                     ▼
           [ Presentation of Rating Rationale to Independent Rating Committee ]
                                     │
                                     ▼
           [ Rating Assigned (e.g., AAA, AA, BBB) & Communicated to Issuer ]
                                     │
                                     ▼
           [ Acceptance & Dissemination to Public + Continuous Surveillance ]
```
'''

U7_DIAG_7 = '''
```
           PORTFOLIO MANAGEMENT & CUSTODIAL OPERATIONAL ARCHITECTURE
                                     │
           [ HNI / Institutional Client ] ──(Allocates Capital)──► [ PMS Fund Manager ]
                                                                        │
                                                                 (Formulates Strategy)
                                                                        │
                                                                        ▼
                                                             [ Execution on Exchanges ]
                                                                        │
                                      ┌─────────────────────────────────┴─────────────────────────────────┐
                                      ▼                                                                   ▼
                         [ Custodian / Clearing Agent ]                                      [ Depository (NSDL/CDSL) ]
                         (Safekeeping of Client Funds & Assets)                              (Electronic Demat Holding)
```
'''

U7_DIAG_8 = '''
```
                 DUAL REGULATORY INTERMEDIARY DOMAIN ALLOCATION
                                     │
                       [ Ministry of Finance (MoF) ]
                                     │
            ┌────────────────────────┴────────────────────────┐
            ▼                                                 ▼
[ RESERVE BANK OF INDIA (RBI) ]                [ SECURITIES & EXCHANGE BOARD (SEBI) ]
  • Governs Credit & Fund Liquidity              • Governs Securities & Fee Intermediaries
  • Entities:                                    • Entities:
    - NBFC-Asset Finance Companies (AFCs)          - Merchant Bankers / Lead Managers
    - Equipment Leasing & HP Companies             - Credit Rating Agencies (CRISIL, ICRA)
    - NBFC-Factors (under Factoring Act)           - Stock Brokers & Depository Participants
    - Housing Finance Companies (HFCs)             - Portfolio Management Service (PMS) Providers
```
'''

# --- UNIT 9 DIAGRAMS ---
U9_DIAG_1 = '''
```
                   TRIPARTITE FACTORING STRUCTURAL MECHANISM
                                     │
          [ Seller / Client ] ────────(1. Delivers Goods)────────► [ Buyer / Debtor ]
                   │                                                       │
                   │ (2. Assigns Invoice Debt)                             │ (4. Pays Full
                   ▼                                                       │     Invoice at
          ┌────────────────┐                                               │     Maturity)
          │  FACTOR / NBFC │ ◄─────────────────────────────────────────────┘
          └────────────────┘
                   │
                   ▼ (3. Prepayment: 80% to 90% Upfront)
          [ Seller receives working capital instantly;
            Remaining 10-20% received after collection minus Factor fee ]
```
'''

U9_DIAG_2 = '''
```
                      STRUCTURAL CLASSIFICATIONS OF FACTORING
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
  [ CREDIT RISK BASIS ]          [ TIMING BASIS ]               [ DISCLOSURE BASIS ]
  • Recourse Factoring           • Advance Factoring            • Disclosed Factoring
    (Bad debts borne by Seller)    (80-90% Prepayment Day 1)      (Notice of Assignment to Buyer)
  • Non-Recourse Factoring       • Maturity Factoring           • Undisclosed Factoring
    (Factor absorbs 100% loss)     (Payment on collection date)   (Debtor unaware of Factor)
```
'''

U9_DIAG_3 = '''
```
           INTERNATIONAL TWO-FACTOR CROSS-BORDER EXPORT WORKFLOW
                                     │
       [ Exporter (Home Country) ] ──(1. Ships Goods)──► [ Importer (Foreign Country) ]
                   │                                                     ▲
   (2. Assigns     │                                                     │ (4. Pays Invoice
       Export Debt)▼                                                     │     on Maturity)
          ┌────────────────┐                                   ┌────────────────┐
          │ EXPORT FACTOR  │ ──(3. Re-assigns Receivables)───► │ IMPORT FACTOR  │
          │ (Home Country) │ ◄──────(5. Remits Funds)───────── │ (Foreign Host) │
          └────────────────┘                                   └────────────────┘
                   │
                   ▼ (Advance Payment: 80%)
       [ Exporter secures working capital & 100% foreign credit protection ]
```
'''

U9_DIAG_4 = '''
```
                 FORFAITING AVALISED BILLS OF EXCHANGE WORKFLOW
                                     │
       [ Exporter (Capital Goods) ] ──(1. Delivers Plant)──► [ Importer (Foreign Buyer) ]
                   │                                                     │
                   │                                          (2. Issues Series of
                   │                                              Promissory Notes)
                   │                                                     ▼
                   │                                         [ Importer's Bank (Aval) ]
                   │                                         (Guarantees Notes "Per Aval")
                   │                                                     │
                   │ ◄──────────────────(3. Delivers Avalised Notes)─────┘
                   │
                   ▼ (4. Surrenders Avalised Notes Without Recourse)
          ┌────────────────┐
          │   FORFAITER    │ ──(5. Pays 100% Cash Minus Discount)──► [ Exporter ]
          └────────────────┘
                   │
                   ▼ (6. Presents Notes for Payment at Maturity: 1 to 5 Years)
          [ Importer's Bank Honors Payment unconditionally ]
```
'''

U9_DIAG_5 = '''
```
              TReDS (TRADE RECEIVABLES DISCOUNTING SYSTEM) PLATFORM
                                     │
           [ MSME Supplier ] ──(1. Uploads Invoice / Factoring Unit)──► [ TReDS Platform ]
                                                                               ▲
           [ Corporate / PSU Buyer ] ──(2. Approves & Accepts Invoice)─────────┤
                                                                               ▼
           [ Multiple Financiers / Banks ] ◄──(3. Bid in Reverse Auction)──────┤
                                                                               │
           [ Lowest Discount Bid Selected Automatically ] ─────────────────────┘
                                     │
                                     ▼
           [ MSME Supplier receives Funds in Account within 24–48 Hours (Without Recourse) ]
```
'''

U9_DIAG_6 = '''
```
                 FACTORING VS. FORFAITING COMPARATIVE MATRIX
                                     │
               FACTORING                                   FORFAITING
   • Short-Term (< 180 Days)                   • Medium/Long-Term (1 to 7 Years)
   • Consumer Goods & Receivables Ledger       • Capital Goods, Industrial Projects
   • Involves Sales Ledger Administration      • Pure Financial Discounting Mechanism
   • Recourse OR Non-Recourse                  • STRICTLY 100% WITHOUT RECOURSE
   • Upfront Advance 80% to 90%                • 100% Cash Paid Upfront (Net of Discount)
   • Unsecured or Open Account Debt            • Secured by Avalised Negotiable Instruments
```
'''

def inject():
    # Unit 5
    p5 = Path('FIMIS/Unit_5/fimis-unit5-financial-markets-pyq-bank.md')
    c5 = p5.read_text(encoding='utf-8')
    c5 = c5.replace(
        '> 📊 **Diagram Required**: YES | **Type**: Structural Taxonomy & Flow Chart | \n**Source**: `Unit5_Financial_Markets.pptx` (Slides 2–3) & Pathak (Chapter 1)',
        '📊 **Diagram Required**: YES | **Type**: Structural Taxonomy & Interbank Flow | **Exam Sketch Target**: Financial Market Taxonomy\n' + U5_DIAG_1.strip()
    )
    c5 = c5.replace(
        '> 📊 **Diagram Required**: YES | **Type**: Operational Workflow & Capital \nMobilization Loop | **Source**: Pathak (Chapter 6) & \n`Unit5_Financial_Markets.pptx` (Slide 25)',
        '📊 **Diagram Required**: YES | **Type**: Operational Workflow & Capital Mobilization | **Exam Sketch Target**: Primary Market Issue Flow\n' + U5_DIAG_2.strip()
    )
    c5 = c5.replace(
        '> 📊 **Diagram Required**: YES | **Type**: End-to-End Operational Workflow | \n**Source**: `Unit5_Financial_Markets.pptx` (Slide 26) & Pathak (Chapter 6)',
        '📊 **Diagram Required**: YES | **Type**: End-to-End Operational Workflow | **Exam Sketch Target**: Book Building Price Discovery\n' + U5_DIAG_3.strip()
    )
    c5 = c5.replace(
        '> 📊 **Diagram Required**: YES | **Type**: Operational Architecture & \nSettlement Flow | **Source**: `Unit5_Financial_Markets.pptx` (Slides 29–31) & \nPathak (Chapter 8)',
        '📊 **Diagram Required**: YES | **Type**: Operational Architecture & Settlement Flow | **Exam Sketch Target**: Secondary Market T+1 Flow\n' + U5_DIAG_4.strip()
    )
    c5 = c5.replace(
        '> 📊 **Diagram Required**: YES | **Type**: Regulatory Architecture & Governance\nMatrix | **Source**: `Unit5_Financial_Markets.pptx` (Slide 12, 29) & Pathak \n(Chapters 4, 5, 9)',
        '📊 **Diagram Required**: YES | **Type**: Regulatory Architecture & Governance | **Exam Sketch Target**: RBI vs SEBI Dual Regulatory Mandate\n' + U5_DIAG_5.strip()
    )
    c5 = c5.replace(
        '> 📊 **Diagram Required**: YES | **Type**: Lifecycle / Workflow Diagram | \n**Source**: `Unit5_Financial_Markets.pptx` (Slides 33–37) & Madura (Chapter 1)',
        '📊 **Diagram Required**: YES | **Type**: Lifecycle / Workflow Diagram | **Exam Sketch Target**: 5-Phase Bubble Lifecycle\n' + U5_DIAG_6.strip()
    )
    p5.write_text(c5, encoding='utf-8')
    print('Unit 5 diagrams injected successfully.')

    # Unit 6
    p6 = Path('FIMIS/Unit_6/fimis-unit6-financial-instruments-pyq-bank.md')
    c6 = p6.read_text(encoding='utf-8')
    c6 = c6.replace(
        '📊 **Diagram Required**: YES | **Type**: Operational Workflow (Interbank Money \nMarket & Liquidity Adjustment Mechanism) | **Source**: \n`Unit6_Financial_Instruments.pptx` / RBI Operational Manuals',
        '📊 **Diagram Required**: YES | **Type**: Operational Workflow (Interbank Money Market) | **Exam Sketch Target**: RBI Liquidity Adjustment Facility (LAF)\n' + U6_DIAG_1.strip()
    )
    c6 = c6.replace(
        '📊 **Diagram Required**: YES | **Type**: Convertible Debenture Payoff & \nValuation Structural Flow | **Source**: `Unit6_Financial_Instruments.pptx` & \nPathak Ch. 17',
        '📊 **Diagram Required**: YES | **Type**: Convertible Debenture Payoff & Valuation Flow | **Exam Sketch Target**: Debenture Conversion Threshold Flow\n' + U6_DIAG_2.strip()
    )
    c6 = c6.replace(
        '📊 **Diagram Required**: YES | **Type**: Priority of Claims Capital Structure \nPyramid | **Source**: `Unit6_Financial_Instruments.pptx` Slide 10',
        '📊 **Diagram Required**: YES | **Type**: Priority of Claims Capital Structure Pyramid | **Exam Sketch Target**: Liquidation Priority Hierarchy\n' + U6_DIAG_3.strip()
    )
    c6 = c6.replace(
        '📊 **Diagram Required**: YES | **Type**: Rights Issue Execution Workflow & \nDilution Mechanics | **Source**: Pathak Ch. 6',
        '📊 **Diagram Required**: YES | **Type**: Rights Issue Execution Workflow & Dilution | **Exam Sketch Target**: Rights Issue vs Renunciation Flow\n' + U6_DIAG_4.strip()
    )
    c6 = c6.replace(
        '📊 **Diagram Required**: YES | **Type**: Derivative Market Taxonomy & Risk \nTransfer Architecture | **Source**: `Unit6_Financial_Instruments.pptx` Slides \n11–16',
        '📊 **Diagram Required**: YES | **Type**: Derivative Market Taxonomy & Risk Transfer | **Exam Sketch Target**: OTC vs Exchange Traded Derivatives\n' + U6_DIAG_5.strip()
    )
    c6 = c6.replace(
        '📊 **Diagram Required**: YES | **Type**: Symmetric (Futures) vs. Asymmetric \n(Options) Payoff Graphs | **Source**: `Unit6_Financial_Instruments.pptx` Slides \n13–14 / Pathak Ch. 9',
        '📊 **Diagram Required**: YES | **Type**: Symmetric (Futures) vs. Asymmetric (Options) Payoffs | **Exam Sketch Target**: Linear vs Hockey-Stick Payoff Graphs\n' + U6_DIAG_6.strip()
    )
    c6 = c6.replace(
        '📊 **Diagram Required**: YES | **Type**: Plain Vanilla Fixed-for-Floating \nInterest Rate Swap Flow Diagram | **Source**: \n`Unit6_Financial_Instruments.pptx` Slide 15 / Madura Ch. 15',
        '📊 **Diagram Required**: YES | **Type**: Plain Vanilla Fixed-for-Floating IRS Flow | **Exam Sketch Target**: 3-Party Interest Rate Swap Mechanism\n' + U6_DIAG_7.strip()
    )
    p6.write_text(c6, encoding='utf-8')
    print('Unit 6 diagrams injected successfully.')

    # Unit 7
    p7 = Path('FIMIS/Unit_7/fimis-unit7-financial-services-pyq-bank.md')
    c7 = p7.read_text(encoding='utf-8')
    c7 = c7.replace(
        '📊 Diagram Required: YES | Type: Structural Workflow | Source: Unit-7.pptx & \nPathak (Ch. 17)',
        '📊 **Diagram Required**: YES | **Type**: Structural Workflow | **Exam Sketch Target**: Fund-Based vs Fee-Based Intermediary Taxonomy\n' + U7_DIAG_1.strip()
    )
    c7 = c7.replace(
        '📊 Diagram Required: YES | Type: Workflow & Mathematical Structure | Source: \nUnit-8.pptx',
        '📊 **Diagram Required**: YES | **Type**: Workflow & Mathematical Structure | **Exam Sketch Target**: Equipment Lease vs Hire Purchase Legal Flow\n' + U7_DIAG_2.strip()
    )
    c7 = c7.replace(
        '📊 Diagram Required: YES | Type: Structural Trade Workflow | Source: \nUnit-9.pptx & Pathak (Ch. 20)',
        '📊 **Diagram Required**: YES | **Type**: Structural Trade Workflow | **Exam Sketch Target**: Factoring vs Forfaiting Trade Finance Flow\n' + U7_DIAG_3.strip()
    )
    c7 = c7.replace(
        '📊 Diagram Required: YES | Type: Lifecycle Workflow | Source: Madura (Ch. 10) & \nPathak',
        '📊 **Diagram Required**: YES | **Type**: Lifecycle Workflow | **Exam Sketch Target**: Venture Capital 5-Stage Investment Lifecycle\n' + U7_DIAG_4.strip()
    )
    c7 = c7.replace(
        '📊 Diagram Required: YES | Type: Structural Issue Management Workflow | Source: \nPathak (Ch. 17) & Unit-7.pptx',
        '📊 **Diagram Required**: YES | **Type**: Structural Issue Management Workflow | **Exam Sketch Target**: Merchant Banking 3-Phase Process\n' + U7_DIAG_5.strip()
    )
    c7 = c7.replace(
        '📊 Diagram Required: YES | Type: Process Architecture | Source: Pathak (Ch. 19) \n& Unit-7.pptx',
        '📊 **Diagram Required**: YES | **Type**: Process Architecture | **Exam Sketch Target**: Credit Rating Agency (CRA) 6-Step Rating Flow\n' + U7_DIAG_6.strip()
    )
    c7 = c7.replace(
        '📊 Diagram Required: YES | Type: Intermediary Architecture | Source: Pathak \n(Ch. 18) & Unit-2.pptx',
        '📊 **Diagram Required**: YES | **Type**: Intermediary Architecture | **Exam Sketch Target**: PMS & Custodial Settlement Architecture\n' + U7_DIAG_7.strip()
    )
    c7 = c7.replace(
        '📊 Diagram Required: YES | Type: Regulatory Jurisdiction Matrix | Source: Unit \n2.pptx & Pathak (Ch. 24)',
        '📊 **Diagram Required**: YES | **Type**: Regulatory Jurisdiction Matrix | **Exam Sketch Target**: RBI vs SEBI Domain Allocation\n' + U7_DIAG_8.strip()
    )
    p7.write_text(c7, encoding='utf-8')
    print('Unit 7 diagrams injected successfully.')

    # Unit 9
    p9 = Path('FIMIS/Unit_9/fimis-unit9-factoring-forfaiting-pyq-bank.md')
    c9 = p9.read_text(encoding='utf-8')
    c9 = c9.replace(
        '`📊 Diagram Required: YES | Type: Structural Flow | Source: Unit-9.pptx / \nPathak Ch. 20`',
        '📊 **Diagram Required**: YES | **Type**: Structural Flow | **Exam Sketch Target**: Tripartite Factoring Mechanism\n' + U9_DIAG_1.strip()
    )
    c9 = c9.replace(
        '`📊 Diagram Required: YES | Type: Classification Tree | Source: Unit-9.pptx / \nPathak Ch. 20`',
        '📊 **Diagram Required**: YES | **Type**: Classification Tree | **Exam Sketch Target**: Factoring Structural Taxonomy\n' + U9_DIAG_2.strip()
    )
    c9 = c9.replace(
        '`📊 Diagram Required: YES | Type: Workflow Architecture | Source: Pathak Ch. \n20`',
        '📊 **Diagram Required**: YES | **Type**: Workflow Architecture | **Exam Sketch Target**: International Two-Factor Cross-Border Flow\n' + U9_DIAG_3.strip()
    )
    c9 = c9.replace(
        '`📊 Diagram Required: YES | Type: Workflow Diagram | Source: Unit-9.pptx / \nPathak Ch. 20`',
        '📊 **Diagram Required**: YES | **Type**: Workflow Diagram | **Exam Sketch Target**: Forfaiting Avalised Bills Discounting Flow\n' + U9_DIAG_4.strip()
    )
    c9 = c9.replace(
        '`📊 Diagram Required: YES | Type: Platform Architecture | Source: Pathak Ch. 20 \n/ Slide Unit 9`',
        '📊 **Diagram Required**: YES | **Type**: Platform Architecture | **Exam Sketch Target**: TReDS Institutional Reverse Auction Platform\n' + U9_DIAG_5.strip()
    )
    c9 = c9.replace(
        '`📊 Diagram Required: YES | Type: Structural Comparison | Source: Unit-9.pptx / \nPathak Ch. 20`',
        '📊 **Diagram Required**: YES | **Type**: Structural Comparison | **Exam Sketch Target**: Factoring vs Forfaiting Comparison Matrix\n' + U9_DIAG_6.strip()
    )
    p9.write_text(c9, encoding='utf-8')
    print('Unit 9 diagrams injected successfully.')

if __name__ == '__main__':
    inject()
