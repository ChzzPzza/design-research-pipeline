```python
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Sample data
data = [
    {"study_id": "test_interview", "source": "primary", "participant_id": "test_interview_L1", "role": "", "date": "", "text": "I struggled to find the export feature in the dashboard."},
    {"study_id": "test_interview", "source": "primary", "participant_id": "test_interview_L2", "role": "", "date": "", "text": "The onboarding tutorial felt too long and I skipped most of it."},
    {"study_id": "test_interview", "source": "primary", "participant_id": "test_interview_L3", "role": "", "date": "", "text": "I like the clean visual design but the navigation labels are confusing."}
]

# Extract text from data
texts = [record['text'] for record in data]

# Vectorize texts
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

# Cluster texts into themes
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)
labels = kmeans.labels_

# Define human-readable theme names
theme_names = [
    "Export Feature Difficulty",
    "Onboarding Tutorial Length",
    "Navigation Confusion"
]

# Count records per theme
counts = [list(labels).count(i) for i in range(num_clusters)]

# Plotting
themes = theme_names
plt.figure(figsize=(10, 6))
plt.barh(themes, counts)
plt.xlabel('Number of Records')
plt.title('Design Research Themes')
plt.tight_layout()
plt.show()
```


