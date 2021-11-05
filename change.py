import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
pdf_dir=BASE_DIR+os.sep+'pdf'+os.sep
pdf_list=os.listdir(pdf_dir)
# print(pdf_list)
for file in pdf_list:
    pdf_extend=os.path.splitext(file)[-1]
    pdf_name=os.path.splitext(file)[0]
    name_list=pdf_name.split('_')
    # print(name_list[0])
    old_name=pdf_dir+file
    new_name=pdf_dir+name_list[0]+pdf_extend
    try:
        os.rename(old_name,new_name)
    except:
        continue
