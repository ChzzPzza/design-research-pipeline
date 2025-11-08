```python
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data
data = [
    {"study_id": "test_interview", "source": "primary", "participant_id": "test_interview_L1", "role": "", "date": "", "text": "I struggled to find the export feature in the dashboard."},
    {"study_id": "test_interview", "source": "primary", "participant_id": "test_interview_L2", "role": "", "date": "", "text": "The onboarding tutorial felt too long and I skipped most of it."},
    {"study_id": "test_interview", "source": "primary", "participant_id": "test_interview_L3", "role": "", "date": "", "text": "I like the clean visual design but the navigation labels are confusing."}
]

# Extract text
texts = [record['text'] for record in data]

# Vectorize text
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

# Cluster into themes (3-8 range, here we use 3)
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
labels = kmeans.labels_

# Define theme names
theme_names = {
    0: "Navigation confusion",
    1: "Onboarding friction",
    2: "Feature accessibility"
}

# Count records per theme
counts = [0] * len(theme_names)
for label in labels:
    counts[label] += 1

# Prepare data for plotting
themes = list(theme_names.values())
counts = counts[:len(themes)]

# Plotting
plt.figure(figsize=(10, 6))
y_pos = range(len(themes))
plt.barh(y_pos, counts, align='center', alpha=0.7)
plt.yticks(y_pos, themes)
plt.xlabel('Number of Records')
plt.title('Design Research Themes Count')
plt.tight_layout()
plt.show()
```


