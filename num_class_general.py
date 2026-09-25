import csv
import math

with open("numerical.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    rec = [[float(row[0]), row[4]] for row in reader]
    rec=sorted(rec)

num_rec = len(rec)

for n in range(num_rec-1):
    sp=(rec[n][0]+rec[n+1][0])/2
    lspy=0
    lspn=0
    gspy=0 
    gspn=0 
    for i in rec:
        if i[0]>sp:
            if i[1]=="yes":
                gspy+=1
            else:
                gspn+=1
        else:
            if i[1]=="yes":
                lspy+=1
            else:
                lspn+=1  

    h_d = 0.0
    p_yes = (lspy + gspy) / num_rec
    p_no = (lspn + gspn) / num_rec
    
    if p_yes > 0:
        h_d -= p_yes * math.log2(p_yes)
    if p_no > 0:
        h_d -= p_no * math.log2(p_no)

    hd_gsp = 0.0
    tot_gsp = gspy + gspn
    
    if tot_gsp > 0:
        if gspy > 0:
            hd_gsp -= (gspy / tot_gsp) * math.log2(gspy / tot_gsp)
        if gspn > 0:
            hd_gsp -= (gspn / tot_gsp) * math.log2(gspn / tot_gsp)

    hd_lsp = 0.0
    tot_lsp = lspy + lspn
    
    if tot_lsp > 0:
        if lspy > 0:
            hd_lsp -= (lspy / tot_lsp) * math.log2(lspy / tot_lsp)
        if lspn > 0:
            hd_lsp -= (lspn / tot_lsp) * math.log2(lspn / tot_lsp)
            
    hd_lsp_gsp = ((tot_lsp / num_rec) * hd_lsp) + ((tot_gsp / num_rec) * hd_gsp)


    gain=h_d-hd_lsp_gsp
    
    print(f"Gain of SP{n+1} (at {sp:.2f}): {gain:.4f}")