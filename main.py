from gpt_usecase import UseCaseGPT

if __name__ == '__main__':

    usecase = UseCaseGPT()
    result = usecase.code_explainer(file_path="farhan_gpt.py")
    print(result)
