from farhan_gpt import MyGPT


class UseCaseGPT(MyGPT):

    def __init__(self):
        MyGPT.__init__(self)

    def get_sentiment(self, text: str) -> str:
        """
        get the sentiment (negatif/positif/netral)
        of the text that you passed in the `text` parameter

        :param text: the text you want to label
        :return: the label in string (negatif/positif/netral)
        """
        input_text = f"""
            cukup jawab dengan kata negatif/positif/netral.

            apa sentimen dari kalimat di bawah ini:

            "{text}"
            """

        result_str = self._input_text(text=input_text)
        return result_str

    def indo_to_english_trans(self, text: str) -> str:
        """
        translate indo text to english

        :param text: the indonesia text you want to translate into english
        :return: the result of translation
        """
        input_text = f"""
            cukup jawab dengan hasil terjemahannya saja.
        
            terjemahkan dalam basaha inggris kalimat di bawah ini:

            {text}
            """

        result_str = self._input_text(text=input_text)
        return result_str

    def code_commenter(self, file_path: str) -> str:
        """
        clean and put comments in the given code

        :param file_path:
        :return: the result the commented code
        """

        with open(file_path, 'r') as f:
            code_text = f.read()

        input_text = f"""
            cukup jawab dengan hasilnya saja.

            tolong tulis ulang code tanpa mengubah
            code apapun di bawah ini
            dan tambahkan comment supaya lebih enak
            dibaca.

            {code_text}
            """

        result_str = self._input_text(text=input_text)

        with open(file_path, 'w') as f:
            f.write(result_str)
        return result_str

    def code_explainer(self, file_path: str) -> str:
        """
        explain the given code in bahasa indonesia

        :param file_path: the file path of code you want to be explained
        :return: the result of code explanation
        """

        with open(file_path, 'r') as f:
            code_text = f.read()

        input_text = f"""
            cukup jawab dengan hasilnya saja.

            tolong jelaskan fungsi code di bawah ini:

            {code_text}
            """

        result_str = self._input_text(text=input_text)

        return result_str
