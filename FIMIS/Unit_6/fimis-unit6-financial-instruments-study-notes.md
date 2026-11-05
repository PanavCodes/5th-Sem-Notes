# Unit 6: Financial Instruments — Comprehensive Study Notes (FIMIS)

> **Course Title**: Financial Institutions, Markets, Instruments and Services (FIMIS)  
> **Course Code**: 702TF0I001 | B.Tech / MBA Tech (Semester V / VI)  
> **Primary Source**: `Unit6_Financial_Instruments.pptx` (Slides 1–22)  
> **Target Standard**: 5-Mark Concise Answers & 10-Mark Essay Blueprints  

---

## 1. Structure & Architecture of Debt Instruments

### ✍️ 5-Mark Quick Shot: Debt Instruments Overview

*   **Core Definition**: Debt instruments represent borrowed capital that obligates the issuer (borrower) to repay the principal amount along with periodic interest (coupon) to the investor (lender) over a specified time horizon.
*   **4 Defining Characteristics**:
    1.  **Fixed/Stipulated Return**: Contractual interest payments (fixed or floating benchmarked) with zero participation in corporate profits.
    2.  **Repayment Priority**: Seniority in claim on income and assets; debt holders are paid before equity holders during liquidation.
    3.  **Defined Maturity**: Fixed tenure (ranging from 7 days for money market paper up to 30 years for sovereign bonds), except perpetual bonds.
    4.  **Lower Risk & Limited Upside**: Lower volatility and default risk compared to equity, but return is capped at the agreed coupon rate.
*   **Key Debt Categories**:
    *   *Sovereign Debt*: Government Securities (G-Secs) & Treasury Bills (T-Bills).
    *   *Corporate Debt*: Corporate Bonds (Secured), Debentures (Unsecured), Non-Convertible Debentures (NCDs), Commercial Papers (CPs).
    *   *Bank/Institutional Debt*: Certificates of Deposit (CDs), Institutional Tax-Free Bonds (NABARD, HUDCO).

#### 📊 Quick Summary Table: Debt Instrument Taxonomies
| Instrument Class | Typical Issuer | Tenure / Maturity | Security / Collateral | Primary Pricing Mechanism |
| :--- | :--- | :--- | :--- | :--- |
| **T-Bills** | Government of India (RBI) | 91, 182, 364 Days | Sovereign (Risk-Free) | Issued at discount, redeemed at Par |
| **Dated G-Secs** | Central / State Governments | 5 to 30 Years | Sovereign (Risk-Free) | Semi-annual fixed/floating coupon |
| **Commercial Papers** | Highly-rated Corporates/FIs | 7 Days to 1 Year | Unsecured Promissory Note | Issued at discount to Face Value |
| **Certificates of Deposit**| Commercial Banks / FIs | 7 Days to 1 Year (Banks) | Dematerialized Money Paper | Issued at discount to Face Value |
| **Corporate NCDs** | Private / Public Corporates | 1 to 10+ Years | Secured or Unsecured | Fixed/Floating periodic coupon |
| **Institutional Bonds** | Development FIs (NABARD) | 10 to 20+ Years | Government Guaranteed / AAA | Fixed Coupon (Tax-Free or Taxable) |

---

### 📚 10-Mark Comprehensive Blueprint: Debt Instruments Architecture

#### Theoretical Foundations & Sovereign Debt Mechanics
Debt instruments serve as the primary credit-allocation mechanism in the financial system, bridging deficit units (governments and corporations requiring capital for infrastructure or working capital) with surplus units (institutional and retail investors seeking predictable cash flows). 

1.  **Sovereign Debt (Government Securities - G-Secs)**:
    *   **Issuance Authority**: Issued by the Reserve Bank of India (RBI) on behalf of the Government of India (GoI) to finance fiscal deficits.
    *   **Treasury Bills (T-Bills)**: Short-term zero-coupon debt instruments issued in three standard tenures: 91-day, 182-day, and 364-day. T-Bills pay no explicit interest; instead, they are issued at a discount to face value and redeemed at par ($100$).
        $$\text{Annualized Yield } (Y) = \frac{F - P}{P} \times \frac{365}{D} \times 100$$
        *Where $F = \text{Face Value}$, $P = \text{Issue/Purchase Price}$, and $D = \text{Tenure in Days}$.*
    *   **Dated Government Securities**: Long-term sovereign bonds with maturities spanning 5 to 30 years. They carry a fixed or floating coupon paid semi-annually.
    *   ⭐ **Must Remember — The 10-Year G-Sec Benchmark**: India's most critical debt benchmark is the 10-year Government Security (yielding ~7% through 2024–25). Its yield serves as the sovereign risk-free baseline used by banks, NBFCs, and rating agencies to price home loans, corporate bonds, and commercial credit across the country.

2.  **Corporate & Money Market Debt Instruments**:
    *   **Corporate Bonds vs. Debentures**: Corporate bonds are typically secured by a specific charge or mortgage on company assets. Debentures represent long-term creditorship instruments that can be secured or unsecured.
    *   **Non-Convertible Debentures (NCDs)**: Pure debt instruments that cannot be converted into equity shares. They offer higher interest rates than bank fixed deposits and are rated by credit rating agencies (CRISIL, ICRA, CARE).
    *   **Commercial Papers (CPs)**: Short-term unsecured promissory notes issued by corporate entities with high credit ratings (minimum A2/A1+) to meet short-term working capital needs. Tenures range from 7 days to 1 year.
    *   **Certificates of Deposit (CDs)**: Dematerialized negotiable money market paper issued by commercial banks and financial institutions against funds deposited. Bank CDs have tenures from 7 days to 1 year; FIs can issue CDs for 1 to 3 years.
    *   **Institutional Tax-Free Bonds**: Issued by public sector financial institutions such as NABARD, HUDCO, and PFC to finance national housing and rural infrastructure projects. They offer long tenures (10–20 years), AAA sovereign support, and tax-exempt coupon payments under Section 10(15)(iv)(h) of the Income Tax Act.

#### The 5 Primary Risks in Debt Security Portfolios
🧠 **Must Understand**: Every debt investor balances yield against five distinct financial risks:
1.  **Credit / Default Risk**: The probability that the issuer defaults on interest payments or principal redemption. Sovereign debt carries zero default risk ($CR = 0$), whereas corporate bonds carry credit risk proportional to their credit rating.
2.  **Interest Rate Risk**: The inverse relationship between bond prices ($P$) and market interest rates ($r$). As market yield rises, existing fixed-coupon bond prices fall ($P \downarrow$). Long-tenure bonds exhibit higher duration and greater price sensitivity to interest rate fluctuations.
3.  **Liquidity Risk**: The ease with which a debt instrument can be converted into cash at fair market value. Dated G-Secs are highly liquid, whereas corporate debentures frequently suffer from illiquid secondary markets.
4.  **Inflation Risk**: The risk that rising inflation erodes the real purchasing power of fixed nominal coupon payments.
5.  **Market Risk**: Price fluctuations driven by broader macroeconomic sentiment, monetary policy shifts, or liquidity squeezes.

```
                    ┌─────────────────────────────────────────┐
                    │      5 Core Debt Portfolio Risks        │
                    └────────────────────┬────────────────────┘
                                         │
     ┌──────────────────┬────────────────┼──────────────────┬──────────────────┐
     ▼                  ▼                ▼                  ▼                  ▼
┌─────────┐        ┌─────────┐      ┌─────────┐        ┌─────────┐        ┌─────────┐
│ Credit  │        │ Interest│      │Liquidity│        │Inflation│        │ Market  │
│  Risk   │        │ Rate R. │      │  Risk   │        │  Risk   │        │  Risk   │
└─────────┘        └─────────┘      └─────────┘        └─────────┘        └─────────┘
 (Default)          (Price vs        (Secondary         (Real Value        (Systemic
                     Yield)          Trading)            Erosion)           Shocks)
```

#### Real-World Case Studies: Corporate Debt & Institutional Bonds
*   🏢 **Reliance Industries vs. IL&FS 2018 Credit Freeze**:
    *   *Reliance Industries*: Demonstrates top-tier corporate debt issuance, routinely raising tens of thousands of crores through secured NCDs at fine, highly competitive coupon rates backed by AAA ratings.
    *   *IL&FS Default Crisis (2018)*: Infrastructure Leasing & Financial Services (IL&FS) defaulted on its commercial papers and inter-corporate deposits in September 2018. Despite carrying AAA ratings shortly before the collapse, the default frozen the entire ₹10-lakh-crore Indian commercial paper market, triggering an acute liquidity crunch across Non-Banking Financial Companies (NBFCs) and mutual funds.
    *   *Lesson*: Credit ratings can lag structural risks; unsecured money market instruments like CPs carry severe contagion risk during defaults.
*   🏛️ **NABARD Tax-Free Bonds**:
    *   NABARD and HUDCO issued long-dated, tax-free bonds to mobilize low-cost long-term capital for rural infrastructure and housing projects. Carrying AAA ratings and explicit sovereign backing, these bonds offered conservative retail investors safety and tax-exempt yields.

---

## 2. Equity Instruments & Comparative Capital Structure

### ✍️ 5-Mark Quick Shot: Equity Instruments Overview

*   **Core Definition**: Equity represents ownership capital in an enterprise raised through the issuance of shares. Equity holders become fractional owners who share in the firm's growth and profits (via dividends and capital gains) but bear residual operational risk.
*   **Role of Exchanges (BSE & NSE)**: Listed stock exchanges—the BSE (established 1875, Asia's oldest exchange) and NSE (established 1992)—provide secondary market liquidity, transparent price discovery, and enforce corporate governance and continuous disclosure rules.
*   **4 Fundamental Features of Equity**:
    1.  **Ownership Stake**: Direct ownership share in the net assets and retained earnings of the enterprise.
    2.  **No Fixed Returns**: Returns are variable and unguaranteed, depending entirely on company profitability and management's dividend distribution policy.
    3.  **Residual Claimants**: In liquidation, equity holders are paid last after all debt creditors, preference shareholders, and statutory liabilities are fully satisfied.
    4.  **Voting Rights**: Equity shareholders exercise corporate control by voting on major corporate decisions, director elections, and mergers/acquisitions.

#### 📊 Quick Summary Table: Debt vs. Equity Structure
| Parameter | Debt Instruments | Equity Instruments |
| :--- | :--- | :--- |
| **Legal Status** | Lender / Creditor | Shareholder / Owner |
| **Return Structure** | Fixed interest payment (Mandatory) | Variable dividends + Capital gains (Discretionary) |
| **Investor Risk** | Lower risk; return capped at coupon | Higher risk; unlimited upside, no downside floor |
| **Liquidation Priority**| First priority claim on assets | Last priority claim (Residual claimant) |
| **Corporate Control** | Zero voting rights | Full voting rights on key resolutions |
| **Maturity Period** | Fixed maturity date (Stipulated tenure) | Indefinite / Perpetual ownership |
| **Tax Treatment** | Interest paid is tax-deductible expense | Dividends paid out of post-tax profits |

---

### 📚 10-Mark Comprehensive Blueprint: Equity Instruments & Comparative Analysis

#### Comprehensive Breakdown of Equity Features
Equity capital forms the primary risk-absorbing cushion of a corporate balance sheet. By selling equity, a company secures perpetual capital without incurring fixed debt-servicing obligations.

1.  **Ownership & Capital Formation**: Equity share capital is divided into units of equal face value (e.g., ₹1, ₹2, or ₹10 per share). Investors purchasing equity shares acquire voting power proportional to their shareholding.
2.  **Governance & Statutory Disclosures**: Stock exchanges (BSE & NSE) enforce strict listing obligations under SEBI (LODR) Regulations 2015. Companies must publish quarterly financial results, disclose price-sensitive information immediately, and maintain independent board representation.
3.  **Residual Risk & Return Mechanics**: Equity offers asymmetric upside potential:
    *   *Upside*: Shareholders enjoy unlimited upside through share price appreciation and dividend distributions as company cash flows grow.
    *   *Downside*: If the company suffers insolvency, equity holders face total capital loss as residual claimants.

#### Deep Multi-Parameter Comparative Breakdown: Debt vs. Equity

```
                             ┌────────────────────────┐
                             │ Corporate Capital Structure│
                             └───────────┬────────────┘
                                         │
                   ┌─────────────────────┴─────────────────────┐
                   ▼                                           ▼
      ┌─────────────────────────┐                 ┌─────────────────────────┐
      │     Debt Financing      │                 │    Equity Financing     │
      ├─────────────────────────┤                 ├─────────────────────────┤
      │ • Senior Creditor Claim │                 │ • Residual Owner Claim  │
      │ • Mandatory Interest    │                 │ • Discretionary Dividend │
      │ • Tax-Deductible Expense│                 │ • Post-Tax Capital      │
      │ • Zero Voting Control   │                 │ • Voting & Governance   │
      │ • Fixed Maturity        │                 │ • Perpetual Horizon     │
      └─────────────────────────┘                 └─────────────────────────┘
```

1.  **Ownership vs. Creditorship**: Debt holders lend capital under a restrictive trust deed without gaining equity ownership. Equity holders purchase actual ownership rights in the firm's balance sheet.
2.  **Financial Obligation & Risk**: Debt interest payments are legally binding obligations; failure to pay triggers bankruptcy proceedings under the Insolvency and Bankruptcy Code (IBC) 2016. Equity dividends are declared at the discretion of the Board of Directors only when distributable profits exist.
3.  **Cost of Capital & Tax Shield**: 
    *   *Debt Cost ($K_d$)*: Cheaper due to lower risk and the interest tax shield:
        $$K_d = i \times (1 - t)$$
        *Where $i = \text{nominal interest rate}$ and $t = \text{corporate tax rate}$.*
    *   *Equity Cost ($K_e$)*: Higher cost of capital reflecting the risk premium demanded by investors for bearing residual risk.
4.  **Capital Structure Dilution**: Issuing debt does not dilute existing shareholder control or EPS. Issuing fresh equity dilutes ownership percentage and voting power.

#### Real-World Case Study: Zomato’s 2021 Initial Public Offer (IPO)
*   🚀 **Context & Structure**: In July 2021, food-tech platform Zomato Limited launched its IPO on the NSE and BSE, raising ₹9,375 crore (₹9,000 crore fresh issue + ₹375 crore offer for sale).
*   📈 **Equity Dynamics**: Investors buying Zomato equity became part-owners of a loss-making but high-growth tech platform. The stock opened at a 51% premium over its issue price of ₹76, peaked above ₹160, later corrected sharply to below ₹50 during global tech sell-offs, before recovering strongly.
*   💡 **Comparative Contrast**: A Zomato debenture holder would have received a fixed 8% coupon regardless of whether Zomato made profits or losses. Conversely, Zomato equity shareholders bore extreme price volatility, receiving no dividends, but participating directly in the enterprise's long-term equity valuation shifts.

---

## 3. Financial Derivatives: Structure, Families & Classification

### ✍️ 5-Mark Quick Shot: Derivatives Overview

*   **Core Definition**: A derivative is a financial contract whose value is derived from the price, index, or value of an underlying asset (such as equities, market indices, commodities, currencies, or interest rates).
*   **3 Market Participants**:
    1.  **Hedgers**: Risk-averse entities using derivatives to lock in prices and eliminate adverse market movements.
    2.  **Speculators**: Risk-seeking traders taking unhedged positions to profit from anticipated price movements.
    3.  **Arbitrageurs**: Traders who simultaneously buy and sell in different markets to exploit risk-free price differentials.
*   **4 Core Contract Families**:
    1.  **Forwards**: Customized OTC contracts to buy/sell an asset at a future date at an agreed price.
    2.  **Futures**: Standardized, exchange-traded contracts with margin requirements, daily Mark-to-Market (MTM), and clearinghouse guarantees.
    3.  **Options**: Contracts granting the right, but not the obligation, to buy (Call) or sell (Put) an asset at a set strike price ($K$).
    4.  **Swaps**: Customized OTC agreements to exchange cash flow streams (e.g., fixed vs. floating interest rates) over a specified period.

#### 📊 Quick Comparison Table: Plain Vanilla vs. Exotic Derivatives
| Feature | Plain Vanilla Derivatives | Exotic Derivatives |
| :--- | :--- | :--- |
| **Structure & Terms** | Standardized, simple, transparent rules | Customized, complex, non-standard terms |
| **Trading Venue** | Exchange-traded (NSE, BSE, MCX) | Over-the-Counter (OTC) private deals |
| **Exercise Options** | Standard American or European exercise | Path-dependent (Knock-In / Knock-Out barriers) |
| **Liquidity & Pricing** | Highly liquid; transparent order books | Illiquid; priced via Monte Carlo/lattice models |
| **Primary Target** | General corporate & institutional hedging | Sophisticated institutional risk structures |

---

### 📚 10-Mark Comprehensive Blueprint: Contract Families & Derivative Mechanics

#### Detailed Exploration of the 4 Derivative Families

```
                        ┌────────────────────────────────────────┐
                        │      Financial Derivative Families     │
                        └───────────────────┬────────────────────┘
                                            │
      ┌─────────────────────┬───────────────┴───────────────┬─────────────────────┐
      ▼                     ▼                               ▼                     ▼
┌───────────┐         ┌───────────┐                   ┌───────────┐         ┌───────────┐
│ Forwards  │         │  Futures  │                   │  Options  │         │   Swaps   │
├───────────┤         ├───────────┤                   ├───────────┤         ├───────────┤
│• Custom   │         │• Standard │                   │• Option   │         │• Cash Flow│
│• OTC      │         │• Exchange │                   │  Right    │         │  Exchange │
│• Counter- │         │• Clearing │                   │• Call/Put │         │• Interest │
│  party R. │         │  Guarantee│                   │• Premium  │         │  / Forex  │
└───────────┘         └───────────┘                   └───────────┘         └───────────┘
```

1.  **Forward Contracts**:
    *   *Mechanics*: Private Over-the-Counter (OTC) agreements between two counterparties.
    *   *Key Features*: Fully customized contract size, expiry date, and delivery location. Settled physically or in cash at maturity.
    *   ⚠️ **Common Exam Pitfall**: Forward contracts carry severe **counterparty default risk** because no exchange or clearinghouse guarantees performance if one party defaults.

2.  **Futures Contracts**:
    *   *Mechanics*: Standardized, exchange-traded agreements to buy or sell a specified quantity of an asset at a predetermined price on a future date.
    *   *Clearinghouse Guarantee*: Organized clearinghouses (e.g., NSCCL at NSE, CCIL) act as central counterparties (buyer to every seller, seller to every buyer), eliminating counterparty risk.
    *   *Margin Accounts & Mark-to-Market (MTM)*:
        *   **Initial Margin**: Upfront cash/collateral deposited before taking a futures position.
        *   **Maintenance Margin**: Minimum balance required in the margin account.
        *   **Daily MTM**: At the end of every trading day, the futures contract is revalued against the closing price. Daily gains are credited and daily losses are debited directly from the margin account.

3.  **Option Contracts**:
    *   *Call Option*: Grants the buyer the **right, but not the obligation**, to *buy* the underlying asset at strike price $K$ on or before expiry $T$.
    *   *Put Option*: Grants the buyer the **right, but not the obligation**, to *sell* the underlying asset at strike price $K$ on or before expiry $T$.
    *   *Asymmetry of Risk & Return*:
        *   **Option Buyer (Long)**: Pays an upfront non-refundable **premium ($P$)**. Risk is strictly capped at the premium paid ($-\text{Premium}$); potential return is theoretically unlimited (Call) or substantial (Put).
        *   **Option Writer/Seller (Short)**: Receives the upfront premium ($P$). Return is strictly capped at the premium received ($+\text{Premium}$); risk is theoretically unlimited if the market moves against the position.
    *   *Option Moneyness*:
        *   *In-the-Money (ITM)*: Call ($S_T > K$), Put ($S_T < K$) — Has positive intrinsic value.
        *   *At-the-Money (ATM)*: Spot price equals Strike price ($S_T = K$).
        *   *Out-of-the-Money (OTM)*: Call ($S_T < K$), Put ($S_T > K$) — Zero intrinsic value.

4.  **Swap Contracts**:
    *   *Interest Rate Swaps (IRS)*: Contractual agreement between two parties to exchange periodic interest rate cash flows based on a specified notional principal amount.
        *   *Plain Vanilla IRS*: One party pays a **fixed rate** and receives a **floating rate** (e.g., benchmarked to MIBOR); the counterparty does the reverse.
    *   *Currency Swaps*: Agreement to exchange principal and fixed/floating interest payments in one currency for those in another currency over the loan's tenure.

#### Plain Vanilla vs. Exotic Derivatives Architecture
*   **Plain Vanilla**: Standardized exchange contracts with clean payoff profiles and high market liquidity (e.g., Nifty Index Futures, standard European Stock Options).
*   **Exotic Derivatives**: Complex OTC structures with non-standard payoffs:
    *   *American vs. European*: American options can be exercised at any time prior to expiry; European options can be exercised **only on the exact expiration date**.
    *   *Path-Dependent Options*: Payoff depends on the historical price trajectory of the underlying asset, not just the final settlement price.
    *   *Barrier Options*: Feature a pre-set barrier price.
        *   **Knock-In Option**: Becomes active only if the underlying price reaches the barrier level.
        *   **Knock-Out Option**: Ceases to exist (knocks out) if the underlying price touches the barrier level.

#### Real-World Case Studies: Derivatives in Action
*   💼 **IT Exporters INR/USD Forward Contracts**: Indian IT exporters (TCS, Infosys) earning revenue in US Dollars lock in future exchange rates (e.g., locking 1 USD = ₹84.50 six months forward) via bank forward contracts to shield rupee profit margins from currency appreciation.
*   ✈️ **IndiGo Airlines Crude Oil Futures**: IndiGo uses long hedges on crude oil futures (MCX/NYMEX) to lock in jet fuel purchase costs, preventing sudden oil price spikes from eroding operational margins.
*   🏛️ **ECB Currency Swap Execution**: An Indian corporation raising a \$100 million External Commercial Borrowing (ECB) enters a currency swap with a foreign exchange bank, converting dollar principal and coupon liabilities into Rupee-denominated obligations to eliminate exchange rate risk.
*   💥 **2008 Indian SME Exotic Forex Derivative Crisis**: In 2007–08, Indian banks sold complex exotic currency derivatives (leveraged Knock-In / Knock-Out options) to exporting SMEs under the guise of "zero-cost currency hedges." When the global financial crisis caused extreme rupee volatility, the embedded leverage knocked in, causing losses running into thousands of crores for exporters and leading to years of court litigation.

---

## 4. Risk-Hedging Strategies & Derivative Payoff Mechanics

### ✍️ 5-Mark Quick Shot: Hedging Strategies Overview

*   **Core Concept**: Hedging involves taking an equal and opposite position in a derivative contract to offset potential price losses in an underlying physical or portfolio asset.
*   **4 Fundamental Strategies**:
    1.  **Long Hedge**: Buying futures/calls to protect against an increase in the future purchase price of an asset (used by consumers/importers).
    2.  **Short Hedge**: Selling futures/puts to protect against a decline in the future selling price of an asset (used by producers/exporters).
    3.  **Protective Put**: Holding a long position in the underlying stock while simultaneously purchasing a Put Option to establish a guaranteed price floor.
    4.  **Covered Call**: Holding a long position in the underlying stock while simultaneously selling a Call Option to collect premium income in a neutral/mildly bullish market.

#### 📊 Quick Summary Table: Core Hedging Strategies
| Strategy | Underlying Position | Derivative Position | Primary Objective | Risk / Reward Profile |
| :--- | :--- | :--- | :--- | :--- |
| **Long Hedge** | Needs to buy asset | **Buy Futures / Call** | Lock in maximum purchase price | Capped purchase price; forgone savings if spot falls |
| **Short Hedge** | Holds/Produces asset | **Sell Futures / Put** | Lock in minimum sale price | Guaranteed sale price; forgone profit if spot rises |
| **Protective Put**| Long Stock ($S_0$) | **Buy Put ($K, P$)** | Floor downside risk ($K - P$) | Capped downside risk; unlimited stock upside |
| **Covered Call** | Long Stock ($S_0$) | **Sell Call ($K, P$)** | Generate income via premium | Capped upside ($K + P - S_0$); unhedged stock downside |

---

### 📚 10-Mark Comprehensive Blueprint: Mathematical Payoff Equations & Execution Mechanics

#### Mathematical Equations for Option Payoffs
Let $S_T = \text{Spot Price at Expiration}$, $K = \text{Strike Price}$, and $P = \text{Option Premium Paid/Received}$.

1.  **Long Call Option (Buyer)**:
    $$\text{Payoff} = \max(0, S_T - K)$$
    $$\text{Net Profit} = \max(0, S_T - K) - P$$
2.  **Short Call Option (Writer)**:
    $$\text{Payoff} = -\max(0, S_T - K) = \min(0, K - S_T)$$
    $$\text{Net Profit} = P - \max(0, S_T - K)$$
3.  **Long Put Option (Buyer)**:
    $$\text{Payoff} = \max(0, K - S_T)$$
    $$\text{Net Profit} = \max(0, K - S_T) - P$$
4.  **Short Put Option (Writer)**:
    $$\text{Payoff} = -\max(0, K - S_T) = \min(0, S_T - K)$$
    $$\text{Net Profit} = P - \max(0, K - S_T)$$

#### Detailed Analysis of Synthetic Option Strategies

##### Strategy A: Protective Put (Long Stock + Long Put)
*   **Execution**: Investor buys 1 share of Stock $A$ at spot price $S_0 =$ ₹100 and buys a Put Option with strike $K =$ ₹100 for premium $P =$ ₹5. Total Initial Investment = $S_0 + P =$ ₹105.
*   **Payoff Equation**:
    $$\text{Net Position Value at Expiration} = S_T + \max(0, K - S_T) - (S_0 + P)$$
*   **Payoff Breakdown Across Expiration Scenarios**:
    *   *Scenario 1: Stock Price Falls to $S_T =$ ₹70*:
        *   Put Option Payoff = $K - S_T = 100 - 70 = +30$ (₹30).
        *   Stock Portfolio Value = ₹70.
        *   Total Position Realized = $70 + 30 = 100$ (₹100).
        *   Net Profit/Loss = $100 - 105 = -5$ (-₹5) (Loss is strictly capped at Put Premium $P$).
    *   *Scenario 2: Stock Price Soars to $S_T =$ ₹150*:
        *   Put Option Expires Unexercised = ₹0.
        *   Stock Portfolio Value = ₹150.
        *   Total Position Realized = ₹150.
        *   Net Profit = $150 - 105 = +45$ (+₹45) (Full participation in upside minus option premium).

```
  Net Profit ($)
       ^
       │                         / (Unlimited Upside)
       │                        /
       │                       /
  ───┬─┼──────────────────────/─────────> Stock Price (S_T)
     │ │                     /
 -P  ├─┴────────────────────/ (Downside Floor Created at Strike K)
       │
```

##### Strategy B: Covered Call (Long Stock + Short Call)
*   **Execution**: Investor owns 1 share of Stock $B$ purchased at $S_0 =$ ₹100 and sells a Call Option with strike $K =$ ₹110 for premium $P =$ ₹4. Net Cash Outflow = $S_0 - P =$ ₹96.
*   **Payoff Equation**:
    $$\text{Net Position Value at Expiration} = S_T - \max(0, S_T - K) + P$$
*   **Payoff Breakdown Across Expiration Scenarios**:
    *   *Scenario 1: Stock Price Remains Stagnant at $S_T =$ ₹100*:
        *   Call Option Expires Unexercised ($0$ loss).
        *   Investor retains stock (₹100) + Call Premium (₹4). Total = ₹104.
        *   Net Profit = $104 - 100 = +4$ (+₹4) (Yield enhancement in flat market).
    *   *Scenario 2: Stock Price Surges to $S_T =$ ₹140*:
        *   Call Buyer Exercises Option at $K =$ ₹110.
        *   Investor must deliver share at $K =$ ₹110.
        *   Total Realized Cash = $110 + 4 = 114$ (₹114).
        *   Net Profit = $114 - 100 = +14$ (+₹14) (Maximum profit capped at $K + P - S_0$).

```
  Net Profit ($)
       ^
 Max   │             ┌────────────────────── (Capped Upside Profit)
 Profit│            ╱
   ├─ ─┼─ ─ ─ ─ ─  ╱
       │          ╱
  ─────┼─────────╱─────────────────────> Stock Price (S_T)
       │        ╱
       │       ╱  (Downside Risk Parallel to Stock)
```

---

## 5. Audit, Synthesis & Master Exam Resources

### 🧮 Master Derivative Payoff Cheat-Sheet

| Strategy / Position | Payoff Equation | Net Profit Equation | Max Loss | Max Profit |
| :--- | :--- | :--- | :--- | :--- |
| **Long Call** | $\max(0, S_T - K)$ | $\max(0, S_T - K) - P$ | $P$ (Premium) | Unlimited |
| **Short Call** | $-\max(0, S_T - K)$ | $P - \max(0, S_T - K)$ | Unlimited | $P$ (Premium) |
| **Long Put** | $\max(0, K - S_T)$ | $\max(0, K - S_T) - P$ | $P$ (Premium) | $K - P$ |
| **Short Put** | $-\max(0, K - S_T)$ | $P - \max(0, K - S_T)$ | $K - P$ | $P$ (Premium) |
| **Protective Put** | $S_T + \max(0, K - S_T)$ | $S_T + \max(0, K - S_T) - S_0 - P$ | $S_0 + P - K$ | Unlimited |
| **Covered Call** | $S_T - \max(0, S_T - K)$ | $S_T - \max(0, S_T - K) + P - S_0$ | $S_0 - P$ | $K + P - S_0$ |

---

### 📚 Consolidated Real-World Case Index

1.  **Reliance Industries NCDs (Corporate Debt)**: Demonstrates top-tier corporate debt issuance via secured Non-Convertible Debentures at competitive rates.
2.  **IL&FS Commercial Paper Default (2018)**: Default on unsecured commercial paper that froze India's ₹10-lakh-crore CP market and triggered a systemic liquidity crisis across NBFCs and mutual funds.
3.  **NABARD Tax-Free Bonds (Institutional Debt)**: AAA-rated long-term sovereign-backed debt financing rural infrastructure with tax-exempt coupons for conservative investors.
4.  **Zomato IPO 2021 (Equity vs. Debt)**: ₹9,375 crore equity listing illustrating residual risk, equity upside, and lack of fixed returns vs. debt stability.
5.  **IT Exporters Rupee Forwards (Forwards)**: TCS/Infosys booking INR/USD forward contracts to lock in conversion rates and eliminate currency volatility risk on export revenues.
6.  **IndiGo Jet Fuel Futures (Futures & Long Hedge)**: Airline buying crude oil/jet fuel futures to hedge against price spikes threatening operating margins.
7.  **ECB Currency Swaps (Swaps)**: Corporate converting US Dollar External Commercial Borrowing principal and interest into Rupee liabilities to remove FX risk.
8.  **2008 Indian SME Exotic Forex Crisis (Exotic Derivatives)**: Exporting companies suffering severe losses from leveraged Knock-In/Knock-Out currency options sold as hedges.

---

### 📋 Slide-by-Slide Coverage Checklist (`Unit6_Financial_Instruments.pptx`)

| Slide # | Slide Title / Topic | Summary of Content Covered | Location in Study Notes | Audit Status |
| :---: | :--- | :--- | :--- | :---: |
| **Slide 1** | Title: Financial Instruments | Overview of Equity, Debt, Derivatives & Real-World Outcomes | Section 1, 2, 3 Intro | ✅ Covered |
| **Slide 2** | Chapter Structure & Overview | Roadmap covering Debt (3-7), Equity (8-10), Derivatives (11-19) | All Sections | ✅ Covered |
| **Slide 3** | What Makes an Instrument "Debt"? | Sovereign Debt, G-Secs, T-Bills (91/182/364d), Dated Securities | Section 1 (5-Mark & 10-Mark) | ✅ Covered |
| **Slide 4** | 10-Year G-Sec Benchmark | ~7% Yield pricing home loans, corporate bonds, NBFC credit | Section 1 (Sovereign Debt) | ✅ Covered |
| **Slide 5** | Corporate Bonds, Debentures & CPs | Secured Bonds, Unsecured Debentures, Commercial Papers | Section 1 (Corporate Debt) | ✅ Covered |
| **Slide 6** | Real-World Debt: Reliance & IL&FS | Reliance NCDs vs IL&FS 2018 CP Default Crisis | Section 1 (Case Studies) | ✅ Covered |
| **Slide 7** | CDs, NCDs & Institutional Bonds | Demat CDs, NCDs, NABARD AAA Tax-Free Bonds | Section 1 (Corporate Debt) | ✅ Covered |
| **Slide 8** | Five Risks in Debt Security | Credit, Interest Rate, Liquidity, Inflation, Market Risk | Section 1 (5 Risks) | ✅ Covered |
| **Slide 9** | Equity: Buying Ownership | Equity capital, BSE (1875) & NSE governance, Zomato IPO | Section 2 (5-Mark & 10-Mark) | ✅ Covered |
| **Slide 10** | 4 Features of Equity | Ownership stake, variable return, residual claim, voting rights | Section 2 (Equity Features) | ✅ Covered |
| **Slide 11** | Side-by-Side: Debt vs Equity | Multi-parameter comparison table (7 parameters) | Section 2 (Summary Table) | ✅ Covered |
| **Slide 12** | Derivatives Overview | Derived value, underlying assets, leverage, 3 participants | Section 3 (5-Mark & 10-Mark) | ✅ Covered |
| **Slide 13** | Forwards & Exporter Case | Customized OTC contracts, IT Exporters forward contracts | Section 3 (Forwards & Case) | ✅ Covered |
| **Slide 14** | Futures & IndiGo Fuel Case | Standardized, MTM, clearinghouse, IndiGo crude oil futures | Section 3 (Futures & Case) | ✅ Covered |
| **Slide 15** | Options: Call & Put | Call/Put rights, Strike price, Premium, Buyer/Writer risk | Section 3 & 4 (Options) | ✅ Covered |
| **Slide 16** | Swaps & ECB Currency Swap | IRS, Currency Swaps, Commodity Swaps, ECB Swap Case | Section 3 (Swaps & Case) | ✅ Covered |
| **Slide 17** | Plain Vanilla vs Exotic | Standard vs Customized, American/European, Barrier Options | Section 3 (Plain vs Exotic) | ✅ Covered |
| **Slide 18** | Exotic Forex Crisis 2008 | 2008 SME exotic derivative losses, Knock-In/Out risk | Section 3 (Exotic Case) | ✅ Covered |
| **Slide 19** | Hedging Strategies | Long Hedge, Short Hedge, Protective Put, Covered Call | Section 4 (Strategies) | ✅ Covered |
| **Slide 20** | Zomato IPO Case Recap | Equity upside vs debt coupon, volatility contrast | Section 2 & Case Index | ✅ Covered |
| **Slide 21** | Key Takeaways Recap | 5 core summary points covering Debt, Equity, Derivatives | Section 5 (Audit & Summary)| ✅ Covered |
| **Slide 22** | Concluding Slide | Course metadata and instructor acknowledgement | Document Header & Footer | ✅ Covered |
