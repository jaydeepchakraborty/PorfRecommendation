from recoprofconst import *

feedback_file_1 = "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/Guru_Survey.xlsx"

prof_nm_lst = []
out_dict = {}

try:
    xl_workbook = xlrd.open_workbook(os.path.join(feedback_file_1))
    xl_sheet = xl_workbook.sheet_by_name("Sheet2")
    
    row = xl_sheet.row(0)
    for idx, cell_obj in enumerate(row):
            cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
            prof_nm_lst.append("".join(cell_obj.value.split()))  
      
    num_cols = xl_sheet.ncols - 1
    num_rows = xl_sheet.nrows - 1
    
    
    for row_idx in range(1,num_cols):
        for col_idx in range(row_idx+1, num_rows):
            cell_obj = xl_sheet.cell(row_idx, col_idx)
            key = prof_nm_lst[row_idx]+"--"+prof_nm_lst[col_idx]
            print(key + "-->"+ cell_obj.value)
    
    

except:
    traceback.print_exc()
#-------------------------------------STOP----------------------------------------

print("---END---")
