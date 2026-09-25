import csv


with open("naive_bayes.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    rec = list(reader)

num_attr = len(rec[0]) - 1
num_rec = len(rec)

def gini(data):
    yes = 0
    no = 0
    l = len(data)
    for row in data:
        if row[-1] == "yes":
            yes+=1
        elif row[-1] == "no":
            no+=1
        else:
            continue
    return 1-((yes/l)**2)-((no/l)**2)

gini_total = gini(rec)
print(f"Gini total: {gini_total:.4f}")  
        
for i in range(num_attr):
    attr_name = header[i]
    unique_values = set()
    for row in rec:
        unique_values.add(row[i])
    for val in unique_values:
        subset_y = []
        subset_n = []
        for row in rec:
            if row[i] == val:
                subset_y.append(row)
            else:
                subset_n.append(row)
        gini_y = gini(subset_y)
        gini_n = gini(subset_n)
        gini_attr = ((len(subset_y) / num_rec) * gini_y) + ((len(subset_n) / num_rec) * gini_n)
        print(f"Gini {attr_name}({val}) (D): {gini_attr:.4f}")
        gini_new = gini_total - gini_attr
        print(f"Gini {attr_name}({val}): {gini_new:.4f}")   
        print("\n")
            
            
            
            
            
            
            
            
            
    