# Data Dictionary

## Fund Master

| Column | Type | Description |
| amfi_code | Integer | Unique AMFI Scheme Code |
| fund_house | Text | Mutual Fund House Name |
| scheme_name | Text | Scheme Name |
| category | Text | Fund Category |
| sub_category | Text | Fund Sub Category |

Source: 01_fund_master.csv

---

## NAV History

| Column | Type | Description |
| amfi_code | Integer | Scheme Code |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

Source: 02_nav_history.csv