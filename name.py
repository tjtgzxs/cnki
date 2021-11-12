import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def change_name():
    pdf_dir=BASE_DIR+os.sep+"pdf"+os.sep
    pdf_list = os.listdir(pdf_dir)
    for file in pdf_list:

        pdf_extend = os.path.splitext(file)[-1]
        pdf_name = os.path.splitext(file)[0]
        old_name = pdf_dir + file
        tmp_name=pdf_name.replace("\"","")
        tmp_name = tmp_name.replace("'", "")
        tmp_name=tmp_name.replace("-","")
        tmp_name=tmp_name.replace(";","")
        tmp_name = tmp_name.replace(":", "")
        tmp_name = tmp_name.replace("!", "")
        tmp_name = tmp_name.replace("！", "")
        tmp_name = tmp_name.replace("：", "")
        tmp_name = tmp_name.replace("？", "")
        tmp_name = tmp_name.replace("?", "")
        tmp_name = tmp_name.replace("、", "")
        # tmp_name=tmp_name.replace("")
        new_name = pdf_dir + tmp_name + pdf_extend
        try:
            os.rename(old_name, new_name)
        except:
            continue



if __name__=="__main__":
    print(change_name())

