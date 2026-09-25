import csv
import math

with open("naive_bayes.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    rec = list(reader)

num_attr = len(rec[0]) - 1

def calculate(data):
    if not data:
        return 0
    
    labels = []
    for row in data:
        labels.append(row[-1])
        
    distinct_labels = set(labels)
    entropy = 0.0
    
    for label in distinct_labels:
        prob = labels.count(label) / len(data)
        entropy -= prob * math.log2(prob)
    return entropy

total_info = calculate(rec)
print(f"Total Info (Base Entropy): {total_info:.4f}\n")

for i in range(num_attr):
    attr_name = header[i]
    attr_info = 0.0
    attr_splitinfo = 0.0
    
    unique_values = set()
    for row in rec:
        unique_values.add(row[i])
        
    for val in unique_values:
        subset = []
        for row in rec:
            if row[i] == val:
                subset.append(row)
                
        subset_size = len(subset)
        total_size = len(rec)
        weight = subset_size / total_size
        
        subset_entropy = calculate(subset)
        
        attr_info += weight * subset_entropy
        attr_splitinfo -= weight * math.log2(weight)
        
    attr_gain = total_info - attr_info
    
    gain_ratio = (attr_gain / attr_splitinfo)
    
    print(f"[{attr_name}]")
    print(f"  Info: {attr_info:.4f}")
    print(f"  Gain: {attr_gain:.4f}")
    print(f"  Split Info: {attr_splitinfo:.4f}")
    print(f"  Gain Ratio: {gain_ratio:.4f}\n")