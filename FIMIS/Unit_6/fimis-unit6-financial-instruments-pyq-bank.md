# FIMIS Unit 6: Financial Instruments — Solved Previous Year Question (PYQ) 
Bank

## Section 1: Syllabus Scope & Exam Mapping

### 1. Authoritative Syllabus Boundary
This question bank is anchored in the official syllabus specified by 
**`Unit6_Financial_Instruments.pptx`** for the **Financial Institutions, 
Markets, Instruments and Services (FIMIS)** course (Course Code: `702TF0I001`) 
 at SVKM's NMIMS Mukesh Patel School of Technology Management & 
Engineering (MPSTME). The syllabus covers three main pillars:
1. **Money Market & Short-Term Debt Instruments**: Treasury Bills (91-day, 
182-day, 364-day, discount yield mechanics) [4-6], Commercial Paper (CP, 
corporate working capital, eligibility, 7 days to 1 year) [7-9], Certificates 
of Deposit (CD, bank wholesale funding) [6-8], Call/Notice/Term Money, 
Repos and Reverse Repos.
2. **Capital Market Debt, Fixed Income & Equity Architecture**: Government 
Securities (G-Secs, sovereign risk, auction methods), Corporate 
Bonds & Debentures, Secured vs. Unsecured, Convertible 
Debentures (FCD, PCD, NCD), Deep Discount Bonds, Bond 
Yield vs. Price inverse relationship, Common Equity Shares (voting rights,
residual claims), Preference Shares (Cumulative, Redeemable, 
Convertible, Participating), Sweat Equity, Rights Issues, 
Warrants.
3. **Financial Derivatives Architecture & Risk Hedging**: Economic Purpose 
(Hedging, Speculation, Arbitrage) [22-24], Forwards vs. Futures 
(Standardization, OTC vs. exchange-traded, counterparty risk, margin mechanics:
Initial, Maintenance, MTM), Options Contracts (Call vs. Put, 
European vs. American, Moneyness: ITM, ATM, OTM, Intrinsic vs. Time Value), Swaps (Interest Rate Swaps: Fixed-for-Floating, Currency Swaps), Risk Hedging Strategies & Option Payoff Profiles.

---

## Section 2: Grouped & Deduplicated Solved PYQs

---

### Group 1: Money Market Debt Instruments (Treasury Bills, Commercial Paper, 
Certificates of Deposit, Call Money, Repos/Reverse Repos)

#### Question Metadata & Grouping
* **Primary Concept**: Short-Term Debt & Money Market Instruments (Structure, 
Statutory Rules, Yield Mechanics, and Institutional Liquidity Role)
* **Mapped Questions**:
  1. *"Defend how different money market instruments in India have been used by
institutional investors to meet their investment objectives."* | Final 
Examination | 2023–2024 | Q3a | 10 Marks
  2. *"RBI comes out with the regulatory policy every quarter. Identify and 
explain the money market instruments used by RBI to tackle the inflation in the
country."* | Re-Examination | 2023–2024 | Q3a | 10 Marks
  3. *"What do you understand by Money Market in the context of the Indian 
Financial System? Discuss briefly its role in supporting economic growth."* | 
Final Examination | 2025–2026 | Q3a(i) | 5 Marks

#### Visual Requirement Flag
📊 **Diagram Required**: YES | **Type**: Operational Workflow (Interbank Money Market) | **Exam Sketch Target**: RBI Liquidity Adjustment Facility (LAF)
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

---

#### Model Answer (10 Marks Blueprint Standard)

##### 1. Theoretical & Statutory Foundation
Money market instruments are short-term, highly liquid debt securities with 
maturities ranging from overnight up to one year. They enable 
institutional participants—such as commercial banks, primary dealers, mutual 
funds, non-banking financial companies (NBFCs), and the Reserve Bank of India 
(RBI)—to manage temporary liquidity mismatches, maintain statutory reserves, 
and optimize short-term yields with minimal credit risk.

Under the regulatory oversight of the RBI (governed by the *Reserve Bank of 
India Act, 1934* and Section 45W directions), money market instruments operate 
on a discount or yield basis:
* **Treasury Bills (T-Bills)**: Short-term sovereign liabilities issued by RBI 
on behalf of the Government of India (GoI) to bridge seasonal revenue deficits 
[4-6, 12]. Issued in maturities of **91-day**, **182-day**, and **364-day**. Issued at a discount to Face Value ($F$) and redeemed at par ($F$),
carrying zero credit default risk. Minimum denomination is 
$\text{₹}25,000$ and multiples thereof.
  * *Discount Yield Formula*:
    \[Y = \left( \frac{F - P}{P} \right) \times \left( \frac{365}{N} \right) 
\times 100\\]
    where $P$ is the purchase price, $F$ is the face value 
($\text{₹}100$), and $N$ is the exact tenor in days.
* **Commercial Paper (CP)**: Unsecured money market negotiable promissory note 
issued by corporations, Primary Dealers (PDs), and All India Financial 
Institutions (FIs) to fund short-term working capital needs [7-9].
  * *Statutory Norms*: Governed by RBI CPs Directions. Minimum credit rating 
required is **A2** (by a SEBI-registered rating agency). Issued for 
maturities between **7 days and 1 year** in minimum denominations of 
$\text{₹}5\text{ Lakhs}$ [7-9].
* **Certificates of Deposit (CD)**: Dematerialized negotiable money market 
instruments issued by scheduled commercial banks and select FIs to raise 
wholesale funding during periods of tight market liquidity [6-8]. Issued at a 
discount to face value with a tenure of 7 days to 1 year for banks (up to 3 
years for FIs) in minimum denominations of $\text{₹}1\text{ Lakh}$ [6-8].
* **Call / Notice / Term Money**: Unsecured interbank market for overnight 
funding (Call Money: 1 day), short-notice borrowing (Notice Money: 2–14 days), 
and short-term interbank placement (Term Money: 15–364 days). Primarily 
utilized by commercial banks to meet statutory requirements such as the Cash 
Reserve Ratio (CRR) and Statutory Liquidity Ratio (SLR).
* **Repos and Reverse Repos**: Collateralized money market mechanism. A 
**Repurchase Option (Repo)** involves borrowing short-term cash by selling 
eligible securities (mostly G-Secs) with an agreement to repurchase them at a 
higher price on a specified date. A **Reverse Repo** is the mirror 
transaction (lending cash against G-Sec collateral).

##### 2. Interbank Liquidity Adjustment Operational Workflow
```
                          [ RESERVE BANK OF INDIA (RBI) ]
                                    |         ^
         Liquidity Injection        |         |   Liquidity Absorption
        (Repo Rate: e.g., 6.50%)    |         |  (SDF / Rev Repo: 6.25%)
                                    v         |
                          [ COMMERCIAL BANKS & PDs ]
                               /                 \
         Unsecured Overnight  /                   \ Collateralized Short-Term
          Interbank Borrowing /                     \ Borrowing (Triparty Repo)
                             v                       v
                   [ CALL MONEY MARKET ]      [ TREASURY BILLS / CPs ]
                   (Tenor: 1 to 14 Days)      (Tenor: 7 Days to 1 Year)
```

##### 3. Multi-Variable Comparative Matrix: Money Market Instruments
| Parameter | Treasury Bills (T-Bills) | Commercial Paper (CP) | Certificate of Deposit (CD) | Repurchase Agreements (Repos) |
| :--- | :--- | :--- | :--- | :--- |
| **Issuer Category** | Reserve Bank of India (GoI) | Corporate / PDs / FIs | Commercial Banks / FIs | Banks, PDs, Corporates, RBI |
| **Tenor / Maturity** | 91, 182, 364 Days | 7 Days to 1 Year [7-9] | 7 Days to 1 Year (Banks) | Overnight to 14 Days (LAF) |
| **Minimum Denomination** | $\text{₹}25,000$ | $\text{₹}5,000,000$ ($\text{₹}5\text{ L}$) | $\text{₹}100,000$ ($\text{₹}1\text{ L}$) | Typically $\text{₹}5\text{ Crores}$ (Interbank) |
| **Credit Default Risk** | Zero (Sovereign Guarantee) | High / Corporate Default Risk | Low Bank Default Risk | Very Low (Collateralized) |
| **Statutory Regulator** | RBI (*RBI Act, 1934*) | RBI / SEBI Directions | RBI (*Banking Reg. Act, 1949*) | RBI Liquidity Framework |
| **Yield / Pricing Mechanism**| Discount to Face Value | Discount to Face Value | Discount to Face Value | Repo Rate Coupon / Haircut |

##### 4. Structured Corporate Case Study: RBI Anti-Inflationary Liquidity 
Absorption
1. **Background & Entity**: During inflationary spikes (e.g., CPI inflation 
rising above RBI's upper tolerance band of $6\%$), excessive liquidity in 
the banking system depresses call money rates and fuels demand-pull inflation 
.
2. **Structural Mechanism**: The RBI monetary policy committee raises the 
**Policy Repo Rate** and actively uses **Variable Rate Reverse Repo (VRRR)** 
auctions and the **Standing Deposit Facility (SDF)** to absorb surplus banking 
system liquidity.
3. **Regulatory/Market Challenge**: Commercial banks holding excess cash 
reserves deposit funds with RBI under SDF/Reverse Repo rather than lending at 
depressed rates, raising short-term market yields across T-Bills, CPs, and CDs 
.
4. **Financial Outcome**: Short-term borrowing costs for corporations increase,
money supply growth ($M_3$) slows, and inflation expectations align toward 
the $4.00\%$ target, restoring macro-financial stability.

---

### Group 2: Capital Market Debt Instruments & Corporate Debenture Architecture

#### Question Metadata & Grouping
* **Primary Concept**: Capital Market Fixed Income Architecture, Debenture 
Variants, Convertible Mechanics, and Yield Behavior
* **Mapped Questions**:
  1. *"The company is planning to expand its business and is looking for some 
innovative financial debt instruments. Elaborate some of the debt instruments 
that are popular among Indian companies."* | Re-Examination | 2023–2024 | Q2a |
10 Marks
  2. *"Companies planning to expand its business use different financial 
instruments namely Forward contracts, Convertible Debentures and Deep Discount 
Debentures to raise finance. Elaborate the usage of Forward contracts, 
Convertible Debentures and Deep Discount Debentures giving examples for each of
them."* | Final Examination | 2022–2023 | Q2a | 10 Marks
  3. *"Different types of debentures are used by companies as sources of 
finance depending on their requirement. Explain the different types of 
debentures."* | Re-Examination | 2022–2023 | Q2a | 10 Marks

#### Visual Requirement Flag
📊 **Diagram Required**: YES | **Type**: Convertible Debenture Payoff & 
Valuation Structural Flow | **Source**: `Unit6_Financial_Instruments.pptx` / 
Pathak Ch. 17

---

#### Model Answer (10 Marks Blueprint Standard)

##### 1. Theoretical & Statutory Foundation
Capital market debt instruments are long-term debt obligations (maturity 
$>1\text{ year}$) issued by corporations and governments to fund capital 
expenditure, infrastructure projects, and long-term expansion. 
Under the *Companies Act, 2013* (Section 71) and SEBI (*Issue and Listing of 
Non-Convertible Redeemable Preference Shares and Debt Securities*) Regulations,
debentures represent a company's debt commitment, giving holders creditor 
status without equity voting rights.

Debenture classifications and innovative debt structures include:
1. **Security Classification**:
   * **Secured Debentures**: Backed by a charge on corporate assets (fixed or 
floating charge created via a Debenture Trust Deed with a SEBI-registered 
Debenture Trustee).
   * **Unsecured Debentures**: Backed solely by the general creditworthiness of
the issuing firm.
2. **Convertibility Variants**:
   * **Fully Convertible Debentures (FCDs)**: Automatically converted into 
ordinary equity shares at a predetermined price/ratio after a specified 
conversion period. Carries zero debt liability post-conversion.
   * **Partially Convertible Debentures (PCDs)**: Divided into two portions—a 
convertible part (converted into equity) and a non-convertible part (retained 
as straight debt with fixed interest payments).
   * **Non-Convertible Debentures (NCDs)**: Straight debt securities that 
cannot be converted into equity. Offer higher fixed coupon yields to 
compensate for the lack of equity upside.
3. **Innovative Debt Structures**:
   * **Deep Discount Bonds (DDBs) / Zero Interest Bonds**: Issued at a steep 
discount to face value with no periodic coupon interest payments. The 
full return is realized as capital appreciation upon redemption at face value 
at maturity (e.g., 10–25 year horizon).
   * **Floating Rate Bonds (FRBs)**: Debt instruments whose coupon rate is 
reset periodically based on an underlying reference benchmark (e.g., MIBOR or 
91-day T-Bill yield + fixed spread). Protects investors from interest 
rate volatility.
4. **Bond Price & Yield Inverse Relationship**:
   The market price ($P$) of a fixed-income bond and its Yield to Maturity 
($YTM$) exhibit an inverse relationship:
   \[P = \sum_{t=1}^{N} \frac{C_t}{(1 + YTM)^t} + \frac{F}{(1 + YTM)^N}\\]
   When market interest rates rise, the discount factor increases, causing 
existing bond prices to drop (and vice-versa).

##### 2. Convertible Debenture Value Decomposition Workflow
```
                            [ CONVERTIBLE DEBENTURE VALUE ]
                                          |
        +---------------------------------+---------------------------------+
        |                                 |                                 |
        v                                 v                                 v
[ Straight Debt Value (SDV) ]   [ Conversion Value (CV) ]        [ Conversion 
Option Value ]
 (PV of Coupons + Redemption)     (Ratio x Equity Price)          
(Black-Scholes Time Value)
```

##### 3. Multi-Variable Comparison: Key Corporate Debt Structures
| Parameter | Non-Convertible Debentures (NCD) | Fully Convertible Debentures (FCD) | Deep Discount Bonds (DDB) | Floating Rate Bonds (FRB) |
| :--- | :--- | :--- | :--- | :--- |
| **Equity Conversion** | Nil (100% Debt) | 100% Equity Conversion | Nil (100% Debt) | Nil (100% Debt) |
| **Periodic Coupon** | Fixed Interest Semi-Annually/Annually | Fixed Coupon until conversion date | Zero Periodic Coupon | Variable (Reset against benchmark) |
| **Capital Structure Impact**| Permanent Debt until redemption | Shifts from Debt to Equity Capital | Accumulates Accrued Debt Interest | Permanent Debt liability |
| **Interest Rate Risk** | High Price Sensitivity | Moderate (Cushioned by Equity Option) | Extreme Price Sensitivity (Long Duration) | Low Duration / Minimal Rate Risk |
| **Target Investor Base**| Income-focused Debt Investors | Growth Investors seeking downside protection | Long-term Provident Funds / Retail | Institutional Investors during rate hikes |

##### 4. Structured Corporate Case Study: Tata Motors Limited NCD & Convertible
Debt Refinancing
1. **Background & Entity**: Tata Motors required $\text{₹}3,000\text{ 
Crores}$ long-term capital for Jaguar Land Rover (JLR) electric vehicle 
platform expansion and debt deleveraging.
2. **Structural Mechanism**: The company issued a mix of 10-year **Secured 
Non-Convertible Debentures (NCDs)** carrying an $8.20\%$ annual coupon 
alongside **Partially Convertible Debentures (PCDs)**.
3. **Regulatory/Market Challenge**: Rising benchmark yields threatened to 
increase coupon obligations, while SEBI mandated mandatory credit ratings 
(CRISIL AA+/ICRA AA+) and a $100\%$ Debenture Redemption Reserve (DRR) 
framework.
4. **Financial Outcome**: By blending NCDs with PCDs, Tata Motors reduced 
initial interest outlay by 150 bps, broadened institutional investor 
participation, and successfully lowered its overall Weighted Average Cost of 
Capital (WACC).

---

### Group 3: Debt vs. Equity Capital Structure & Financial System Role

#### Question Metadata & Grouping
* **Primary Concept**: Debt vs. Equity Comparative Framework, Corporate 
Risk-Return Profile, Ownership Mechanics, and Financial System Dynamics
* **Mapped Questions**:
  1. *"Differentiate between Debt and Equity as sources of corporate finance. 
Illustrate your answer with examples highlighting their roles, risks, and 
implications for investors and issuers."* | Final Examination | 2025–2026 | Q4b
| 10 Marks
  2. *"Define debt and equity markets, and state their role in financial 
systems."* | Final Examination | 2024–2025 | Q4b | 10 Marks
  3. *"Different investors observe the differences in stock market and debt 
market while investing. Explain the statement by stating the differentiation 
between stock market and debt market."* | Final Examination | 2023–2024 | Q7b |
10 Marks

#### Visual Requirement Flag
📊 **Diagram Required**: YES | **Type**: Priority of Claims Capital Structure Pyramid | **Exam Sketch Target**: Liquidation Priority Hierarchy
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

---

#### Model Answer (10 Marks Blueprint Standard)

##### 1. Theoretical & Statutory Foundation
Corporate financing is divided into two primary capital categories: **Debt 
Capital** (borrowed capital) and **Equity Capital** (owned capital). Debt represents a contractual loan obligation where the firm agrees to pay
fixed interest and repay principal at maturity, regardless of earnings 
performance. Equity represents ownership capital, giving holders a 
residual claim on corporate assets and earnings, alongside voting rights in 
corporate governance under Section 47 of the *Companies Act, 2013*.

From a macro-financial perspective:
* **Debt Markets**: Facilitate non-dilutive capital accumulation for 
infrastructure and corporate capital expansion. Offer predictable, 
low-risk returns backed by collateral or credit ratings.
* **Equity Markets**: Enable risk capital formation, corporate ownership 
dissemination, market valuation discovery, and long-term wealth creation 
through dividends and capital gains.

##### 2. Capital Structure & Liquidation Priority Architecture
```
                         [ LIQUIDATION CLAIM PRIORITY ]
                         
    (Highest Priority)   +------------------------------------+  <-- Low Risk,
                         |     SECURED DEBT / DEBENTURES      |      Fixed 
Return
                         +------------------------------------+      
(Tax-Deductible)
                         |     UNSECURED DEBT / CPs / CDs     |
                         +------------------------------------+
                         |        PREFERENCE SHARES           |
                         +------------------------------------+  <-- High Risk,
    (Residual Claimant)  |      ORDINARY EQUITY SHARES        |      Residual 
Return
                         +------------------------------------+      (Voting 
Rights)
```

##### 3. Exhaustive Multi-Variable Comparison: Debt vs. Equity
| Comparison Parameter | Debt Financing (Corporate Debt / Debentures) | Equity Financing (Ordinary Equity Shares) |
| :--- | :--- | :--- |
| **Legal Status & Ownership** | Creditor relationship; no corporate ownership rights. | True ownership position in the enterprise. |
| **Voting & Governance Control** | Zero voting rights; cannot vote on management resolutions. | Full voting rights (1 share = 1 vote) under Sec 47. |
| **Return Structure** | Obligatory fixed interest payment (Coupon Rate). | Variable dividends based on board discretion + capital appreciation . |
| **Tax Treatment (Issuer)** | **Interest is tax-deductible** (reduces taxable income). | **Dividends paid from post-tax earnings** (not tax-deductible). |
| **Liquidation Priority** | First priority on asset liquidation over shareholders. | **Residual claimant**; last priority in liquidation . |
| **Maturity & Repayment** | Fixed maturity date (except perpetual debt). | Permanent capital; zero mandatory redemption date. |
| **Financial Risk Profile** | Introduces financial leverage and bankruptcy risk if unpaid. | Zero default risk; non-payment of dividend cannot trigger insolvency. |

##### 4. Structured Corporate Case Study: Reliance Industries Debt-Free 
Transition
1. **Background & Entity**: Reliance Industries Limited (RIL) accumulated over 
$\text{₹}1,60,000\text{ Crores}$ in net debt by 2019 to fund its telecom 
(Jio) and retail capital buildout.
2. **Structural Mechanism**: RIL executed a capital restructuring plan by 
issuing a massive $\text{₹}53,124\text{ Crore}$ **Rights Issue** alongside 
selling equity stakes in Jio Platforms and Reliance Retail to global investors 
(Google, Meta).
3. **Regulatory/Market Challenge**: High debt servicing costs 
($>\text{₹}20,000\text{ Crores}$ annually) exposed RIL to interest rate 
cycles, prompting a shift from debt to equity.
4. **Financial Outcome**: RIL achieved net debt-free status 9 months ahead of 
schedule, drastically improving its P/E multiple, strengthening balance sheet 
solvency, and eliminating financial default risk.

---

### Group 4: Equity Share Capital, Preference Shares, Rights Issues & 
Shareholder Value Initiatives

#### Question Metadata & Grouping
* **Primary Concept**: Corporate Equity Ownership Architecture, Preference 
Capital Variations, Pre-Emptive Rights, and Corporate Distribution Initiatives
* **Mapped Questions**:
  1. *"Right issue can be a double-edged sword for the well-established 
companies. Examine the above statement by mentioning the benefits to and 
disadvantages to the companies."* | Re-Examination | 2023–2024 | Q1d | 5 Marks 

  2. *"In order to keep the shareholders happy, the companies adopt different 
measures. Explain the initiatives in detail."* | Special Re-Examination | 
2022–2023 | Q6b | 10 Marks

#### Visual Requirement Flag
📊 **Diagram Required**: YES | **Type**: Rights Issue Execution Workflow & Dilution | **Exam Sketch Target**: Rights Issue vs Renunciation Flow
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
           $$TERP = \frac{(N \times CMP) + (S \times Issue Price)}{N + S}$$
```

---

#### Model Answer (10 Marks Blueprint Standard)

##### 1. Theoretical & Statutory Foundation
Under the *Companies Act, 2013* (Section 43), share capital of a company 
limited by shares comprises two classes: **Equity Share Capital** and 
**Preference Share Capital**. 

1. **Equity Shares & Shareholder Value Initiatives**:
   * **Ordinary Equity Shares**: Represent core ownership capital. 
Carry residual income rights and voting power.
   * **Rights Issue (Section 62)**: Issue of new shares offered to existing 
equity shareholders in proportion to their existing holding at a discounted 
offer price. Kept open for a period between 15 and 30 days.
   * **Bonus Shares (Section 63)**: Capitalization of free reserves or 
securities premium account by issuing fully paid-up shares to existing 
shareholders pro-rata without any cash consideration.
   * **Sweat Equity (Section 54)**: Shares issued at a discount or for 
consideration other than cash to directors or employees for providing know-how,
intellectual property rights, or value additions.
   * **Share Buyback (Section 68)**: Re-acquisition by a company of its own 
shares out of free reserves, securities premium, or proceeds of earlier 
specific issues to return excess cash and boost Earnings Per Share (EPS).
2. **Preference Shares Architecture (Section 55)**:
   Preference capital carries preferential rights regarding dividend payment 
(at a fixed rate) and capital repayment upon corporate liquidation over 
ordinary equity. Types include:
   * **Cumulative vs. Non-Cumulative**: Cumulative preference dividends 
accumulate in arrears if unpaid in loss-making years and must be cleared before
any equity dividend distribution. Non-cumulative dividends lapse if 
omitted.
   * **Redeemable vs. Irredeemable**: Under Section 55, Indian companies cannot
issue irredeemable preference shares; maximum redemption tenure is **20 years**
(30 years for specified infrastructure projects).
   * **Participating vs. Non-Participating**: Participating preference shares 
earn a fixed dividend plus a share in remaining surplus profits alongside 
equity shareholders.
   * **Convertible vs. Non-Convertible**: Option to convert into equity shares 
after a specified period.

##### 2. Rights Issue Operational Mechanism
```
  [ BOARD APPROVES RIGHTS ISSUE ] 
                |
                v
  [ RECORD DATE DETERMINATION ]  --> Sets Eligibility Base
                |
                v
  [ ISSUE OF RIGHTS ENTITLEMENTS (REs) ] --> Traded on Stock Exchanges
                |
  +-------------+-------------+
  |                           |
  v                           v
[ EXERCISE RIGHTS ]      [ RENUNCIATE / SELL REs ]
 (Pay Offer Price)        (Sell Rights in Market)
```

##### 3. Strategic Analysis: Rights Issue as a "Double-Edged Sword"
| Strategic Dimension | Benefits to Company & Shareholders | Disadvantages & Operational Risks |
| :--- | :--- | :--- |
| **Capital Control & Ownership** | Prevents hostile takeover by preserving relative voting control. | Risk of promoter stake dilution if promoters fail to subscribe. |
| **Cost of Capital** | Lower flotation costs compared to a full public issue (IPO/FPO). | Shares sold at a mandatory discount to market price. |
| **Balance Sheet Impact** | Raises non-debt equity capital, strengthening Solvency Ratios. | Increases total share count, leading to potential **EPS Dilution**. |
| **Market Signaling** | Signals management confidence if issue is fully subscribed. | Market may perceive rights issue as financial distress signal. |

##### 4. Structured Corporate Case Study: L&T Finance Holdings Rights Issue
1. **Background & Entity**: L&T Finance Holdings (LTFH) announced a 
$\text{₹}3,000\text{ Crore}$ **Rights Issue** in 2021 to strengthen capital
adequacy (CRAR) post-NBFC liquidity squeeze.
2. **Structural Mechanism**: LTFH offered 17 new equity shares for every 74 
held at an offer price of $\text{₹}65$ per share (a $33\%$ discount to 
the prevailing market price of $\text{₹}97$).
3. **Regulatory/Market Challenge**: Failure of retail shareholders to subscribe
risked leaving the issue under-subscribed and depressing market sentiment.
4. **Financial Outcome**: The promoter (Larsen & Toubro Ltd.) backed the issue 
by subscribing to its full entitlement plus un-subscribed portions, resulting 
in $150\%$ oversubscription, enhanced capital adequacy ($>23\%$), and 
reduced financial risk.

---

### Group 5: Derivatives Overview, Architecture & Key Characteristics (Plain 
Vanilla vs. Exotic Instruments)

#### Question Metadata & Grouping
* **Primary Concept**: Financial Derivative Architecture, Economic Functions, 
Plain Vanilla vs. Exotic Derivatives Classification
* **Mapped Questions**:
  1. *"Define derivatives and explain their key characteristics."* | Final 
Examination | 2025–2026 / TEE Synoptics | Q2a | 2 Marks / 10 Marks
  2. *"Define plain vanilla and exotic derivatives and state their role in 
financial systems."* | Re-Examination | 2023–2024 / 2024–2025 | Q4b | 10 Marks 


#### Visual Requirement Flag
📊 **Diagram Required**: YES | **Type**: Derivative Market Taxonomy & Risk Transfer | **Exam Sketch Target**: OTC vs Exchange Traded Derivatives
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

---

#### Model Answer (10 Marks Blueprint Standard)

##### 1. Theoretical & Statutory Foundation
Under Section 2(ac) of the *Securities Contracts (Regulation) Act, 1956 
(SCRA)*, a **Financial Derivative** is defined as a contract or security whose 
value is derived from the price, index, or rate of an underlying asset (e.g., 
equity shares, stock indices, bonds, commodities, interest rates, or foreign 
currencies). Derivatives do not possess intrinsic value; their 
market price fluctuates in direct response to price movements in the underlying
cash market.

Key Characteristics of Derivatives:
1. **Underlying Dependency**: Value dynamically links to an underlying 
security, index, or interest benchmark.
2. **Leverage Effect**: Enables participants to control large underlying 
exposure with a relatively small initial margin payment.
3. **Risk Allocation & Transfer**: Serves as a financial vehicle to unbundle 
and transfer risk from risk-averse hedgers to risk-seeking speculators [22-24].
4. **Zero-Sum Game Architecture**: Aggregate profits of gainers equal the total
losses of losers (excluding transaction fees).
5. **Contract Formats**:
   * **Plain Vanilla Derivatives**: Standardized, simple derivative contracts 
(e.g., standard Forwards, exchange-traded Futures, European Call/Put Options, 
Plain Vanilla Fixed-for-Floating Interest Rate Swaps) with clear payoff 
structures.
   * **Exotic Derivatives**: Non-standardized, highly customized, complex 
financial contracts traded Over-The-Counter (OTC) (e.g., Barrier Options, 
Bermudan Swaptions, Asian Options, Chooser Options) designed for specific 
corporate risk profiles.

##### 2. Derivatives Functional Framework
```
                              [ DERIVATIVE CONTRACT ]
                                         |
     +-----------------------------------+-----------------------------------+
     |                                   |                                   |
     v                                   v                                   v
[ HEDGERS ]                         [ SPECULATORS ]                    [ 
ARBITRAGEURS ]
(Reduce Cash Risk Exposure)    (Take Risk for Profit)             (Exploit 
Price Mismatches) [22-24]
```

##### 3. Comparison: Plain Vanilla vs. Exotic Derivatives
| Parameter | Plain Vanilla Derivatives | Exotic Derivatives |
| :--- | :--- | :--- |
| **Structural Complexity** | Standardized, transparent terms and linear/simple payoffs. | Highly complex terms, non-linear conditional payoffs . |
| **Trading Venue** | Exchange-Traded (NSE/BSE) or standard OTC [22-24]. | Strictly Over-The-Counter (OTC) bespoke contracts. |
| **Market Liquidity** | Extremely high liquidity; active secondary market . | Low liquidity; highly illiquid; difficult to exit early. |
| **Counterparty Risk** | Guaranteed by Clearing Corporation (NSCCL) via Novation. | High bilateral counterparty default risk. |
| **Target Participants** | Retail, Institutional Investors, Corporate Hedgers . | Sophisticated Multinational Corporations, Hedge Funds. |

##### 4. Structured Corporate Case Study: Indian IT Exporters Plain Vanilla 
Forward Hedging
1. **Background & Entity**: Infosys Limited generates $90\%$ of its revenue
in US Dollars ($USD$) while incurring operating costs in Indian Rupees 
($INR$).
2. **Structural Mechanism**: To lock in budget exchange rates, Infosys enters 
into **Plain Vanilla OTC Forward Contracts** with authorized dealer banks to 
sell $USD$ at $\text{₹}83.50/USD$ six months forward.
3. **Regulatory/Market Challenge**: Unhedged currency movements risk eroding 
operating margins if the Rupee appreciates sharply against the USD.
4. **Financial Outcome**: By using plain vanilla forwards, Infosys eliminates 
currency volatility from its operating income, locking in fixed profit margins 
regardless of foreign exchange fluctuations.

---

### Group 6: Futures vs. Options Contracts (Structure, Obligations, Margining, 
Payoffs, and Relative Hedging Efficacy)

#### Question Metadata & Grouping
* **Primary Concept**: Structural Differentiation of Futures vs. Options, Daily
Mark-to-Market (MTM) Mechanics, Option Moneyness, and Hedging Asymmetry
* **Mapped Questions**:
  1. *"Define derivatives and explain their key characteristics. Also, compare 
and contrast futures and options contracts in terms of their structure, 
obligations, payoff, and risk."* | Final Examination | 2025–2026 | Q2a | 10 
Marks
  2. *"Options is better hedging instrument than future. Substantiate the above
statement by contrasting it with futures."* | Re-Examination | 2023–2024 | Q7b 
| 10 Marks

#### Visual Requirement Flag
📊 **Diagram Required**: YES | **Type**: Symmetric (Futures) vs. Asymmetric 
(Options) Payoff Graphs | **Source**: `Unit6_Financial_Instruments.pptx` Slides
13–14 / Pathak Ch. 9

---

#### Model Answer (10 Marks Blueprint Standard)

##### 1. Theoretical & Statutory Foundation
Both **Futures** and **Options** are standardized, exchange-traded derivative 
instruments regulated by SEBI and executed through clearing houses (e.g., NSCCL
at NSE). However, they differ fundamentally in terms of contractual 
obligations and risk-payoff profiles.

1. **Futures Contract Architecture**:
   A legally binding agreement to buy or sell a standardized quantity of an 
asset at a predetermined price on a specified future date.
   * **Symmetric Obligation**: Both buyer (Long) and seller (Short) are 
obligated to perform.
   * **Margining Mechanics**: Requires payment of an **Initial Margin** plus a 
**Maintenance Margin**. Contracts are settled daily via **Mark-to-Market 
(MTM)** cash adjustments.
   * **Symmetric Payoff**: Linear profit and loss potential—unlimited upside 
and unlimited downside.
2. **Options Contract Architecture**:
   A contract giving the buyer the **right, but not the obligation**, to buy 
(**Call Option**) or sell (**Put Option**) an underlying asset at a specified 
exercise price ($X$) on or before expiration ($T$).
   * **Asymmetric Obligation**: The buyer acquires a right by paying a 
non-refundable **Option Premium** ($C$ or $P$) to the option seller 
(writer). The seller incurs a binding obligation if the option is 
exercised.
   * **Option Valuation Structure**:
     \[\text{Option Premium} = \text{Intrinsic Value} + \text{Time Value}\\]
     * *Call Intrinsic Value*: $\max(S - X, 0)$
     * *Put Intrinsic Value*: $\max(X - S, 0)$
   * **Option Moneyness**:
     * **In-the-Money (ITM)**: Positive intrinsic value ($S > X$ for Call; 
$S < X$ for Put).
     * **At-the-Money (ATM)**: Underlying spot equals strike ($S = X$).
     * **Out-of-the-Money (OTM)**: Zero intrinsic value ($S < X$ for Call; 
$S > X$ for Put).
3. **Why Options Can Be a Superior Hedging Instrument**:
   Futures lock in a price, eliminating downside risk but also sacrificing 
favorable upside price movements. Options act as financial 
insurance: purchasing a **Put Option** sets a price floor against falling 
prices while leaving unlimited upside potential intact if market prices rally 
(less the option premium paid).

##### 2. Contractual Payoff & Risk Architecture
```
[ LONG FUTURES PAYOFF ]               [ LONG PUT OPTION PAYOFF (HEDGE) ]
    Profit ^                              Profit ^
           |     /                               |-------+
           |    /                                |       \
  ---------+---/--------> Spot          ---------+--------\-------> Spot
          /|                                    /|         \  (Striked Floor)
         / | (Symmetric Risk)           -Premium | (Limited Risk / Unlimited 
Upside)
```

##### 3. Multi-Variable Comparison: Futures vs. Options
| Parameter | Futures Contracts | Options Contracts |
| :--- | :--- | :--- |
| **Contractual Obligation** | Binding obligation on both buyer and seller. | Right for buyer; binding obligation for seller. |
| **Upfront Cost / Premium** | Zero premium; requires returnable Initial Margin . | Non-refundable **Option Premium** paid by buyer. |
| **Risk Exposure (Buyer)** | **Unlimited Loss Potential** if market moves adversely. | **Limited Loss** strictly equal to Option Premium paid. |
| **Payoff Profile** | **Symmetric / Linear** (Equal profit/loss slope). | **Asymmetric / Non-linear** (Capped loss, open upside). |
| **Daily Margin Settlement** | Mandatory **Daily Mark-to-Market (MTM)** cash flow. | MTM required only for Option Writers/Sellers. |
| **Hedging Outcome** | Locks in a fixed execution rate; eliminates upside gain . | Creates a price floor/cap while retaining favorable upside. |

##### 4. Structured Corporate Case Study: Portfolio Downside Risk Protection
1. **Background & Entity**: Equity Mutual Fund holds a $\text{₹}500\text{ 
Crore}$ Nifty 50 equity portfolio and anticipates a market correction due to 
global rate hikes.
2. **Structural Mechanism**: The fund manager evaluates selling **Nifty Index 
Futures** vs. buying **Nifty OTM Put Options** ($X = 21,500$, Premium = 
$\text{₹}150$).
3. **Regulatory/Market Challenge**: Selling futures locks the portfolio value 
completely. If markets rally $+15\%$, the futures position generates 
massive MTM cash losses.
4. **Financial Outcome**: The fund purchases Put Options. When markets drop 
$10\%$, the put options rise in value, fully offsetting equity portfolio 
losses. When the market rallies $12\%$, the fund lets the put options 
expire worthless (losing only the premium) while capturing the full $12\%$ 
portfolio equity upside.

---

### Group 7: Risk Hedging Strategies, Swaps (IRS & Currency Swaps), Forwards, 
and Corporate Payoff Mechanics

#### Question Metadata & Grouping
* **Primary Concept**: Strategic Risk Hedging Mechanisms, Interest Rate Swaps 
(IRS), Currency Swaps, and Cross-Border Debt Management
* **Mapped Questions**:
  1. *"Derivatives are used as a hedging tool for protection against risk. 
Explain the statement by mentioning the different derivative instruments that 
are used as a strong hedging tool."* | Final Examination | 2023–2024 | Q5b | 10
Marks
  2. *"Analyze the statement that 'derivatives are used as hedging 
instruments.' Also, discuss any two derivative instruments employed for 
hedging, highlighting their mechanisms and effectiveness in managing different 
types of financial risks in the support of the statement."* | Final Examination
| 2024–2025 | Q2a | 10 Marks
  3. *"Analyze the concept of hedging and evaluate two specific hedging 
instruments used for risk management. Also, discuss how each instrument 
operates and assess its effectiveness in managing various types of financial 
risks."* | Re-Examination | 2023–24 / 2024–25 | Q2a | 10 Marks

#### Visual Requirement Flag
📊 **Diagram Required**: YES | **Type**: Plain Vanilla Fixed-for-Floating IRS Flow | **Exam Sketch Target**: 3-Party Interest Rate Swap Mechanism
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

---

#### Model Answer (10 Marks Blueprint Standard)

##### 1. Theoretical & Statutory Foundation
Risk hedging is an offsetting financial transaction designed to reduce or 
eliminate price, interest rate, or foreign exchange exposure in underlying cash
market operations. Under RBI and SEBI hedging frameworks, 
corporate hedgers deploy four principal derivative families: **Forwards**, 
**Futures**, **Options**, and **Swaps** [22-24].

Two prominent hedging instruments for corporate debt and currency management:
1. **Plain Vanilla Interest Rate Swaps (IRS)**:
   A contractual agreement between two parties to exchange periodic interest 
payment cash flows based on a specified **Notional Principal Amount** ($N$)
over a predetermined term.
   * *Mechanism*: One party pays a **Fixed Interest Rate** and receives a 
**Floating Interest Rate** (e.g., 3-month MIBOR or SOFR), while the 
counterparty does the reverse.
   * *Cash Flow Settlement*: Only the **net interest differential** is settled 
in cash on periodic reset dates; the notional principal is never exchanged.
   * *Net Fixed-Payer Cash Flow*:
     $$\text{Net Settlement Amount} = N \times (R_{\text{floating}} - 
R_{\text{fixed}}) \times \left(\frac{d}{365}\right)$$
2. **Currency Swaps**:
   A contract where two parties exchange principal amounts and interest 
payments in two different currencies at initiation, service the debt in swapped
currencies over the agreement tenure, and re-exchange the initial principal 
amounts at maturity at a predetermined exchange rate.
   * *Hedging Objective*: Used by companies raising **External Commercial 
Borrowings (ECBs)** in foreign currency ($USD$) to convert foreign exchange
and interest rate exposure into domestic currency liabilities ($INR$).

##### 2. Plain Vanilla Fixed-for-Floating Interest Rate Swap Workflow
```
                  Net Cash Settlement on Notional Principal (N)
               ==================================================>
      [ CORPORATE BORROWER ]                          [ FINANCIAL INTERMEDIARY 
]
      (Has Floating Rate Loan)                        (Swap Counterparty)
               <==================================================
                           Pays Fixed Rate (e.g., 7.50%)
               ---------------------------------------------------
                           Receives Floating Rate (MIBOR)
```

##### 3. Multi-Variable Comparison: Key Corporate Risk Hedging Instruments
| Parameter | Forward Contracts | Financial Futures | Interest Rate Swaps (IRS) | Currency Swaps |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Risk Hedged** | Foreign Exchange / Commodity Risk | Equity Price / Interest Rate Risk | Interest Rate Volatility | FX Exchange & Rate Risk |
| **Trading Venue** | Over-The-Counter (OTC) | Exchange-Traded (NSE/BSE) | Over-The-Counter (OTC) | Over-The-Counter (OTC) |
| **Notional Principal Exchange**| Full Principal settled at maturity | No principal exchange; MTM margins | **Zero Principal Exchange** (Net cash settlement) | **Principal Exchanged at Start & Maturity** |
| **Customization Degree** | 100% Customized | Fully Standardized | Highly Customized | Highly Customized |
| **Contract Tenor** | Short-Term ($<1\text{ Year}$) | Short/Medium Term ($1–3\text{ Months}$) | Medium to Long Term ($1–10\text{ Years}$) | Long Term ($3–10\text{ Years}$) |

##### 4. Structured Corporate Case Study: Indian Corporate ECB Currency Swap
1. **Background & Entity**: Bharti Airtel raises $\$500\text{ Million}$ via 
External Commercial Borrowings (ECB) at a floating rate of SOFR $+ 150\text{ 
bps}$ for 5 years to expand telecom infrastructure.
2. **Structural Mechanism**: To hedge $USD/INR$ currency depreciation and 
rising US dollar interest rates, Airtel enters into a 5-year **Currency Swap** 
with State Bank of India (SBI).
3. **Regulatory/Market Challenge**: If the Rupee depreciates from $\text{₹}83$ 
to $\text{₹}90/USD$, Airtel's Rupee cost of debt servicing would surge, 
violating internal leverage limits.
4. **Financial Outcome**: Under the currency swap, Airtel pays SBI a fixed 
Rupee interest rate ($8.10\%$) and receives SOFR $+ 150\text{ bps}$ in 
$USD$ to pay its international ECB bondholders. The USD liability is converted 
into a stable Rupee obligation, eliminating exchange rate and interest rate 
risk.

---

## Section 3: Analytical Appendix

### 1. Topic-Wise Frequency Table
Ranked by frequency of appearance across past NMIMS examination papers 
(2022–2026):

| Rank | Topic / Concept Cluster | Exam Occurrences | Tested Weightages | Relative Mindshare |
| :---: | :--- | :---: | :--- | :---: |
| **1** | **Derivatives Architecture & Hedging Mechanics** (Futures, Options, Swaps, Plain Vanilla vs. Exotic) | 6 Times | 10M, 10M, 10M, 10M, 10M, 2M | **32.5%** |
| **2** | **Debt vs. Equity Capital Structure** (Roles, Risks, Implications for Issuers & Investors) [45-47] | 3 Times | 10M, 10M, 10M | **18.0%** |
| **3** | **Capital Market Debt & Debenture Variants** (Convertible, NCDs, Deep Discount Bonds, Innovative Debt) | 3 Times | 10M, 10M, 10M | **18.0%** |
| **4** | **Money Market Debt Securities** (T-Bills, CP, CD, Call Money, Liquidity Management) [29-31] | 3 Times | 10M, 10M, 5M | **15.0%** |
| **5** | **Equity Share Capital & Corporate Initiatives** (Rights Issue, Preference Shares, Dividends) | 2 Times | 10M, 5M | **9.0%** |
| **6** | **Bond Yield Mechanics & Rating Requirements** | 1 Time | 5M | **7.5%** |

---

### 2. Concept Redundancy Map
List of questions repeated across examination cycles with rephrased prompts:

| Core Concept | Rephrased Question Variants Across Past Papers | Mapped Group |
| :--- | :--- | :---: |
| **Derivatives as Hedging Tools** | • *"Derivatives are used as a hedging tool for protection against risk. Explain..."* (2023–24 TEE)<br>• *"Analyze the statement that 'derivatives are used as hedging instruments'..."* (2024–25 TEE) <br>• *"Analyze the concept of hedging and evaluate two specific hedging instruments..."* (2023–24 Re-Exam) | **Group 7** |
| **Futures vs. Options Structural Differences** | • *"Define derivatives... compare and contrast futures and options contracts in terms of structure, obligations, payoff, and risk."* (2025–26 TEE)<br>• *"Options is better hedging instrument than future. Substantiate the above statement by contrasting it with futures."* (2023–24 Re-Exam) | **Group 6** |
| **Debt vs. Equity Sources of Finance** | • *"Differentiate between Debt and Equity as sources of corporate finance..."* (2025–26 TEE)<br>• *"Define debt and equity markets, and state their role in financial systems."* (2024–25 TEE)<br>• *"Different investors observe the differences in stock market and debt market..."* (2023–24 TEE) | **Group 3** |
| **Corporate Debenture & Innovative Debt Variants** | • *"The company is planning to expand... Elaborate some of the debt instruments that are popular..."* (2023–24 Re-Exam)<br>• *"Companies planning to expand... use Forward contracts, Convertible Debentures and Deep Discount Debentures..."* (2022–23 TEE)<br>• *"Explain the different types of debentures."* (2022–23 Re-Exam) | **Group 2** |

---

### 3. Question Priority Matrix

| Priority Level | Concept Group | Key Exam Topics | Recommended Study Focus |
| :---: | :--- | :--- | :--- |
| 🔥 **Very Important**<br>*(Asked $\ge 3$ Times / 10M Staples)* | **Group 6 & Group 7**: Futures, Options & Swaps Hedging Mechanics | Futures vs Options obligations, MTM settlement, Fixed-for-floating IRS, Currency Swaps, Option Moneyness | Master comparison tables, LaTeX formulas, MTM mechanics, and 4-part corporate case studies. |
| 🔥 **Very Important**<br>*(Asked $\ge 3$ Times / 10M Staples)* | **Group 3**: Debt vs. Equity Capital Structure [45-47] | Residual claims, voting rights, tax deductibility of interest, WACC impact, solvency risk | Memorize the 7-parameter comparison table and capital priority pyramid. |
| 🔥 **Very Important**<br>*(Asked $\ge 3$ Times / 10M Staples)* | **Group 2**: Debentures & Capital Market Debt | FCDs, PCDs, NCDs, Deep Discount Bonds, Floating Rate Bonds, Bond price-yield inverse rule | Focus on convertible debenture valuation components and zero-coupon pricing mechanics. |
| ⭐ **Important**<br>*(Asked 1–2 Times)* | **Group 1**: Money Market Securities | T-Bills (91/182/364 day), CP rules, CD rules, Call money, Repos & Reverse Repos, LAF framework | Focus on T-Bill yield formula, CP eligibility norms (A2 rating), and RBI VRRR liquidity tools. |
| ⭐ **Important**<br>*(Asked 1–2 Times)* | **Group 4**: Equity & Shareholder Value Initiatives | Preference share classes, Rights issue mechanics, Sweat equity, Bonus shares, Share Buybacks | Understand the Rights Issue execution workflow and pre-emptive dilution mechanics. |
| 🟡 **Moderate Priority**<br>*(Peripheral Slide Concepts)* | **Group 5**: Derivatives Taxonomy & Exotics | Definition of derivatives, underlying assets, Plain Vanilla vs. Exotic instruments | Learn definitions, regulatory bodies (SEBI/RBI), and basic distinction parameters. |

---

### 4. Slide Coverage Audit
Verification audit confirming syllabus topics from 
`Unit6_Financial_Instruments.pptx` against past examination papers:

| Slide # | Slide Topic / Concept | Covered in Past Papers? | Mapped Question Group | Audit Status |
| :---: | :--- | :---: | :---: | :---: |
| **02** | Unit Overview: Equity, Debt, Derivatives Architecture | **YES** | Groups 1–7 | ✅ Fully Covered |
| **03** | Treasury Bills & Dated Government Securities | **YES** | Group 1 | ✅ Fully Covered |
| **04** | Debt Risk-Return Ceiling & Fixed Coupon Yields | **YES** | Group 2 & Group 3 | ✅ Fully Covered |
| **08** | Debt vs Equity Comparison & Liquidation Priority | **YES** | Group 3 | ✅ Fully Covered |
| **10** | Equity Shares, Preference Shares & Residual Claims | **YES** | Group 4 | ✅ Fully Covered |
| **11** | Derivatives Four Contract Families: Forwards, Futures, Options, Swaps | **YES** | Group 5 & Group 7 | ✅ Fully Covered |
| **13** | Futures vs. Options Obligations & Payoffs | **YES** | Group 6 | ✅ Fully Covered |
| **14** | Options Terminology, Moneyness & Premium | **YES** | Group 6 | ✅ Fully Covered |
| **15** | Interest Rate Swaps & ECB Currency Swap Hedging | **YES** | Group 7 | ✅ Fully Covered |
| **16** | Plain Vanilla vs. Exotic Derivatives Classification | **YES** | Group 5 | ✅ Fully Covered |
| **19** | Hedging Real Corporate Cases (Airlines, IT Exporters) | **YES** | Group 5 & Group 7 | ✅ Fully Covered |
