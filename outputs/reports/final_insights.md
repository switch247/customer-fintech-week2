# Final Insights & Recommendations

**Key Performance Indicators (KPI) check**:

- **Total reviews**: 1200
- **Banks covered**: Bank of Abyssinia, Commercial Bank of Ethiopia, Dashen Bank
- **Sentiment scores available**: True
- **Thematic labels available**: True
- **AHT (Average Handling Time)**: MISSING — KPI unmet (no `AHT` column).

## Visualizations

- **sentiment_trends**: `outputs\figures\sentiment_trends.png`
- **rating_distribution**: `outputs\figures\rating_distribution.png`
- **Bank of Abyssinia_positive_keywords**: `outputs\figures\wordcloud_Bank of Abyssinia_positive.png`
- **Bank of Abyssinia_negative_keywords**: `outputs\figures\wordcloud_Bank of Abyssinia_negative.png`
- **Commercial Bank of Ethiopia_positive_keywords**: `outputs\figures\wordcloud_Commercial Bank of Ethiopia_positive.png`
- **Commercial Bank of Ethiopia_negative_keywords**: `outputs\figures\wordcloud_Commercial Bank of Ethiopia_negative.png`
- **Dashen Bank_positive_keywords**: `outputs\figures\wordcloud_Dashen Bank_positive.png`
- **Dashen Bank_negative_keywords**: `outputs\figures\wordcloud_Dashen Bank_negative.png`

## Bank-level Insights and Recommendations

### Bank of Abyssinia

- **Top drivers**: good, app, the, and, this, best, please, bank.
- **Top pain points**: the, app, and, this, worst, but, you, bank.

- **Recommendation**: Perform targeted UX testing to validate flows users report as confusing.
- **Recommendation**: Improve monitoring and release rollback procedures.

### Commercial Bank of Ethiopia

- **Top drivers**: good, app, the, and, very, best, nice, this.
- **Top pain points**: the, and, app, not, this, why, cbe, what.

- **Recommendation**: Perform targeted UX testing to validate flows users report as confusing.
- **Recommendation**: Improve monitoring and release rollback procedures.

### Dashen Bank

- **Top drivers**: app, the, and, good, best, bank, dashen, this.
- **Top pain points**: the, app, and, not, worst, this, bank, ever.

- **Recommendation**: Perform targeted UX testing to validate flows users report as confusing.
- **Recommendation**: Improve monitoring and release rollback procedures.

## Cross-bank comparison

- Compare banks by mean sentiment and rating distributions (see visualizations).
- Look for differences in common pain points (e.g., one bank may show more connection/OTP problems while another shows crashes).

## Ethics & Bias

- Reviews are self-selected and may over-represent frustrated or highly satisfied users (selection bias).
- Language differences and automated translation can distort sentiment scores.
- Consider demographic and channel biases (Google Play users differ from in-branch customers).

---

Generated with `scripts/generate_insights.py`