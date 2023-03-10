# import the module/class
from gpt_usecase import UseCaseGPT

if __name__ == '__main__':

    # define the UseCaseGPT()
    usecase = UseCaseGPT()
    # pass your code path you want to be explained as the argument in the file_path parameter
    result = usecase.code_explainer(file_path="farhan_gpt.py")
    # the explanation will be returned as a string
    print(result)
