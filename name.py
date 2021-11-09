import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def change_name():
    pdf_dir=BASE_DIR+os.sep+"pdf"+os.sep
    pdf_list = os.listdir(pdf_dir)
    return  pdf_list


if __name__=="__main__":
    print(change_name())

