# nutritional-semantic-analysis
**The Problem:** Healthy options often lose out to comfort food because they suffer from a severe branding problem. The goal was to investigate this semantic gap and determine if we could algorithmically nudge users toward better dietary choices without them feeling like they are sacrificing taste.

**The Methodology:** I mined and processed a massive, crowdsourced dataset of over 230,000 Food.com recipes. After quantifying the linguistic differences between health categories, I leveraged Natural Language Processing (NLP) and Random Forest models to build and evaluate personalized recipe recommendation engines.

**The Impact:** The analysis proved that unhealthy recipes are three to five times more likely to rely on highly appetizing keywords. Furthermore, the modeling phase revealed the limits of hyper-personalization on messy, user-generated platforms, demonstrating that a simpler, statistically sound Bayesian Average sorting system is actually much more effective at driving positive user engagement.

If this Bayesian-sorted recommendation engine were deployed as a live feature, success would be measured against the following commercial and engagement metrics:

*   **Primary Metric (North Star):** **Recipe Conversion Rate.** Measured by the percentage of users who click "Save Recipe" or "Add to Grocery List" from the recommended feed.
*   **Secondary Engagement Metrics:**
    *   **Click-Through Rate (CTR):** Tracking the CTR on "Healthy" tagged recipes placed in the top 5 slots versus the baseline.
    *   **Session Length & Bounce Rate:** Ensuring that prioritizing healthier, less-hedonic recipes does not negatively impact overall platform browsing time.
*   **Technical Metric:** **Recommendation Latency.** Ensuring the Bayesian sorting algorithm executes within <200ms to maintain a seamless UX during search queries.
