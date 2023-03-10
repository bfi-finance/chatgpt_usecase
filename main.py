# from farhan_gpt import MyGPT
from gpt_usecase import UseCaseGPT

if __name__ == '__main__':
    # gpt = MyGPT()
    #
    # input_text = """
    # cukup jawab dengan kata negatif/positif/netral
    #
    # apa sentimen dari kalimat di bawah ini:
    #
    # "Sy ngeliat bokep krn sudah muak dgn kehidupan"
    # """
    # response = gpt.input_text(text=input_text)
    # print(response)

    # text = """
    # Lagian pake sok asik bagi-bagi tiket konser K-Pop
    # padahal biar elektabilitas naik udah bener perbanyak
    # foto kucing Menhan aja wqwqwqwqwqwqwqwqwqwqqwqwqwqwqwqqwqqwqwqwq
    # """

    usecase = UseCaseGPT()
    result = usecase.code_explainer(file_path="farhan_gpt.py")
    print(result)
