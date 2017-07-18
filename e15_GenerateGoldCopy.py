from recoprofconst import *

crt_feedback_list = [
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Guru_Survey.xlsx",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Guru_Survey_tmp.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Ashutosh_Survey.xlsx",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Ashutosh_Survey_tmp.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Dhananjay_Survey.xlsx",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Dhananjay_Survey_tmp.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Ram_Survey.xlsx",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Ram_Survey_tmp.csv"]


mrg_feedback_list = [
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Guru_Survey_tmp.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Ashutosh_Survey_tmp.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Dhananjay_Survey_tmp.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Ram_Survey_tmp.csv"]

merged_feedback = "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/merged_feedback.csv"
final_merged_file = "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/final_merged_feedback.csv"
gold_copy = "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/gold_copy.csv"

#-------------------------------------createTmpFeedback START----------------------------------------
def createTmpFeedback():

    count = len(crt_feedback_list)
    
    for i in range(0, count,2):
        curr_feedback_file = crt_feedback_list[i]
        tmp_curr_feedback_file = crt_feedback_list[i+1]
        
        rater = curr_feedback_file.split("/")[-1]
        rater = rater[:-12]
        
        prof_nm_lst = []
        out_dict = {}
        
        try:
            xl_workbook = xlrd.open_workbook(os.path.join(curr_feedback_file))
            xl_sheet = xl_workbook.sheet_by_name("Sheet2")
            
            row = xl_sheet.row(0)
            for idx, cell_obj in enumerate(row):
                    cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
                    cell_val = cell_obj.value.strip()
                    prof_nm_lst.append("".join(cell_val.split()))  
              
            num_cols = xl_sheet.ncols - 1
            num_rows = xl_sheet.nrows
            
            
            with open(tmp_curr_feedback_file, "w") as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                writer.writerow(["id", rater])
                for row_idx in range(1,num_cols):
                    for col_idx in range(row_idx+1, num_rows):
                        cell_obj = xl_sheet.cell(row_idx, col_idx)
                        key = prof_nm_lst[row_idx]+"--"+prof_nm_lst[col_idx]
                        call_val = cell_obj.value.strip() if cell_obj.value.strip() != 'NA' else 'N'
                        writer.writerow([key, call_val])
            
        except:
            traceback.print_exc()
#-------------------------------------createTmpFeedback STOP----------------------------------------


#-------------------------------------mergeTmpFeedback START----------------------------------------
def mergeTmpFeedback(file1,file2,ind):
    
    ind = ind + 1
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    merged = df1.merge(df2, on="id", how="outer").fillna("")
    merged.to_csv(merged_feedback, index=False)
    if(ind<len(mrg_feedback_list)):
        mergeTmpFeedback(mrg_feedback_list[ind],merged_feedback,ind) 
    
#-------------------------------------mergeTmpFeedback STOP----------------------------------------  


#-------------------------------------pruneMrgFeedback START----------------------------------------
def pruneMrgFeedback():
    
    with open(merged_feedback, 'r') as inp, open(final_merged_file, 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if "NongYe" not in row[0] and "FengJu" not in row[0]:
                writer.writerow(row)
    
#-------------------------------------pruneMrgFeedback STOP----------------------------------------   
 

#-------------------------------------crtGoldCopy START----------------------------------------
def crtGoldCopy():
    
    with open(final_merged_file, 'r') as inp, open(gold_copy, 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            max_feedback = Counter(row).most_common(1)
            max_feedback_tup = max_feedback[0]
            row.append(max_feedback_tup[0])
            writer.writerow(row)
    
#-------------------------------------crtGoldCopy STOP---------------------------------------- 


createTmpFeedback()
mergeTmpFeedback(mrg_feedback_list[0],mrg_feedback_list[1],1)
pruneMrgFeedback()
crtGoldCopy()

print("---END---")
