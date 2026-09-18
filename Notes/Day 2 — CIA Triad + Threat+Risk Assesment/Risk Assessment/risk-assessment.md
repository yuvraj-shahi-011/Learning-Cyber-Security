# Day 02 — Risk Assessment

## First Risk Register

| ID  | Asset            | Threat     | Vulnerability       | Likelihood | Impact | Risk |
| --- | ---------------- | ---------- | ------------------- | ---------: | -----: | ---: |
| R01 | Admin Account    | Attacker   | No MFA              |          4 |      5 |   20 |
| R02 | Customer DB      | Data thief | Weak access control |          4 |      5 |   20 |
| R03 | Website          | DDoS       | No protection       |          3 |      4 |   12 |
| R04 | Employee Account | Phisher    | Poor awareness      |          4 |      4 |   16 |
| R05 | Server           | Attacker   | Unpatched software  |          3 |      5 |   15 |

## Risk Formula

**Risk = Likelihood × Impact**

### Example

**R01:**

Likelihood = 4

Impact = 5

**Risk = 4 × 5 = 20**

## Risk Interpretation

| Risk Score | Level    |
| ---------: | -------- |
|        1–5 | Low      |
|       6–10 | Medium   |
|      11–15 | High     |
|      16–25 | Critical |

## Observations

* **R01:** The admin account has a high risk because MFA is not enabled.
* **R02:** The customer database has a high risk because weak access control could allow unauthorized access to sensitive information.
* **R03:** The website could become unavailable because it has no DDoS protection.
* **R04:** Poor employee security awareness increases the risk of successful phishing attacks.
* **R05:** Unpatched server software may contain vulnerabilities that attackers could exploit.

## Recommended Controls

| ID  | Recommended Control                                                    |
| --- | ---------------------------------------------------------------------- |
| R01 | Enable Multi-Factor Authentication (MFA)                               |
| R02 | Implement Role-Based Access Control (RBAC) and least privilege         |
| R03 | Use DDoS protection and traffic filtering                              |
| R04 | Conduct security-awareness and phishing training                       |
| R05 | Apply security patches and maintain a vulnerability-management process |

## Key Concepts

**Asset:** Something valuable that needs protection.

**Threat:** Something capable of causing harm to an asset.

**Vulnerability:** A weakness that can be exploited by a threat.

**Likelihood:** The probability that a threat will exploit a vulnerability.

**Impact:** The damage that could result if the threat occurs.

**Risk:** The combination of likelihood and impact.
